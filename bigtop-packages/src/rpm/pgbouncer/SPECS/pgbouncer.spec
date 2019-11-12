%define debug_package %{nil}

Name: pgbouncer
Version: %{pgbouncer_version}
Release: %{pgbouncer_release}
Summary: Connection pool for Greenplum Database
Group: Development/Tools

Buildroot: %(mktemp -ud %{_tmppath}/%{pgbouncer_name}-%{version}-%{release}-XXXXXX)
License:  BSD License
Source0: pgbouncer-%{pgbouncer_base_version}.tar.gz
Source1: do-component-build 
Source2: install_%{name}.sh
Source3: bigtop.bom
Source4: pgbouncer.service
Source5: pgbouncer


Requires: bash
Provides: pgbouncer
AutoReqProv: no

%description 
The Pgbouncer package provides connection pool for the Greenplum Database.

%prep
%setup -q -n %{name}-%{pgbouncer_base_version}

%build
bash $RPM_SOURCE_DIR/do-component-build

%install
%__rm -rf $RPM_BUILD_ROOT
/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{pgbouncer_rest_version}
cp -R  %{SOURCE4} $RPM_BUILD_ROOT/usr/lib/systemd/system/
cp -R  %{SOURCE5} $RPM_BUILD_ROOT/etc/pam.d/

%pre
getent group pgbouncer >/dev/null || groupadd -r pgbouncer
getent passwd pgbouncer >/dev/null || useradd -c "pgbouncer" -s /sbin/nologin -g pgbouncer -r pgbouncer 2> /dev/null || :


%files 
%defattr(-,root,root,755)
/usr/bin/*
/etc/pgbouncer/
/usr/lib/systemd/system/*
/usr/share/doc/pgbouncer/
/etc/pam.d/pgbouncer
/usr/share/man/man1/*
/usr/share/man/man5/*
%attr(0755,pgbouncer,pgbouncer)/var/log/pgbouncer
%attr(0755,pgbouncer,pgbouncer)/var/run/pgbouncer