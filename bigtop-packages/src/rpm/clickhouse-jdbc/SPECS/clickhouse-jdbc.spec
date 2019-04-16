%define __jar_repack 0

# disable debuginfo packages
%define debug_package %{nil}

Name:		clickhouse-jdbc
Version:	%{clickhouse_jdbc_version}
Release:	%{clickhouse_jdbc_release}
Summary:	Yandex ClickHouse DBMS jdbc driver

Group:		Applications/Databases
License:	Apache License, Version 2.0
Vendor: Yandex
Packager: ArenaData
Url: https://clickhouse.yandex/
Source0:	clickhouse-jdbc-%{clickhouse_jdbc_version}.tar.gz
Source1:  do-component-build
Source2:  install_clickhouse-jdbc.sh
#BIGTOP_PATCH_FILES

%description
Yandex ClickHouse DBMS jdbc driver

%prep
%setup -q -n clickhouse-jdbc-%{clickhouse_jdbc_version}
#BIGTOP_PATCH_COMMANDS

%build
bash %{SOURCE1} %{clickhouse_jdbc_version}

%install
%__rm -rf $RPM_BUILD_ROOT 

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{clickhouse_jdbc_version}

%files
# just include the whole directory
%defattr(-,root,root)
/usr/share/doc/clickhouse-jdbc
/usr/share/licenses/clickhouse-jdbc
/usr/share/java/*

%changelog
