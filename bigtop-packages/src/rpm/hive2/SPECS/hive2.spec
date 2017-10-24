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
%define hadoop_username hadoop
%define etc_hive2 /etc/%{name}
%define config_hive2 %{etc_hive2}/conf
%define conf_hcatalog %{_sysconfdir}/hive2-hcatalog/conf
%define conf_webhcat  %{_sysconfdir}/hive2-webhcat/conf
%define usr_lib_hive2 /usr/lib/%{name}
%define usr_lib_hcatalog /usr/lib/hive2-hcatalog
%define var_lib_hive2 /var/lib/%{name}
%define var_lib_hcatalog /var/lib/%{name}-hcatalog
%define var_log_hcatalog /var/log/%{name}-hcatalog
%define usr_bin /usr/bin
%define hive2_config_virtual hive2_active_configuration
%define man_dir %{_mandir}
%define hive2_services hive2-metastore hive2-server2 hive2-hcatalog-server hive2-webhcat-server
# After we run "ant package" we'll find the distribution here
%define hive2_dist build/dist

%define doc_hive2 %{_docdir}/%{name}
%define alternatives_cmd update-alternatives

%global initd_dir %{_sysconfdir}/rc.d

Name: hive2
Version: %{hive2_version}
Release: %{hive2_release}
Summary: Hive is a data warehouse infrastructure built on top of Hadoop
License: ASL 2.0
URL: http://hive2.apache.org/
Group: Development/Libraries
Buildroot: %{_topdir}/INSTALL/hive2-%{version}
BuildArch: noarch
Source0: apache-hive-%{hive2_base_version}-src.tar.gz
Source1: do-component-build
Source2: install_hive.sh
#BIGTOP_PATCH_FILES
Requires: hadoop-client, bigtop-utils >= 0.7, zookeeper
Conflicts: hadoop-hive

%description 
Hive is a data warehouse infrastructure built on top of Hadoop that provides tools to enable easy data summarization, adhoc querying and analysis of large datasets data stored in Hadoop files. It provides a mechanism to put structure on this data and it also provides a simple query language called Hive QL which is based on SQL and which enables users familiar with SQL to query this data. At the same time, this language also allows traditional map/reduce programmers to be able to plug in their custom mappers and reducers to do more sophisticated analysis which may not be supported by the built-in capabilities of the language.

%prep
%setup -q -n apache-hive-%{hive2_base_version}-src

#BIGTOP_PATCH_COMMANDS

%build
bash %{SOURCE1}

#########################
#### INSTALL SECTION ####
#########################
%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} \
  --prefix=$RPM_BUILD_ROOT \
  --build-dir=%{_builddir} \
  --doc-dir=$RPM_BUILD_ROOT/%{doc_hive2} \
  --etc-dir=$RPM_BUILD_ROOT/%{etc_hive2} \
  --version=%{hive2_base_version}


%pre
getent group  hive >/dev/null || groupadd -r hive
getent passwd hive >/dev/null || useradd -c "Hive" -s /sbin/nologin -g hive -r -d %{var_lib_hive2} hive 2> /dev/null || :

# Manage configuration symlink
%post

#######################
#### FILES SECTION ####
#######################
%files
%{usr_lib_hive2}
