# TODO:
# - fix ac/am scripts to regeneration works
# - version with db support? ;)
Summary:	A tool for storing key/value pairs in a hash database
Summary(pl.UTF-8):   Narzędzie do zapisywania par klucz/wartość w tablicach haszowanych
Name:		dbtool
Version:	1.6
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	ftp://ftp.daemon.de/scip/Apps/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	a8e3f0982b42b0dbb3b9c1c31c975060
BuildRequires:	gdbm-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pcre-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dbtool can be used to store and retrieve data in a key/value format in
a hash database. Perl compatible regular expressions are supported
both for storing and retrieving of data. It's main advantages are the
ability to maintain huge amounts of data and speed. dbtool supports
encrypted databases.

%description -l pl.UTF-8
dbtool może być używany do zapisywania i odczytywania danych w
formacie klucz/wartość w tablicy haszowanej. Kompatybilne z perlem
wyrażenia regularne są obsługiwane zarówno dla odczytu jak i zapisu
danych. Głównymi celami programu są zdolność do zarządzania ogromnymi
ilościami danych oraz prędkość. dbtool obsługuje także szyfrowane
bazy.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/dbtool
%{_mandir}/man?/dbtool.*
