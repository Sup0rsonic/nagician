import os
import sys
import subprocess
import threading
import re

import exploit

modname = None
debug = True
is_cmd = False
modid = None

vardic = {}



class handler():



    def getcmd(self):
        cmd = raw_input('Nagcian-' + str(modid) + '>')
        cmdlist = ['use','exploit','set','show','bnet','back','help','exit','cd','eval','find']
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
        else:
            try:
                print '[+]410 Exec:' + cmd
                subprocess.Popen(cmd,shell=True)
            except:
                print '[!]215 Exec Failed:' + cmd

    def use(self,modname):
        try:
            global modid
            mod = re.sub('/','.',modname)
            if debug == True:
                print '[#]500 debug:' + mod
            modid = mod
            evastr = 'import  ' + mod
            if debug == True:
                print '[#]500 debug' + evastr
            exec(evastr)
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
            if debug == True:
                print modid
            del(modid)
            modid = None
        except:
            print '[!]212 Back failed: ' + str(modname)

    def exploit(self):
        global vardic
        global is_cmd
        global modid
        modid = modid.strip('lib.')
        try:
            for var in vardic.keys():
                vargen = str(var) + '= \'' + str(vardic[var]) + '\''
                print vargen
                exec(vargen)
                exec('global ' + var)
                if debug == True:
                    print '[#]500 debug registered variable' + var
            modname = modid + '.exp(vardic)'
            if debug == True:
                print '[#]500 debug' + modname
            exec(modname)
        except Exception,e:
            print '[!]220 Exploit failed.'
            print str(e)

    def eval(self,cmd):
        try:
            print '[#]500 debug' + cmd
            exec(cmd)
        except Exception,e:
            print '[#]500 debug Exception:' + str(e)

    def show(self,mod):
        global modid
        execmd = modid + '.' + mod + '()'
        try:
            if debug == True:
                print '[#]500 debug' + execmd
            exec(execmd)
        except:
            print '[!]223 Exec failed.'

    def cd(self,dir):
        try:
            os.chdir(dir)
            print '[*]402 Current dir:' + dir
        except:
            print '[!]213 Dir change failed.'

    def exit(self):
        sys.exit('Exit.')

    def find(self,modname):
        path = os.path.realpath(__file__)
        filepath = re.findall('.*/',path)
        expath = filepath[0] + '/exploit'
        if debug == True:
            print '[#]500 debug' + expath
        for file in os.listdir(expath):
            if file.endswith('.py'):
                if re.findall(modname,file) != []:
                    print '[*]416 Find: exloit/' + file




#cmdhandler = handler()
#while True:
#    cmdhandler.getcmd()
