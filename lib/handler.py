import os
import sys
import subprocess
import threading
import re


modname = None
debug = True
is_cmd = False
modid = None

vardic = {}


class handler():



    def getcmd(self):
        cmd = raw_input('Nagcian-' + str(modid) + '>')
        cmdlist = ['use','exploit','set','show','bnet','back','help','exit','cd']
        temcmd = re.split(' ',cmd)
        if debug == True:
            print '[#]500 debug' + str(temcmd)
        if temcmd[0] in cmdlist:
            if debug == True:
                print '[#]500 debug' + cmd
            strcount = 0
            exestr = temcmd[0] + '('
            if debug == True:
                print '[#]500 debug' + str(exestr)
            temcmd.reverse()
            temcmd.pop()
            temcmd.reverse()
            for i in temcmd:
                if debug == True:
                    print '[#]500 debug' + str(strcount)
                exestr += '\'' + str(temcmd[strcount]) + '\''
                strcount += 1
                exestr += ','
            exestr = exestr.strip(',')
            exestr += ')'
            try:
                exestr = 'self.%s '% exestr
                exec(exestr)
            except Exception,e:
                if debug == True:
                    print '[#]500 debug Err:' + str(e)
                print '[!]201 Exec command error:' + str(exestr)

    def use(self,modname):
        try:
            global modid
            mod = re.sub('/','.',modname)
            if debug == True:
                print '[#]500 debug:' + mod
            modid = mod
            __import__(mod)
        except Exception,err:
            print '[!]210 Use error:' + str(err)

    def set(self,name,value):
        global vardic
        vardic[name] = value
        print '[*]400 %s has been set to %s' %(name,value)
        if debug == True:
            print '[#]500 debug' + str(vardic)

    def back(self):
        try:
            #mod = re.sub('/','.',modname)
            global modid
            del(modid)
            modid = None
        except:
            print '[!]212 Back failed: ' + str(modname)

    def exploit(self):
            global vardic
            global  is_cmd
            global modid
        #try:
            for var in vardic.keys():
                vargen = str(var) + '=' + str(vardic[var])
                exec(vargen)
                if debug == True:
                    print '[#]500 debug registered variable' + var
            modname = modid + '.exp()'
            if debug == True:
                print '[#]500 debug' + modname
                exec(modname)
        #except:
            print '[!]220 Exploit failed.'

    def show(self):
        global modid

cmdhandler = handler()
while True:
    cmdhandler.getcmd()

