Summary:	XvMC library
Summary(pl.UTF-8):	Biblioteka XvMC
Name:		xorg-lib-libXvMC
Version:	1.0.14
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/lib/libXvMC-%{version}.tar.xz
# Source0-md5:	a90a5f01102dc445c7decbbd9ef77608
Source1:	XvMCConfig
Source2:	xvmcinfo.c
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool >= 2:2
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 1.6
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libX11 >= 1.6
Provides:	libXvMCW = %{version}
Obsoletes:	libXvMCW < 1
# withdrawn (and never useful) Mesa drivers
Obsoletes:	Mesa-libXvMC-r300 < 10
Obsoletes:	Mesa-libXvMC-softpipe < 10
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
Requires:	xorg-lib-libX11-devel >= 1.6
Requires:	xorg-lib-libXext-devel
# for <X11/extensions/Xvlib.h> in <X11/extensions/XvMClib.h>
Requires:	xorg-lib-libXv-devel
# after vldXvMC.h removal
Requires:	xorg-proto-videoproto-devel >= 2.3.3-2019.1.2
Requires:	xorg-proto-xproto-devel
Provides:	libXvMCW-devel = %{version}
Obsoletes:	libXvMCW-devel < 1

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
Obsoletes:	libXvMCW-static < 1

%description static
XvMC (X-Video Motion Compensation) library.

This package contains the static libXvMC libraries.

%description static -l pl.UTF-8
Biblioteka XvMC (X-Video Motion Compensation, czyli kompensacji ruchu
dla X-Video).

Pakiet zawiera statyczne biblioteki libXvMC.

%prep
%setup -q -n libXvMC-%{version}
cp -p %{SOURCE2} .

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%{__cc} %{rpmcflags} -I./include %{rpmldflags} -L./src/.libs xvmcinfo.c -lX11 -lXv -lXvMC -o xvmcinfo

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

install -Dp %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/XvMCConfig
install -Dp xvmcinfo $RPM_BUILD_ROOT%{_bindir}/xvmcinfo

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXvMC*.la
# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/libXvMC/XvMC_API.txt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xvmcinfo
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
%{_includedir}/X11/extensions/XvMClib.h
%{_includedir}/X11/extensions/vldXvMC.h
%{_pkgconfigdir}/xvmc.pc
%{_pkgconfigdir}/xvmc-wrapper.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXvMC.a
%{_libdir}/libXvMCW.a
