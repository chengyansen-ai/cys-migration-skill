# 全球词库 · 批量多样生成（半身照 / 千条级）

> 本文件是 cys迁移技能 v1.4.0 的扩展参考。解决用户的硬需求：
> **批量生成上千条提示词，且背景不换皮、服装款式+颜色不换色、饰品多样**。
> 数据来自全球抓取（颜色 556 命名色 / 拍摄地 120+ / 廓形 25 / 传统服饰 50 / 珠宝 60+）+ 技能 9 段式模板。

---

## 一、四条防"换皮重复"铁律

| # | 维度 | 唯一性 key | 规则 |
|---|------|-----------|------|
| 1 | **背景** | 场景身份 = 地点类型 × 子地点 | 光线/天气是独立叠加层，**不计入"换皮"**；两条可同为"黄昏"但必须是不同地点 |
| 2 | **服装** | 五元组 = (款式构造, 颜色, 材质, 领型, 图案) | 五元组整体不可复现 → 杜绝"只换色/只换领口"的伪重复 |
| 3 | **饰品** | 60+ 上半身饰品池轮转 | 每条 1-3 件，组合分散，避免单一饰品霸屏 |
| 4 | **半身照** | 半身专用负向 | 移除原负向的 `half body / bust portrait / upper body only / cropped legs / shoes missing` 禁令 |

---

## 二、生成器（唯一事实来源）

- **脚本**：`D:/workbuddy/2026-07-07-12-24-28/gen_1000_halfbody.py`
- **产出**：`D:/workbuddy/2026-07-07-12-24-28/1000_半身照_提示词.txt`（1000 条 + 半身负向）
- **运行**：`python gen_1000_halfbody.py`（固定随机种子 20260707，可复现）
- **校验**：生成后打印报告，要求 背景唯一=1000、服装五元组唯一=1000、完全重复提示词=0

### 池规模（全球抓取沉淀）
- 颜色：**363** 个命名色（白/蓝/绿/大地/黄/橙/红/粉/紫/棕/灰/黑/灰褐 13 族）
- 服装款式构造：**166** 种（西式廓形 25 + 当代成衣 + 全球传统民族 50+ + 高级戏剧）
- 材质 32 / 领型 20 / 图案 20
- 上半身饰品：**76** 种（项链/耳环/手链/臂环/胸针/发饰/鼻环/戒指等）
- 背景场景：**19 个地点类型 × 子地点 + 30 个独立扩展场景** = 去重后 970+，再补时段变体稳过 1000

---

## 三、半身照专用负向提示词（全部千条共用 · 已去绝对化）

```
(worst quality:1.5), (low quality:1.5), (bad anatomy:1.4), (bad hands:1.4), (bad fingers:1.3), extra fingers, fewer fingers, mutated hands, malformed hands, missing fingers, fused fingers, blurry, lowres, jpeg artifacts, (distorted proportions:1.5), watermark, text, signature, logo, extra limbs, floating limbs, duplicate limbs, two heads, garbled face, q-version, chibi, (plastic skin:1.3), oversmooth, doll face, wax figurine, mannequin, airbrushed, 3d render, cgi, anime style, cartoon style, illustration, (head too big:1.5), asymmetrical eyes, cross-eyed, bad pupils, disfigured, unnatural skin texture, over-saturated colors, grainy noise, oversharpened, mutated face, deformed face, ugly face, asymmetrical face, bad teeth, (nudity:1.5), (pornographic:1.5), (explicit sexual content:1.5), (see-through fabric:1.4), (sheer showing underwear:1.4), (underwear visible:1.4), (panties visible:1.4), (crotch visible:1.5), (sexual suggestion:1.3), (vulgar:1.3), (low-class:1.3), (solo:1.4), (no other people:1.4), (no extra person:1.4), (no crowd:1.4), (no animals:1.4), (empty background:1.3), (clean background:1.3), (no bystander:1.4), (tacky:1.3), (gaudy:1.3), (cheap looking:1.3), (low-class fashion:1.3), (outdated fashion:1.2), (old-fashioned:1.2), (kitsch:1.2), (tacky style:1.3), (vulgar style:1.3)
```

> **2026-07-07 重构**：半身照专用负向同样遵循"去绝对化"原则——
> - **不含**全身构图层（`half body / bust / upper body only / cropped legs / shoes missing` 已删，半身照本就要半身）。
> - **含**平台合规层（只禁真违规：裸/透视露内衣/内裤外露/私处/色情暗示/低俗；**不**禁短裤/裙/露腿/露肩/深V，合理可露）。
> - **含**动作迁移层（背景无活物：solo/无人/无动物/干净背景）。
> - **含**审美兜底（防庸俗老旧 tacky/gaudy/cheap/outdated，保抖音快手流量）。
> - 若某条想完全不露肉，临时叠加：`(shorts:1.3),(mini skirt:1.3),(exposed thighs:1.3)`。

---

## 四、颜色重复的现实边界（诚实说明）

全球命名色约 360 个，生成 1000 条**必然有色相重复**。本方案用「款式+材质+领型+图案 均不同」保证不会出现"只换色的伪重复"。若用户坚持要 1000 个**完全不同色相**，需引入：
- `色相 + 明度 + 饱和度` 三元组描述，或
- `渐变 / 拼色 / 撞色` 复合色描述

来把颜色维度从 ~360 扩展到上千。

---

## 五、与"动作迁移全身图"的关系

| 用途 | 模板 | 负向 | 构图 |
|------|------|------|------|
| **动作迁移源图**（原主线） | 9 段式全身 + 鞋履入镜 + 头身比修正 | 包严版/铁律版（禁 half body/short） | 全身垂直 T-pose |
| **半身照批量**（本文件） | 9 段式半身 + 饰品多样 | 半身专用负向 | 腰部以上 85mm 浅景深 |

两者是**不同业务场景**，不要混用负向（半身照用了全身负向会被误杀）。

---

## 六、复用方式

1. 直接拿 `1000_半身照_提示词.txt` 用（已生成 1000 条）。
2. 换风格/换数量：改 `gen_1000_halfbody.py` 里的池子或 `range(1000)`，重跑即可，唯一性自动保证。
3. 想换皮肤/人种/光影：改脚本顶部对应池（HAIRSTYLES/EYES/LIPS/MAKEUP/POSES/LIGHTING）。
