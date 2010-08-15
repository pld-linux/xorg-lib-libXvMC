Summary:	XvMC library
Summary(pl.UTF-8):	Biblioteka XvMC
Name:		xorg-lib-libXvMC
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXvMC-%{version}.tar.bz2
# Source0-md5:	bfc7524646f890dfc30dea1d676004a3
Source1:	XvMCConfig
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-util-util-macros >= 1.3
Provides:	libXvMCW = %{version}
Obsoletes:	libXvMCW
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XvMC (X-Video Motion Compensation) library.

%description -l pl.UTF-8
Biblioteka XvMC (X-Video Motion Compensation, czyli kompensacji ruchu
dla X-Video).

%package devel
Summary:	Header files for libXvMC library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXvMC
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXv-devel
Provides:	libXvMCW-devel = %{version}
Obsoletes:	libXvMCW-devel

%description devel
XvMC (X-Video Motion Compensation) library.

This package contains the header files needed to develop programs that
use libXvMC.

%description devel -l pl.UTF-8
Biblioteka XvMC (X-Video Motion Compensation, czyli kompensacji ruchu
dla X-Video).

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXvMC.

%package static
Summary:	Static libXvMC libraries
Summary(pl.UTF-8):	Biblioteki statyczne libXvMC
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libXvMCW-static = %{version}
Obsoletes:	libXvMCW-static

%description static
XvMC (X-Video Motion Compensation) library.

This package contains the static libXvMC libraries.

%description static -l pl.UTF-8
Biblioteka XvMC (X-Video Motion Compensation, czyli kompensacji ruchu
dla X-Video).

Pakiet zawiera statyczne biblioteki libXvMC.

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

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/XvMCConfig

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXvMC.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXvMC.so.1
%attr(755,root,root) %{_libdir}/libXvMCW.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXvMCW.so.1
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/XvMCConfig

%files devel
%defattr(644,root,root,755)
%doc XvMC_API.txt
%attr(755,root,root) %{_libdir}/libXvMC.so
%attr(755,root,root) %{_libdir}/libXvMCW.so
%{_libdir}/libXvMC.la
%{_libdir}/libXvMCW.la
%{_includedir}/X11/extensions/XvMClib.h
%{_pkgconfigdir}/xvmc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXvMC.a
%{_libdir}/libXvMCW.a
