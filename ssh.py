#-*- coding: utf-8 -*-
#!/usr/bin/python
import paramiko
import datetime
import os
import threading

def sshd(ip,username,passwd,cmd):
    try:
        paramiko.util.log_to_file('paramiko.log')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip,22,username,passwd,timeout=3)
        for m in cmd:
            stdin,stdout,stderr = ssh.exec_command(m)
            #stdin.write("Y")   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            # outerr = stderr.readlines()
            #屏幕输出
            for o in out:
                print o,
                print '%s\tOK\n'%(ip)
        ssh.close()
    except :
        print '%s\tError\n'%(ip)

if __name__=='__main__':
    cmds=open("cmd.txt") #从文件读取命令
    cmd=cmds.readlines()
    cmds.close()
    username = "user"  #用户名
    print "Begin......"
    hosts=open("iplist.txt") #本地服务器列表
    host=hosts.readlines()
    hosts.close()
    for list in host:
        line = list.split()
        ip = line[0].strip()
        pwd = 'password'
        a=threading.Thread(target=sshd,args=(ip,username,pwd,cmd))
        a.start()
