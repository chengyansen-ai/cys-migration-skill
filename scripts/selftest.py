#!/usr/bin/env python3
# 人像提示词生成器自测：跑生成器小批量，检查是否输出 OK（唯一性/协调度/搭配逻辑自检）
# 用法：python scripts/selftest.py
import os, sys, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def run(script, n=20):
    print(f"\n=== 自测 {script} (n={n}) ===")
    r = subprocess.run([sys.executable, os.path.join(HERE, script), str(n)],
                       capture_output=True, text=True)
    tail = (r.stdout or "")[-600:]
    print(tail)
    if r.returncode != 0:
        print("WARN: 运行失败\n", (r.stderr or "")[-500:])
        return False
    # 生成器末尾打印 OK / WARN：OK 表示唯一性与搭配逻辑自检全部通过
    return "OK" in tail


if __name__ == "__main__":
    ok = True
    ok &= run("gen_v3.py", 20)
    ok &= run("gen_v4_halfbody.py", 20)
    print("\n===== 人像提示词生成器 selftest:", "OK" if ok else "WARN", "=====")
    sys.exit(0 if ok else 1)
