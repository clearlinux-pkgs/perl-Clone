#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Clone
Version  : 0.39
Release  : 2
URL      : https://cpan.metacpan.org/authors/id/G/GA/GARU/Clone-0.39.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GARU/Clone-0.39.tar.gz
Summary  : 'recursively copy Perl datatypes'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Clone-lib
Requires: perl-Clone-man

%description
Clone - recursively copy Perl datatypes
=======================================
[![Build Status](https://travis-ci.org/garu/Clone.png?branch=master)](https://travis-ci.org/garu/Clone)
[![Coverage Status](https://coveralls.io/repos/garu/Clone/badge.png?branch=master)](https://coveralls.io/r/garu/Clone?branch=master)
[![CPAN version](https://badge.fury.io/pl/Clone.svg)](https://metacpan.org/pod/Clone)

%package lib
Summary: lib components for the perl-Clone package.
Group: Libraries

%description lib
lib components for the perl-Clone package.


%package man
Summary: man components for the perl-Clone package.
Group: Default

%description man
man components for the perl-Clone package.


%prep
%setup -q -n Clone-0.39

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/Clone.pm
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Clone/autosplit.ix

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.26.1/x86_64-linux-thread-multi/auto/Clone/Clone.so

%files man
%defattr(-,root,root,-)
/usr/share/man/man3/Clone.3
