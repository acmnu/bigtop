%define __jar_repack 0

# disable debuginfo packages
%define debug_package %{nil}

Name:		clickhouse-odbc
Version:	%{clickhouse_odbc_version}
Release:	%{clickhouse_odbc_release}
Summary:	Yandex ClickHouse DBMS ODBC driver

Group:		Applications/Databases
License:	Apache License, Version 2.0
Vendor: Yandex
Packager: ArenaData
Url: https://clickhouse.yandex/
Source0:	clickhouse-odbc-%{clickhouse_odbc_version}.tar.gz
Source1:  do-component-build
Source2:  install_clickhouse-odbc.sh
#BIGTOP_PATCH_FILES
Requires:  unixODBC
Requires:  libtool-ltdl

%description
Yandex ClickHouse DBMS ODBC driver

%prep
%setup -q -n clickhouse-odbc-%{clickhouse_odbc_version}
#BIGTOP_PATCH_COMMANDS

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{clickhouse_odbc_version}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
# just include the whole directory
%defattr(-,root,root)
/usr/local

%changelog
