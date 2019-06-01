# ============================================================================
# FILE: util.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# ============================================================================

import glob
import re
import typing

from pynvim import Nvim


def globruntime(runtimepath: str, path: str) -> typing.List[str]:
    ret: typing.List[str] = []
    for rtp in re.split(',', runtimepath):
        ret += glob.glob(rtp + '/' + path)
    return ret


def debug(vim: Nvim, expr: typing.Any) -> None:
    if hasattr(vim, 'out_write'):
        string = (expr if isinstance(expr, str) else str(expr))
        vim.out_write('[denite] ' + string + '\n')
    else:
        print(expr)
