#!/usr/bin/env python3
# cys-migration 技能自测：跑生成器小批量 + BANNED 合规校验，输出 OK/WARN
# 用法：python scripts/selftest.py
import os, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# 读内联 BANNED 权威源（仓库根 banned-words.txt）
_SHARED = os.path.join(os.path.dirname(os.path.dirname(HERE)), "banned-words.txt")
try:
    BANNED = [l.strip() for l in open(_SHARED, encoding="utf-8") if l.strip()]
except FileNotFoundError:
    BANNED = ["裸露", "裸体", "全裸", "半裸", "走光", "透视", "内裤",
              "私处", "色情", "性暗示", "情色", "淫秽", "露点"]


def run(script, n=20):
    print(f"\n=== 自测 {script} (n={n}) ===")
    r = subprocess.run([sys.executable, os.path.join(HERE, script), str(n)],
                       capture_output=True, text=True)
    tail = (r.stdout or "")[-600:]
    print(tail)
    if r.returncode != 0:
        print("WARN: 运行失败\n", (r.stderr or "")[-500:])
        return False
    # 生成器末尾打印 OK / WARN；合规命中须为 0
    if "抖音违规词命中" in tail and "抖音违规词命中       : 0" not in tail:
        print("WARN: 检测到违规词命中")
        return False
    return "OK" in tail


if __name__ == "__main__":
    ok = True
    ok &= run("gen_v3.py", 20)
    ok &= run("gen_v4_halfbody.py", 20)
    print("\n===== cys-migration selftest:", "OK" if ok else "WARN", "=====")
    sys.exit(0 if ok else 1)
