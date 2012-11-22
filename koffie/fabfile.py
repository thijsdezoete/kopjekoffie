from fabric.api import local

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
