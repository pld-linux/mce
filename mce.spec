#
Summary:	Maemo MCE library
Name:		mce
Version:	1.5.6
Release:	1
License:	BSD
Group:		Development/Libraries
Source0:	http://repository.maemo.org/pool/bora/free/source/mce-dev_1.5.6.tar.gz
# Source0-md5:	b3a28fe9bcec2fc7ae70f5d819bf3d1a
URL:		https://maemo.org
#BuildRequires:	python-devel
#BuildRequires:	xulrunner-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maemo MCE library.

%package devel
Summary:	Headers for Maemo MCE library
Group:		Development/Libraries

%description devel
Headers for Maemo MCE library.

%prep
%setup -q -n mce-dev-%{version}

%build
#%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pkgconfigdir},%{_includedir}/mce}

#%{__make} install \
#	DESTDIR=$RPM_BUILD_ROOT
install mce.pc $RPM_BUILD_ROOT%{_pkgconfigdir}
install include/mce/*.h $RPM_BUILD_ROOT%{_includedir}/mce/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog NEWS README

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/mce.pc
%{_includedir}/mce
