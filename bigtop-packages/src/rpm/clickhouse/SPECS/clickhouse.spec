%define __jar_repack 0

Name:		clickhouse
Version:	%{clickhouse_version}
Release:	%{clickhouse_release}
Summary:	Yandex ClickHouse DBMS

Group:		Applications/Databases
License:	Apache License, Version 2.0
Vendor: Yandex
Packager: ArenaData
Url: https://clickhouse.yandex/
Source0:	clickhouse-%{clickhouse_version}.tar.gz
Source1:  do-component-build
Source2:  install_clickhouse.sh
#BIGTOP_PATCH_FILES

%description
ClickHouse is an open-source column-oriented database management
system that allows generating analytical data reports in real time.

#
# clickhouse-client
#
%package client
Summary: %{name} client binary
Requires: %{name}-server = %{version}-%{release}

%description client
This package contains client binary for ClickHouse DBMS.

#
# clickhouse-common-static
#
%package common-static
Summary: %{name} common static binaries

%description common-static
This package contains static binaries for ClickHouse DBMS

#
# clickhouse-server-common
#
%package server-common
Summary: Common configuration files for %{name}

%description server-common
This package contains common configuration files for ClickHouse DBMS.

#
# clickhouse-server
#
%package server

Summary: Server files for %{name}
Requires: %{name}-common-static = %{version}-%{release}
Requires: %{name}-server-common = %{version}-%{release}

%description server
This package contains server files for ClickHouse DBMS.

#
# clickhouse-test
#
%package test
Summary: %{name} test suite
Requires: %{name}-server = %{version}-%{release}

%description test
This package contains test suite for ClickHouse DBMS


%prep
%setup -q -n clickhouse-%{clickhouse_version}
#BIGTOP_PATCH_COMMANDS

%build
bash %{SOURCE1}

%install
%__rm -rf $RPM_BUILD_ROOT

/bin/bash %{SOURCE2} $RPM_BUILD_ROOT %{clickhouse_version}


%post client
getent group clickhouse >/dev/null || groupadd -r clickhouse
getent passwd clickhouse >/dev/null || useradd -c "Clickhouse server" -s /sbin/nologin -g clickhouse -d /var/lib/clickhouse -r -M  clickhouse 2> /dev/null || :
mkdir -p /etc/clickhouse-client/conf.d
chown -R ${CLICKHOUSE_USER}:${CLICKHOUSE_GROUP} /etc/clickhouse-client || true

%post server
if [ $1 = 1 ]; then
	sbin/chkconfig --add clickhouse-server
fi

getent group clickhouse >/dev/null || groupadd -r clickhouse
getent passwd clickhouse >/dev/null || useradd -c "Clickhouse server" -s /sbin/nologin -g clickhouse -d /var/lib/clickhouse -r -M  clickhouse 2> /dev/null || :

if [ ! -d /var/lib/clickhouse ]; then
	mkdir -p /var/lib/clickhouse
	chown clickhouse:clickhouse /var/lib/clickhouse
	chmod 700 /var/lib/clickhouse
fi

if [ ! -d /var/log/clickhouse-server ]; then
	mkdir -p /var/log/clickhouse-server
	chown root:clickhouse /var/log/clickhouse-server
	chmod 775 /var/log/clickhouse-server
fi

if [ -d "/var/log/clickhouse-server/build" ]; then
	rm -f /var/log/clickhouse-server/build/*.cpp /var/log/clickhouse-server/build/*.so ||:
fi


%preun server
/sbin/service clickhouse-server stop > /dev/null 2>&1
/sbin/chkconfig --del clickhouse-server


%files client
/usr/bin/clickhouse-client
/usr/bin/clickhouse-local
/usr/bin/clickhouse-compressor
/usr/bin/clickhouse-benchmark
%config(noreplace) /etc/clickhouse-client/config.xml
/usr/bin/clickhouse-extract-from-config

%files common-static
/usr/bin/clickhouse
%config(noreplace) /etc/security/limits.d/clickhouse.conf
# folder
/usr/share/clickhouse

%files server-common
%config(noreplace) /etc/clickhouse-server/config.xml
%config(noreplace) /etc/clickhouse-server/users.xml

%files server
/usr/bin/clickhouse-server
/usr/bin/clickhouse-clang
/usr/bin/clickhouse-lld
/usr/bin/clickhouse-copier
/usr/bin/clickhouse-odbc-bridge
/usr/bin/clickhouse-report
/usr/bin/clickhouse-obfuscator
# TODO
#/etc/systemd/system/clickhouse-server.service
/etc/init.d/clickhouse-server
/etc/cron.d/clickhouse-server
# folder
/usr/share/clickhouse
%config(noreplace) /etc/security/limits.d/clickhouse.conf
# append file that seems to be obsoleted
/usr/bin/clickhouse-format

%files test
/usr/bin/clickhouse-test
/usr/bin/clickhouse-test-server
/usr/bin/clickhouse-performance-test
# folder
/usr/share/clickhouse-test
%config(noreplace) /etc/clickhouse-client/client-test.xml
%config(noreplace) /etc/clickhouse-server/server-test.xml

%changelog
