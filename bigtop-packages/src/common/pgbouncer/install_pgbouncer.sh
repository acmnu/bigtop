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


install -d -m 0755 "${prefix}/usr/bin/"
install -d -m 0755 "${prefix}/etc/pgbouncer/"
install -d -m 0755 "${prefix}/usr/lib/systemd/system"
install -d -m 0755 "${prefix}/usr/share/man/man1"
install -d -m 0755 "${prefix}/usr/share/man/man5"
install -d -m 0755 "${prefix}/usr/share/doc/pgbouncer"
install -d -m 0755 "${prefix}/etc/pam.d/"
install -d -m 0755 "${prefix}/var/log/pgbouncer"
install -d -m 0755 "${prefix}/var/run/pgbouncer"



cp -R pgbouncer "${prefix}/usr/bin/"
cp -R etc/pgbouncer.ini "${prefix}/etc/pgbouncer/"
cp -R doc/pgbouncer.1  "${prefix}/usr/share/man/man1"
cp -R doc/pgbouncer.5  "${prefix}/usr/share/man/man5"
cp -R AUTHORS "${prefix}/usr/share/doc/pgbouncer"
cp -R COPYRIGHT "${prefix}/usr/share/doc/pgbouncer"
cp -R NEWS.md "${prefix}/usr/share/doc/pgbouncer"
cp -R README.md "${prefix}/usr/share/doc/pgbouncer"

