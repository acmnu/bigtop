%define debug_package %{nil}

Name: gptkh
Version: %{gptkh_version}
Release: %{gptkh_release}
Summary: Connection pool for Greenplum Database
Group: Development/Tools

Buildroot: %(mktemp -ud %{_tmppath}/%{gptkh_name}-%{version}-%{release}-XXXXXX)
License:  Arenadata License
Source0: gptkh-%{gptkh_base_version}.tar.gz
Source1: do-component-build 
Source2: install_%{name}.sh
Source3: bigtop.bom

Requires: bash, gpdb
Provides: gptkh
AutoReqProv: no

%description 
GpTKH - is a Greenplum extension for "transaction-like" data loading into ClickHouse via PXF.

%prep
%setup -q -n %{name}-%{gptkh_base_version}

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{gptkh_base_version}


%files 
%attr(0755,root,root) /usr/lib/gpdb/lib/postgresql/*
%attr(0644,root,root) /usr/lib/gpdb/share/postgresql/extension/*
