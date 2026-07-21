---
title: "Day 01 · nanoGPT 仓库跑通记录"
date: 2026-07-21
tags: [nanoGPT, day01, source-reading, milestone]
status: done
---

# 📌 Day 01 · nanoGPT 仓库跑通记录

> 📍 **项目**：岗 1 推理优化 · W1  
> **日期**：2026-07-21  
> **状态**：✅ 完成

## 🎯 今日目标

- [x] 在 Colab 上挂载 Google Drive
- [x] 克隆 nanoGPT 仓库（用 ghfast.top 镜像）
- [x] 安装依赖（tiktoken）
- [x] 训练 shakespeare_char，跑通端到端
- [x] 跑推理生成 Shakespeare 风格文本

## 🛠 操作记录（**粘真实命令**）

```bash
# 1. 挂 Google Drive
from google.colab import drive
drive.mount('/content/drive')

# 2. 设置工作目录（持久化）
WORK_DIR = '/content/drive/MyDrive/llm-intern-prep'
os.makedirs(WORK_DIR, exist_ok=True)
%cd {WORK_DIR}

# 3. 克隆 nanoGPT（用 ghfast.top 镜像，中国地区快）
!git clone --depth 1 https://ghfast.top/https://github.com/karpathy/nanoGPT.git

# 4. 训练（默认 fp32 配置 + 2000 iter + 关闭 torch.compile）
%cd nanoGPT
!python train.py config/train_shakespeare_char.py \
    --max_iters=2000 \
    --compile=False

# 5. 推理采样
!python sample.py --out_dir=out-shakespeare-char --device=cuda \
    --max_new_tokens=500 --num_samples=2 --temperature=0.8 --top_k=200
```

## 📊 关键数据

| 项目 | 值 |
|---|---|
| GPU | Tesla T4（14.56 GB VRAM） |
| GPU 内存峰值 | ~1.9 GB |
| 模型参数 | 10.65M |
| Iter 数 | 2000（受限于时间和效果平衡） |
| 单 iter 时间 | ~580ms |
| MFU | 0.65% |
| Loss 起点 | 4.27 |
| Loss 收敛 | ~1.x |
| 总训练时长 | ~16 分钟 |

## 🧠 关键疑问（**没解决不睡觉**）

### 1. mfu = 0.65% 是什么意思？为什么这么低？

> **mfu = Model FLOPs Utilization**（模型算力利用率）  
> 把 GPU 想象成一辆 F1 赛车（理论极速 350 km/h），mfu 就是这趟开了多少百分比。

| mfu | 含义 | 典型场景 |
|---|---|---|
| 0-1% | ⚠️ 极低 | 小模型 / 显存读数据是大头 |
| 1-10% | ⚠️ 偏低 | 不用 compile 的中等模型 |
| 10-30% | ✅ 正常 | 有 compile，没 FlashAttention |
| 30-50% | ✅ 好 | 用 Triton kernel / FlashAttention |
| 50-70% | 🌟 极好 | H100 + 满血优化 |

我们 0.65% 正常吗？**对 nano-scale 模型 + T4 + 无 compile，正常**。  
**这就是岗 1 工作要解决的核心问题之一**—— 让 mfu 涨上去。

### 2. bf16 + compile=False 在 T4 上为何比 fp32 + compile=True 还慢？

> T4 有 bf16 Tensor Core 加速，但**只对 fused kernel 有效**。  
> 没有 torch.compile / Triton，bf16 反而增加类型转换开销，**拖累小模型**。  
> 大模型（7B+）使用 bf16 加速才明显。  
> **最终方案**：默认 fp32 配置（+ torch.compile on T4 也行，只是 mfu 上限就那样）

### 3. `train.py:196` 的 FutureWarning 是啥？

> `torch.cuda.amp.GradScaler` 在 PyTorch 2.x 已重命名为 `torch.amp.GradScaler('cuda', ...)`  
> 警告，不影响训练。

## 📚 学到的知识

1. **nanoGPT 是 ~300 行的玩具级 GPT 实现**
   - `train.py` 训练循环
   - `model.py` 模型（含 CausalSelfAttention / Block / MLP）
   - `config/train_*.py` 超参配置文件
   - `sample.py` 推理 / 采样脚本

2. **shakespeare_char 数据集是字符级**
   - 1.1MB 莎士比亚文本
   - vocab size = **65**（英文字符 + 标点 + 空格）
   - 1,003,854 train tokens / 111,540 val tokens

3. **Colab 持久化关键是 Google Drive**
   - `/content/` 是临时的
   - 必须 `cd /content/drive/MyDrive/...` 否则关掉就丢

4. **ghfast.top 镜像解决 GitHub 连接问题**
   - 中国地区访问 github.com 经常 timeout
   - 镜像仓库：`ghfast.top/https://github.com/...`
   - 大部分 GitHub 项目都能找到对应镜像

5. **Checkpoint 保存策略**
   - nanoGPT 默认 `always_save_checkpoint=False`，**只在 val loss 改善时保存**
   - 之前 step 250 的 ckpt 没保留的原因就是这个
   - 想要"保留最后一次的"就要 `always_save_checkpoint=True`

## 📅 明日计划（2026-07-22）

1. **精读 `model.py` 的 `CausalSelfAttention.forward()` 全部代码**
   - 画数据流图（ASCII）
   - 每行代码对应到论文公式
2. **看论文 Attention Is All You Need §3.2**（在 arxiv.org/abs/1706.03762）
   - 重点看 Scaled Dot-Product Attention 公式
3. **写 `day02-casual-attn.md`**

## 🔗 复现命令（任何人可复现）

```bash
git clone --depth 1 https://ghfast.top/https://github.com/karpathy/nanoGPT.git
cd nanoGPT
python data/shakespeare_char/prepare.py
python train.py config/train_shakespeare_char.py --max_iters=2000 --compile=False
python sample.py --out_dir=out-shakespeare-char --device=cuda \
    --max_new_tokens=500 --num_samples=2
```
