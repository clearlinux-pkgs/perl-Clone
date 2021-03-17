#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Clone
Version  : 0.45
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Clone-0.45.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Clone-0.45.tar.gz
Summary  : 'recursively copy Perl datatypes'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Clone-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::COW)

%description
Clone - recursively copy Perl datatypes
=======================================
[![Build Status](https://travis-ci.org/garu/Clone.png?branch=master)](https://travis-ci.org/garu/Clone)
[![Coverage Status](https://coveralls.io/repos/garu/Clone/badge.png?branch=master)](https://coveralls.io/r/garu/Clone?branch=master)
[![CPAN version](https://badge.fury.io/pl/Clone.svg)](https://metacpan.org/pod/Clone)

%package dev
Summary: dev components for the perl-Clone package.
Group: Development
Provides: perl-Clone-devel = %{version}-%{release}
Requires: perl-Clone = %{version}-%{release}

%description dev
dev components for the perl-Clone package.


%package perl
Summary: perl components for the perl-Clone package.
Group: Default
Requires: perl-Clone = %{version}-%{release}

%description perl
perl components for the perl-Clone package.


%prep
%setup -q -n Clone-0.45
cd %{_builddir}/Clone-0.45

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
/usr/share/man/man3/Clone.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/Clone.pm
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Clone/Clone.so
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/auto/Clone/autosplit.ix
