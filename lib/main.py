import urllib
import urllib2
import re
import paramiko
import subprocess
import socket

#OS_IMPORT_TEST
import os

#todo:Command handler
#THIS PART WILL BEEN REWRITED!

module = None
cmdlist = ['exploit','use','back','set']
dir = '/'
is_cmd = 0
debug = True

class commandhandler():

    def handler(self):

        while True:
            cmd = raw_input('Nagician-' + str(module) + " >")
            try:
                print '[*]100 Preload'
                self.commandexec(cmd)
            except Exception,w:
                if debug == True:
                    print '[!]210 Preload Failed'

    def commandexec(self,cmd):
#todo improve shell experience
        if cmd == '':
            print '[*]120 Null command'
            return

        print '[*]101 Exec %s' % cmd
        for arg in cmdlist:
            global is_cmd

            if re.findall(arg,cmd) != []:
                global dic,is_cmd,i
                is_cmd = 1
                try:
                    #todo:case
                    if debug == True:
                        print is_cmd
                    dic = re.split(' ',cmd)
                    if debug == True:
                        print '[#]500 Debug dic= %s' %str(dic)
                    if dic[0] == 'exploit':
                        exec('exploit(%s)' % str(module))
                    elif dic[0] == 'back':
                        if debug == True:
                            print "[#]500 Debug back"
                        modname = dic[1]
                        self.back(str(modname))
                        module = None
                    elif dic[0] == set:
                        var = re.split('=',dic[1])
                        vardic = {}

                    elif dic[0] == 'use':
                        self.use(str(dic[1]))
                        is_cmd = 1
                    if debug == True:
                        print str(is_cmd)

                except Exception,e:
                    if debug == True:
                        print '[!]201 Exec failed'
            else:
                is_cmd = 0
                pass


        try:
            global is_cmd
            print is_cmd
            if is_cmd == 0:
                if re.findall('cd',cmd) != []:
                    dir = re.findall('cd (.*)',cmd)
                    os.chdir(str(dir[0]))
                else:
                    if is_cmd == 0:
                        subprocess.Popen(cmd,shell=True)
        except Exception,e:
            if debug == True:
                print e
            print '[!]211 Popen Failed'


    def use(self,mod):
        try:
            global module
            module = mod
            mod = re.sub('/','.',mod,5)
            mod = 'mod.' + mod
            if debug == True:
                print '[#]500 Debug modname: %s' % mod
            __import__(mod)
        except Exception,e:
            print '[!]212 Import failed'
            print e

    def back(self,mod):
        global module
        module = None
