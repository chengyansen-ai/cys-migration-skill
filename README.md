<p align="center">
  <img src="https://img.shields.io/badge/version-v4.0.0-blue?style=flat-square" alt="version">
  <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="license">
  <img src="https://img.shields.io/badge/format-Agent%20Skill-blueviolet?style=flat-square" alt="format">
  <img src="https://img.shields.io/badge/语言-中文-orange?style=flat-square" alt="language">
  <img src="https://img.shields.io/badge/platform-通用-success?style=flat-square" alt="platform">
  <img src="https://img.shields.io/badge/风格预设-30%2B-brightgreen?style=flat-square" alt="styles">
  <img src="https://img.shields.io/badge/生产实测-Krea2%20Verified-ff69b4?style=flat-square" alt="krea2">
  <img src="https://img.shields.io/badge/数据样本-5%2C000%2B%20条-9cf?style=flat-square" alt="data">
</p>

<br>

<h1 align="center">🎬 cys 全能 AI 人像提示词工程技能库</h1>

<p align="center">
  <b>9 段式模板 × Krea2 生产级实测 × 跨平台通用</b><br>
  从真实出图中淬炼的人像提示词方法论 —— 让每一段提示词都能直接出图
</p>

<p align="center">
  <b>作者</b> cys &nbsp;·&nbsp; <b>适配</b> Coze / Dify / Claude / Codex / ComfyUI / Krea2 / GPT Image 2<br>
  <b>核心理念</b> 真实感第一 · 量产先行 · 数据驱动
</p>

<br>

---

## 📊 数据全景

本技能的所有模板、约束、参数，均来自 **自有实测语料 + 全球文献爬取 + 平台热点挖掘 + 真实出图迭代**：

| 数据来源 | 规模 | 用途 |
|---|---|---|
| **自有提示词库** | **5,000+ 条** | 提炼"写法基因" → 9 段式模板与真实感内核 |
| **全球指南深抽取** | **22 篇**（跨欧美/中东/日韩/拉美/国内） | 验证公式共识、负向词库、文化增强技法 |
| **平台热点整站深爬** | **4,141+ 条**（抖音/TikTok/小红书/B站/微博/IG/YT） | 跳舞穿搭爆款词库、鞋履热点趋势 |
| **模板合集精读** | **80+ 份**，高相关精读 **16 份** | 补全国风/仙侠/华丽写法细节 |
| **公式交叉验证** | **4 大体系** | 证明 9 段式模板方向正确 |
| **学术方法论** | **1 篇** ACM IMX'23 | 文化提示词增强（Cultural Prompt Augmentation） |
| **⚡ 实测验证** | **Krea2 生产环境**出图迭代 | 参数级实操验证，非理论推导 |

> 💡 **核心亮点**：本技能不是纸上谈兵的理论模板——全部参数经过 Krea2 两阶段 hires-fix 管线实测，头身比从 1:5 修正到 1:7~1:7.5 ✅

---

## ✨ 核心能力一览

### 🧩 提示词引擎

| 能力 | 说明 |
|---|---|
| **中文 9 段式模板** | 人物→面容→妆容→身材→装饰→动作→服装→环境→摄像，前 4 段跨图复用，后 5 段每图定制 |
| **双版本输出** | ✨ 支持 **全身照**（ComfyUI 运用源图）+ **上半身中景照**（视频成片参考） |
| **ComfyUI 运用硬性约束** | 垂直站姿 / T-pose / 鞋履入镜 / 头≤25%·腿≥65%，带 CHECK LIST |
| **30+ 种风格预设** | 10 类国风形制 + 20+ 类现代/海外美学 |
| **CLIP 选型速查** | Klein 9B→Qwen3-8B / Flux.1→T5-XXL / LongCLIP 破 77 token |

### 🔬 生产实测（最有价值）

| 能力 | 说明 |
|---|---|
| **Krea2 管线实测** | ✅ Node 109 负向词模板（1.5 权重分层）<br>✅ CFG 黄金法则（粗采 3.0 / 精修 1.0）<br>✅ LoRA 三件套机制（enable_lora? / Strength / Trigger） |
| **头身比修正技法** | Token 权重反转 + LoRA ≤0.6 + 低角度仰拍，1:5 → 1:7~1:7.5 |
| **协调生成 v3 方法论** | 15 大风格类 × 专属词库，领×袖冲突检测，抖音精确短语合规 |
| **批量生成能力** | 千条级生成器已验证：1000 条全唯一、零重复、零违规 |

### 🌐 跨平台

| 能力 | 说明 |
|---|---|
| **安装方式** | Coze 编程 / Dify / Claude Code / Codex CLI / Cursor / Windsurf / Cline / Aider / Continue / 爱马仕 |
| **全球知识加固** | 22 篇指南沉淀 + 跨文化美学签名 + 4 大公式共识 + ACM 文化增强 |

---

## 🎯 解决什么痛点

无论用哪个平台出人像图，以下痛点本技能可直接规避：

| # | 痛点 | 后果 | 解法 |
|---|---|---|---|
| 1 | **头大身小**（1:5 → 目标 1:7） | ComfyUI 运用判失败 | Token 反转 + LoRA ≤0.6 + 低角度仰拍 |
| 2 | **鞋履被裁切** | 骨架替换吃不到脚 | 硬约束鞋履≥6% + 负向词双保险 |
| 3 | **塑料感 / 一键 AI 脸** | 视频被识破，不推流 | 真实感内核 + 负向词防护 |
| 4 | **透视畸变** | 广角拉长或压缩 | 全身等比无畸变 + 50mm/135mm 镜头 |
| 5 | **头占比偏高** | 压不下头部 | 低角度仰拍 + 强制头≤25% |
| 6 | **动作过多** | 人物漂移、穿模 | T-pose 范式，四肢自然垂直 |
| 7 | **背景空洞** | 平台不推流 | 绚丽 + 画框感 + 主色三件套 |
| 8 | **LoRA 放大头部** | 比例失衡 | 降权 + 提示词反向补偿 |

---

## 🚀 快速安装

本技能采用 **Anthropic Agent Skills 开放格式**（`SKILL.md` + `references/`），主流平台均可加载。

| 平台 | 安装方式 |
|---|---|
| **Coze 编程** | 上传打包的 `.zip`（含 `SKILL.md`），系统自动解析 |
| **Dify** | 提示词模板法：嵌入 9 段式模板 + `{{变量}}` 占位 |
| **Claude Code** | 放入 `~/.claude/skills/cys-migration-skill/` |
| **Codex CLI** | 放入 `~/.codex/skills/cys-migration-skill/` |
| **Cursor / Windsurf / Cline / Aider / Continue** | 放入对应 skills 目录 |
| **爱马仕（Hermes）等国产平台** | 按提示词模板接入 |
| **手动法** | 打开 `SKILL.md` 直接复制提示词使用 |

---

## 🧩 9 段式模板速览

```
人物：[人设]，[景别]，[场景]，年龄约20岁左右的青春年华，[站姿类型]
面容：[真实感内核：东方精致五官 / 水光肌 / 圆眼有神 / 瓜子脸]
妆容：[真实感内核：清透底妆 / 淡雅眼妆 / 裸粉唇釉]
身材：[真实感内核：匀称挺拔 / 曲线自然 / 白皙透粉凝脂肌]
装饰：[发色 / 珠宝配饰 / 美甲，可按需改]
动作：[ComfyUI 运用范式：垂直站立 T-pose；或自由范式：重氛围]
服装：[视觉重心在下半身，鞋履四要素：跟高+鞋头+材质+细节]
环境：[具体场景 + 前景画框 + 中景 + 远景 + 光效 + 主色调]
摄像：[头≤25% / 腿≥65% / 鞋履≥6% / 全身等比无畸变]
```

> 原则：**提示词本体用中文**，复杂详细优先，长度无限制。

### 两种构图输出

| 场景 | 全身照（ComfyUI 运用源图） | 上半身中景照（视频成片参考） |
|---|---|---|
| **段1 景别** | 全身垂直站立照，标准采集站姿 | 上半身中景构图（取景至腰部以上） |
| **段6 动作** | 双脚并拢重心均匀，T-pose 全身采集 | 上半身范式：正面直立，双手自然摆放 |
| **段7 鞋履** | 鞋履入镜，清晰展示在画面最底部 | 鞋履不入镜，与下半身协调搭配 |
| **段9 约束** | 鞋履≥6%，头≤25%，腿≥65% | 85mm 镜头，头面部≤40% |

---

## 📋 ComfyUI 运用硬性约束（CHECK LIST）

生成运用源图时，**逐条核对**：

- [ ] 全身垂直站立 / 标准采集站姿（T-pose）
- [ ] 双脚平行或并拢，双手自然下垂贴身体两侧
- [ ] 头部正直、面部正对镜头；双肩下沉；脊柱笔直
- [ ] **鞋履完整入镜，占比 ≥ 画面高度 6%**
- [ ] **头部占比 ≤ 画面总高 25%；腿部区域 ≥ 人物高度 65%**
- [ ] 全身等比无畸变、无 AI 痕迹
- [ ] 8K 超高清、RAW 格式、焦点从头到脚清晰锐利
- [ ] 构图居中，人物占画面约 80% 高度

---

## 🔬 Krea2 生产参数实测（2026-07-08 验证）

> ⚡ 这是本技能**最值钱的内容**——来自 `生图-01-批量动漫.json` 工作流，经多轮出图验证的参数，直接复制可用。

### 两阶段 hires-fix 管线

| 阶段 | 采样器 | 步数 | CFG | 调度器 | 分辨率 |
|---|---|---|---|---|---|
| 粗采 | KSamplerAdvanced | 8 | **3.0** | linear_quadratic | 1080×1920 |
| 放大 | ImageUpscaleWithModel | — | — | — | — |
| 精修 | KSamplerAdvanced | 10 | **1.0** | euler / simple | latent 输入 |

### CFG 黄金法则

```
粗采 CFG=3.0 → 锁定画风，细节最佳
精修 CFG=1.0 → 避免过强引导崩坏人脸
⚠ 永不用 CFG=0 → 粗采阶段需要 CFG=3.0 维持构图稳定
```

### Node 109 负向词模板（实测版，权重分层）

```
(worst quality:1.5), (low quality:1.5), (bad anatomy:1.3), (bad hands:1.3),
(extra fingers:1.4), (missing fingers:1.4), (mutated:1.3), (deformed:1.3),
(ugly:1.3), (bad proportions:1.3), (blurry:1.2), (oversaturated:1.2),
(photorealistic:1.3), (realistic:1.3), (3d render:1.3), (cgi:1.2),
(watermark:1.2), (text:1.2), (signature:1.2), (username:1.2)
```

> ComfyUI 运用图追加：`cropped feet, shoes missing, (head too big:1.4)`

| 权重层 | 作用 |
|---|---|
| **1.5**（最高） | 质量兜底：worst/low quality |
| **1.3-1.4** | 解剖防错 + Krea2 防漂移 |
| **1.2** | 噪声过滤 |

### LoRA 三件套机制

| 参数 | 说明 | 建议值 |
|---|---|---|
| `enable_lora?` | LoRA 开关 | `true` |
| `LoRA Strength` | 权重 | **≤ 0.6**（角色 LoRA 放大头部偏置，必须降权） |
| `Trigger Word` | 训练触发词 | 按角色填写 |

> **实测结论**：头身比 1:7~1:7.5 ✅、垂直 T-pose ✅、鞋履 6-8% ✅、五官/皮肤/背景达标 ✅
>
> 常见短板已通过负向词与 CHECK LIST 兜底：手部融合 / 裙装形制 / 膝踝过渡 / 光影一致 / 发丝质感

---

## 📈 头身比修正技法（从 1:5 到 1:7~1:7.5）

**提示词 + LoRA 权重 + 机位**三段联动，缺一不可：

```
1️⃣ Token 权重反转（最关键）
   面部描述→精简版（去"脸/眼/唇"冗余形容词）
   腿脚描述→强化版（下半身占 4/5、鞋履≥6%、腿≥65%）
   原理：描述重心 = 模型画面重心

2️⃣ LoRA 权重 ≤ 0.6
   角色 LoRA 训练数据多为特写→天然放大头部
   关闭冲突放大类 LoRA，保留细节增强 LoRA

3️⃣ 135mm + 膝高机位
   长焦压缩透视拉长身形 + 低角度自然压头
   提示词中呼应："全身等比无畸变无透视压缩"

4️⃣ 硬约束兜底
   头≤25% + 腿≥65% + 鞋履≥6%
```

> 国外论坛印证：Krea2 实例用 `low-angle camera perspective` 拉长身形；全身常见坑 `two heads / not full body` → 印证本技法有效。

---

## 🧠 CLIP / 文本编码器速查

| 底模 | 推荐 CLIP | 节点 | 备注 |
|---|---|---|---|
| **Klein 9B** | `qwen_3_8b.safetensors` | LongCLIPTextEncodeFlux | 中文最优，超长提示词需 LongCLIP |
| **Klein 4B** | `qwen_3_4b.safetensors` | LongCLIPTextEncodeFlux | 轻量版 |
| **Krea2** | Krea2 专用 CLIP（type=krea2） | 标准文本编码 | 原生超长上下文，无需 LongCLIP |
| **Flux.1** | T5-XXL | CLIPTextEncodeFlux | Klein 链路不通用 |
| **Z-Image** | Qwen3-8B CLIP | LongCLIPTextEncodeFlux | 遵循 Flux 链路配置 |

---

## 🎨 风格预设（30+ 种）

### 国风 · 10 类形制

| 风格 | 关键词 | 配色 |
|---|---|---|
| 🏮 魏晋风骨 | 黛蓝罗纱交领、竹林晨雾 | 翠竹绿 · 晨雾白 · 光束金 |
| 🌸 唐风盛世 | 齐胸襦裙、云头锦履、牡丹园 | 牡丹粉 · 汉白玉白 · 琉璃金 |
| 🏯 宋制清雅 | 雪白百迭裙、天青褙子 | 天青 · 雪白 · 水绿 |
| 🏛️ 明制端庄 | 石青百褶长裙、玄黑立领长袄 | 汉白玉白 · 琉璃金 · 地砖灰 |
| 🎭 民国名媛 | 改良旗袍、老洋房爵士 | 旗袍色 · 老上海暖黄 · 暗红 |
| 🏜️ 敦煌西域 | 飞天披帛、金箔阔腿、莫高窟 | 壁画彩 · 赭红 · 光束金 |
| 🌙 暗黑哥特 | 丝绒曳地裙、古堡彩窗 | 深夜蓝 · 银 · 火光橙 |
| 🤠 西部牛仔 | 高腰牛仔、流苏皮马甲 | 牛仔蓝 · 荒漠赭 · 落日金 |
| 🌲 童话森林 | 层叠薄纱、苔藓森林 | 翠绿 · 金 · 童话粉彩 |
| 🏙️ 当代风尚 | 解构半裙、艺术画廊 | 白 · 水磨石灰 · 画作彩 |

### 现代 / 海外 · 20+ 种美学

```
赛博朋克   | 哑黑机能风衣、霓虹街区、全息 UI
日式和风   | 振袖和服、桐木屐、岚山竹林
韩系韩服   | 高腰齐胸长裙、盘发发簪、韩屋庭院
运动机能   | 冲锋衣、束脚机能裤、徒步靴
复古港风   | 亮片吊带、霓虹茶餐厅、镜面银
芭蕾舞者   | 交叉绑带 leotard、薄纱蓬裙、练功房
Mob Wife   | 皮草大衣、豹纹紧身裙、霸气黑帮感
Quiet Luxury | 无 logo 羊绒、挺括西装、old money
Coquette   | 巴洛克蕾丝、蝴蝶结、doll-like 甜欲
美拉德     | 大地色系叠穿、焦糖/咖啡/卡其
多巴胺     | 高饱和亮色、趣味图案
法式优雅   | 碎花茶歇裙、丝巾、左岸咖啡馆
英伦学院   | 格纹西装、针织马甲、百褶裙
北欧极简   | 燕麦廓形大衣、直筒西裤
波西米亚   | 流苏开衫、印花长裙、旷野花海
蒸汽朋克   | 铜扣长风衣、齿轮护目镜、黄铜工厂
未来科幻   | 银白连体服、发光线路、悬浮都市
```

> 完整鞋履/配色/环境词库见 `references/style-presets.md`

---

## 💡 使用示例

**示例 A · 中文 9 段式（ComfyUI 运用源图 · 唐风）**

```
人物：20岁亚洲年轻女性，全身垂直站立照，大唐盛世的牡丹园，标准采集站姿
面容：[套用真实感内核]
妆容：[套用真实感内核]
身材：[套用真实感内核]
装饰：[黑长直发，简约珠宝配饰]
动作：[ComfyUI 运用范式] 脚穿胭脂红云头锦履，平底，鞋面盘金绣凤穿牡丹纹
服装：视觉重心在下半身：齐胸襦裙高腰及踝，胭脂红长裙占据画面4/5
环境：大唐盛世牡丹园，汉白玉栏杆蜿蜒，主色牡丹粉+汉白玉白+琉璃金
摄像：[ComfyUI 运用范式] 全身等比无畸变，头≤25%，腿≥65%
```

**示例 B · 英文摄影风（GPT Image 2 · 仙门圣女）**

```
Full body photograph of a young Chinese woman, celestial maiden.
She wears a floor-length soft lilac sheer silk hanfu.
Footwear: ivory silk slippers with silver cloud embroidery.
Standing naturally, feet parallel.
Shot on 50mm f/2.8, Kodak Portra 400.
```

**示例 C · 赛博朋克（变量段替换）**

```
服装：哑黑机能风衣敞开，网纱连衣裙垂坠及踝；脚穿厚底机能靴
环境：雨夜霓虹街区，全息广告浮空
摄像：[ComfyUI 运用范式] 头≤25%，腿≥65%，鞋履≥6%
```

---

## 🏗️ 协调生成 + 批量生产

千条级生成的工业化解决方案：

| 能力 | 规格 | 验证结果 |
|---|---|---|
| **风格类 × 专属词库** | 15 大类，每类 14 款服装 + 5 鞋履 + 8~12 饰品 + 11+ 背景 | 协调度 **100%** ✅ |
| **背景唯一性** | 1,956 种 场景×光影 组合池，pop() 弹出 | 1000/1000 唯一 ✅ |
| **内部冲突检测** | 领×袖矛盾自动拦截 | 实测 **0 冲突** ✅ |
| **抖音合规** | 精确短语白名单匹配 | 实测 **0 违规** ✅ |
| **款式唯一性** | 八元组编码 | 1000/1000 唯一 ✅ |

---

## 📂 仓库结构

```
cys-migration-skill/
├── SKILL.md                      # 技能主体（完整模板 + 约束 + 技法 + Krea2 实测 + 协调生成）
├── README.md                     # 本文件
├── LICENSE                       # MIT © 2026 cys
└── references/
    ├── style-presets.md          # 30+ 种风格签名 / 鞋履配色 / 服装词库
    ├── global-knowledge.md       # 22 篇指南：负向词库 / 文化增强 / 多平台写法
    ├── dance_fashion-trends.md   # 4,141+ 条平台热点（跳舞/穿搭/鞋履/BGM）
    ├── global-taxonomy.md        # 15 大类风格专属词库（防换皮铁律）
    └── coordinated-generation.md # v3 协调生成方法论 + 冲突检测 + 抖音合规
```

---

## 📜 许可证

本项目以 **MIT License** 开源，详见 [LICENSE](./LICENSE)。

---

<br>

<p align="center">
  <b>Made by cys</b><br>
  <sub>AI 摄影提示词工程 · 生产验证 · 跨平台通用 · 数据驱动 · 实测优先 · 迭代不止</sub>
</p>

<br>
