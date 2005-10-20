Summary:	XvMC library
Summary(pl):	Biblioteka XvMC
Name:		xorg-lib-libXvMC
Version:	0.99.1
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/lib/libXvMC-%{version}.tar.bz2
# Source0-md5:	530faaf14b9f9d8d0766e45b72f0d97d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXv-devel
BuildRequires:	xorg-util-util-macros
Provides:	libXvMCW = %{version}
Obsoletes:	libXvMCW
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XvMC library.

%description -l pl
Biblioteka XvMC.

%package devel
Summary:	Header files libXvMC development
Summary(pl):	Pliki nagłówkowe do biblioteki libXvMC
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXv-devel
Provides:	libXvMCW-devel = %{version}
Obsoletes:	libXvMCW-devel

%description devel
XvMC library.

This package contains the header files needed to develop programs that
use these libXvMC.

%description devel -l pl
Biblioteka XvMC.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXvMC.

%package static
Summary:	Static libXvMC libraries
Summary(pl):	Biblioteki statyczne libXvMC
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libXvMCW-static = %{version}
Obsoletes:	libXvMCW-static

%description static
XvMC library.

This package contains the static libXvMC libraries.

%description static -l pl
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libXvMC*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXvMC*.so
%{_libdir}/libXvMC*.la
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xvmc.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libXvMC*.a
