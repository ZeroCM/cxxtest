#! /usr/bin/env python
# encoding: utf-8

def configure(ctx):
    ctx.load('cxxtest')
    if ctx.check_cxxtest_version() < (4, 4):
        ctx.fatal('cxxtest version is too old')

def build(ctx):
    return
