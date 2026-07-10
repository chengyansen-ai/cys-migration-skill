# -*- coding: utf-8 -*-
"""
提炼脚本：从桌面两份源文件（写实人像5000条 + COS汇总csv）提炼
「服装 / 鞋履 / 背景场景 / 光线」词库，写入写实人像技能/references/real-portrait-corpus.md。

处理原则（用户指令）：
1) 提炼不整包 —— 只抽 服装/鞋履/背景场景/光线 词汇，不整包塞入技能。
2) 删模板句 —— 删除 CSV 里固定的「冷白皮，精致的纯欲五官」开头 + 「固定摄影尾参」。
3) 过 BANNED 精确短语校验（读 banned-words.txt）。
4) 人工剔除 透视/低胸/挑逗特写 等暴露/暗示条目。
5) 只保留动作迁移需要的提示词（垂直全身·鞋履入镜）；非动作迁移的判定不需要即不加。

源文件（外部输入，非技能运行时依赖，路径请按需自行替换）：
  input/写实人像5000条.txt
  input/提示词汇总.csv
"""
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, "..", "references")
SHARED = os.path.join(HERE, "..")  # 共享约束文件（banned-words.txt 等）已内联至本仓库根目录
SRC_TXT = r"input/写实人像5000条.txt"
SRC_CSV = r"input/提示词汇总.csv"
OUT = os.path.join(REF, "real-portrait-corpus.md")

# ---------- 1. BANNED 精确短语（来自 本仓库，读不到则回退内联） ----------
FALLBACK_BANNED = ["裸露", "裸体", "全裸", "半裸", "走光", "透视", "内裤",
                   "私处", "色情", "性暗示", "情色", "淫秽", "露点"]
try:
    with open(os.path.join(SHARED, "banned-words.txt"), encoding="utf-8") as f:
        BANNED = [l.strip() for l in f if l.strip()]
    if not BANNED:
        BANNED = FALLBACK_BANNED
except Exception:
    BANNED = FALLBACK_BANNED

# ---------- 2. 人工剔除（暴露/暗示/挑逗特写 相关） ----------
MANUAL_BAN = [
    "透视", "低胸", "挑逗", "比基尼", "半透明", "透肤", "深V", "乳沟", "事业线",
    "腿根", "开叉至", "露胸", "露乳", "私处", "内裤", "内衣", "胸罩", "胸衣",
    "湿身", "渔网", "网袜", "吊带袜", "性感", "妩媚", "暧昧", "媚态", "酥胸",
    "丰乳", "巨乳", "翘臀", "胸臀", "露脐", "露背", "低腰", "开叉", "微敞",
    "微露", "滑落", "蕾丝内衣", "黑色蕾丝", "透明", "薄纱透", "透出肌肤",
    "隐约", "若隐若现", "春光", "迷人", "妖娆", "魅惑", "诱惑",
]
# 注：上面部分词（开叉/微敞/微露/滑落/隐约/若隐若现/透出肌肤）属"擦边暗示"，
# 严格审查下一并剔除；若某服装词因此被误删，会在人工复核阶段救回。

ALL_BAN = set(BANNED) | set(MANUAL_BAN)


def is_bad(text):
    return any(w in text for w in ALL_BAN)


# ---------- 3. 读取源 ----------
def read_txt(path):
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8", errors="ignore") as f:
        return [l.strip() for l in f if l.strip()]


def read_csv(path):
    if not os.path.exists(path):
        return []
    rows = []
    with open(path, encoding="utf-8", errors="ignore") as f:
        lines = f.read().splitlines()
    # 简单 CSV 解析（提示词内容可能含逗号，但本文件列数固定 3 列，且第3列是长文本）
    for ln in lines[1:]:  # 跳过表头
        if not ln.strip():
            continue
        # 按逗号切，前两段为 序号/文件名，剩余全并为 提示词内容
        parts = ln.split(",", 2)
        if len(parts) >= 3:
            rows.append(parts[2].strip())
        else:
            rows.append(ln.strip())
    return rows


# ---------- 4. 抽取函数（受控修饰符 + 名词，干净词表） ----------
PUNCT = "，。、；：！？\n"

# 修饰符字符集（颜色/材质/版型/设计点），只从这里面取前缀，绝不混入姿势动词
MOD = ("白黑红蓝绿黄粉紫棕灰金银浅深亮暗柔光滑哑光金属皮革丝绸棉麻针织雪纺"
       "纱漆皮绒毛网透薄粗细紧松高短长及踝过膝露肩背交叉系带绑带荷叶波浪褶"
       "立体绣印条格波碎珠亮哑做旧复古宫廷欧式日式中绣花镂空宽松修身无袖"
       "圆领V领高领挂脖抹胸吊带开衫大翻领双排扣单排扣落肩垫肩收腰A字鱼尾"
       "百褶蓬蓬包臀铅笔阔腿工装运动休闲学院风复古未来科技赛博朋克蒸汽波")
MOD_CLASS = "[" + MOD + "]"

# 各品类名词（受控词典，扫描命中即收）
CLOTH_NOUNS = [
    "风衣", "大衣", "外套", "夹克", "衬衫", "T恤", "针织上衣", "针织衫", "毛衣",
    "卫衣", "背心", "吊带", "抹胸", "礼服", "婚纱", "婚服", "睡裙", "和服", "振袖",
    "浴衣", "女仆装", "巫女服", "战斗服", "制服", "连体衣", "连衣裙", "旗袍", "袄",
    "披风", "斗篷", "马甲", "上衣", "短裙", "长裙", "半身裙", "百褶裙", "格纹裙",
    "鱼尾裙", "铅笔裙", "短裤", "热裤", "长裤", "阔腿裤", "牛仔裤", "紧身裤",
    "九分裤", "打底裤", "运动短裤", "裙裤", "丝袜", "连裤袜", "过膝袜", "长筒袜",
    "棉袜", "及膝袜", "大腿袜", "蕾丝袜", "及踝袜", "中筒袜",
]
FOOT_NOUNS = [
    "高跟鞋", "尖头高跟鞋", "细跟高跟鞋", "粗跟高跟鞋", "厚底高跟鞋", "高跟凉鞋",
    "凉鞋", "细带凉鞋", "玛丽珍鞋", "运动鞋", "跑鞋", "板鞋", "帆布鞋", "靴子",
    "短靴", "长靴", "过膝靴", "马丁靴", "牛仔靴", "高跟木屐", "木屐", "拖鞋",
    "乐福鞋", "牛津鞋", "松糕鞋", "芭蕾鞋", "穆勒鞋", "豆豆鞋", "懒人鞋",
]
BG_NOUNS = [
    "走廊", "台球厅", "浴室", "阳台", "石阶", "教室", "办公室", "卧室", "客厅",
    "健身房", "飞机客舱", "河畔", "水边", "街道", "店铺", "公园", "婚礼", "日式房间",
    "欧式房间", "酒店", "楼梯", "天台", "地铁", "夜店", "吧台", "游泳池", "沙滩",
    "山顶", "屋顶", "厨房", "书房", "画室", "摄影棚", "舞台", "车厢", "码头", "车站",
    "庭院", "海边", "竹林", "樱花树", "花园", "露台", "阁楼", "仓库", "工厂", "废墟",
    "桥", "雨中", "雪地", "草地", "麦田", "花海", "城市", "古镇", "庙宇", "教堂",
    "城堡", "图书馆", "霓虹街", "巷弄", "天台", "泳池", "绿洲", "沙漠", "旷野",
]
LIGHT_NOUNS = [
    "均匀明亮", "柔和均匀", "暖黄色", "侧上方", "霓虹", "蓝红霓虹", "聚光灯",
    "侧后光", "自然光", "侧逆光", "黑白影调", "红色灯光", "烛光", "月光", "冷色调",
    "顶光", "逆光", "柔光", "硬光", "晨光", "夕阳", "黄昏", "夜晚人造光", "环境光",
    "窗光", "暖光", "冷光", "丁达尔", "轮廓光", "伦勃朗光", "荧光", "霓虹灯", "补光",
    "边缘光", "戏剧光", "漫射光", "散射光", "暖调", "冷调", "明暗对比", "高调",
    "低调", "立体光", "蝴蝶光",
]


def clean(chunk):
    chunk = chunk.strip()
    while chunk and chunk[-1] in PUNCT:
        chunk = chunk[:-1]
    return chunk.strip()


def extract_by_nouns(text, nouns):
    out = set()
    for noun in nouns:
        # 前缀限定在修饰符字符集内（最多 10 个），得到「颜色/材质 + 名词」干净短语
        for m in re.finditer(r"(?:" + MOD_CLASS + r"{0,10}?)" + re.escape(noun), text):
            c = clean(m.group(0))
            if 2 <= len(c) <= 16 and not is_bad(c):
                out.add(c)
    return out


def extract_clothing(text):
    return extract_by_nouns(text, CLOTH_NOUNS)


def extract_footwear(text):
    return extract_by_nouns(text, FOOT_NOUNS)


def extract_background(text):
    return extract_by_nouns(text, BG_NOUNS)


def extract_lighting(text):
    return extract_by_nouns(text, LIGHT_NOUNS)


# ---------- 5. 动作迁移可用源图（严格筛选） ----------
# 需要：全身 + 垂直站立 + 鞋履入镜 + 无暴露/暗示 + 无坐姿/倚靠/曲腿
POSE_EXCLUDE = ["坐", "倚", "靠", "蹲", "趴", "卧", "跪", "曲", "弯", "环抱", "支撑",
                "搭在", "搭着", "盘腿", "交叠", "蜷", "侧坐", "抬", "托", "扶", "握",
                "撩", "触", "整理", "前倾", "后仰", "微侧", "侧对", "侧身", "转身"]
ARM_OK = ["自然下垂", "双臂自然", "双手自然", "直立", "并拢", "平行", "垂直", "站姿挺拔", "双脚"]


def is_migration_ready(text):
    if is_bad(text):
        return False
    if not ("全身" in text or "全身入镜" in text):
        return False
    if not ("鞋" in text or "靴" in text or "木屐" in text):
        return False
    # 排除非垂直姿势
    for w in POSE_EXCLUDE:
        if w in text:
            return False
    # 必须含垂直/手臂自然下垂信号
    if not any(w in text for w in ARM_OK):
        return False
    return True


def strip_template(prompt):
    # 删 CSV 固定开头「冷白皮，精致的纯欲五官...」
    prompt = re.sub(r"^一个极具魅力的年轻亚洲女性，冷白皮，[^，]*?五官[^，]*?，", "", prompt)
    prompt = re.sub(r"冷白皮，精致的纯欲五官，?", "", prompt)
    # 删固定摄影尾参
    prompt = re.sub(r"8k分辨率.*?逼真的细节。?$", "", prompt)
    prompt = re.sub(r"超高清.*?精致细节。?$", "", prompt)
    prompt = re.sub(r"杰作.*?逼真的细节。?$", "", prompt)
    prompt = re.sub(r"大师级摄影.*?逼真细节。?$", "", prompt)
    return prompt.strip()


# ---------- 6. 主流程 ----------
def main():
    txt_lines = read_txt(SRC_TXT)
    csv_rows = read_csv(SRC_CSV)
    print(f"[源] txt 行数={len(txt_lines)}  csv 行数={len(csv_rows)}")

    clothing, footwear, bg, light = set(), set(), set(), set()
    for t in txt_lines + csv_rows:
        clothing |= extract_clothing(t)
        footwear |= extract_footwear(t)
        bg |= extract_background(t)
        light |= extract_lighting(t)

    print(f"[抽取] 服装={len(clothing)} 鞋履={len(footwear)} 背景={len(bg)} 光线={len(light)}")

    # 动作迁移可用源图（仅 txt，csv 全为坐姿/侧卧判定不需要）
    ready = []
    for t in txt_lines:
        if is_migration_ready(t):
            ready.append(strip_template(t))
    print(f"[动作迁移可用] 严格筛选得 {len(ready)} 条")

    # 排序
    clothing = sorted(clothing)
    footwear = sorted(footwear)
    bg = sorted(bg)
    light = sorted(light)

    # 写 markdown
    lines = []
    lines.append("# 真人写实人像语料库（real-portrait-corpus）")
    lines.append("")
    lines.append("> 提炼自桌面两份源文件：**肖像（5000条提示词）.txt** + **提示词汇总.csv**（COS 汇总）。")
    lines.append("> 处理原则：提炼不整包（仅抽 服装/鞋履/背景/光线 词汇）；删除 CSV 固定模板句「冷白皮，精致的纯欲五官」+ 固定摄影尾参；过 `banned-words.txt` 精确短语 + 人工剔除透视/低胸/挑逗/暗示条目；仅保留动作迁移需要的提示词。")
    lines.append("> 本文件相对路径存于技能内，换机/换会话不断链。")
    lines.append("")
    lines.append("## 一、服装词库（上装 / 下装 / 连衣 / 特殊）")
    lines.append("")
    for w in clothing:
        lines.append(f"- {w}")
    lines.append("")
    lines.append("## 二、鞋履词库")
    lines.append("")
    for w in footwear:
        lines.append(f"- {w}")
    lines.append("")
    lines.append("## 三、背景场景词库")
    lines.append("")
    for w in bg:
        lines.append(f"- {w}")
    lines.append("")
    lines.append("## 四、光线词库")
    lines.append("")
    for w in light:
        lines.append(f"- {w}")
    lines.append("")
    lines.append("## 五、动作迁移可用源图提示词（垂直全身 · 鞋履入镜 · 严格筛选）")
    lines.append("")
    lines.append(f"> 从 5000 条写实提示词中，按「全身 + 垂直站立 + 鞋履入镜 + 无坐姿/倚靠/曲腿 + 无暴露暗示」严格筛选，共 **{len(ready)}** 条。")
    lines.append("> CSV（COS 汇总）全部为侧坐/侧卧/倚靠姿势，判定**非动作迁移需要**，已整体排除，不纳入本技能。")
    lines.append("")
    for i, p in enumerate(ready, 1):
        lines.append(f"{i}. {p}")
    lines.append("")

    os.makedirs(REF, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"[写出] {OUT}")
    print(f"[大小] {os.path.getsize(OUT)} bytes")


if __name__ == "__main__":
    main()
