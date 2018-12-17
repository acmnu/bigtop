%define debug_package %{nil}

Name: pxf
Version: %{pxf_version}
Release: %{pxf_release}
Summary: Connection pool for Greenplum Database
Group: Development/Tools

BuildArch: x86_64
Buildroot: %(mktemp -ud %{_tmppath}/%{pxf_name}-%{version}-%{release}-XXXXXX)
License:  BSD License
Source0: pxf-%{pxf_base_version}.tar.gz
Source1: do-component-build 
Source2: install_%{name}.sh
Source3: bigtop.bom
Source4: pxf.service


Requires: bash
Provides: pxf
AutoReqProv: no

%description 
The pxf package provides connection pool for the Greenplum Database.

%prep
%setup -q -n %{name}-%{pxf_base_version}

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{pxf_version}
cp -R  %{SOURCE4} $RPM_BUILD_ROOT/etc/systemd/system/

%pre
getent group pxf >/dev/null || groupadd -r pxf
getent passwd pxf >/dev/null || useradd -c "pxf" -s /sbin/nologin -g pxf -r pxf 2> /dev/null || :



%files 
%defattr(-,root,root,755)
%config(noreplace) /etc/pxf/
%attr(0755,pfx,pxf) /usr/lib/pxf/
%attr(0664,root,root)/etc/systemd/system/*

%changelog

