from fabric.api import *


def less():
    local("lessc /Users/matt/code/spudder/collegecreeper/scr/static/less/spudderspuds/spudderspuds.less /Users/matt/code/spudder/collegecreeper/scr/static/css/spudderspuds.css")