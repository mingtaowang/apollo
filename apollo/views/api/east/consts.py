# -*- coding: utf-8 -*-

from apollo.libs.storify import storify

RANK_TOPS = storify(dict(
    FIRST=1,
    SECOND=2,
    THIRD=3
))

# 过滤查看的代码
FILTER_AWAY = storify(dict(
    AWAY=1,
    NORMAL=0,
))

# 操作类型
ACTION = storify(dict(
    HIDE=0,
    SHOW=1,
))

