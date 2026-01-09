"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                           DOT-TO-DOT TASK PROMPTS                             ║
║                                                                               ║
║  Prompts for dot-to-dot connection tasks.                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import random


# ══════════════════════════════════════════════════════════════════════════════
#  DOT-TO-DOT PROMPTS
# ══════════════════════════════════════════════════════════════════════════════

def _get_color_description(rgb: tuple[int, int, int]) -> str:
    """Convert RGB tuple to color description."""
    r, g, b = rgb
    if r < 100 and g < 100 and b > 150:
        return "blue"
    elif r > 150 and g < 100 and b < 100:
        return "red"
    elif r > 200 and g > 200 and b > 200:
        return "white"
    elif r < 50 and g < 50 and b < 50:
        return "black"
    else:
        return f"RGB({r}, {g}, {b})"


def get_prompt(task_data: dict = None, task_type: str = "default") -> str:
    """
    Generate a detailed prompt for the dot-to-dot task.
    
    Args:
        task_data: Dictionary containing task information (num_dots, connection_type, etc.)
        task_type: Type of task (key in PROMPTS dict) - kept for backward compatibility
        
    Returns:
        Detailed prompt string
    """
    if task_data is None:
        task_data = {}
    
    num_dots = task_data.get("num_dots", 5)
    connection_type = task_data.get("connection_type", task_type)
    
    # Get color descriptions
    dot_color = task_data.get("dot_color", (50, 50, 200))
    line_color = task_data.get("line_color", (200, 50, 50))
    dot_color_desc = _get_color_description(dot_color)
    line_color_desc = _get_color_description(line_color)
    
    # Base prompt template following the reference format
    if connection_type == "sequential":
        prompt = (
            f"The scene shows {num_dots} circular objects (dots) scattered across a white background. "
            f"Each object is a filled {dot_color_desc} circle with a black outline. "
            f"Each circle is labeled with a number from 1 to {num_dots}, displayed in black text centered on the circle. "
            f"Starting from dot 1, draw straight lines connecting the dots in strict numerical order: "
            f"first draw a line from dot 1 to dot 2, then from dot 2 to dot 3, continuing sequentially "
            f"until you reach dot {num_dots}. Each line should be drawn as a {line_color_desc} straight line segment "
            f"connecting the centers of the two consecutive numbered dots. "
            f"Continue this process until all {num_dots} dots are connected in numerical sequence, "
            f"forming a continuous path from dot 1 to dot {num_dots}."
        )
    elif connection_type == "path":
        prompt = (
            f"The scene shows {num_dots} circular objects (dots) scattered across a white background. "
            f"Each object is a filled {dot_color_desc} circle with a black outline. "
            f"Each circle is labeled with a number from 1 to {num_dots}, displayed in black text centered on the circle. "
            f"The numbers indicate the order in which the dots should be visited. "
            f"Starting from dot 1, draw straight lines connecting the dots following the numbered sequence: "
            f"draw a line from dot 1 to dot 2, then from dot 2 to dot 3, continuing in order "
            f"until you reach dot {num_dots}. Each line should be drawn as a {line_color_desc} straight line segment "
            f"connecting the centers of the two consecutive numbered dots. "
            f"Continue this process until all {num_dots} dots are connected following the numbered sequence, "
            f"forming a complete continuous path that visits each dot exactly once in the order indicated by their numbers."
        )
    elif connection_type == "random":
        prompt = (
            f"The scene shows {num_dots} circular objects (dots) scattered across a white background. "
            f"Each object is a filled {dot_color_desc} circle with a black outline. "
            f"Each circle is labeled with a number from 1 to {num_dots}, displayed in black text centered on the circle. "
            f"Starting from dot 1, draw straight lines connecting the dots in the order indicated by their numbers: "
            f"draw a line from dot 1 to dot 2, then from dot 2 to dot 3, continuing in the numbered sequence "
            f"until you reach dot {num_dots}. Each line should be drawn as a {line_color_desc} straight line segment "
            f"connecting the centers of the two consecutive numbered dots. "
            f"Continue this process until all {num_dots} dots are connected following the numbered order, "
            f"forming a continuous path from dot 1 to dot {num_dots}."
        )
    else:  # default
        prompt = (
            f"The scene shows {num_dots} circular objects (dots) scattered across a white background. "
            f"Each object is a filled {dot_color_desc} circle with a black outline. "
            f"Each circle is labeled with a number from 1 to {num_dots}, displayed in black text centered on the circle. "
            f"Starting from dot 1, systematically connect all the dots by drawing straight lines between them in numerical order. "
            f"Draw a line from dot 1 to dot 2, then from dot 2 to dot 3, continuing sequentially "
            f"until you reach dot {num_dots}. Each line should be drawn as a {line_color_desc} straight line segment "
            f"connecting the centers of the two consecutive numbered dots. "
            f"Ensure that each dot is connected exactly once in the sequence, and continue this process "
            f"until all {num_dots} dots are connected in numerical order, forming a complete continuous path "
            f"from the first dot to the last dot."
        )
    
    return prompt


def get_all_prompts(task_type: str = "default") -> list[str]:
    """Get all prompts for a given task type (for backward compatibility)."""
    # Return a list with one prompt for backward compatibility
    return [get_prompt(task_type=task_type)]
