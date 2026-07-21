# 📚 02 · mini-vLLM 项目（Project B）— 计划中

**目标**：通过精读 vLLM 模块 + 手敲 mini-vLLM（500-1000 行 PyTorch），建立生产级 LLM serving 的工程能力。  
**W3-W4 完成标志**：
- 能讲清 PagedAttention 内存管理逻辑（15 分钟内）
- 能写一个 mini-vLLM 支持 Qwen2.5-0.5B 推理 + 连续 batching
- 面试能讲出 vLLM 与 SGLang 的 3 个主要差异

## 📂 子目录

| 目录 | 内容 | 状态 |
|---|---|---|
| [notes/](./notes) | vLLM 模块精读笔记 | 🔴 待启动 |
| [my_mini_vllm/](./my_mini_vllm) | 自己手敲的 mini-vLLM | 🔴 待启动 |

## 🎯 三大核心模块（精读）

| # | 模块 | 核心价值 |
|---|---|---|
| 1 | `vllm/core/scheduler.py` | 调度决策决定 throughput |
| 2 | `vllm/attention/` | PagedAttention（vLLM 招牌创新） |
| 3 | `vllm/worker/` | 模型并行 + KV cache 物理布局 |

**不读** vLLM 全部代码。只精读 3 个核心 + 2 个外围接口（api_server / engine）。

## 🗓 W3-W4 时间线

| 天 | 任务 |
|---|---|
| Day 11-12 | 跑通 `vllm serve` + 单请求 trace + 画流程图 |
| Day 13-14 | 三模块精读 |
| Day 15-18 | 写 mini-vLLM（500-1000 行） |
| Day 19-20 | 对比 throughput + 写博客 |

## 🚀 里程碑

- [ ] mono-vLLM 在 10 并发请求下稳定
- [ ] 与原 vLLM throughput 在 ±50% 内
- [ ] block manager 处理变长序列正确
- [ ] prefix caching 验证通过

## 📚 参考资料

- 📖 [vLLM 官方 repo](https://github.com/vllm-project/vllm)
- 📄 [PagedAttention 论文](https://arxiv.org/abs/2309.06180)（SOSP 2023）
- 📄 [FlashAttention 论文](https://arxiv.org/abs/2205.14135)
