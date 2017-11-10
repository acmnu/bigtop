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

usage() {
  echo "
usage: $0 <options>
  Required not-so-options:
     --build-dir=DIR             path to hive/build/dist
     --prefix=PREFIX             path to install into

  Optional options:
     --doc-dir=DIR               path to install docs into [/usr/share/doc/hive]
     --hive-dir=DIR               path to install hive home [/usr/lib/hive]
     --installed-hive-dir=DIR     path where hive-dir will end up on target system
     --bin-dir=DIR               path to install bins [/usr/bin]
     --examples-dir=DIR          path to install examples [doc-dir/examples]
     --hcatalog-dir=DIR          path to install hcatalog [/usr/lib/hcatalog]
     --installed-hcatalog-dir=DIR path where hcatalog-dir will end up on target system
     ... [ see source for more similar options ]
  "
  exit 1
}

OPTS=$(getopt \
  -n $0 \
  -o '' \
  -l 'prefix:' \
  -l 'doc-dir:' \
  -l 'etc-dir:' \
  -l 'build-dir:' \
  -l 'version:' -- "$@")

if [ $? != 0 ] ; then
    usage
fi

eval set -- "$OPTS"
while true ; do
    case "$1" in
        --prefix)
        PREFIX=$2 ; shift 2
        ;;
        --build-dir)
        BUILD_DIR=$2 ; shift 2
        ;;
        --doc-dir)
        DOC_DIR=$2 ; shift 2
        ;;
        --etc-dir)
        ETC_DIR=$2 ; shift 2
        ;;
        --version)
        VERSION=$2 ; shift 2
        ;;
        --)
        shift ; break
        ;;
        *)
        echo "Unknown option: $1"
        usage
        exit 1
        ;;
    esac
done

for var in PREFIX BUILD_DIR ; do
  if [ -z "$(eval "echo \$$var")" ]; then
    echo Missing param: $var
    usage
  fi
done

mkdir -p "$PREFIX/usr/lib"
cd $PREFIX/usr/lib
tar xf "${BUILD_DIR}/apache-hive-${VERSION}-src/packaging/target/apache-hive-${VERSION}-bin.tar.gz"

mv apache-hive-2.3.0-bin hive

CONF_DIR=/etc/hive
CONF_DIST_DIR=/etc/hive/conf.dist

install -d -m 0755 $PREFIX/etc/hive
install -d -m 0755 $PREFIX/etc/hive/conf
mv $PREFIX/usr/lib/hive/conf $PREFIX/etc/hive/conf.dist
ln -sfn /etc/hive/conf $PREFIX/usr/lib/hive/conf

BIN_DIR=$PREFIX/usr/bin
INSTALLED_HIVE_DIR=/usr/lib/hive
INSTALLED_HCATALOG_DIR=${INSTALLED_HCATALOG_DIR:-/usr/lib/hive/hcatalog}

install -d -m 0755 ${BIN_DIR}
for file in hive beeline hiveserver2
do
  wrapper=$BIN_DIR/$file
  cat >>$wrapper <<EOF
#!/bin/bash

# Autodetect JAVA_HOME if not defined
if [ -e /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
  . /usr/lib/bigtop-utils/bigtop-detect-javahome
fi

BIGTOP_DEFAULTS_DIR=\${BIGTOP_DEFAULTS_DIR-/etc/default}
[ -n "\${BIGTOP_DEFAULTS_DIR}" -a -r \${BIGTOP_DEFAULTS_DIR}/hbase ] && . \${BIGTOP_DEFAULTS_DIR}/hbase

export HIVE_HOME=$INSTALLED_HIVE_DIR
exec $INSTALLED_HIVE_DIR/bin/$file "\$@"
EOF
  chmod 755 $wrapper
done

wrapper=$BIN_DIR/hcat
cat >>$wrapper <<EOF
#!/bin/sh

BIGTOP_DEFAULTS_DIR=${BIGTOP_DEFAULTS_DIR-/etc/default}
[ -n "${BIGTOP_DEFAULTS_DIR}" -a -r ${BIGTOP_DEFAULTS_DIR}/hadoop ] && . ${BIGTOP_DEFAULTS_DIR}/hadoop

# Autodetect JAVA_HOME if not defined
if [ -e /usr/lib/bigtop-utils/bigtop-detect-javahome ]; then
  . /usr/lib/bigtop-utils/bigtop-detect-javahome
fi

# FIXME: HCATALOG-636 (and also HIVE-2757)
export HIVE_HOME=/usr/lib/hive
export HIVE_CONF_DIR=/etc/hive/conf
export HCAT_HOME=$INSTALLED_HCATALOG_DIR

export HCATALOG_HOME=$INSTALLED_HCATALOG_DIR
exec $INSTALLED_HCATALOG_DIR/bin/hcat "\$@"
EOF
chmod 755 $wrapper

