#!/usr/bin/env python
# coding: utf-8
#
# Filename:   test_core.py
# Author:     Peinan ZHANG
# Created at: 2018-06-24

from python_packaging.core import add


def test_add():
    assert add(1, 1) == 2
