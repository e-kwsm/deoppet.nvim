# =============================================================================
# FILE: deoppet.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# License: MIT license
# =============================================================================

import re

from deoplete.base.source import Base


class Source(Base):
    def __init__(self, vim):
        Base.__init__(self, vim)

        self.name = 'deoppet'
        self.mark = '[dp]'
        self.rank = 200

    def gather_candidates(self, context):
        bvars = self.vim.current.buffer.vars
        if 'deoppet_snippets' not in bvars or not isinstance(
                bvars['deoppet_snippets'], dict):
            return []

        m1 = re.match(r'\w+$', context['complete_str'])
        m2 = re.match(r'\S+$', context['complete_str'])
        snippets = bvars['deoppet_snippets'].values()
        if m1 and m2 and m1.group(0) != m2.group(0):
            snippets = [x for x in snippets if x['options']['word']]
        candidates = []
        for x in snippets:
            if x['options'].get('head'):
                m = re.search(r'^\s*(\S+)$', context['input'])
                if m and m.group(1) in x['trigger']:
                    candidates += [{'word': x['trigger']}]
            elif not x['regexp'] or self.vim.call(
                    'matchstr', context['input'], x['regexp']):
                candidates += [{'word': x['trigger']}]
        return candidates
