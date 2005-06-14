# TODO:
# - fix ac/am scripts to regeneration works
# - version with db support? ;)
Summary:	A tool for storing key/value pairs in a hash database
Summary(pl):	Narzêdzie do zapisywania par klucz/warto¶æ w tablicach haszowanych
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

%description -l pl
dbtool mo¿e byæ u¿ywany do zapisywania i odczytywania danych w
formacie klucz/warto¶æ w tablicy haszowanej. Kompatybilne z perlem
wyra¿enia regularne s± obs³ugiwane zarówno dla odczytu jak i zapisu
danych. G³ównymi celami programu s± zdolno¶æ do zarz±dzania ogromnymi
ilo¶ciami danych oraz prêdko¶æ. dbtool obs³uguje tak¿e szyfrowane
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
