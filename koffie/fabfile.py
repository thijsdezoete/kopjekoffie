from __future__ import with_statement
from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['seastar']

def test():
    local('./manage.py test article')

def commit():
    local('git pull')
    local('git add -p && git commit')

def push():
    local('git push origin master')

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
    #prepare_deploy()
    code_dir = '/opt/domains/kopjekoffie.eu/src/kopjekoffie'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            code_dir = '/opt/domains/kopjekoffie.eu/src/'
            run("git clone git@github.com:thijsdezoete/kopjekoffie.git %s" % code_dir)
            code_dir = '/opt/domains/kopjekoffie.eu/src/kopjekoffie'
    with cd(code_dir):
         run("git pull")
         run("find . -type f -name '*.pyc'")
         run("find . -type f -name '*.pyc' -exec rm {} \; ;")
    with cd(code_dir + '/koffie'):
         run("sudo uwsgi --ini=uwsgi.ini")
