import os
import sys
import subprocess
import threading
import re

modname = None
debug = True
is_cmd = False

class handler():

    def getcmd(self):
        cmd = raw_input('Nagcian-' + str(modname))
        cmdlist = ['use','exploit','set','show','bnet','back','help','exit','cd']
        temcmd = re.split(' ',cmd)
        if temcmd[0] in cmdlist:
            if debug == True:
                print '[#]500 debug' + cmd
            if temcmd[0] == 'use':


    def use(self,modname):
        try:
            mod = re.sub('/','.',modname)
            if debug == True:
