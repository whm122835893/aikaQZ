#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
补回被重写页面丢失的 data-v 作用域属性。

背景：页面是从源站抓的静态快照，site.css 里的业务样式全部带[data-v-xxxxxxxx] 作用域。
重写页面时若把data-v 属性删掉，页面上所有布局/配色都会静默失效（表现为纯文本无样式）。

本脚本从原始快照 crawl4/*.html 反查每页真实的 scope id，再批量补回模板。
"""
import io, os, re, glob, collections

CRAWL = '/root/.codebuddy/artifact/2f8a7d30-9c21-4f0b-1d3f-4c48460d2000/crawl4'
VIEWS = 'src/views'

# 需要修复的页面 -> 快照文件名
TARGETS = {
    'account/OrderList.vue':        'pages__account__orderList.html',
    'account/MarketOrderList.vue':  'pages__account__marketOrderList.html',
    'account/BidList.vue':          'pages__account__bidList.html',
    'colorfulMix/ColorfulMix.vue':  'pages__colorfulMix__colorfulMix.html',
}

TPL_RE = re.compile(r'<template>(.*)</template>', re.S)
TAG_RE = re.compile(r'<(uni-[a-z-]+)((?:\s[^>]*?)?)(/?)>')


def scope_of(snap_file):
    s = io.open(os.path.join(CRAWL, snap_file), encoding='utf-8').read()
    c = collections.Counter(re.findall(r'data-v-([0-9a-f]{8})', s))
    # 排除 uni 内置空态组件的 scope（4d930ea0 / a0f2fc02 之类，出现频次远低于主scope）
    return c.most_common(1)[0][0]


def patch(rel, scope_id):
    p = os.path.join(VIEWS, rel)
    s = io.open(p, encoding='utf-8').read()
    m = TPL_RE.search(s)
    assert m, 'template not found in ' + rel
    tpl = m.group(1)
    if 'data-v-' in tpl:
        print('%-34s 已有 data-v，跳过' % rel)
        return

    n = 0

    def repl(mo):
        nonlocal n
        tag, attrs, selfclose = mo.group(1), mo.group(2), mo.group(3)
        n += 1
        return '<%s data-v-%s%s%s>' % (tag, scope_id, attrs, selfclose)

    new_tpl = TAG_RE.sub(repl, tpl)
    s = s[:m.start(1)] + new_tpl + s[m.end(1):]
    io.open(p, 'w', encoding='utf-8').write(s)
    print('%-34s + data-v-%s  （%d 个标签）' % (rel, scope_id, n))


for rel, snap in TARGETS.items():
    patch(rel, scope_of(snap))