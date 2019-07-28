#!/bin/sh
#
# Copyright 2019 Loopring Inc. All Rights Reserved.
# Author: hoss@loopring.org (Ma Chao)

./prepare.py &&

# After starting the minikube, the --registry-mirror options were wrote into
# config.json file at $HOME/.minikube/machines/minikube/config.json. And when
# starting minikube with minikube start, it will reload the config from the
# file config.json again.
minikube start --registry-mirror=https://registry.docker-cn.com && minikube dashboard
