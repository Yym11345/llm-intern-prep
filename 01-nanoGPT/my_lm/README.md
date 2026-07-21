# 🛠 my_lm · 从 0 手敲的 mini-GPT

> 这一目录是**完全自己手写**的 mini-GPT 实现。  
> **绝不参考 nanoGPT 代码**——写完再对比差异。

## 📝 实现计划

### Day 6（周二）：从 0 写 attention

- [ ] `my_attention.py`: scaled dot-product + causal mask + multi-head
- [ ] 单元测试：随机数据上输出与 nanoGPT 一致（误差 <1e-5）

### Day 7（周三）：写完整 Block + 模型

- [ ] `my_block.py`: LayerNorm + attention + MLP + 残差
- [ ] `my_model.py`: 完整 GPT 模型

### Day 8（周四）：训练循环

- [ ] `my_train.py`: 训练循环 + AdamW + 学习率调度

### Day 9（周五）：推理循环

- [ ] `my_sample.py`: 推理循环

### Day 10（周六）：端到端 + 论文对照

- [ ] 训练莎士比亚数据集
- [ ] 跑推理，对比 nanoGPT 输出
- [ ] 写文档 + 对照论文写反思

## ⚠️ 黄金原则

- **绝对不抄**——手关 nanoGPT 文件，写完再开
- **变量名自己起**（不抄 Karpathy 风格）
- **注释全用自己的话**（不抄注释）
- **每写一个文件即 commit**

## 🎯 完成标准

- [ ] mini-GPT 在同一数据上训练后可生成 Shakespeare 风格文本
- [ ] `my_attention.forward()` 输出与 nanoGPT `CausalSelfAttention.forward()` 在随机数据上一致
- [ ] 训练时长与 nanoGPT 在同硬件上 ±20%
- [ ] README 里有完整的"我从这里学到了什么"
