#!/bin/sh
#
# Copyright 2019 Loopring Fund. All Rights Reserved.
# Author: hoss@loopring.org (Ma Chao)

rm -rf ./tools

id=$(docker create hosschao/k8s-mac)
docker cp $id:/tools ./tools
docker rm -v $id

./init.sh
