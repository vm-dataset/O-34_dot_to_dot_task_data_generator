#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║              DOT-TO-DOT TASK GENERATION WITH NEW PROMPTS                      ║
║                                                                               ║
║  Generate dot-to-dot tasks using the updated detailed prompt system.          ║
╚══════════════════════════════════════════════════════════════════════════════╝

Usage:
    python examples/generate_with_new_prompts.py --num-samples 20
    python examples/generate_with_new_prompts.py --num-samples 50 --output data/my_output --seed 42
    python examples/generate_with_new_prompts.py --num-samples 100 --connection-type path
"""

import argparse
from pathlib import Path
import sys

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import OutputWriter
from src import TaskGenerator, TaskConfig


def main():
    parser = argparse.ArgumentParser(
        description="Generate dot-to-dot task dataset with detailed prompts",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    # Generate 20 tasks with default settings
    python examples/generate_with_new_prompts.py --num-samples 20
    
    # Generate 50 tasks with custom output directory and seed
    python examples/generate_with_new_prompts.py --num-samples 50 --output data/my_output --seed 42
    
    # Generate 100 tasks with path connection type
    python examples/generate_with_new_prompts.py --num-samples 100 --connection-type path
    
    # Generate tasks without videos (faster)
    python examples/generate_with_new_prompts.py --num-samples 30 --no-videos
    
    # Generate tasks with custom colors
    python examples/generate_with_new_prompts.py --num-samples 20 --num-dots 7
        """
    )
    
    parser.add_argument(
        "--num-samples",
        type=int,
        required=True,
        help="Number of task samples to generate"
    )
    
    parser.add_argument(
        "--output",
        type=str,
        default="data/questions",
        help="Output directory (default: data/questions)"
    )
    
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility"
    )
    
    parser.add_argument(
        "--no-videos",
        action="store_true",
        help="Disable video generation (faster)"
    )
    
    parser.add_argument(
        "--num-dots",
        type=int,
        default=5,
        help="Number of dots per task (default: 5, range: 3-15)"
    )
    
    parser.add_argument(
        "--connection-type",
        type=str,
        choices=["sequential", "path", "random"],
        default="sequential",
        help="Connection type: sequential (1-2-3-...), path (shortest path), or random (default: sequential)"
    )
    
    parser.add_argument(
        "--dot-color",
        type=str,
        default=None,
        help="Dot color as RGB tuple, e.g., '50,50,200' (default: blue)"
    )
    
    parser.add_argument(
        "--line-color",
        type=str,
        default=None,
        help="Line color as RGB tuple, e.g., '200,50,50' (default: red)"
    )
    
    args = parser.parse_args()
    
    # Parse colors if provided
    dot_color = (50, 50, 200)  # Default blue
    line_color = (200, 50, 50)  # Default red
    
    if args.dot_color:
        try:
            dot_color = tuple(map(int, args.dot_color.split(',')))
            if len(dot_color) != 3:
                raise ValueError("Color must have 3 values (R, G, B)")
        except ValueError as e:
            print(f"Error parsing dot color: {e}")
            print("Using default blue color")
            dot_color = (50, 50, 200)
    
    if args.line_color:
        try:
            line_color = tuple(map(int, args.line_color.split(',')))
            if len(line_color) != 3:
                raise ValueError("Color must have 3 values (R, G, B)")
        except ValueError as e:
            print(f"Error parsing line color: {e}")
            print("Using default red color")
            line_color = (200, 50, 50)
    
    print(f"🎲 Generating {args.num_samples} dot-to-dot tasks...")
    print(f"   Configuration:")
    print(f"   - Number of dots per task: {args.num_dots}")
    print(f"   - Connection type: {args.connection_type}")
    print(f"   - Dot color: RGB{dot_color}")
    print(f"   - Line color: RGB{line_color}")
    print(f"   - Generate videos: {not args.no_videos}")
    if args.seed:
        print(f"   - Random seed: {args.seed}")
    print()
    
    # Configure task
    config = TaskConfig(
        num_samples=args.num_samples,
        random_seed=args.seed,
        output_dir=Path(args.output),
        generate_videos=not args.no_videos,
        num_dots=args.num_dots,
        connection_type=args.connection_type,
        dot_color=dot_color,
        line_color=line_color,
    )
    
    # Generate tasks
    generator = TaskGenerator(config)
    tasks = generator.generate_dataset()
    
    # Write to disk
    writer = OutputWriter(Path(args.output))
    writer.write_dataset(tasks)
    
    print()
    print(f"✅ Done! Generated {len(tasks)} tasks in {args.output}/{config.domain}_task/")
    print()
    print("Each task includes:")
    print("  - first_frame.png: Initial state with numbered dots")
    print("  - final_frame.png: Final state with connected dots")
    print("  - prompt.txt: Detailed task instructions")
    if not args.no_videos:
        print("  - ground_truth.mp4: Solution video showing connection process")
    
    # Show example prompt
    if tasks:
        print()
        print("Example prompt from first task:")
        print("-" * 80)
        print(tasks[0].prompt)
        print("-" * 80)


if __name__ == "__main__":
    main()

