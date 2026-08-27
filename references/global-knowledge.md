# 全球提示词知识加固（爬取沉淀 · 2026-07-07）

本文件沉淀自「Firecrawl 深抽取 22 篇权威指南 + WebSearch 多区域发现（欧美/中东西亚/日韩/南亚/拉美/国内）」。用于把全球提示词工程的共识、跨文化美学、负向词库、平台特性，固化进 `cys-portrait` 技能。

---

## 一、提示词公式共识（多源交叉验证 → 印证本技能 9 段式）

| 来源 | 公式 / 顺序 | 关键洞见 |
|---|---|---|
| artprompthq（写实人像） | `[主体]+[动作/姿态]+[环境]+[光影/情绪]+[镜头/技术]+[风格]` | **SD 优先处理序列前面的 token** → 主体/姿态要写最前；顺序=权重 |
| sureprompts（6 段式） | subject → action → environment → style → technical(camera/lighting/aspect) | DALL-E 吃散文；Midjourney 吃逗号分隔；SD/Flux 混用 |
| promptprepare（**CRAFT**） | **C**ontext(主体+场景) · **R**endering(风格/媒介) · **A**tmosphere(情绪+光) · **F**idelity(镜头+构图) · **T**ool(参数+负向) | 结构化框架，首遍出图质量立升 |
| 腾讯（已验证中文体系） | 新手：主体+场景+风格+光线+构图+画质+背景；进阶：主体(特征/姿态)+艺术风格+材质质感+光影+镜头视角+画质+色彩+背景+**负面** | 与 9 段式**同源**——中文社区独立得出相同结构 |

> **结论**：本技能的「人物→面容→妆容→身材→装饰→动作→服装→环境→摄像」是上述共识的**国风写实特化版**，方向正确无需改。差异仅在：本技能把"面容/妆容/身材/装饰"抽成可复用的「真实感内核」，并针对动作迁移场景强化了站姿与鞋履的前置。

### Token 优先级建议（参考）
- 模型对 **prompt 前部 token 权重更高**（artprompthq 实测）。
- 因此：把「主体身份 + 站姿类型 + 下半身重心」放在最前；修饰形容词（材质/光影）靠后。
- 9 段式天然满足（人物→动作在前，装饰/服装/环境在后）。迁移图尤其要把"全身垂直站立 + 鞋履入镜"前置。

---

## 二、负向提示词库（ComfyUI / Flux 专用 · 用户工作流支持）

ComfyUI/Flux2 支持独立 Negative 输入框，务必填。直接复制可用：

```
(worst quality:1.4), (low quality:1.4), (bad anatomy:1.3), (bad hands:1.3),
extra fingers, missing fingers, too many fingers, deformed hands, mutated hands,
blurry, out of focus, motion blur, (oversaturated:1.2), (underexposed:1.2),
(distorted proportions:1.3), bad composition, watermark, signature, text, logo,
extra limbs, missing limbs, floating limbs, disconnected body, broken joints,
duplicate, (plastic skin:1.2), oversmooth, doll face, wax figurine, 3d render,
cropped feet, shoes missing, (head too big:1.4), q-version, chibi
```

要点：
- **比例失真专项**：`(head too big:1.4)` + `(distorted proportions:1.3)` 双保险，与正向提示词中"人物比例自然、避免夸张变形"的描述呼应。
- **鞋履专项**：`cropped feet, shoes missing` 反向兜底，杜绝迁移图脚被裁。
- **塑料感专项**：`(plastic skin:1.2), oversmooth, doll face, wax figurine` —— 与正向"皮下血色/毛孔/绒毛"双管齐下。
- 权重用 `(xxx:1.x)` 语法，Flux2 的 Qwen CLIP 吃这套括号权重。

---

## 三、跨文化美学签名（扩展风格库，直击全球题材）

> 用法：用户要做「中东/波斯/印度/拉美/日韩」风人像时，取下方签名填进段7（服装）+段8（环境）+段9（摄像氛围）。

### A. 中东 / 波斯 / 阿拉伯（Middle East）
- **服装**：Abaya（及地宽松长袍，黑/深蓝，罩头）→ 可改为彩色织金长袍；Thobe 白袍；Hijab/头巾；绣金几何纹（阿拉伯式蔓藤纹 Arabesque）；绿松石/琥珀珠宝；尖头平底 Moorish 鞋
- **环境**：清真寺拱券与马赛克、沙漠落日、香料集市（souk）、波斯地毯、水烟馆暖光；整体色调：赭红 + 金 + 绿松石蓝
- **氛围词**：ornate arabesque, islamic geometric pattern, warm lantern glow, desert golden hour
- **文化增强**：用 GPT 把基础 prompt 注入"传统纹饰/浓彩/宗教节庆符号"（见第四节）

### B. 印度 / 南亚（South Asia）
- **服装**：Sari（6码纱丽，金线绣边）+ Blouse；Salwar Kameez；Lehenga 婚礼裙；Bindi 额饰；鼻环；手绘 henna 纹
- **环境**：泰姬陵/宫殿拱廊、香料园、排灯节万灯、恒河晨雾；色调：宝红 + 金 + 孔雀蓝
- **人像词**：deep brown eyes, caramel skin, long black hair, traditional silk sari, jasmine flowers in hair

### C. 拉美（Latin America）
- **服装**：安第斯刺绣披肩（manta）、墨西哥刺绣裙（China Poblana）、_flowy_ 大摆裙；鲜花头冠（Flor de Cempasúchil）
- **环境**：殖民古城彩色立面、亡灵节万寿菊海、热带沙滩、安第斯山；色调：赭红 + 明黄 + 翠绿
- **氛围**：vibrant fiesta, warm tropical light, folk embroidery

### D. 日韩（Japan / Korea）
- **和风**：和服（振袖/浴衣）、带缔腰带、木屐（geta）、艺伎白妆 OR 现代原宿；樱/红叶/鸟居/竹林
- **韩风**：韩服（한복）高腰裙+短上衣、盘发发簪；韩屋庭院、樱花、极简韩式美学
- **氛围**：soft pastel, minimalist, cherry blossom, serene, film grain

---

## 四、文化提示词增强技法（Cultural Prompt Augmentation）

来源：ACM IMX'23 论文《Enhancing Arabic Content Generation with Prompt Augmentation》（Wala Elsharif et al.）。方法已验证有效。

**原理**：直接写"阿拉伯/国风/波斯少女"→ 模型只会给泛化结果；用 **LLM（GPT/Qwen）先把基础 prompt 扩写（augment）**，注入**该文化专属的视觉符号**（服饰剪裁、传统纹样、节庆符号、典型配色、场景器物），文化表征准确度显著提升（论文 Fig.1 a→c 对比明显）。

**操作步骤（用户可复用）**：
1. 写基础 prompt（如"中东少女全身照"）。
2. 让 AI 扩写：*"请为这段提示词注入中东/波斯文化专属视觉细节：传统服饰剪裁、阿拉伯式几何纹样、典型珠宝、节庆/建筑场景、浓彩配色，保持全身垂直站姿与鞋履入镜。"*
3. 把扩写结果作为最终提示词喂图。

> 对用户的价值：做「国风/敦煌/战甲/西域」题材时，用此法让文化符号**更准更地道**，避免"四不像"。本技能段7（服装）+段8（环境）可直接套用此增强。

---

## 五、平台特性速查（决定路线与写法）

| 平台 | 提示词偏好 | 与用户工作流关系 |
|---|---|---|
| **ComfyUI / Flux2 Klein** | Tag 混散文；支持负向；Qwen CLIP 吃中文+括号权重 | **用户主线（路线 A）** |
| **GPT Image 2** | 自然语言散文（prose）；不吃负向框；吃"full body, feet visible" | **路线 B 英文风** |
| Midjourney v7 | 逗号分隔 descriptor；`--ar --v` 参数；`--no` 负向 | 参考构图/风格 |
| DALL-E 3 | 完整句子散文；强语义理解 | 参考英文风 |
| Stable Diffusion 3.5 | Tag 式；负向强；ControlNet | 同类 |
| Leonardo / Ideogram / Kling / Runway | 各带专属参数 | 视频向参考 |

> 用户业务（参考图→动作迁移→图生视频→抖音）以 ComfyUI/Flux2 为主、GPT Image 2 为辅，故技能默认路线 A 中文 + 路线 B 英文摄影风，已覆盖。

---

## 六、全球资源地图（爬取发现的权威站点）

### 欧美指南
apatero.com · letsenhance.io · sureprompts.com · bestprompt.art · promptprepare.com · imagera.ai · gptprompts.ai · stability.ai/guides

### Prompt 数据库 / 社区
PromptHero · Lexica.art · Civitai(+中文站) · PromptDen · PromptBase · PromptSpace · topai.ink（全球10000+）

### 中东西亚
ACM 阿拉伯论文 · Araby.ai · PromptBase(波斯) · ReelMind(波斯生成器) · a1.art(middle-eastern) · BasedLabs(middle-eastern)

### 亚洲
PixAI / NovelAI（日韩）· Pixu.ai（South-Asian 317条 / Latin-American / Brazil 309条）· iamziana.medium（印度写实）

### 国内（中文）
腾讯新闻关键词体系 · 少数派提示词网站大全 · 知乎20个站 · cubistai 资源库 · 腾讯云质量词 · 国内7款平台横评
平台：即梦、可灵、通义万相、海螺、LiblibAI、吐司、6pen、堆友

### CLIP / Flux2 Klein
docs.comfy.org/flux-2-klein · cnb.cool ComfyUI-FLUX.2-klein(9B→qwen_3_8b) · acaiy.cn 深度指南 · runninghub qwen-clip 工作流 · github black-forest-labs/flux2（Mistral 上采样）· comfy.icu LongCLIPTextEncodeFlux
