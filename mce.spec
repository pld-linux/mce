Summary:	Maemo MCE (Mode Control Entity) modules
Summary(pl.UTF-8):	Moduły MCE (Mode Control Entity) dla Maemo
Name:		mce
Version:	1.8.128.12
Release:	0.1
License:	LGPL v2.1
Group:		Libraries
#Source0Download: https://github.com/maemo-leste/mce/releases
Source0:	https://github.com/maemo-leste/mce/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	be3c5139c80b992e972a16a08534220a
URL:		https://maemo.org/
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	dsme-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libcal-devel
BuildRequires:	libconic-devel
BuildRequires:	libdevlock-devel
BuildRequires:	osso-systemui-dbus-devel
BuildRequires:	pkgconfig
BuildRequires:	upower-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MCE is responsible of handling display control (active/dim/blank),
activity monitoring (keys, buttons), keyboard backlight, ambient light
sensor (ALS), LEDs and device mode control. In addition, MCE is
responsible for providing interface to proximity, accelometer and
vibra devices.

%description -l pl.UTF-8
MCE odpowiada za obsługę sterowania obrazem (aktywność, ściemnianie,
wygaszanie), monitorowanie aktywności (klawisze, przyciski),
podświetlenie klawiatury, czujnik światła otoczenia (ALS - Ambient
Light Sensor), diody LED i sterowanie trybem urządzenia. Ponadto MCE
odpowiada za udostępnianie interfejsu do czujnika zbliżeniowego,
akcelerometru oraz wibratora.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	INSTALL="install -m755" \
	INSTALL_DATA="install -m644" \
	MODULEDIR=$RPM_BUILD_ROOT%{_libdir}/mce/modules

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_sbindir}/devlock-blocker
%attr(755,root,root) %{_sbindir}/mce
%dir %{_libdir}/mce
%dir %{_libdir}/mce/modules
%attr(755,root,root) %{_libdir}/mce/modules/libaccelerometer.so
%attr(755,root,root) %{_libdir}/mce/modules/libalarm.so
%attr(755,root,root) %{_libdir}/mce/modules/libaudiorouting.so
%attr(755,root,root) %{_libdir}/mce/modules/libbattery-upower.so
%attr(755,root,root) %{_libdir}/mce/modules/libcallstate.so
%attr(755,root,root) %{_libdir}/mce/modules/libcamera.so
%attr(755,root,root) %{_libdir}/mce/modules/libdisplay.so
%attr(755,root,root) %{_libdir}/mce/modules/libfilter-brightness-als.so
%attr(755,root,root) %{_libdir}/mce/modules/libfilter-brightness-simple.so
%attr(755,root,root) %{_libdir}/mce/modules/libhomekey.so
%attr(755,root,root) %{_libdir}/mce/modules/libinactivity.so
%attr(755,root,root) %{_libdir}/mce/modules/libkeypad.so
%attr(755,root,root) %{_libdir}/mce/modules/libled.so
%attr(755,root,root) %{_libdir}/mce/modules/libvibrator.so
%dir %{_sysconfdir}/mce
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mce/mce.ini
/etc/dbus-1/system.d/mce.conf
/etc/gconf/schemas/devicelock.schemas
/etc/gconf/schemas/security.schemas
%dir /var/lib/mce
%config(noreplace) %verify(not md5 mtime size) /var/lib/mce/mode
%dir /var/run/mce
