# 双非研二 · 5 个月冲 MiniMax / 智谱级大模型算法实习 · 完整方案

## Context（为什么写这个方案）

- **画像**：双非（非 985/211）CS 硕士，暑假过后开研二，约 2026-07-21 → 2026-12-21 共 5 个月窗口
- **目标公司**：MiniMax（月之暗面）、智谱、Stepfun、零一万物、百川、阿里通义实验室、字节豆包、腾讯混元、蚂蚁、深度求索等
- **现状自评**：零 LLM 经验 / 偏工程实现 / 想投 "对齐/RLHF" 与 "推理优化"
- **招聘窗口**：2026 年 11-12 月秋招补录 + 寒假实习

## 一次说透：哪些岗对你"全力以赴也够得到"，哪些够不到

| 岗类 | 是否可达 | 原因 |
|---|---|---|
| **预训练核心算法**（Pre-training Loss/Architecture/Scaling） | ❌ 放弃 | 卡顶会论文+985 PhD+长时间工程经验 |
| **纯 RLHF/对齐研究**（设计新对齐算法发论文） | ❌ 放弃 | 同上，且 5 个月内不可能磨出第一作顶会 |
| **LLM 推理优化 / 部署 / Serving 工程师** | ✅ **主推 1** | 工程为王，看代码和 benchmark；开源贡献可作作品集 |
| **LLM 后训练工程化 / Alignment Engineering**（SFT、DPO 工程化、Agent、Tool-use、评测、数据工程） | ✅ **主推 2** | 算法原理可突击，工程落地为重；与你的"对齐偏好"最近 |
| LLM 应用 / RAG / Agent 工程师 | ✅ 兜底 | 与你偏好不完全一致，但若上面两条没冲进去，可以此作为备胎 |

**结论：你列的两个偏好里，"RLHF/对齐"我会翻译成 "**后训练工程化 + Agent/Tool-use**"，保留了你喜欢的算法味道，同时避开"卷算法研究岗必死"的坑。这两个岗位在 MiniMax/智谱内部都有大量 HC，并且相对 985 友好（看重代码和落地）**。

---

## 🏆 Top 2 推荐岗位（你用尽全力够得着）

### 🥇 岗 1：**大模型推理优化工程师**（LLM Inference/Serving Engineer）

**为什么主推**：
- 与你"偏工程实现"画像 100% 匹配
- 双非友好：MiniMax、智谱、月之暗面、Stepfun、B 站、网易、商米的推理团队都明确接受双非强代码选手
- 作品集强信号：GitHub 上的 vLLM/SGLang PR、性能 benchmark、量化 tool 都被认可
- 面试可量化：TTFT、TPOT、throughput、memory 比 paper 还好讲

**目标公司列表（按可达性排序）**：
1. **MiniMax（优先）**——工程岗招人多，2025-2026 扩招到 200+ HC
2. **智谱 GLM 团队**——本土最友好的大厂之一
3. **Stepfun 阶跃星辰**——独角兽中招人相对猛
4. **阿里通义实验室 / Qwen 团队**——工程岗 HC 多，>30% 双非
5. **字节豆包 Seed Infra**——招推理系统工程师，对外相对开放
6. **蚂蚁、网易、bilibili、商米、面壁**——中等难度

**JD 关键词（按出现频率）**：
`vLLM` `SGLang` `TGI` `continuous batching` `PagedAttention` `KV cache` `量化(GPTQ/AWQ/FP8)` `CUDA` `Triton` `TensorRT-LLM` `speculative decoding` `prefill-decode disaggregation`

---

### 🥈 岗 2：**LLM 后训练工程化 / Alignment Engineer**（推荐包装：SFT + DPO 工程化 + Agent/Tool-use）

**为什么这是你"对齐偏好"的正确翻译**：
- 同一类团队（智谱 GLM、MiniMax、月之暗面、DeepSeek 都叫 "Post-training" 团队），JD 写着 "RLHF" 但实际偏工程
- 双非可达路径：把 SFT→DPO→Reward Model→PPO 这条链路实现 + 调优 + 评测做到极熟练，做过实际项目即可
- 兜底方向：如果你对 RLHF 数学感到吃力，转投 "Agent/Tool-use/RAG" 同岗不同项目，依然属于 Post-training/Alignment 团队

**目标公司列表**：
1. **智谱 GLM（对齐团队）**——最容易进的本土 LLM 公司之一
2. **MiniMax 后训练团队**——HC 多，节奏快
3. **零一万物 / 百川 / 面壁**——本土独角兽
4. **字节豆包对齐组**——难度中上，但 HC 大
5. **腾讯混元、蚂蚁、京东探索研究院**——备选

**JD 关键词**：
`SFT` `DPO` `KTO` `SimPO` `RLHF/PPO` `Reward Model` `Tool-use/Tool Calling` `Function Calling` `Agent` `RAG` `LLaMA-Factory` `XTuner` `ms-swift` `Megatron-LM` `DeepSpeed` `OpenRLHF` `verl` `lm-evaluation-harness`

---

## 🎯 5 个月里程碑路线图（W1-W22，每周一任务级）

### **Month 1（W1-W4）：LLM 基础突击 + 编程筑基**

> 必须打透的硬基础，否则后面全崩

- **W1**（7.22-7.28）：CS 基础复习 + Python 高级（异步、装饰器、typing）
  - 任务：刷完 *Effective Python* 90 条中至少 50 条
  - 任务：LeetCode hot 100 题单 30 题（重点链表/树/DP）
- **W2**（7.29-8.4）：PyTorch 深入 + Transformer 原理
  - 任务：**手写 scaled-dot-product attention + multi-head + positional encoding**（不调库，从零写）
  - 任务：跑通 nanoGPT 训练一个字符级模型（看 Karpathy 视频）
  - 任务：精读 *Attention is All You Need* 1 遍
- **W3**（8.5-8.11）：HuggingFace Transformers / datasets / peft / accelerate
  - 任务：用 HF Transformers + trl 完成第一次 LoRA SFT（Qwen2.5-0.5B）
  - 任务：精读 LLaMA2 / LLaMA3 paper
- **W4**（8.12-8.18）：DeepSpeed / FSDP / ZeRO + 模型并行基础
  - 任务：在 7B 模型上跑通 FSDP 训练，理解 `stage=1/2/3`
  - 任务：精读一篇 model parallelism survey（按需）
  - 任务：建立 GitHub 仓库 `llm-intern-prep`，后续所有项目和笔记都放这里（≥3 星标作品集）

### **Month 2（W5-W8）：岗 1（推理优化）主线**

- **W5**（8.19-8.25）：vLLM 源码精读
  - 任务：通读 `vllm/worker/` 和 `vllm/core/scheduler.py`，理解 PagedAttention
  - 任务：在 2 张 GPU（如有）上跑通 vLLM serving，记录 TTFT/TPOT/throughput
- **W6**（8.26-9.1）：SGLang / TGI 二选一深入
  - 任务：在 SGLang 上搭一个 multi-turn 对话 demo，对比 vLLM 性能
  - 任务：精读 SGLang 的 RadixAttention 实现
- **W7**（9.2-9.8）：量化专题
  - 任务：实操 GPTQ → AWQ → BitsAndBytes (NF4) → FP8，对同一 7B 模型做 4 档量化
  - 任务：用 lm-evaluation-harness 评测量化前后质量差异（MMLU/GSM8K/C-Eval）
  - 任务：写一篇技术博客《Qwen2.5-7B 量化实战》
- **W8**（9.9-9.15）：CUDA / Triton 入门
  - 任务：精读 Triton 官方教程 + 写 2 个 Triton kernel（向量加 + Softmax）
  - 任务：在 vLLM 里跑通 speculative decoding（EAGLE-2 或 n-gram）

> **里程碑产出**：GitHub 上有完整的"量化 benchmark + vLLM 部署 demo"项目 + 1 篇技术博客

### **Month 3（W9-W12）：岗 2（后训练工程化）主线**

- **W9**（9.16-9.22）：SFT / DPO 工程化
  - 任务：用 LLaMA-Factory / ms-swift 在 Qwen2.5-7B 上跑 SFT，再跑 DPO
  - 任务：精读 DPO 论文并手写 DPO loss
- **W10**（9.23-9.29）：Reward Model + PPO 原理与实战
  - 任务：用 trl 的 `PPOTrainer` 跑通一个 PPO demo
  - 任务：精读 InstructGPT / RLHF 综述
- **W11**（9.30-10.6）：评测体系
  - 任务：用 lm-evaluation-harness + OpenCompass 跑通 MMLU/C-Eval/GSM8K/IFEval
  - 任务：自己设计一个 domain-specific 评测任务（如中文推理）
- **W12**（10.7-10.13）：Agent / Tool-use
  - 任务：用 LangGraph / smolagents 搭一个多 Agent 系统（研究助手 + 代码助手）
  - 任务：复现 ReAct / ToolACE 类论文核心思路（任选 1 篇）

> **里程碑产出**：SFT → DPO → Reward → PPO → 评测 → Agent 全链路 GitHub 仓库 + 2 篇技术博客

### **Month 4（W13-W18）：综合作品集冲刺 + 刷题 + 论文阅读**

- **W13**（10.14-10.20）：综合项目 1——**推理优化旗舰项目**
  - 任务：从 0 搭一个 production-ready inference service：vLLM + Triton + Prometheus + 压测脚本 + 量化开关
  - 任务：在 README 里写清楚 latency/throughput/memory/cost 四个轴
- **W14**（10.21-10.27）：综合项目 2——**后训练旗舰项目**
  - 任务：从 0 跑一个完整 post-training pipeline：base model → SFT → DPO → RM → PPO → 评测 → 部署
  - 任务：用 wandb / swanlab 全程可视化
- **W15**（10.28-11.3）：综合项目 3——**Agent 项目（差异化亮点）**
  - 任务：搭一个真实场景的 Agent（如论文自动综述 / 数据分析助手 / 知乎自动答题）
  - 任务：发布到 HuggingFace Spaces 或 GitHub，能直接体验
- **W16**（11.4-11.10）：8 篇必读论文清单
  - 任务：精读 LLaMA / Qwen / DeepSeek / RLHF 综述 / DPO / Mamba / FlashAttention / speculative decoding，每篇输出 Markdown 笔记（建议发布知乎/CSDN）
- **W17**（11.11-11.17）：刷题冲击
  - 任务：LeetCode hot 100 + LLM 八股文（transformer/attention/位置编码/RMSNorm/SwiGLU/RoPE/KV cache/PagedAttention/投机解码）
  - 任务：每天 2 题 + 1 个八股主题
- **W18**（11.18-11.24）：简历 + 投递素材包
  - 任务：写 2 版简历（推理优化向 + 后训练工程向）
  - 任务：写冷启动邮件模板、准备 GitHub 主页、复盘作品集链接

### **Month 5（W19-W22）：集中投递 + 面试**

- **W19**（11.25-12.1）：投递日（**重要日期：12 月 1 日前**完成第一轮撒网）
  - 任务：投递 ≥30 家公司，列出目标公司优先级
  - 任务：内推渠道：脉脉、知乎、X、即刻、各公司招聘官网、Boss 直聘
- **W20**（12.2-12.8）：面试 1 → 5：每次面完立刻复盘
- **W21**（12.9-12.15）：面试 6 → 10 + 复盘剧本
- **W22**（12.16-12.22）：沉淀 offer 选择 / 二次投递（如有失败）

---

## 🎒 必读书单 + 资源清单（按岗拆）

### 岗 1（推理优化）
- 📄 *FlashAttention*（tri Dao）+ *PagedAttention*（vLLM）
- 📄 *EAGLE / Medusa / Lookahead*（speculative decoding）
- 📄 *SmoothQuant / AWQ / GPTQ* 三篇 paper
- 📖 *Computer Systems: A Programmer's Perspective*（CSAPP，CUDA 章节）
- 🔧 代码：vLLM、SGLang、TGI、TensorRT-LLM、Triton 官方 tutorial
- 🎥 YouTube: `GPU MODE` channel, `AIChipTalk`, `ZOMI 讲解`（B站）

### 岗 2（后训练）
- 📄 *InstructGPT*、*DPO*、*KTO*、*RLAIF*、*SimPO*、*Process Reward Model*
- 📄 *Self-RAG*、*ReAct*、*Toolformer*、*Function Calling Survey*
- 📄 *DeepSeek-R1 / Qwen3*（后训练范式论文）
- 🔧 代码：LLaMA-Factory、ms-swift、XTuner、trl、OpenRLHF、verl
- 🔧 评测：lm-evaluation-harness、OpenCompass、IFEval、MT-Bench

### 通用
- 李沐 *Dive into LLM*（动手学大模型）
- Andrej Karpathy *Let's reproduce GPT-2 / nanoGPT 系列*
- HuggingFace 官方 course

---

## ⚠️ 5 个月时间约束下的取舍（重要！）

| Item | 是否必做 | 备注 |
|---|---|---|
| LeetCode 200 题 | ✅ 必 | 至少 hot 100 + LLM 岗常考题型 |
| 8 篇核心论文精读 | ✅ 必 | 列在 W16 |
| 2 篇技术博客发布 | ✅ 必 | 知乎/CSDN，**公开发表**能换内推 |
| 3 个 GitHub 项目 | ✅ 必 | 1 推理优化旗舰 + 1 后训练旗舰 + 1 Agent |
| CUDA / Triton | 🟧 看岗 1 强度 | 学 2 个 Triton kernel 即可，不必啃 PTX |
| 多模态 | ❌ 砍 | 不在目标岗能力栈内 |
| 顶会论文投稿 | ❌ 砍 | 时间不允许 |
| 刷 Kaggle | ❌ 砍 | ROI 低 |
| 完整研一课程补考 | ✅ 必 | 别挂科，否则实习 offer 会被收回 |

---

## 🧭 投递策略

### 投递节奏（**双非要广撒网，30 家起步**）
- **第 1 批**（11.25-12.1）：20 家，重点：智谱、MiniMax、Stepfun、零一万物、面壁、阿里通义、字节、网易、商米
- **第 2 批**（12.2-12.8）：10 家，重点：蚂蚁、腾讯混元、京东、bilibili、OPPO、vivo、美团
- **兜底批**（12 月中下旬）：小米、联想、地平线、寒武纪、毫末智行、文远知行、知行合一、毫末

### 简历钩子
1. **必须置顶的标题**：`大模型算法工程师（推理优化 / 后训练方向）`
2. **GitHub 主页置顶**：`llm-intern-prep` 仓库的 README 写明"5 个月转 LLM 实战作品集"
3. **项目命名要"看得懂"**：不要叫 "test1"，叫 `qwen2-7b-vllm-benchmark` / `post-training-pipeline-from-scratch`
4. **博客要发到公开平台**（知乎/CSDN/CSDN-掘金），不放笔记孤儿
5. **冷启动信**（Cover Letter）模板：
   > "我是 XX 大学 CS 硕士研二，零 LLM 背景 5 个月自学，已完成 X 个生产级项目（GitHub: 链接）。贵团队在 Y 方向的工作令我印象深刻，希望申请算法实习岗。"

### 面试核心考点（双非必须熟的"八股文"）
- Transformer 完整推导（手写 scaled-dot-product attention → MH → Add & Norm → FFN）
- RoPE / ALiBi / 各种位置编码对比
- KV cache + PagedAttention 原理 + 显存计算
- Speculative decoding 原理
- RLHF / DPO / PPO 流程图、loss 公式
- SFT → DPO → RLHF 的演进与 trade-off
- vLLM / SGLang / TGI 三大部署框架区别
- CUDA / Triton 基础（写一个 kernel 的能力）
- 8-bit/4-bit 量化原理与差异
- 长上下文优化（Linear/Sliding Window/Differential Attention）
- Tool/Function Calling、Agent 框架、COT/ReAct 范式

---

## 🔁 风险兜底方案

如果到 W14（10 月底）感觉推理优化岗 push 不了：

- **路径 A**：收缩为 "Agent / Tool-use / RAG 算法工程师"，仍属于 Post-training 团队 JD 范围
- **路径 B**：收缩为 "数据/评测工程师"，切入大模型团队
- **路径 C**：投递大厂的 LLM infra 团队（如阿里 PAI、字节 ML 平台、腾讯 Angel）

如果 W18（11 月中）简历还没 ready：
- 主动出击，给每家目标公司 5 个组发冷启动信，不要等 JD 完美
- 找学长学姐 / 校友内推（脉脉、知乎私信）

---

## ✅ 验证清单（5 个月后判断你能否拿到 offer）

1. **硬技能验证**：
   - [ ] 能 30 分钟内讲清 Transformer 全部组件与公式
   - [ ] 能 15 分钟内手写 PagedAttention 内存管理逻辑
   - [ ] 能 10 分钟内讲清 RLHF 三阶段各自 loss 设计
2. **作品集验证**：
   - [ ] GitHub 3 个公开项目，每个 ≥50 star 或被 fork
   - [ ] 2 篇公开技术博客，每篇 ≥2000 阅读
   - [ ] HuggingFace / ModelScope 上传过 ≥1 个微调后的 checkpoint 或 demo
3. **面试验证**：
   - [ ] 至少 5 场真实面试（含日常实习的面试也能算）
   - [ ] 至少 1 个 final round 进入率
4. **卡学历兜底**：
   - [ ] 即使双非，简历也能通过关键词 ATS
   - [ ] 拿到 ≥3 个面试机会（**双非最痛点是过不了简历关**）

---

## 📌 关键单一动作（最重要的一句话）

> **现在（今天）就建立 GitHub 仓库 `llm-intern-prep`，今天就提交 README，把这份 plan 贴上去。每天至少 commit 一次。** 这是你 5 个月后简历上的"作品集主干"，也是双非唯一能逆袭路径里最确定的武器。

---

## 备注（用于执行时回看）

- 路径随时可调整：如果 Month 2 发现推理优化比想象中难，转 Month 3 后训练时加大训练数据 / 评测占比
- 所有时间安排以"投递日 2026-12-01"为锚点倒推
- 任何一周断了，下周必须补上，否则月度里程碑崩盘
- 不推荐并行 3 个方向，必砍掉 1 个——已砍"纯学术对齐研究"

---

# 附录 A：岗 1（推理优化）深度行动手册

> 用户在初版 plan 后要求补充：本附录给出**岗 1 推理优化工程师**方向的可执行级深度手册、论文清单、面试题库。岗 2（后训练方向）如后续需要可继续追加附录 B。

## A.1 推理优化 · 4 个能力模块（贯穿 Month 2 全程）

| 模块 | 占比 | 说明 |
|---|---|---|
| **M1：推理引擎原理** | 30% | vLLM / SGLang / TGI / TensorRT-LLM 源码与架构 |
| **M2：CUDA / Triton 内功** | 25% | 写 kernel、显存优化、性能 profiling |
| **M3：量化与压缩** | 25% | GPTQ / AWQ / SmoothQuant / FP8 / KV cache 量化 |
| **M4：系统级优化** | 20% | speculative decoding、prefill-decode 分离、调度、MoE 推理 |

---

## A.2 推理优化 · 每周日任务卡（W5-W8 + W13 旗舰周复盘）

### W5｜vLLM 入门（`week-5-vllm-deep-dive/`）
- [ ] 看 *vLLM: Easy, Fast, and Cheap LLM Serving with PagedAttention* 论文（Kwon et al., SOSP'23）
- [ ] 克隆 vLLM 仓库，git checkout v0.6.x（稳定版）
- [ ] 通读 `vllm/engine/arg_utils.py` → 理解启动参数：`--tensor-parallel-size --gpu-memory-utilization --max-num-seqs --block-size`
- [ ] 通读 `vllm/core/scheduler.py`：理解 FCFS / SJF 调度、`block_manager`、`prefix caching`
- [ ] 在 1 张 A100 / 4090 上服务 Qwen2.5-7B-Instruct
- [ ] 用 `vllm bench serve` 跑一组 baseline，记录 TTFT / TPOT / throughput
- [ ] **输出物**：1 篇博客《vLLM 部署 Qwen2.5-7B-Instruct 实战 + PagedAttention 解读》

### W6｜SGLang + TGI 对比（`week-6-sglang-vs-tgi/`）
- [ ] 部署 SGLang，跑通 multi-turn conversation demo
- [ ] 精读 SGLang 的 RadixAttention 论文：*RadixAttention: Linear-Time Sequence Parallelism for LLM Serving*
- [ ] TGI 在 7B 模型上跑通
- [ ] 在同一硬件、同一 prompt set 下，对 vLLM / SGLang / TGI 做 benchmark
- [ ] **输出物**：1 个 benchmark 表格（GitHub README）+ 1 篇对比博客

### W7｜量化专题（`week-7-quantization/`）
- [ ] 实现 4 个量化方案 on Qwen2.5-7B：
  - **GPTQ**（使用 `auto-gptq`）
  - **AWQ**（使用 `autoawq`）
  - **BitsAndBytes NF4**（4-bit）
  - **FP8**（使用 `transformer-engine`，需 H100）
- [ ] 用 `lm-evaluation-harness` 评测量化前后在 MMLU / GSM8K / IFEval 上的差异
- [ ] 对每个量化方法记录：模型大小、显存峰值、latency、quality delta
- [ ] **输出物**：1 篇《Qwen2.5-7B 量化四档对比》博客 + benchmark JSON

### W8｜CUDA / Triton + speculative decoding
- [ ] 精读 FlashAttention-2 / FlashAttention-3 paper 核心算法
- [ ] Triton 教程：`triton-lang/triton` 仓库的 `tutorials/` 目录 0-3 课
- [ ] 写 2 个 Triton kernel：
  - 1 个向量加
  - 1 个 fused softmax（对比 PyTorch 实现，加速比 ≥3x）
- [ ] 在 vLLM 中启用 `--speculative-model`（EAGLE-2 或 n-gram），记录加速效果
- [ ] **输出物**：Triton kernel 项目 + vLLM speculative decoding 性能对比 JSON

---

## A.3 推理优化 · 必读论文清单（按优先级）

### P0（精读 + 写笔记）
| # | 论文 | 一句话核心 | 你要会讲 |
|---|---|---|---|
| 1 | *Attention Is All You Need* (NeurIPS'17) | Transformer 原论文 | 手写 attention 公式 |
| 2 | *FlashAttention* (NeurIPS'22) | IO-aware softmax tiling | tile 分块与显存复用 |
| 3 | *FlashAttention-2/3* | 改进并行、FP8 支持 | 与 v1 区别、warp-specialization |
| 4 | *vLLM / PagedAttention* (SOSP'23) | 虚拟内存式 KV cache | block table、prefix caching |
| 5 | *SGLang / RadixAttention* | Radix tree KV cache 复用 | LRU 淘汰、跨请求复用 |
| 6 | *GPTQ* (ICLR'23) | 逐层二阶量化 | OBFP、Hessian 逆、Group size |
| 7 | *AWQ* | 激活感知权重量化 | 1% salient channels 保护 |
| 8 | *SmoothQuant* | 激活难、权重易的对角均衡 | per-channel / per-tensor scale |
| 9 | *EAGLE / EAGLE-2* | 投机解码 next-token 预测 | draft model 训练、accept 策略 |
| 10 | *Medusa* | 多 head 并行投机 | tree attention、accept 树 |
| 11 | *DistServe / Splitwise* | prefill-decode disaggregation | 双 stage 调度、token-level |
| 12 | *DeepSeek-V3* 推理 | MoE + FP8 + MLA | expert parallelism、MLA KV cache |
| 13 | *Qwen2 / Qwen2.5 Technical Report* | dense 模型推理优化 | GQA、YaRN 长文 |

### P1（略读 + 会讲核心贡献）
- *Tensor Parallel / Pipeline Parallel* 经典（Megatron-LM）
- *LoRA / QLoRA*（虽不是推理，但面试常考）
- *KV cache compression*（H2O / Scissorhands / StreamingLLM）
- *Linear attention 系列*（Mamba / RWKV / RetNet）
- *Differential Attention / MLA*（DeepSeek）
- *Speculative decoding 综述*（Leviathan et al.）
- *MoE inference*（DeepSeek-V3、Mixtral serving paper）

### 不需要读
- 全量 RLHF paper（除非面岗 2）
- 多模态对齐 paper
- 数据合成 paper

---

## A.4 推理优化 · 50 道面试题库（八股文 + 手写题）

### 模块一：Transformer 基础（10 题）
1. 手写 scaled-dot-product attention，包括 masking 和 scaling 因子解释
2. 手写 multi-head attention 的拆分与合并（Q/K/V reshape）
3. RoPE 公式 + 为什么比绝对位置编码好 + 与 ALiBi 比较
4. RMSNorm vs LayerNorm，SwiGLU vs GeLU 的计算复杂度
5. Grouped Query Attention (GQA) 为什么能省 KV cache
6. KV cache 在 decoding 阶段每步复用的依据是什么
7. FlashAttention 的核心思想：为什么比朴素 attention 更快
8. Multi-Query Attention (MQA) 与 GQA、MLA 的差别
9. 长上下文的 attention 优化：Flash、Ring、Linear 各代表什么思路
10. 手写 sliding window attention 的 mask 矩阵

### 模块二：vLLM / PagedAttention 机制（10 题）
11. PagedAttention 相比朴素 KV cache 的显存节省点
12. block size 的选择对 throughput 的影响（典型 16）
13. continuous batching 与 static batching 的对比
14. prefix caching 在哪些场景收益最大（system prompt 复用）
15. vLLM 的 swap space 机制与 CPU offload
16. vLLM 如何处理 variable-length sequence 的 padding
17. Chunked prefill 与普通 prefill 的差别
18. vLLM 的 `--max-num-seqs` 与 `--max-num-batched-tokens` 关系
19. vLLM 调度器的优先级策略（FCFS、SJF、剩余时间短优先）
20. vLLM 中 tensor parallel 与 pipeline parallel 的混合策略

### 模块三：SGLang / TGI（5 题）
21. SGLang 的 RadixAttention 如何用 Radix tree 组织 KV cache
22. SGLang 的前端 DSL（结构化编程）与 token-level 优化
23. TGI 的 Rust 实现带来的吞吐优势
24. 对比 vLLM / SGLang / TGI / TensorRT-LLM 的适用场景
25. SGLang 的 speculative decoding 支持

### 模块四：量化（8 题）
26. GPTQ 的逐层量化原理：OBFP 列式 Hessian 近似
27. GPTQ 中 group size（如 128）的作用与 trade-off
28. AWQ 为什么强调 activation-aware
29. SmoothQuant 的对角均衡矩阵如何数学推导
30. FP8 (E4M3 / E5M2) 与 INT8 量化在 LLM 上的精度对比
31. KV cache 量化的难点与代表方案（KVQuant、KV-Quant、Atom）
32. 为什么 weight-only 量化对 LLM 比 activation 量化更安全
33. 量化感知训练 (QAT) 与训练后量化 (PTQ) 在 LLM 上的差异

### 模块五：投机解码 / 调度（6 题）
34. Speculative decoding 的数学原理（为什么能精确保持分布）
35. EAGLE 与 Medusa 的本质区别
36. prefill-decode disaggregation 的优势：解耦 compute-bound 与 memory-bound
37. MoE 推理中 expert parallelism 与 tensor parallel 的 trade-off
38. 推理服务中的 SLO 设计：TTFT、TPOT、TBT 的含义
39. 在有限显存下同时跑 2 个 7B 模型的方法（TP/PP/Offload）

### 模块六：CUDA / Triton 基础（5 题）
40. CUDA 的 SIMT 架构解释 warp / block / grid
41. 解释 shared memory / register / global memory 的 latency 数量级
42. Triton 的 block size 选取 trade-off
43. 手写一个向量化加法的 Triton kernel
44. 解释 FlashAttention 用 CUDA 实现时的 tiling 切分

### 模块七：评测与压测（3 题）
45. 解释 TTFT / TPOT / TBT / throughput 的测量方法
46. 如何用 `vllm bench serve` 复现 llama.cpp / TGI 的报告数字
47. 评测时 warmup 的意义与典型配置

### 模块八：系统设计（3 题）
48. 设计一个 production-grade LLM 推理服务（SLO、调度、配额、监控）
49. 一个 64 卡 A100 集群怎么部署 671B 的 DeepSeek-V3
50. 突发流量（峰值 10x）下的推理容灾方案

---

## A.5 推理优化 · 项目作品集模板（旗舰项目用 W13）

仓库名建议：`production-llm-inference-stack` 或 `qwen-inference-benchmarks`

```
production-llm-inference-stack/
├── README.md                  ← 把 4 个轴说清楚：latency / throughput / memory / cost
├── docker/
│   ├── Dockerfile.vllm
│   └── Dockerfile.triton
├── configs/
│   ├── qwen2.5-7b-vllm.yaml
│   ├── qwen2.5-72b-tp4.yaml
│   └── ds-v3-moe.yaml
├── benchmarks/
│   ├── latency_throughput.py  ← vLLM 原生 benchmark 二次封装
│   ├── quality_eval.py        ← lm-evaluation-harness 包装
│   └── cost_calculator.py     ← 折算 $/1M tokens
├── quantization/
│   ├── gptq.py
│   ├── awq.py
│   ├── bitsandbytes_nf4.py
│   └── fp8.py
├── kernels/
│   ├── flash_attention_triton.py
│   ├── fused_softmax_triton.py
│   └── paged_attention.py
├── speculative/
│   ├── eagle2_integration.md
│   └── medusa_integration.md
├── serving/
│   ├── multi_gpu_launcher.sh
│   ├── prometheus_exporter.py
│   └── grafana_dashboard.json
├── notebooks/
│   ├── 01_kv_cache_explained.ipynb
│   ├── 02_paged_attention.ipynb
│   └── 03_quantization_ablation.ipynb
└── blog/
    └── blog_urls.md           ← 把知乎/CSDN 博客链接回填
```

---

## A.6 推理优化 · 双非简历钩子建议

简历项目行（**事实导向，不要夸大**）：

> ❌ "熟练使用 vLLM"
> ✅ "从零搭建 Qwen2.5-7B 生产级推理服务：vLLM + Triton kernel + GPTQ/AWQ/FP8 三档量化；支持 4-way tensor parallel + prefix caching + EAGLE-2 speculative decoding；TTFT 120ms、TPOT 35ms、throughput 2400 tokens/s/A100。"

> ❌ "理解 Transformer"
> ✅ "手写 scaled-dot-product attention、MHA、GQA、RoPE、RMSNorm、SwiGLU 共 6 个核心组件；阅读 vLLM / FlashAttention 源码并产出 4 篇技术博客。"

> ❌ "做过量化"
> ✅ "在 Qwen2.5-7B 上完成 GPTQ / AWQ / NF4 / FP8 四档量化的端到端 benchmark，量化前后质量损失 <0.5%（MMLU），模型体积压缩 4x。"

---

## A.7 推理优化 · 公司投递冷启动信模板（Cover Letter）

```
Subject: 实习申请 - 大模型推理优化方向 - [姓名] - [学校]

[HR 老师 / 招聘负责人] 您好，

我是 [姓名]，[双非学校名] 计算机硕士研二在读。虽然本科非 985/211，
但 5 个月内已系统补完 LLM 基础，独立完成以下工程级项目：

1. Qwen2.5-7B 生产级推理服务（vLLM + Triton kernel + 4 档量化）
   GitHub: github.com/[your-name]/production-llm-inference-stack
2. vLLM/SGLang/TGI 三大框架对比 benchmark（吞吐量提升 2-3x）
3. 4 篇技术博客累计阅读量 6000+
   知乎 / CSDN: [链接列表]

我特别关注 [具体公司] 的 [具体团队] 在 [具体技术方向] 的工作，
例如 [复述某个具体技术博客 / 博客中提到的痛点]。

附件为简历及 GitHub 主页，期待与您进一步沟通。

[姓名]
[手机] | [邮箱] | [GitHub]
```

---

## A.8 推理优化 · 兜底复习表（最后 2 周用）

| Day | 复习模块 | 重点 |
|---|---|---|
| D-14 | M1 引擎 | vLLM 调度 + PagedAttention 计算 + SGLang Radix |
| D-13 | M2 算子 | Triton kernel 手写 + FlashAttention 流程 |
| D-12 | M3 量化 | GPTQ/AWQ/SmoothQuant 数学推导各 1 遍 |
| D-11 | M4 调度 | speculative decoding + prefill-decode 分离 |
| D-10 | 模拟 1 | 全套 50 题顺序过（前 30 题） |
| D-9 | 查漏 | 30 题中卡壳的专题再精读 |
| D-8 | M1+M2 模拟面试（同学扮演面试官） |
| D-7 | M3+M4 模拟面试 |
| D-6 | 简历 / 项目 / 博客 串讲 3 遍 |
| D-5 | 50 题抽题 20 题（防止考原题不熟） |
| D-4 | 自我介绍 + 反问环节排练 |
| D-3 | mock interview 完整 1 次（含系统设计题） |
| D-2 | 放松 + 复盘 50 题笔记 |
| D-1 | 早睡 + 设备测试 |
| D-0 | 面试日 |

---

# 附录 C：岗 1 推理优化 · 开源项目驱动学习计划

## C.0 第一性原理分析：你的"源码→流程→手敲→论文"4 步法是否对？

### 路径对比

| 维度 | 传统路径：论文→算法→代码→工程 | 你提出的路径：源码→流程→手敲→论文 |
|---|---|---|
| 起点 | 理论（top-down） | 工程实现（bottom-up） |
| 学习风格 | 学院派 | 工程师派 |
| 上手速度 | 慢（理论先行） | 快（先看到成果） |
| 与岗 1 匹配度 | 中（理论扎实但工程弱） | 高（目标岗就是工程型） |
| 可能的问题 | 落地慢、易"纸上谈兵" | 易"知其然不知其所以然" |

### 你的方法**适合你**的判断 ✅

你提出这个路径的核心理由：
1. **方向匹配**：岗 1 是**工程实现型**岗位，论文不是产品，员工价值用代码 / throughput / latency 度量
2. **效率考量**：5 个月窗口紧张，论文→算法的传统路径会浪费 1-2 个月在定理证明上
3. **你已具备的基础**："偏工程实现"已经声明你的强项是写代码，工程→理论比理论→工程效率更高

### 但是**必须修补的 3 个风险** ⚠️

风险 1：**先入为主偏差**
> 看代码后看论文，会把作者的"trade-off 选择"误解为"唯一正确"——错过论文中明确写出的其他方案（baseline comparisons）和 "why not X"

修补：**论文阶段必须主动寻找"作者否决的方案"**——每篇论文读出"为什么作者没选 X / Y / Z"

风险 2：**工程噪音淹没核心**
> vLLM 10 万行代码中，核心调度 + attention ≈ 5000 行（5%）。如果你"读完 vLLM 全部代码"，90% 时间花在错误处理、配置解析、跨 GPU 通信上

修补：**采用"模块化精读"策略**——只读 3-5 个核心模块，跳过外围

风险 3：**横向抽象缺失**
> 只看实现，看不到 kernel / algorithm / system 三个层次的差异

修补：**手敲阶段同时手写"系统设计白板"**——讲清楚"如果让我重写我会怎么设计"，对比仓库里的实现

### 调整后的 4 步法（采纳你的内核，修复风险）

你的 4 步法框架不变，做以下微调：

| 步骤 | 你的原始 | 我的调整 | 调整理由 |
|---|---|---|---|
| 1. 源码 | 通读 | **快读 + 模块化精读**（先建地图，再精读 5-10% 核心） | 防噪音淹没 |
| 2. 流程 | 跑通 demo | **跑通 + Trace + 画 2 张图**（数据流 + 控制流，标注 shape） | 加深工程具象感 |
| 3. 手敲 | 复现 | **不复现仓库，从 0 自己起名写，注释全部用自己的话** | 强制深度，避免"抄" |
| 4. 论文 | 后期补 | **穿插式 + 反问式**（每读一段代码，反问自己"论文里作者会怎么说"） | 防后见之明 |

---

## C.1 强烈推荐的两个开源项目（基于 ROI 排序）

### 项目 A：**nanoGPT**（Andrej Karpathy）

- **仓库**：`https://github.com/karpathy/nanoGPT`
- **规模**：~300 行 Python（`train.py` + `model.py` + `sample.py`）
- **核心价值**：完整 toy GPT 实现（训练 + 推理）
- **必读指数**：⭐⭐⭐⭐⭐
- **门槛**：极低，能跑 PyTorch 训练即可
- **上手到 value**：30 分钟

### 项目 B：**vLLM**（UC Berkeley / LMSYS / Anyscale 主导）

- **仓库**：`https://github.com/vllm-project/vllm`
- **规模**：~10w 行 Python（C++ kernel 子模块）
- **核心价值**：业界事实标准 LLM serving 框架（SOSP'23 论文开源版）
- **必读指数**：⭐⭐⭐⭐⭐
- **门槛**：中高，但只精读 3 个模块可大幅降低门槛
- **上手到 value**：1-2 周（取决于 GPU 可用性）

---

## C.2 为什么是这两个项目（候选对比 + 排除法）

### 候选项目池

| 项目 | 语言 | 行数 | 价值 | 门槛 | 推荐度 |
|---|---|---|---|---|---|
| **nanoGPT** | Python | 300 | mini 完整 LLM | 极低 | ⭐⭐⭐⭐⭐ |
| **vLLM** | Python | 10w+ | 生产级 serving | 中高 | ⭐⭐⭐⭐⭐ |
| llama.cpp | C++ | 5w+ | CPU/边缘推理 | 中（C++） | ⭐⭐⭐ |
| flash-attention | CUDA/C++ | 1w+ | 极致 attention kernel | 高 | ⭐⭐⭐ |
| SGLang | Python | 5w+ | RadixAttention + DSL | 中 | ⭐⭐⭐ |
| TGI | Rust | 10w+ | HF 官方 serving | 高（Rust） | ⭐⭐ |
| TensorRT-LLM | Python/C++ | 20w+ | NVIDIA 官方 | 高 | ⭐⭐ |
| DeepSpeed-MII | Python | 3w+ | 微软推理 | 中 | ⭐⭐ |
| AutoGPTQ / AWQ | Python | 1w+ | 量化实现 | 中 | ⭐⭐⭐ |
| triton | Python | 3w+ | Python-to-GPU 编译器 | 中（要写 kernel） | ⭐⭐⭐ |
| Mini-LLM（教学） | Python | 500 | 简化版 vLLM | 低 | ⭐⭐⭐（**可选第二阶段**） |

### 排除法推理（为什么不要别的）

❌ **llama.cpp（C++）**：C++ 不在岗 1 主流 JD 中，MiniMax/智谱工程岗 JD 多写"Python + PyTorch + CUDA"。C++ 写 tokenizer / KV cache / quantization 是好的，但 ROI 比 vLLM 低
- **可选保留场景**：如果 W3-W4 发现自己对低层 GPU 内存布局有强烈兴趣，再回头读 llama.cpp 的 KV cache 部分

❌ **flash-attention**：kernel 级项目，含大量 CUDA C++ 和 template meta-programming。**对零基础 W1-W2 阶段过早**
- **可选保留场景**：W5 之后，作为项目 B 的延伸读 kernel 部分即可

❌ **SGLang**：太新（2024 起），仓库迭代频繁，且结构不如 vLLM 稳定（社区反馈）。对刚转 LLM 的人不友好
- **可选保留场景**：投 MiniMax / Stepfun 等公司可作为 W6-W8 的第二项目补充

❌ **TGI**：Rust 实现，需要 Rust 基础。岗 1 招聘 JD 几乎不要求 Rust

❌ **DeepSpeed-MII / TensorRT-LLM**：工程体量大、文档分散

✅ **为什么 nanoGPT + vLLM 是最优组合**

1. **范围互补**：nanoGPT 帮你建立"Transformer + 训练 + 推理"的**完整心智模型**；vLLM 在此基础上叠加"生产级 serving 的所有复杂度"
2. **门槛递进**：300 行 → 10w 行的跨度，刚开始可能不适应，但如果用"模块化精读"策略，可平滑过渡
3. **业界认可**：vLLM 是几乎所有目标公司 JD 第一关键词（vLLM, SGLang, TGI 三大框架里 **vLLM 是最常出现的**）
4. **技能栈匹配**：Python + PyTorch + asyncio + CUDA（vLLM 子模块）— 这正是岗 1 的 JD 关键词

---

## C.3 学习顺序：先 nanoGPT（W1-W2）再 vLLM（W3-W4+）

### 为什么不能反？

如果你先 vLLM：
- 10w 行代码里，第一周搞不清入口
- 注意力模块被 KV cache / block manager / async engine 包裹，无法聚焦
- 失去"为什么需要 KV cache"的朴素直觉

如果你先 nanoGPT：
- 看到朴素 attention 实现→推理时每 token 重新计算 → 性能差
- 自然带出"KV cache 是什么、为什么需要、PagedAttention 解决什么"的痛点
- 再看 vLLM 立刻有共鸣

→ **正确顺序：先小到大，先简到繁，先朴素到优化**

---

## C.4 项目 A：nanoGPT · 详细 4 步法（W1-W2，共 14 天）

### Step 1：源码精读（W1 前半 5 天）

| Day | 任务 | 产出 |
|---|---|---|
| Day 1 | 克隆仓库，跑 `python train.py`（默认配置），记录训练时长 | 训练好的 `ckpt.pt` |
| Day 1 | 通读 `train.py` 全文（约 150 行）：数据加载 → 模型初始化 → 训练循环 | 流程粗图 |
| Day 2 | 通读 `model.py`：GPT 类 / Block / CausalSelfAttention / MLP / LayerNorm / GELU | 类结构图 |
| Day 3 | 重点精读 `CausalSelfAttention.forward()`：QKV 拆分 → 缩放点积 → causal masking → Softmax → dropout → out 投影 | 公式对照笔记 |
| Day 3 | 重点精读 `MLP` 的 GELU 实现 + `Block` 的残差 + LayerNorm | 同上 |
| Day 4 | 读 `data/` 下的字符预处理和 tokenizer 构建 | tokenizer 笔记 |
| Day 4 | 跑 `python sample.py` 跑几轮生成，看效果 | 生成文本样本 |
| Day 5 | 改超参（block 数量 / 头数 / 学习率），观察 loss 曲线变化 | 对比实验 markdown |

**关键问题清单（带着读）**：
- [ ] `attn @ (q @ k.transpose(-2,-1)) * (1.0 / math.sqrt(k.size(-1)))` 中 `* (1/sqrt(d_k))` 来自哪里？
- [ ] `mask = torch.tril(torch.ones(...))` 的 causal mask 为什么这样设计？
- [ ] `nn.Parameter(torch.zeros(n_embd))` 用于 LayerNorm 的 gain 是为什么？
- [ ] 残差连接 `x = x + self.attn(self.ln_1(x))` 的顺序为什么先 LN 再 attention？

### Step 2：流程图（W1 后半 2 天）

画 2 张图（手画 + Markdown 描述）：

**图 1：数据流**（推理时）
```
text "Hello world"
       │
       ▼
[tokenizer.encode] ─→ tensor([15496, 995])
       │
       ▼
[wte + wpe] ─→ shape (T=2, n_embd=384)
       │
       ▼
[Block × 6]
   ├─ [LN1]
   ├─ [CausalSelfAttention]
   │   ├─ QKV = linear(x)            (T, 3*d)
   │   ├─ reshape → (B, T, 3, n_head, d_head)
   │   ├─ q,k,v 拆分
   │   ├─ att = q @ k.T / sqrt(d)    (B, n_head, T, T)
   │   ├─ mask = tril(ones(T,T))
   │   ├─ att = masked_fill(-inf)
   │   ├─ att = softmax(att)
   │   ├─ att = dropout(att)
   │   ├─ x = att @ v
   │   ├─ reshape & proj
   │   └─ out (T, n_embd)
   ├─ [residual: x = x + attn_out]
   ├─ [LN2]
   ├─ [MLP (Linear → GELU → Linear)]
   └─ [residual: x = x + mlp_out]
       │
       ▼
[LN_f]
       │
       ▼
[lm_head: linear(n_embd → vocab_size)] ─→ (T, vocab_size)
       │
       ▼
[sampler: top-k, temperature] ─→ token_id
       │
       ▼
[tokenizer.decode] ─→ "Hello world" + new token
```

**图 2：控制流**（训练循环 vs 推理循环对比表）

| | 训练 | 推理 |
|---|---|---|
| 输入 | batch 序列 | 1 条 prompt |
| 前向计算 | 整句一次性 | 1 token 接 1 token（自回归） |
| 损失 | cross-entropy(logits, target) | 无 |
| 反向 | yes（autograd） | no |
| 优化器 | AdamW step | 无 |
| 显存开销 | 激活 / 梯度 / 优化器状态都存 | 仅 KV（无 KV 缓存时，每步重算整句 attention） |

### Step 3：手敲复现（W2 前半 5 天）

**关键原则：不参考、不抄、变量名自己起**

| Day | 任务 |
|---|---|
| Day 1 | 新建 `my_lm/` 文件夹，从 0 写 `my_attention.py`：实现 scaled dot-product + causal mask + multi-head |
| Day 2 | 写 `my_block.py`：LN + attention + MLP + 残差 |
| Day 3 | 写 `my_model.py`：完整 GPT 模型 |
| Day 4 | 写 `my_train.py`：训练循环 + AdamW |
| Day 5 | 写 `my_sample.py`：推理循环 |

**自检清单**：
- [ ] 自己写的 attention 输出与 nanoGPT 在随机数据上**完全一致**（允许 <1e-5 浮点误差）
- [ ] 自己写的 GPT 在莎士比亚数据集上能训练到 loss < 2.0
- [ ] 训练时长与 nanoGPT 在同一硬件 ±20% 内

### Step 4：对照论文（W2 后半 4 天，结合 2-3 篇）

**论文 1**：*Attention Is All You Need* (NeurIPS 2017)
- 重点章节：3.1 / 3.2 / 3.3（看 Scaled Dot-Product Attention 公式）
- 重点问题：用论文公式对照自己写的 attention，找出 1-2 个未实现的部分

**论文 2**：*GPT-2* 论文 (Language Models are Unsupervised Multitask Learners)
- 重点章节：第 2 节（模型）+ 第 3 节（训练）
- 重点问题：为什么 GPT 用 LayerNorm？论文里怎么解释？

**论文 3**：*Llama*（可选 Touvron et al., 2023）
- 重点章节：第 2 节（前置 LayerNorm + RMSNorm）/ 第 3 节（SwiGLU）/ 位置编码（RoPE）
- 重点问题：RMSNorm vs LayerNorm 的代码差异 / RoPE 的复数旋转数学

### nanoGPT 阶段产出

- `my_lm/` 仓库：自己的手敲版 mini GPT
- `nanoGPT_notes/` 仓库：源码精读笔记（每天一篇）
- 1 篇公开博客：《从 0 写一个 GPT：300 行 vs 1000 行的工程化权衡》（知乎/CSDN）

---

## C.5 项目 B：vLLM · 详细 4 步法（W3-W4+ 持续到 W8）

### Step 1：模块化精读（W3 共 7 天）

**核心原则**：**不读全部 vLLM，只读 3 个核心模块 + 2 个外围接口**

#### 核心模块 A：`vllm/core/scheduler.py`（调度器，约 1000 行）
- 为什么选：调度决策直接决定 throughput，是面试最常考点（continuous batching、prefix caching）
- 重点函数：
  - `Scheduler.schedule()`：决定下一批要 forward 的请求
  - `Scheduler._add_seq()` / `_remove_seq()`：队列管理
  - `Budget` 类：KV cache 预算控制
  - 优先级策略：FCFS / SJF / priority

#### 核心模块 B：`vllm/attention/`（attention 计算）
- 为什么选：PagedAttention 是 vLLM 招牌创新
- 重点文件：
  - `vllm/attention/backends/xformers.py` / `flash_attn.py` / `paged_attn.py`
  - `vllm/attention/selector.py`：怎么选 backend
  - 重点函数：`PagedAttention.forward_with_block_table()`（理解 block_id → physical KV block 的映射）

#### 核心模块 C：`vllm/worker/`（worker 进程）
- 为什么选：模型并行 + KV cache 物理布局的工程体现
- 重点文件：
  - `vllm/worker/worker.py`：`Worker.execute_model()` 的执行链
  - `vllm/worker/model_runner.py`：实际跑 forward 的组件

#### 外围接口（只读接口签名，不读实现）：
- `vllm/entrypoints/api_server.py`：HTTP server 入口
- `vllm/engine/async_llm_engine.py`：异步 API 包装
- `vllm/model_executor/model_loader/`：模型加载器

#### 阅读顺序
```
第 1 天：跑通 `vllm serve Qwen/Qwen2.5-7B-Instruct`，看 HTTP 接口
第 1 天：通读 entrypoints/api_server.py 的入口逻辑
第 2-3 天：精读 vllm/core/scheduler.py（这是核心）
第 4-5 天：精读 vllm/attention/ 的 PagedAttention 实现
第 6-7 天：精读 vllm/worker/ 与 model_runner
```

### Step 2：流程图 + Trace（W3 后半 3 天）

**跑通流程**：
1. 在 1 张 4090 / A100 上跑 `vllm serve Qwen/Qwen2.5-7B-Instruct`
2. 用 `wrk` 或 `locust` 打并发 1000 个请求
3. 抓 trace：
   - HTTP POST → API server 收到 → AsyncLLMEngine.add_request() → EngineCore.process() → Scheduler.add_request() → Worker.execute_model() → forward → KV cache 写入 → response 流回

**2 张图**：

**图 1：一次推理请求的状态机**
```
[Idle] --新请求--> [Waiting Queue] --scheduler 轮询--> [Running] --生成 token--> [Running] --EOS 或 max_tokens--> [Finished] --> [返回 response]
   ↑
   └──── 调度失败（显存不足）──── [Recompute Queue]
```

**图 2：vLLM 一次 forward 的数据流**
```
input_ids (B, T) 
    ↓ embed
hidden_states (B, T, d) 
    ↓ 12 个 Block 堆叠（× n_layers）
    ↓ 每个 Block:
    ├─ LN
    ├─ QKV 投影 → split → reshape → (B*H, T, d_head)
    ├─ PagedAttention:
    │   ├─ query @ K_block_table
    │   ├─ softmax + V_block_table
    │   └─ out
    ├─ O 投影
    ├─ MLP (FC + GELU + FC)
    ↓
logits (B, T, vocab)
    ↓ sample
next_token (B,)
```

### Step 3：手敲 mini-vLLM（W4 共 7 天）

**目标**：写一个 ~500-1000 行的 mini-vLLM，**支持 Qwen2.5-0.5B 推理 + 连续 batching + PagedAttention**

**架构示意**：
```
mini_vllm/
├── my_block_manager.py    # 管理 KV cache 的物理 block
├── my_scheduler.py        # 连续 batching 调度
├── my_paged_attention.py  # PagedAttention forward
├── my_engine.py           # 整合，运行 forward
└── my_server.py           # 简易 HTTP 接口（FastAPI 即可）
```

**手写步骤**：
| Day | 任务 |
|---|---|
| Day 1 | 写 `my_block_manager.py`：实现 block 分配 / 释放 / prefix caching（用 dict 模拟 block table） |
| Day 2 | 写 `my_paged_attention.py`：用 PyTorch 实现 PagedAttention（不需要 CUDA，只是算法正确性） |
| Day 3 | 写 `my_scheduler.py`：连续 batching，调度 algorithm 让 batch 总是满 |
| Day 4 | 写 `my_engine.py`：把 Qwen2.5-0.5B 模型 + block manager + scheduler 串联 |
| Day 5 | 跑通！能对 Qwen2.5-0.5B 进行推理 |
| Day 6 | 用并发请求测试 mini-vLLM 和原 vLLM 的 throughput 对比（同一硬件） |
| Day 7 | 写 README：架构图、性能对比、可改进点 |

**自检清单**：
- [ ] mini-vLLM 在 10 并发请求下不崩
- [ ] 与原 vLLM throughput 在 ±50% 内（0.5B 模型应接近 naive PyTorch 但不是 vLLM 加速版）
- [ ] block manager 能正确处理变长序列
- [ ] prefix caching 正确（用相同 prefix 的两个请求复用了 KV）

### Step 4：对照论文（W4 后半 4 天，结合）

**论文 1**：*Efficient Memory Management for Large Language Model Serving with PagedAttention* (Kwon et al., SOSP 2023)
- 必读章节：Abstract / §3 / §4 / §6
- 重点问题：
  - 为什么 vLLM 选择 block size 16？
  - vLLM 如何处理 beam search 的复制？
  - chunked prefill 的 motivation 是什么？

**论文 2**：*FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness* (Dao et al., NeurIPS 2022)
- 重点章节：§3 算法
- 重点问题：FlashAttention 与 PagedAttention 怎么结合？

**论文 3**：*DeepSeek-V3 Technical Report*（节选推理部分）
- 重点章节：关于 MLA、FP8、MoE inference

**论文阅读技巧——第一性原理角度**：
- 每读完论文一节，**强迫自己写一段"对比代码中实现"**：比如"论文里写 block size 选择 16 是实验得出的，代码里硬编码 16 是否合理"
- 找"作者否决的方案"——论文中"为什么不选 baseline X"的章节通常被忽略，但这是面试常考点

### vLLM 阶段产出

- `mini_vllm/` 仓库：自己手写的简化版
- `vllm_notes/` 仓库：3 个核心模块的源码精读笔记（共 30+ 篇）
- 1 篇公开博客：《从 vLLM 源码看 PagedAttention：为什么是 block size 16 而不是 32》
- 1 篇公开博客：《Mini-vLLM 手写全记录：500 行复现 vLLM 调度核心》

---

## C.6 横跨 nanoGPT + vLLM 的 5 个月日历视图

```
W1  ┃ ▓▓▓░░ ░░░░░ ┃ nanoGPT Step 1 (源码精读)
W2  ┃ ░░▓▓▓ ▓▓▓░░ ┃ nanoGPT Step 2 (流程图) + Step 3 (手敲) + Step 4 (论文)
W3  ┃ ░░░░ ▓▓▓▓▓ ┃ vLLM Step 1 (源码 3 模块精读)
W4  ┃ ░░░░ ░░▓▓▓ ┃ vLLM Step 2 (Trace+流程) + Step 3 (mini-vLLM)
W5-W7 ┃ ░░░░░░░░░ ┃ vLLM 扩展（量化、FlashAttention 集成、speculative decoding）
W8  ┃ ░░░░░░░░░ ┃ 复盘、查漏、补笔记、补博客
W9-W22 ┃ ░░░░░░░░░ ┃ 转 Month 3 后训练工程化（岗 2 主线），W13 用 mini-vLLM 做旗舰项目
```

**关键节点**：
- **W2 末**：自己写的 mini GPT 训练+推理完整跑通
- **W4 末**：mini-vLLM 完成（500-1000 行 PyTorch + 简单 HTTP 接口）
- **W5-W8**：复用 mini-vLLM 加量化、FlashAttention 集成、speculative decoding
- **W13**：用 mini-vLLM 作为旗舰项目核心，结合 vLLM 真实部署，做"推理优化旗舰项目"（参考附录 A 的 production-llm-inference-stack 模板）

---

## C.7 验证清单（岗 1 学习计划成功标志）

W4 末你应该能回答以下问题：

1. **nanoGPT 知识**：
   - [ ] 不看任何资料，手写 scaled-dot-product attention（30 行 PyTorch）
   - [ ] 解释 causal mask 为何能并行化训练解码的 GPT
   - [ ] 手写一段 LayerNorm，并解释为何放在 attention 之前是"pre-norm"（Llama 风格）

2. **vLLM 知识**：
   - [ ] 凭记忆画出 vLLM 一次请求的完整数据流（从 HTTP 到 GPU kernel）
   - [ ] 解释 block size 16 对吞吐和碎片的影响
   - [ ] 解释 continuous batching 与 static batching 的差异
   - [ ] 解释 prefix caching 的 block 复用规则
   - [ ] 能说清 vLLM 与 SGLang 的 3 个主要差异

3. **手敲能力**：
   - [ ] mini-vLLM 仓库有 README、有 benchmark、对原始 vLLM 有清晰改进方向

4. **论文理解**：
   - [ ] PagedAttention 论文能列出 3 个 baseline 与 vLLM 的 trade-off
   - [ ] FlashAttention 论文能用自己的话讲清楚 tiling 为什么能省 IO
   - [ ] 找 1 篇最近 3 个月的 vLLM-arxiv 工作，能用一张图概括其核心创新

---

## C.8 可选第三项目（如果 W6 还有精力）

如果 W5-W6 还想继续深入，可加一个**有针对性的**第三项目：

| 偏好 | 项目 | 学习重点 |
|---|---|---|
| 强化 CUDA / Triton 内功 | **flash-attention**（Tri Dao 仓库） | CUDA kernel 写法 + tiling + FlashAttention-2/3 的演进 |
| 强化 CPU / 边缘部署 | **llama.cpp** | C++ + 量化 + ggml 张量库 |
| 看更多 serving 架构对比 | **SGLang** | RadixAttention + DSL（结构化 generation） |
| 强化量化的工程实现 | **AutoGPTQ + AWQ** | GPTQ 的 Hessian 计算 + AWQ 的激活感知 scale |
| 看 PyTorch 底层 | **torchtitan**（PyTorch 官方）+ **torch.compile** | PyTorch native LLM 框架 + 计算图编译 |

**不建议**：
- ❌ 不要在 W5 之后还读 huggingface/transformers 全仓库（太大太杂）
- ❌ 不要被"完整跑通一个超大项目"诱惑（团队越大你越抓不住主线）

---

## C.9 仓库结构最终样态

```
github.com/[your-name]/llm-intern-prep
├── README.md                              # 总入口
├── 01-nanoGPT/
│   ├── my_lm/                             # 自己手敲的 mini GPT
│   ├── nanoGPT_notes/                     # 源码精读笔记
│   └── blog_urls.md
├── 02-mini-vllm/
│   ├── my_mini_vllm/                      # 自己手敲的 mini-vLLM
│   ├── vllm_notes/                        # 3 个核心模块笔记
│   └── blog_urls.md
├── 03-quantization-bench/                 # W7 量化专题产物
├── 04-finetune-from-scratch/              # W9-W12 后训练产物
├── 05-flash-attention-notes/              # W5-W8 补充阅读
└── papers/                                # 13 篇 P0 + 论文笔记
```

GitHub 主页置顶 `01-nanoGPT/my_lm` 和 `02-mini-vllm/my_mini_vllm`，这两个是简历最强武器。

---

## C.10 岗 1 · 第一性原理总结

> **5 个月能成的原因**：vLLM 是工程密集型项目**而非数学密集型**——这意味着你不需要证明定理，只需要读懂代码、写对代码、跑出 benchmark。**双非的劣势（学术资源不足）在这个岗类几乎不影响**。你的所有焦虑都应该在"读完多少行代码""写过多少行代码"上量化。

> **学习公式**：(vLLM 调参经验) + (自己的代码量) + (3 篇公开博客) = **过简历关 + 过一面 + 过二面**。


