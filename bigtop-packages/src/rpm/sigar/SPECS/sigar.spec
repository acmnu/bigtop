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
%define man_dir %{_mandir}

%if  %{?suse_version:1}0
%define bin_sigar /usr/lib64
%define doc_sigar /usr/share/doc/%{name}-%{sigar_base_version}
%define autorequire no
%else
%define bin_sigar /usr/lib64
%define doc_sigar /usr/share/doc/%{name}-%{sigar_base_version}
%define autorequire yes
%endif
%define  debug_package %{nil}

Name: sigar
Version: %{sigar_version}
Release: %{sigar_release}
Summary: Hyperic Sigar
URL: https://github.com/hyperic/sigar
Group: Development/Libraries
Buildroot: %{_topdir}/INSTALL/%{name}-%{version}
License: ASL 2.0
Source0: sigar-%{sigar_base_version}.tar.gz
Source1: do-component-build
#BIGTOP_PATCH_FILES
AutoReqProv: %{autorequire}

%description
sigar

%prep
%setup -n %{name}-%{sigar_base_version}

#BIGTOP_PATCH_COMMANDS

%build

%install
%__rm -rf $RPM_BUILD_ROOT
bash %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{bin_sigar}
mkdir -p $RPM_BUILD_ROOT%{doc_sigar}

cp -f -r build/build-src/*.so $RPM_BUILD_ROOT%{bin_sigar}
cp -f -r AUTHORS $RPM_BUILD_ROOT%{doc_sigar}
cp -f -r LICENSE $RPM_BUILD_ROOT%{doc_sigar}
cp -f -r NOTICE  $RPM_BUILD_ROOT%{doc_sigar}
cp -f -r README $RPM_BUILD_ROOT%{doc_sigar}
cp -f -r ChangeLog $RPM_BUILD_ROOT%{doc_sigar}


%files
%defattr(-,root,root)
%{bin_sigar}
%{doc_sigar}

%changelog
