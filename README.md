<p align="center">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
  <img src="https://img.shields.io/badge/format-Agent%20Skill-blue" alt="format">
  <img src="https://img.shields.io/badge/语言-中文-orange" alt="language">
  <img src="https://img.shields.io/badge/platform-Coze%20%7C%20ComfyUI%20%7C%20GPT--Image--2-purple" alt="platform">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="version">
</p>

<h1 align="center">cys 人像动作迁移提示词库</h1>

<p align="center">
  <b>专为人像生成 · 动作迁移 · 图生视频工作流量身定制的 AI 摄影提示词工程技能</b><br>
  基于 5000+ 条真实出图提示词提炼的中文 9 段式模板、动作迁移硬性约束、风格预设与英文 GPT 摄影风
</p>

<p align="center">
  <b>作者：</b> cys &nbsp;·&nbsp; <b>适用模型：</b> ComfyUI(Flux2 Klein / Z-Image) · GPT Image 2 · Wan · LTX
</p>

---

## 📑 目录

- [✨ 特性](#-特性)
- [🎯 解决什么痛点](#-解决什么痛点)
- [📂 目录结构](#-目录结构)
- [🚀 安装与使用](#-安装与使用)
- [🧩 中文 9 段式模板](#-中文-9-段式模板)
- [🎬 动作迁移硬性约束](#-动作迁移硬性约束)
- [🎨 风格预设](#-风格预设)
- [💡 使用示例](#-使用示例)
- [📄 文件说明](#-文件说明)
- [📜 许可证](#-许可证)
- [⚠️ 免责声明](#-免责声明)

---

## ✨ 特性

| 能力 | 说明 |
|---|---|
| **中文 9 段式模板** | 人物→面容→妆容→身材→装饰→动作→服装→环境→摄像，真实感内核跨图复用，变量段每图定制 |
| **动作迁移硬性约束** | 强制垂直站姿 / T-pose / 鞋履入镜 / 头≤25%·腿≥65%，让骨架识别与人物替换一次成功 |
| **头身比修正技法** | 来自 V1→V5 真实迭代：提示词 + LoRA 权重 + 机位三件套联动把 1:5.5 拉回 1:7~1:7.5 |
| **10 大风格预设** | 国风 / 华丽 / 战甲 / 仙侠 / 赛博朋克 / 抖音爆款等，含鞋履配色与服装签名词库 |
| **双路线提示词** | 路线 A 中文分段（ComfyUI / CLIP 中文更优）；路线 B 英文摄影风（GPT Image 2 胶片质感） |
| **负向词库 + 平台写法** | 覆盖 ComfyUI / GPT Image 2 / Midjourney / DALL·E 的写法差异与反 AI 痕迹负向词 |

---

## 🎯 解决什么痛点

本技能服务于一条完整的 **AI 内容生产流水线**：

```
GPT Image 2 / ComfyUI 生成全身参考图  ──(本技能产出提示词)──▶  动作迁移 / 姿势迁移
        │                                                              │
        ▼                                                              ▼
   图生视频  ──────────────────────────────────────────────▶  抖音 / TikTok 发布
```

- **头号痛点**：全身像「头大身小」（比例 1:5，目标 1:7~1:7.5）——见下方头身比修正技法。
- **角色资产**：`cys001` / `cheng002` / `shuazi` 等角色 LoRA 会叠加进图，提示词需反向补偿其头部放大偏置。
- **业务落点**：可沉淀为可复用的提示词生产资产，服务于 AI 工作流定制。

---

## 📂 目录结构

```
cys-migration-skill/
├── SKILL.md                      # 技能主体：模板、约束、技法、风格、示例
├── references/                   # 参考知识库（按需加载）
│   ├── style-presets.md          # 国风 / 华丽 / 战甲 / 仙侠 / 鞋履配色词库
│   ├── global-knowledge.md       # 负向词库 / 文化增强 / 多平台写法差异
│   └── dance_fashion-trends.md   # 抖音 / TikTok 跳舞穿搭爆款库
├── LICENSE                       # MIT
└── README.md                     # 本文件
```

---

## 🚀 安装与使用

### 方式一：扣子（Coze）编程
1. 打开 **coze.cn** → 右侧栏「扣子编程」→「技能」选项卡。
2. 点右上角「上传 Skill 文件包」，选择本仓库打包的 `.zip`。
3. 系统自动解析 `SKILL.md`，部署后即可在对话框 `@` 调用。

### 方式二：本地 / 兼容 Agent Skills 的客户端
将本仓库整体放入技能的加载目录（如 WorkBuddy 的 `skills/`、Claude 的 skill 目录），客户端会按 `SKILL.md` 的 frontmatter 自动注册。

### 方式三：手动复制提示词
直接打开 `SKILL.md`，按需求套用 9 段式模板，复制生成的提示词粘贴到 ComfyUI / GPT Image 2 即可出图。

---

## 🧩 中文 9 段式模板

顺序固定，前 4 段「面容 / 妆容 / 身材 / 装饰」是**真实感内核**（跨图高度复用），后 5 段为变量段：

```
人物：[人设]，[景别]，[场景]，年龄约20岁左右的青春年华，[站姿类型]，展现完美身材比例
面容：[真实感内核 · 东方辨识度精致五官 / 水光肌 / 圆眼有神 / 瓜子脸]
妆容：[真实感内核 · 眼妆神采 / 裸粉唇釉 / 无瑕水光底妆]
身材：[真实感内核 · 匀称挺拔 / 曲线自然 / 白皙透粉凝脂水光肌]
装饰：[发色 / 珠宝配饰 / 美甲，可按需改]
动作：[迁移范式：垂直站立 T-pose；或自由范式：重氛围]
服装：[视觉重心在下半身，写明鞋履四要素：跟高+鞋头+材质+细节+「清晰完整展示在画面最底部」]
环境：[具体场景 + 前景画框 + 中景 + 远景 + 光效 + 主色调]
摄像：[迁移范式：全身等比无畸变 / 头≤25% / 腿≥65% / 鞋履清晰；或自由华丽范式]
```

> 原则：**提示词本体用中文**（中文描述 + 英文摄影参数），复杂详细优先，长度无限制。

---

## 🎬 动作迁移硬性约束

生成「动作迁移源图」时**逐条核对**，缺一条就补：

- [ ] 全身垂直站立 / 标准采集站姿（T-pose）
- [ ] 双脚平行或并拢，双手自然下垂贴身体两侧，手指放松
- [ ] 头部正直、面部正对镜头、下巴微收；双肩下沉水平；脊柱笔直；双膝伸直；脚踝并拢
- [ ] 鞋履完整入镜、清晰可见，占比 ≥ 画面高度 6%
- [ ] 头部面部占比 ≤ 画面总高 25%；腰部到脚底腿部区域 ≥ 人物高 65%
- [ ] 全身等比无畸变、无透视压缩；无 AI 痕迹

---

## 🎨 风格预设

内置 10+ 风格签名，例如：

| 风格 | 关键词方向 |
|---|---|
| 国风 / 唐风 | 齐胸襦裙、云头锦履、牡丹园、汉白玉栏杆、琉璃金 |
| 仙侠 | 清冷仙姬、长裙飘逸、山湖晨雾、银线绣纹 |
| 华丽 / 抖音爆款 | 绚丽背景、强虚化、高饱和主色、霓虹光效 |
| 战甲 | 金属护甲、战损质感、冷调打光（替代易误审的「破甲」表述） |
| 赛博朋克 | 霓虹光效、湿润街面反射、全息 UI、紫青配色 |

完整鞋履配色、服装签名见 `references/style-presets.md`。

---

## 💡 使用示例

**示例 A · 中文 9 段式（动作迁移源图 · 唐风）**

```
人物：清丽雅致的中国少女模特，全身垂直站立照，大唐盛世的牡丹园，年龄约20岁左右的青春年华，标准采集站姿，展现完美身材比例
面容：[套用真实感内核：东方辨识度精致五官 / 水光肌 / 圆眼有神 / 瓜子脸]
妆容：[套用真实感内核]
身材：[套用真实感内核]
装饰：[黑长直发，简约珠宝配饰]
动作：[迁移范式] 脚穿胭脂红云头锦履，平底，鞋面胭脂红织锦盘金绣凤穿牡丹纹，鞋口滚金边清晰完整地展示在画面最底部
服装：视觉重心在下半身：齐胸襦裙高腰及踝，胭脂红长裙自胸前高腰线垂坠及踝，裙摆微A字占据画面4/5；上半身月白真丝大袖对襟衫，内搭同色系抹胸，脚穿胭脂红云头锦履清晰完整展示在画面最底部
环境：大唐盛世牡丹园，层层牡丹在午后阳光下娇艳欲滴，汉白玉栏杆蜿蜒，远处大明宫飞檐金碧辉煌，整体色调以牡丹粉、汉白玉白与琉璃金为主
摄像：[迁移范式] 全身等比无畸变，头≤25%，腿≥65%，鞋履清晰可见
```

**示例 B · 英文摄影风（GPT Image 2 · 仙门圣女）**

```
Full body photograph of a young Chinese woman, celestial maiden. She wears a floor-length soft lilac sheer silk hanfu with silver snowflakes. Jewelry: floral hair ornaments, silver hoops, turquoise bead necklace. Footwear: ivory silk slippers with silver cloud embroidery. Standing naturally with arms at her sides, feet parallel on the ground, looking calmly at the camera with mouth closed. Background: Mountain lake at dawn with mirror-still water reflecting pine-covered peaks, mist hovering over the surface, ancient stone steps leading to the water. Shot on 50mm prime lens at f/2.8, natural soft diffused lighting, shallow depth of field, Kodak Portra 400 film, sharp focus on face.
```

---

## 📄 文件说明

- **`SKILL.md`**：技能主体。`---` 之间的 frontmatter（`name` + `description`）供客户端自动识别；正文含模板、约束、头身比技法、风格预设与完整示例。
- **`references/`**：三个参考知识库，按需加载，避免主文件过长：
  - `style-presets.md` — 风格与鞋履配色词库
  - `global-knowledge.md` — 负向词库与多平台写法差异
  - `dance_fashion-trends.md` — 抖音 / TikTok 跳舞穿搭爆款

---

## 📜 许可证

本项目以 **MIT License** 开源，详见 [LICENSE](./LICENSE)。

---

## ⚠️ 免责声明

本技能提供的模板与提示词**仅供 AI 图像生成学习与创作使用**。出图效果取决于具体模型、LoRA 权重与采样参数，请在你自己的环境中充分测试后再用于生产。作者不对因使用本技能产生的任何结果负责。

---

<p align="center">Made by <b>cys</b> · AI 摄影提示词工程</p>
