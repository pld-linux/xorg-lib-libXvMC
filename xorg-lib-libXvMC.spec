# $Rev: 3321 $, $Date: 2005-08-15 12:17:57 $
#
Summary:	XvMC library
Summary(pl):	Biblioteka XvMC
Name:		xorg-lib-libXvMC
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXvMC-%{version}.tar.bz2
# Source0-md5:	ad6b4feda17d720d52e2c097289e0fcd
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-proto-videoproto-devel
BuildRoot:	%{tmpdir}/libXvMC-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
XvMC library.

%description -l pl
Biblioteka XvMC.


%package devel
Summary:	Header files libXvMC development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXvMC
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXvMC = %{version}-%{release}
Requires:	xorg-lib-libXv-devel

%description devel
XvMC library.

This package contains the header files needed to develop programs that
use these libXvMC.

%description devel -l pl
Biblioteka XvMC.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXvMC.


%package static
Summary:	Static libXvMC libraries
Summary(pl):	Biblioteki statyczne libXvMC
Group:		Development/Libraries
Requires:	xorg-lib-libXvMC-devel = %{version}-%{release}

%description static
XvMC library.

This package contains the static libXvMC library.

%description static -l pl
Biblioteka XvMC.

Pakiet zawiera statyczn± bibliotekê libXvMC.


%prep
%setup -q -n libXvMC-%{version}


%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}


%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,wheel) %{_libdir}/libXvMC*.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXvMC*.la
%attr(755,root,wheel) %{_libdir}/libXvMC*.so
%{_pkgconfigdir}/xvmc.pc


%files static
%defattr(644,root,root,755)
%{_libdir}/libXvMC*.a
