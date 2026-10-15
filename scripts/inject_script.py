#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
向已有静态快照页注入 <script setup> 的通用工具。

踩过的坑：SFC 解析器要求 <template> 必须闭合，如果script 被追加到文件末尾
而</template> 也在其后，解析器会把 script 整段当作模板文本（表现为
`descriptor.scriptSetup` 长度为 0，且编译报 "Tags with side effect"）。
所以这里统一保证结构为：

    <template> ... </template>

    <script setup> ... </script>
"""
import re
import sys

SCRIPT_RE = re.compile(r'<script setup>.*?</script>', re.S)


def inject(path, script):
    s = open(path, encoding='utf-8').read()

    # 已有 script 则替换
    m = SCRIPT_RE.search(s)
    if m:
        s = s[:m.start()] + script.strip() + s[m.end():]
        open(path, 'w', encoding='utf-8').write(s)
        return 'replaced'

    # 没有 template 标签则新建
    if '<template>' not in s:
        s = '<template>\n  <uni-view class="page"></uni-view>\n</template>\n\n' + script + '\n'
        open(path, 'w', encoding='utf-8').write(s)
        return 'created'

    # 已有的情形：尾部可能是 "...</script>\n\n</template>"（script 在 template 内）
    m2 = re.search(r'<script setup>.*?</script>\s*\n\s*</template>\s*\n?\s*$', s, re.S)
    if m2:
        blk = SCRIPT_RE.search(m2.group(0)).group(0)
        s = s[:m2.start()].rstrip() + '\n</template>\n\n' + blk.strip() + '\n'
        open(path, 'w', encoding='utf-8').write(s)
        return 'moved'

    # 正常情形：在最后一个 </template> 之后追加
    i = s.rfind('</template>')
    s = s[:i + len('</template>')].rstrip() + '\n\n' + script.strip() + '\n'
    open(path, 'w', encoding='utf-8').write(s)
    return 'appended'


if __name__ == '__main__':
    print(inject(sys.argv[1], sys.stdin.read()))