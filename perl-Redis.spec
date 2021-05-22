#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Redis
Version  : 1.998
Release  : 10
URL      : https://cpan.metacpan.org/authors/id/D/DA/DAMS/Redis-1.998.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DA/DAMS/Redis-1.998.tar.gz
Summary  : 'Perl binding for Redis database'
Group    : Development/Tools
License  : Artistic-2.0
Requires: perl-Redis-license = %{version}-%{release}
Requires: perl-Redis-perl = %{version}-%{release}
Requires: perl(IO::Socket::Timeout)
Requires: perl(Try::Tiny)
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(IO::Socket::Timeout)
BuildRequires : perl(IO::String)
BuildRequires : perl(Module::Build::Tiny)
BuildRequires : perl(Test::Deep)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::SharedFork)
BuildRequires : perl(Test::TCP)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Redis,
version 1.998:
Perl binding for Redis database

%package dev
Summary: dev components for the perl-Redis package.
Group: Development
Provides: perl-Redis-devel = %{version}-%{release}
Requires: perl-Redis = %{version}-%{release}

%description dev
dev components for the perl-Redis package.


%package license
Summary: license components for the perl-Redis package.
Group: Default

%description license
license components for the perl-Redis package.


%package perl
Summary: perl components for the perl-Redis package.
Group: Default
Requires: perl-Redis = %{version}-%{release}

%description perl
perl components for the perl-Redis package.


%prep
%setup -q -n Redis-1.998
cd %{_builddir}/Redis-1.998

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Redis
cp %{_builddir}/Redis-1.998/LICENSE %{buildroot}/usr/share/package-licenses/perl-Redis/b8c4d541f43eb6518a9f41d1a6b1e73edab724dd
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Redis.3
/usr/share/man/man3/Redis::Hash.3
/usr/share/man/man3/Redis::List.3
/usr/share/man/man3/Redis::Sentinel.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Redis/b8c4d541f43eb6518a9f41d1a6b1e73edab724dd

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Redis.pm
/usr/lib/perl5/vendor_perl/5.34.0/Redis/Hash.pm
/usr/lib/perl5/vendor_perl/5.34.0/Redis/List.pm
/usr/lib/perl5/vendor_perl/5.34.0/Redis/Sentinel.pm
