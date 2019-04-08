#!/bin/bash

# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

set -e
set -x

prefix=$1
version=$2

#cd build
#DAEMONS="clickhouse clickhouse-test clickhouse-compressor clickhouse-client clickhouse-server"
#for daemon in $DAEMONS; do \
#  scl enable devtoolset-7 "DESTDIR=${prefix} cmake3 -DCOMPONENT=$daemon -P cmake_install.cmake"; \
#done
#cd ..
mkdir -p ${prefix}/usr
ls tmpdirname/*
cp -r tmpdirname/* ${prefix}/

# Create folders structure to be distributed
#mkdir -p ${prefix}/etc/clickhouse-server
#mkdir -p ${prefix}/etc/clickhouse-client
#mkdir -p ${prefix}/etc/init.d
#mkdir -p ${prefix}/etc/cron.d
#mkdir -p ${prefix}/etc/security/limits.d

#mkdir -p ${prefix}/usr/bin
#mkdir -p ${prefix}/usr/share/clickhouse/bin
#mkdir -p ${prefix}/usr/share/clickhouse/headers

# Copy files from source into folders structure for distribution
# BUILDDIR = rpmbuild/BUILD
#cp debian/clickhouse-server.init   ${prefix}/etc/init.d/clickhouse-server
#cp debian/clickhouse-server.cron.d ${prefix}/etc/cron.d/clickhouse-server
#cp debian/clickhouse.limits        ${prefix}/etc/security/limits.d/clickhouse.conf
#cp dbms/programs/server/config.xml ${prefix}/etc/clickhouse-server/
#cp dbms/programs/server/users.xml  ${prefix}/etc/clickhouse-server/
