from __future__ import with_statement
from fabric.api import local
from fabric.api import local, settings, abort, run, cd
from fabric.contrib.console import confirm

def test():
    local('./manage.py test article')

def commit():
    local('git add -p && git commit')

def push():
    local('git push origin master')

def prepare_deploy():
    test()
    commit()
    push()

def deploy():
    code_dir = '/opt/domains/kopjekoffie.eu/src/kopjekoffie'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            code_dir = '/opt/domains/kopjekoffie.eu/src/'
            run("git clone git@github.com:thijsdezoete/kopjekoffie.git %s" % code_dir)
            code_dir = '/opt/domains/kopjekoffie.eu/src/kopjekoffie'
    with cd(code_dir):
         run("git pull")
         run("touch app.wsgi")
