Summary:	Maemo MCE (Mode Control Entity) definitions
Summary(pl.UTF-8):	Definicje MCE (Mode Control Entity) dla Maemo
Name:		mce
Version:	1.5.6
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/%{name}-dev_%{version}.tar.gz
# Source0-md5:	b3a28fe9bcec2fc7ae70f5d819bf3d1a
URL:		https://maemo.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maemo MCE (Mode Control Entity) definitions.

%description -l pl.UTF-8
Definicje MCE (Mode Control Entity) dla Maemo.

%package devel
Summary:	Maemo MCE (Mode Control Entity) definition headers
Summary(pl.UTF-8):	Pliki nagłówkowe definiujące MCE (Mode Control Entity) dla Maemo
Group:		Development/Libraries

%description devel
Maemo MCE (Mode Control Entity) definition headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe definiujące MCE (Mode Control Entity) dla Maemo.

%prep
%setup -q -n mce-dev-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkgconfigdir},%{_includedir}/mce}

install mce.pc $RPM_BUILD_ROOT%{_pkgconfigdir}
install include/mce/*.h $RPM_BUILD_ROOT%{_includedir}/mce

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%{_includedir}/mce
%{_pkgconfigdir}/mce.pc
