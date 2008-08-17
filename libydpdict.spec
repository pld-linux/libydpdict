Summary:	Interface with YDP dictionaries
Summary(pl.UTF-8):	Interfejs do słowników YDP
Name:		libydpdict
Version:	1.0.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://toxygen.net/ydpdict/%{name}-%{version}.tar.gz
# Source0-md5:	e6d5989d74c275e23fad0e2a5cc997fe
URL:		http://toxygen.net/ydpdict/
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
przez Young Digital Planet (angielski-polski/polsko-angielski i/lub
niemiecko-polski/polsko-niemiecki).

Pakiet ten zawiera tylko biobloteką, bez plików słownika. Aby
skorzystać z danych, potrzebujesz kopie plików słowników z YDP oraz
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
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/ydpdict
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
