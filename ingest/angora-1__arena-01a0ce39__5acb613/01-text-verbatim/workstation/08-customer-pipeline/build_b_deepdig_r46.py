# -*- coding: utf-8 -*-
"""r46 · B 档深挖：把 b_deepdig_data_1.py / _2.py 里的内容，追加到 TR Customers/B/*.md。

规则（沿用 r45）：
- 只在每个 B/*.md 末尾追加一个「附：B 档深挖（r46）」小节；已有标记则跳过（幂等）。
- 不合并文件、不改动原有 7 段正文、不动 A/ 与 C/。
- 没有数据的档位写一段"本轮未覆盖"的诚实说明，绝不编造。

用法：python build_b_deepdig_r46.py
"""
import importlib.util
import io
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..', '..'))
OUT_B = os.path.join(ROOT, 'TR Customers', 'B')

MARK = '## 附：B 档深挖（r46 · 2026-11-01）'


def load(path):
    spec = importlib.util.spec_from_file_location(os.path.basename(path)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.D


DATA = {}
DATA.update(load(os.path.join(HERE, 'b_deepdig_data_1.py')))
DATA.update(load(os.path.join(HERE, 'b_deepdig_data_2.py')))

FALLBACK = """
### 本轮未覆盖
本档在 r46（B 档深挖）中**未被分配到检索时间**，因此**没有新增公开信息**。
理由与后续动作：

- 该档的资料密度低于本轮优先级（本轮优先处理了"已在卖交换机 / 有明确品类 / 有可核实主体"的档位）。
- **不编造**：此处不留任何未经核实的公司信息；现有联系人/电话仍以 `111` 原始记录为唯一锚点。
- 下一轮的默认动作：**一次通话建档**（公司全称 / 业务 / 一年多少台 PoE / 谁采购），再决定是否投入。

### 证据等级与空白
- 已核实：**无新增**。
- 空白：公司全称、地址、规模、现供应商 —— 待补。
"""


def num_of(fn):
    m = re.match(r'^(\d{3})-', fn)
    return str(int(m.group(1))) if m else None


def main():
    files = sorted(f for f in os.listdir(OUT_B) if f.endswith('.md'))
    written = skipped = fallback = missing = 0
    for fn in files:
        n = num_of(fn)
        if n is None:
            print('!! 无法解析序号:', fn)
            continue
        path = os.path.join(OUT_B, fn)
        with io.open(path, encoding='utf-8') as fh:
            text = fh.read()
        if MARK in text:
            skipped += 1
            continue
        body = DATA.get(n)
        if body:
            written += 1
        else:
            body = FALLBACK
            fallback += 1
            missing += 1
            print('   (no data)', fn)
        body = body.strip('\n')
        if not body.startswith('###') and not body.startswith('⚠') and not body.startswith('#'):
            body = '### 说明\n' + body
        out = text.rstrip('\n') + '\n\n---\n\n' + MARK + '\n\n' + body + '\n'
        with io.open(path, 'w', encoding='utf-8') as fh:
            fh.write(out)

    print('B files:', len(files))
    print('written:', written)
    print('fallback:', fallback)
    print('skipped (已有标记):', skipped)
    # 校验
    total_lines = 0
    for fn in files:
        with io.open(os.path.join(OUT_B, fn), encoding='utf-8') as fh:
            t = fh.read()
        total_lines += len(t.splitlines())
        assert MARK in t, fn
    print('B total lines:', total_lines)


if __name__ == '__main__':
    sys.exit(main())
