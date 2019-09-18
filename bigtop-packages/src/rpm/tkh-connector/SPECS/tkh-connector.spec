%define debug_package %{nil}

Name: tkh-connector
Version: %{tkh_connector_version}
Release: %{tkh_connector_release}
Summary: Connection pool for Greenplum Database
Group: Development/Tools

Buildroot: %(mktemp -ud %{_tmppath}/%{tkh_connector_name}-%{version}-%{release}-XXXXXX)
License:  BSD License
Source0: tkh-connector-%{tkh_connector_base_version}.tar.gz
Source1: do-component-build 
Source2: install_%{name}.sh
Source3: bigtop.bom

Requires: bash, pxf
Provides: tkh_connector
AutoReqProv: no

%description 
The tkh_connector package provides connection pool for the Greenplum Database.

%prep
%setup -q -n %{name}-%{tkh_connector_base_version}

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{tkh_connector_base_version}


%files 
%defattr(-,root,root,755)
/usr/lib/pxf/lib/*
