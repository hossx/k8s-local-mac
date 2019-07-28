#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2019 Loopring Inc. All Rights Reserved.

__author__ = 'hoss@loopring.org (Ma Chao)'

import os
import sys
import subprocess

KUBE_VERSION = '1.14.0'
MINIKUBE_VERSION = '1.2.0'
VB_VERSION = '6.0.10'

VB_FILE_NAME = 'VirtualBox-6.0.10-132072-OSX.dmg'

def parse_minikube_version(version_str):
    version = version_str.split(':')[1].strip()
    return version[1:]

def parse_kubectl_version(version_str):
    version = version_str.split(',')[2].split('"')[1].strip()
    return version[1:]

def parse_vb_version(version_str):
    return version_str[0:6]

def check_or_install(cmd, version_arg, version, parse_version, install_func):
    is_pass = False
    try:
        version_str = subprocess.check_output([cmd] + version_arg)
        installed_version = parse_version(version_str)
        print 'current %s version is %s'%(cmd, installed_version)
        is_pass = (version == installed_version)
    except:
        print '%s is not installed'%(cmd)
    if not is_pass:
        install_func(cmd, version)

def install(cmd, version):
    print 'installing %s %s ...'%(cmd, version)
    command = 'sudo cp %s/tools/%s /usr/local/bin/'%(sys.path[0], cmd)
    print command
    subprocess.call(command, shell=True)

def install_vb(cmd, version):
    print 'installing %s %s ...'%(cmd, version)
    cmds = []
    cmds.append('hdiutil attach %s/tools/%s'%(sys.path[0], VB_FILE_NAME))
    cmds.append(
        'sudo installer -pkg /Volumes/VirtualBox/VirtualBox.pkg -target "/"')
    cmds.append('hdiutil detach /Volumes/VirtualBox/')
    exe_commands(cmds)

def exe_commands(cmds):
    for cmd in cmds:
        print cmd
        subprocess.call(cmd, shell=True)

def set_env():
    cmds = []

    cmds.append('minikube delete')
    cmds.append('rm -rf ~/.minikube')

    cmds.append('minikube config set cpus 4')
    cmds.append('minikube config set disk-size "40g"')
    cmds.append('minikube config set memory 8192')
    cmds.append('minikube config set kubernetes-version %s'%(KUBE_VERSION))

    exe_commands(cmds)

def main():
    check_or_install('minikube', ['version'], MINIKUBE_VERSION,
        parse_minikube_version, install)

    check_or_install('kubectl', ['version','--client=true'], KUBE_VERSION,
        parse_kubectl_version, install)

    check_or_install('VBoxManage', ['--version'], VB_VERSION,
        parse_vb_version, install_vb)

    set_env()

if __name__ == '__main__':
    main()
