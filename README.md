# Dot-to-Dot Task Data Generator 🔗

A synthetic data generator for creating dot-to-dot connection tasks for video model evaluation and reasoning tasks. Generates puzzles where numbered dots need to be connected in a specific order, along with solution videos and prompts.

This task generator follows the [template-data-generator](https://github.com/vm-dataset/template-data-generator.git) format and is compatible with [VMEvalKit](https://github.com/Video-Reason/VMEvalKit.git).

Repository: [O-34_dot_to_dot_task_data_generator](https://github.com/vm-dataset/O-34_dot_to_dot_task_data_generator)

---

## 📋 About Dot-to-Dot Tasks

Dot-to-dot tasks are reasoning puzzles where numbered dots are arranged on a canvas, and the task is to connect them in numerical order by drawing lines between consecutive points. This generator creates:

- **Initial state images**: Dots numbered 1, 2, 3... arranged on a canvas
- **Final state images**: The same dots with lines connecting them in order
- **Solution videos**: Animated videos showing the connection process step-by-step
- **Task prompts**: Natural language instructions for completing the task

These tasks are useful for:
- Evaluating visual reasoning capabilities in AI models
- Training video prediction models
- Testing sequential reasoning and planning abilities
- Creating educational puzzles and games

---

## 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/vm-dataset/O-34_dot_to_dot_task_data_generator.git
cd O-34_dot_to_dot_task_data_generator

# 2. Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install -e .

# 4. Generate dot-to-dot tasks
python examples/generate.py --num-samples 50
```

---

## 📁 Project Structure

```
dot-to-dot-generator/
├── core/                    # Core utilities and base classes
│   ├── base_generator.py   # Abstract base generator class
│   ├── schemas.py          # Pydantic data models
│   ├── image_utils.py      # Image rendering utilities
│   ├── video_utils.py      # Video generation utilities
│   └── output_writer.py    # File output handler
├── src/                     # Dot-to-dot task implementation
│   ├── generator.py        # Dot-to-dot task generator
│   ├── prompts.py          # Task instruction prompts
│   └── config.py           # Configuration settings
├── examples/
│   └── generate.py         # Command-line entry point
└── data/questions/         # Generated output directory
```

---

## 📦 Output Format

Each generated task produces a directory with the following files:

```
data/questions/dot_to_dot_task/{task_id}/
├── first_frame.png          # Initial state: numbered dots (REQUIRED)
├── final_frame.png          # Final state: dots with connecting lines (REQUIRED)
├── prompt.txt               # Task instructions (REQUIRED)
└── ground_truth.mp4         # Solution video showing connection process (OPTIONAL)
```

### Example Output

- **first_frame.png**: Shows 5 dots labeled 1-5 scattered on a white canvas
- **final_frame.png**: Shows the same dots with red lines connecting 1→2→3→4→5
- **prompt.txt**: "Connect the dots in numerical order by drawing lines between them. Start from dot 1 and continue sequentially until all dots are connected."
- **ground_truth.mp4**: Animated video showing each line being drawn sequentially

---

## ⚙️ Configuration

All configuration is done through `src/config.py`. You can customize:

### Task Parameters

- `num_dots`: Number of dots in the puzzle (default: 5, range: 3-15)
- `dot_radius`: Size of each dot in pixels (default: 8, range: 5-20)
- `line_width`: Thickness of connecting lines (default: 3, range: 2-5)
- `show_numbers`: Whether to display numbers on dots (default: True)
- `connection_type`: How dots are connected - `"sequential"`, `"path"`, or `"random"` (default: "sequential")

### Visual Settings

- `dot_color`: RGB color of dots (default: (50, 50, 200) - blue)
- `line_color`: RGB color of connecting lines (default: (200, 50, 50) - red)
- `background_color`: RGB background color (default: (255, 255, 255) - white)
- `image_size`: Canvas dimensions (default: (512, 512))

### Video Settings

- `generate_videos`: Whether to create solution videos (default: True)
- `video_fps`: Frame rate for videos (default: 10)

### Generation Settings

- `num_samples`: Number of tasks to generate
- `domain`: Task domain name (default: "dot_to_dot")
- `random_seed`: Seed for reproducibility
- `output_dir`: Output directory path

---

## 🎯 Usage Examples

### Basic Generation

Generate 50 dot-to-dot tasks with default settings:

```bash
python examples/generate.py --num-samples 50
```

### Custom Output Directory

Save tasks to a custom location:

```bash
python examples/generate.py --num-samples 100 --output data/my_tasks
```

### Reproducible Generation

Use a seed for reproducible results:

```bash
python examples/generate.py --num-samples 100 --seed 42
```

### Without Videos

Generate tasks without solution videos (faster):

```bash
python examples/generate.py --num-samples 100 --no-videos
```

### Custom Configuration

Modify `src/config.py` to change default parameters:

```python
class TaskConfig(GenerationConfig):
    num_dots: int = Field(default=10)  # Generate puzzles with 10 dots
    dot_color: tuple[int, int, int] = Field(default=(255, 0, 0))  # Red dots
    connection_type: str = Field(default="path")  # Use path connection
```

---

## 🎨 Connection Types

The generator supports different connection patterns:

1. **Sequential** (default): Connect dots in strict numerical order (1→2→3→4→5)
2. **Path**: Connect dots following a path that visits each exactly once
3. **Random**: Random connection order (still numbered for clarity)

---

## 📝 Prompt Types

The generator includes multiple prompt templates:

- **default**: General instructions for connecting dots
- **sequential**: Instructions emphasizing sequential order
- **path**: Instructions about creating a continuous path
- **shape**: Instructions about revealing a hidden shape

Prompts are randomly selected for each task to add variety.

---

## 🔧 Advanced Usage

### Programmatic Generation

```python
from pathlib import Path
from src import TaskGenerator, TaskConfig

# Configure generator
config = TaskConfig(
    num_samples=10,
    num_dots=7,
    dot_color=(0, 100, 200),
    generate_videos=True,
    output_dir=Path("output/tasks")
)

# Generate tasks
generator = TaskGenerator(config)
tasks = generator.generate_dataset()

# Tasks are now available as TaskPair objects
for task in tasks:
    print(f"Task {task.task_id}: {task.prompt}")
```

---

## 📊 Task Statistics

After generation, you can find statistics about your dataset:

- Total number of tasks generated
- Distribution of connection types
- Average number of dots per task
- Video generation success rate

---

## 🤝 Contributing

Contributions are welcome! Areas for improvement:

- Additional connection patterns (geometric shapes, letters, etc.)
- Difficulty levels (easy/medium/hard based on dot count and arrangement)
- Custom dot shapes and styles
- Multi-frame intermediate states
- Export formats (JSON, COCO, etc.)

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.