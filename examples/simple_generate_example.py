#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    SIMPLE GENERATION CODE EXAMPLE                             ║
║                                                                               ║
║  Simple example showing how to generate dot-to-dot tasks with new prompts.   ║
╚══════════════════════════════════════════════════════════════════════════════╝

This is a minimal example showing how to use the updated prompt system.
"""

from pathlib import Path
import sys

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import OutputWriter
from src import TaskGenerator, TaskConfig


# Example 1: Basic generation with default settings
def example_basic():
    """Generate 20 tasks with default settings."""
    print("Example 1: Generating 20 tasks with default settings...")
    
    config = TaskConfig(
        num_samples=20,
        output_dir=Path("data/questions"),
        generate_videos=True,
    )
    
    generator = TaskGenerator(config)
    tasks = generator.generate_dataset()
    
    writer = OutputWriter(Path("data/questions"))
    writer.write_dataset(tasks)
    
    print(f"✅ Generated {len(tasks)} tasks")
    print(f"   Example prompt: {tasks[0].prompt[:100]}...")


# Example 2: Custom configuration
def example_custom():
    """Generate tasks with custom settings."""
    print("\nExample 2: Generating tasks with custom settings...")
    
    config = TaskConfig(
        num_samples=10,
        output_dir=Path("data/custom_output"),
        generate_videos=True,
        num_dots=7,  # 7 dots per task
        connection_type="path",  # Use path connection
        dot_color=(0, 150, 0),  # Green dots
        line_color=(255, 0, 0),  # Red lines
        random_seed=42,  # For reproducibility
    )
    
    generator = TaskGenerator(config)
    tasks = generator.generate_dataset()
    
    writer = OutputWriter(Path("data/custom_output"))
    writer.write_dataset(tasks)
    
    print(f"✅ Generated {len(tasks)} tasks with custom settings")
    print(f"   Full prompt from first task:")
    print(f"   {tasks[0].prompt}")


# Example 3: Generate without videos (faster)
def example_no_videos():
    """Generate tasks without videos for faster generation."""
    print("\nExample 3: Generating tasks without videos...")
    
    config = TaskConfig(
        num_samples=50,
        output_dir=Path("data/fast_output"),
        generate_videos=False,  # No videos = faster
        num_dots=5,
    )
    
    generator = TaskGenerator(config)
    tasks = generator.generate_dataset()
    
    writer = OutputWriter(Path("data/fast_output"))
    writer.write_dataset(tasks)
    
    print(f"✅ Generated {len(tasks)} tasks (no videos)")


# Example 4: Different connection types
def example_connection_types():
    """Generate tasks with different connection types."""
    print("\nExample 4: Generating tasks with different connection types...")
    
    connection_types = ["sequential", "path", "random"]
    
    for conn_type in connection_types:
        print(f"\n  Generating 5 tasks with '{conn_type}' connection type...")
        
        config = TaskConfig(
            num_samples=5,
            output_dir=Path(f"data/{conn_type}_tasks"),
            generate_videos=False,
            connection_type=conn_type,
            num_dots=6,
        )
        
        generator = TaskGenerator(config)
        tasks = generator.generate_dataset()
        
        writer = OutputWriter(Path(f"data/{conn_type}_tasks"))
        writer.write_dataset(tasks)
        
        print(f"  ✅ Generated {len(tasks)} tasks")
        print(f"     Prompt preview: {tasks[0].prompt[:150]}...")


if __name__ == "__main__":
    # Run examples
    print("=" * 80)
    print("Dot-to-Dot Task Generation Examples with New Prompts")
    print("=" * 80)
    
    # Uncomment the example you want to run:
    
    # example_basic()
    # example_custom()
    # example_no_videos()
    # example_connection_types()
    
    # Or run all examples:
    example_basic()
    example_custom()
    example_no_videos()
    example_connection_types()
    
    print("\n" + "=" * 80)
    print("All examples completed!")
    print("=" * 80)

