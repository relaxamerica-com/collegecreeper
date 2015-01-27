from fabric.api import *


def less():
    local("lessc /Users/matt/code/spudder/collegecreeper/scr/static/less/spudderspuds/spudderspuds.less /Users/matt/code/spudder/collegecreeper/scr/static/css/spudderspuds.css")

def path():
    local("export PATH=$PATH:/Users/matt/code/spudder/collegecreeper/assets/gaesdk/1.9.0/google_appengine/")