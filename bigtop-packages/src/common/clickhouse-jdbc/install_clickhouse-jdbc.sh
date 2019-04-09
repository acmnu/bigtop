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

install -d -m 0755 ${prefix}/usr/share/java
install -d -m 0755 ${prefix}/usr/share/doc/clickhouse-jdbc
install -d -m 0755 ${prefix}/usr/share/licenses/clickhouse-jdbc
#install -d -m 0755 ${prefix}/usr/share/maven-poms
#install -d -m 0755 ${prefix}/usr/share/maven-metadata

cp target/clickhouse-jdbc-${version}-jar-with-dependencies.jar ${prefix}/usr/share/java/clickhouse-jdbc-${version}.jar

cp AUTHORS CHANGELOG README.md ${prefix}/usr/share/doc/clickhouse-jdbc
cp LICENSE ${prefix}/usr/share/licenses/clickhouse-jdbc

cd ${prefix}/usr/share/java/
ln -s clickhouse-jdbc-${version}.jar clickhouse-jdbc.jar
