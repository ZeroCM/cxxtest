#! /usr/bin/env python
# encoding: utf-8

import waflib

def configure(ctx):
    ctx.load('cxxtest')
    if ctx.check_cxxtest_version() < (4, 4):
        ctx.fatal('cxxtest version is too old')

def build(ctx):

    ctx.env.CXXTEST_ROOT = ctx.path.get_src().abspath()

    if not waflib.Options.options.skip_git:
        ctx(rule = 'OUTPUT=$(cd %s && git rev-parse HEAD && \
                   ((git tag --contains ; echo "<no-tag>") | head -n1) \
                    && git diff) && echo "$OUTPUT" > ${TGT}' %
                    (ctx.env.CXXTEST_ROOT),
            target = 'cxxtest.gitid',
            always = True)

        gitidNode = ctx.path.get_bld().find_or_declare('cxxtest.gitid')
        ctx.install_files('${PREFIX}',
                          gitidNode,
                          cwd = ctx.srcnode,
                          relative_trick = True)

    if ctx.variant == 'sign':
        return
