Summary:	XvMC library
Summary(pl.UTF-8):   Biblioteka XvMC
Name:		xorg-lib-libXvMC
Version:	1.0.4
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXvMC-%{version}.tar.bz2
# Source0-md5:	b54600573daf9d1a29b952e8d35b389e
Source1:	XvMCConfig
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-util-util-macros >= 1.1.0
Provides:	libXvMCW = %{version}
Obsoletes:	libXvMCW
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XvMC library.

%description -l pl.UTF-8
Biblioteka XvMC.

%package devel
Summary:	Header files for libXvMC library
Summary(pl.UTF-8):   Pliki nagłówkowe biblioteki libXvMC
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXv-devel
Provides:	libXvMCW-devel = %{version}
Obsoletes:	libXvMCW-devel

%description devel
XvMC library.

This package contains the header files needed to develop programs that
use libXvMC.

%description devel -l pl.UTF-8
Biblioteka XvMC.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXvMC.

%package static
Summary:	Static libXvMC libraries
Summary(pl.UTF-8):   Biblioteki statyczne libXvMC
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libXvMCW-static = %{version}
Obsoletes:	libXvMCW-static

%description static
XvMC library.

This package contains the static libXvMC libraries.

%description static -l pl.UTF-8
Biblioteka XvMC.

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXvMC.so.*.*.*
%attr(755,root,root) %{_libdir}/libXvMCW.so.*.*.*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/XvMCConfig

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMC.so
%attr(755,root,root) %{_libdir}/libXvMCW.so
%{_libdir}/libXvMC.la
%{_libdir}/libXvMCW.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xvmc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXvMC.a
%{_libdir}/libXvMCW.a
