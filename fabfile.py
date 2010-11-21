#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement

from glob import glob
from fabric.api import local


test_path = lambda kind: " ".join(glob('*/tests/%s' % kind))

def test():
    unit()
    functional()
    acceptance()

def unit():
    local('nosetests --verbosity=2 -s %s' % test_path('unit'), capture=False)

def functional():
    local('nosetests --verbosity=2 -s %s' % test_path('functional'), capture=False)

def acceptance():
    local('lettuce', capture=False)
