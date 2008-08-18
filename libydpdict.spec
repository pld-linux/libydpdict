Summary:	Interface with YDP dictionaries
Summary(pl.UTF-8):	Interfejs do słowników YDP
Name:		libydpdict
Version:	1.0.0
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://toxygen.net/ydpdict/%{name}-%{version}.tar.gz
# Source0-md5:	e6d5989d74c275e23fad0e2a5cc997fe
URL:		http://toxygen.net/ydpdict/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library makes it easy for a program to read the dictionaries
distributed by Young Digital Planet (English-Polish/Polish-English
and/or German-Polish/Polish-German).

This package only contains the library, it does not contain the
dictionary files. To use it, you need a copy of the dictionary from
YDP and a program which can use this library (e.g. ydpdict).

%description -l pl.UTF-8
Biblioteka ta pozwala na łatwy dostęp do słowników rozpowszechnianych
przez Young Digital Planet (angielsko-polski/polsko-angielski i/lub
niemiecko-polski/polsko-niemiecki).

Pakiet ten zawiera tylko bioblotekę, bez plików słownika. Aby
skorzystać z danych, potrzebne są kopie plików słowników z YDP oraz
program korzystający z tej biblioteki (n.p. ydpdict).

%package devel
Summary:	Header files for libydpdict library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libydpdict
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libydpdict library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libydpdict.

%package static
Summary:	Static libydpdict library
Summary(pl.UTF-8):	Statyczna biblioteka libydpdict
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libydpdict library.

%description static -l pl.UTF-8
Statyczna biblioteka libydpdict.

%prep
%setup -q

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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libydpdict.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libydpdict.so.2

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libydpdict.so
%{_libdir}/libydpdict.la
%{_includedir}/ydpdict
%{_pkgconfigdir}/libydpdict.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libydpdict.a
