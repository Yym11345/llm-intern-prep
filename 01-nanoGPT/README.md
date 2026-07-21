# 📚 01 · nanoGPT 项目（Project A）

**目标**：通过精读 + 手敲 nanoGPT（300 行代码），建立 Transformer + 训练 + 推理的完整心智模型。  
**W1-W2 完成标志**：能给别人手写 scaled-dot-product attention + 解释 KV cache + 能手敲出一个 1000 行的 my_lm。

## 📂 子目录

| 目录 | 内容 | 状态 |
|---|---|---|
| [notes/](./notes) | 按日期的学习笔记 | 🟢 进行中 |
| [my_lm/](./my_lm) | 自己手敲的 mini-GPT（无参考） | 🔴 待启动 |
| [paper-notes/](./paper-notes) | 论文精读笔记 | 🔴 待启动 |
| [snippets/](./snippets) | 复用代码片段 | 🔴 待启动 |
| [results/](./results) | benchmark 结果 / 日志 | 🟢 进行中 |

## 🎯 W1-W2 学习清单

- [x] Day 1：nanoGPT 在 Colab T4 上跑通
- [ ] Day 2：精读 `CausalSelfAttention.forward()` + 画数据流图
- [ ] Day 3：精读 `Block` + `MLP` + 残差连接
- [ ] Day 4：改超参 sweep（depth / heads / context）
- [ ] Day 5：对照 *Attention is All You Need* 论文
- [ ] Day 6-10：手敲 `my_lm` mini-GPT（无参考）

## 📚 参考资料

- 📖 [nanoGPT 官方 repo](https://github.com/karpathy/nanoGPT)
- 🎬 [Let's build GPT](https://www.youtube.com/watch?v=kCc8FmEh1Mo)（Karpathy 视频）
- 📄 [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
- 📄 [GPT-2 论文](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf)
- 📄 [Llama 论文](https://arxiv.org/abs/2302.13971)
