%define debug_package %{nil}

Name: pxf
Version: %{pxf_version}
Release: %{pxf_release}
Summary: Connection pool for Greenplum Database
Group: Development/Tools

Buildroot: %(mktemp -ud %{_tmppath}/%{pxf_name}-%{version}-%{release}-XXXXXX)
License:  BSD License
Source0: pxf-%{pxf_base_version}.tar.gz
Source1: do-component-build 
Source2: install_%{name}.sh
Source3: bigtop.bom
Source4: pxf.service
#BIGTOP_PATCH_FILES


Requires: bash, java-1.8.0-openjdk-devel
Provides: pxf
AutoReqProv: no

%description 
The pxf package provides connection pool for the Greenplum Database.

%prep
%setup -q -n %{name}-%{pxf_base_version}
#BIGTOP_PATCH_COMMANDS

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{pxf_version}
cp -R  %{SOURCE4} $RPM_BUILD_ROOT/usr/lib/systemd/system/

%pre
getent group pxf >/dev/null || groupadd -r pxf
getent passwd pxf >/dev/null || useradd -c "pxf" -s /sbin/nologin -g pxf -r pxf 2> /dev/null || :


%post
mkhomedir_helper pxf
systemctl daemon-reload


%files 
%defattr(-,root,root,755)
/usr/lib/systemd/system/*
%config(noreplace) %attr(0755,pxf,pxf) /etc/pxf/
%attr(0755,pxf,pxf) /usr/lib/pxf/
%attr(0755,pxf,pxf) /var/log/pxf/
%attr(0755,pxf,pxf) /var/run/pxf/
%attr(0755,pxf,pxf) /var/lib/pxf

%changelog

