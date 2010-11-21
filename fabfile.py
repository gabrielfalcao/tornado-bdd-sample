#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement

import os
import tempfile
from glob import glob
from fabric.api import local, env, put, run, cd, sudo

env.hosts = ['ec2-184-72-36-115.us-west-1.compute.amazonaws.com']
env.key_filename = os.path.expanduser('~/.ssh/gabrielfalcao.pem')
env.user = 'ubuntu'

test_path = lambda kind: " ".join(glob('*/tests/%s' % kind))

def tarball():
    tardir = tempfile.gettempdir()
    local('rm -rf app.tar.bz2')
    tarpath = os.path.join(tardir, 'app.tar.bz2')
    local('tar cjf %s .' % tarpath)
    return tarpath

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

def deploy():
    tarpath = tarball()
    run('rm -rf tornado-bdd-sample')
    run('mkdir tornado-bdd-sample')
    put(tarpath, 'tornado-bdd-sample/app.tar.bz2')
    with cd('~/tornado-bdd-sample'):
        run('tar xjf app.tar.bz2')
        run('rm -f app.tar.bz2')
        for port in range(8000, 8004):
            sudo('./deploy/server stop %d' % port)

    sudo('/etc/init.d/monit restart')
    sudo('/etc/init.d/nginx restart')

