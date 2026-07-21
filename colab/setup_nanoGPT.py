# -*- coding: utf-8 -*-
"""
岗 1 W1 nanoGPT · 一键启动（Colab 持久化版）
=============================================

用法（在 Colab 单元格里直接运行）：

    1. 打开 https://colab.research.google.com/
    2. 新建 notebook
    3. 新建一个 cell，把下面这一行粘贴进去，运行：
           %run /content/drive/MyDrive/llm-intern-prep/setup_nanoGPT.py
       或者把整个脚本内容粘贴到一个 cell 里直接跑
    4. 第一次会让你授权 Google Drive，按提示点确认

实现的功能：
    - 挂载 Google Drive 到 /content/drive
    - 在 Drive 上创建 /llm-intern-prep/ 工作目录（持久）
    - 克隆 nanoGPT 仓库（如果还没克隆）
    - 安装必要依赖
    - GPU 自检
    - 数据准备
    - 可选：开始训练（在最后的 __main__ 里设置 RUN_TRAIN = True/False）
"""

import os
import sys
import importlib


def mount_drive():
    """挂载 Google Drive"""
    from google.colab import drive
    drive.mount('/content/drive')


def setup_workdir():
    """设置工作目录"""
    WORK_DIR = '/content/drive/MyDrive/llm-intern-prep'
    os.makedirs(WORK_DIR, exist_ok=True)
    os.chdir(WORK_DIR)
    print(f'[OK] 工作目录: {WORK_DIR}')
    return WORK_DIR


def clone_nanogpt():
    """克隆 nanoGPT（用 ghfast.top 镜像，回退 github 直连）"""
    if os.path.exists('nanoGPT'):
        print('[OK] nanoGPT 已存在，跳过克隆')
    else:
        print('[...] 克隆 nanoGPT (ghfast.top 镜像)...')
        ret = os.system('git clone --depth 1 https://ghfast.top/https://github.com/karpathy/nanoGPT.git')
        if ret != 0:
            print('[!] 镜像失败，回退 GitHub 直连...')
            os.system('git clone --depth 1 https://github.com/karpathy/nanoGPT.git')
    os.chdir('nanoGPT')
    print(f'[OK] 当前路径: {os.getcwd()}')


def install_deps():
    """安装必要依赖"""
    print('[...] 安装 tiktoken (如果缺)...')
    try:
        importlib.import_module('tiktoken')
        print('[OK] tiktoken 已装')
    except ImportError:
        os.system(f'{sys.executable} -m pip install -q tiktoken')
        print('[OK] tiktoken 已安装')


def gpu_check():
    """GPU 自检"""
    print('\n=== GPU 自检 ===')
    os.system('nvidia-smi --query-gpu=name,memory.total,driver_version --format=csv')
    import torch
    print(f'PyTorch: {torch.__version__}')
    print(f'CUDA available: {torch.cuda.is_available()}')
    if torch.cuda.is_available():
        print(f'Device: {torch.cuda.get_device_name(0)}')
        print(f'VRAM total: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB')


def data_prep():
    """数据准备：shakespeare_char"""
    print('\n=== 数据准备 ===')
    os.system('python data/shakespeare_char/prepare.py')


def train(max_iters=None, compile_flag=False):
    """训练 nanoGPT
    参数：
        max_iters: 覆盖默认迭代数（None 用 config 里的值）
        compile_flag: 是否启用 torch.compile（T4 通常无需，开了反而需要 triton）
    """
    print('\n=== 训练 ===')
    cmd = 'python train.py config/train_shakespeare_char.py'
    if compile_flag is False:
        cmd += ' --compile=False'
    if max_iters is not None:
        cmd += f' --max_iters={max_iters}'
    print(f'[CMD] {cmd}')
    os.system(cmd)


def sample(max_new_tokens=500, num_samples=2, temperature=0.8, top_k=200):
    """推理采样"""
    print('\n=== 推理 / 采样 ===')
    cmd = (
        f'python sample.py --out_dir=out-shakespeare-char --device=cuda '
        f'--max_new_tokens={max_new_tokens} --num_samples={num_samples} '
        f'--temperature={temperature} --top_k={top_k}'
    )
    print(f'[CMD] {cmd}')
    os.system(cmd)


def show_status():
    """显示当前目录的运行状态（再开 session 时用）"""
    print('\n=== 当前状态 ===')
    print(f'路径: {os.getcwd()}')
    print('\n-- nanoGPT 文件 --')
    os.system('ls | head -20')
    print('\n-- 上次产物 --')
    if os.path.exists('out-shakespeare-char'):
        os.system('ls -la out-shakespeare-char/')
    else:
        print('(未找到 out-shakespeare-char，请先跑数据准备和训练)')


# ============================================================
# 主流程
# ============================================================
if __name__ == '__main__':
    print('=' * 60)
    print('  岗 1 W1 nanoGPT · 一键启动（Colab 持久化版）')
    print('=' * 60)

    # ---- 阶段 1：环境搭建（每次 session 必做） ----
    mount_drive()           # 挂载 Drive
    setup_workdir()         # cd 到 Drive 上的工作目录
    clone_nanogpt()         # 克隆 nanoGPT（已存在则跳过）
    install_deps()          # 安装依赖

    # ---- 阶段 2：GPU 自检 ----
    gpu_check()

    # ---- 阶段 3：数据准备（第一次必跑，之后跳过） ----
    if not os.path.exists('data/shakespeare_char/train.bin'):
        data_prep()
    else:
        print('\n[OK] 数据已准备好 (train.bin 存在)，跳过')

    # ---- 阶段 4：训练 ----
    # 默认不自动跑训练（5000 iter 在 T4 上约 5-8 分钟）
    # 想自动跑就把 RUN_TRAIN 设为 True
    RUN_TRAIN = False
    if RUN_TRAIN and not os.path.exists('out-shakespeare-char/ckpt.pt'):
        train(compile_flag=False)
    else:
        ckpt_exists = os.path.exists('out-shakespeare-char/ckpt.pt')
        if ckpt_exists:
            print(f'\n[OK] 已有 checkpoint (out-shakespeare-char/ckpt.pt)，跳过训练')
        else:
            print(f'\n[...] 尚未训练。在新 cell 里手动跑：')
            print(f'    train(compile_flag=False)')
            print(f'    或者直接: !python train.py config/train_shakespeare_char.py --compile=False')

    # ---- 阶段 5：推理（如果有 ckpt 才跑） ----
    if os.path.exists('out-shakespeare-char/ckpt.pt'):
        sample()
    else:
        print('\n[...] 没有 ckpt，跳过采样')

    # ---- 显示状态 ----
    show_status()

    print('\n' + '=' * 60)
    print('  完成。下一步建议：')
    print('  - 在新 cell 里跑 sample() 复现推理')
    print('  - 或者打开 model.py / train.py 开始精读源码（Day 1-5 任务）')
    print('=' * 60)
