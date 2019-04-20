#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Clone
Version  : 0.41
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/G/GA/GARU/Clone-0.41.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GA/GARU/Clone-0.41.tar.gz
Summary  : Recursive copy of nested objects.
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Clone-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
No detailed description available

%package dev
Summary: dev components for the perl-Clone package.
Group: Development
Requires: perl-Clone-lib = %{version}-%{release}
Provides: perl-Clone-devel = %{version}-%{release}
Requires: perl-Clone = %{version}-%{release}

%description dev
dev components for the perl-Clone package.


%package lib
Summary: lib components for the perl-Clone package.
Group: Libraries

%description lib
lib components for the perl-Clone package.


%prep
%setup -q -n Clone-0.41

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
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Clone.pm
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Clone/autosplit.ix

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Clone.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Clone/Clone.so
