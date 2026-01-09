#!/usr/bin/env python3
"""
快速生成代码示例 - 使用新的详细prompt系统
Quick generation code example using the new detailed prompt system
"""

from pathlib import Path
import sys

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from core import OutputWriter
from src import TaskGenerator, TaskConfig

# ============================================================================
# 生成20道独一无二的数据
# Generate 20 unique tasks
# ============================================================================

# 配置任务参数
config = TaskConfig(
    num_samples=20,                    # 生成20个任务
    output_dir=Path("data/questions"), # 输出目录
    generate_videos=True,              # 生成视频（设为False可加快速度）
    num_dots=5,                        # 每个任务的点数（3-15）
    connection_type="sequential",      # 连接类型: "sequential", "path", "random"
    dot_color=(50, 50, 200),          # 点的颜色 (RGB) - 蓝色
    line_color=(200, 50, 50),         # 线的颜色 (RGB) - 红色
    random_seed=None,                  # 随机种子，设为整数可复现结果
)

# 创建生成器并生成任务
generator = TaskGenerator(config)
tasks = generator.generate_dataset()

# 写入磁盘
writer = OutputWriter(Path("data/questions"))
writer.write_dataset(tasks)

# 打印结果
print(f"✅ 成功生成 {len(tasks)} 个任务")
print(f"   输出目录: data/questions/dot_to_dot_task/")
print(f"\n第一个任务的prompt示例:")
print("-" * 80)
print(tasks[0].prompt)
print("-" * 80)

