Name:           perl-Moose
Version:        0.57
Release:        2%{?dist}
Summary:        Complete modern object system for Perl 5
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Moose/
# source tends to flip between these three authors
Source0:        http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Moose-%{version}.tar.gz
#Source0:        http://search.cpan.org/CPAN/authors/id/S/SA/SARTAK/Moose-%{version}.tar.gz
#Source0:        http://search.cpan.org/CPAN/authors/id/S/ST/STEVAN/Moose-%{version}.tar.gz
#Source0:        http://search.cpan.org/CPAN/authors/id/G/GR/GRODITI/Moose-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

# core
BuildRequires:  perl(Test::More)         >= 0.62
BuildRequires:  perl(ExtUtils::MakeMaker)
# cpan
BuildRequires:  perl(Class::MOP)         >= 0.65
BuildRequires:  perl(Module::Build) 
BuildRequires:  perl(Filter::Simple) 
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Sub::Exporter)      >= 0.954
BuildRequires:  perl(Sub::Install)       >= 0.92
BuildRequires:  perl(Test::Exception)    >= 0.21
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(UNIVERSAL::require) >= 0.10
# optional test #1 (in no particular order)
BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage)
# optional test #2
BuildRequires:  perl(DBM::Deep) >= 0.983, perl(DateTime::Format::MySQL)
# optional test #3
BuildRequires:  perl(HTTP::Headers), perl(Params::Coerce), perl(URI)
# optional test #4
# commented out as Locale::US's license is ambiguous at the moment, precluding
# packaging it.
#BuildRequires:  perl(Regexp::Common), perl(Locale::US)
# optional test #5
BuildRequires:  perl(IO::File), perl(IO::String)
# optional test #6
BuildRequires:  perl(Test::Deep)
# optional test #7 
BuildRequires:  perl(Declare::Constraints::Simple)
# optional test #8 (as of 0.20)
BuildRequires:  perl(Module::Refresh)
# optional tests #9 (as of 0.57)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Output)


%description
Moose is an extension of the Perl 5 object system.

Yes, I know there has been an explosion recently of new ways to build
objects in Perl 5, most of them based on inside-out objects and other
such things. Moose is different because it is not a new object system
for Perl 5, but instead an extension of the existing object system.

Moose is built on top of Class::MOP, which is a metaclass system for
Perl 5. This means that Moose not only makes building normal Perl 5
objects better, but it also provides the power of metaclass programming.

While Moose is very much inspired by Perl 6, it is not itself Perl
6.  Instead, it is an OO system for Perl 5. I built Moose because I was
tired or writing the same old boring Perl 5 OO code, and drooling over
Perl 6 OO. So instead of switching to Ruby, I wrote Moose :)

%prep
%setup -q -n Moose-%{version}

find t/ -type f -exec perl -pi -e 's|^#!/usr/local/bin|#!/usr/bin|' {} +

# remove the originals of patched files...
find . -name '*.orig' -exec rm -v {} +

# Filter unwanted Provides:
cat << \EOF > %{name}-prov
#!/bin/sh
%{__perl_provides} $* |\
  sed -e '/perl(MyMoose.*)/d; /perl(Bar)/d; /perl(Foo)/d'    
EOF

%define __perl_provides %{_builddir}/Moose-%{version}/%{name}-prov
chmod +x %{__perl_provides}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README doap.rdf t/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Sat Sep 06 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.57-2
- add additional test BR's

* Sat Sep 06 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.57-1
- update to 0.57

* Fri Jul 18 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.54-1
- update to 0.54

* Sat Jun 28 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.51-1
- update to 0.51

* Tue Jun 17 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.50-1
- update to 0.50
- drop obviated test patch

* Wed May 28 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.44-2
- bump

* Wed May 21 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.44-1
- update to 0.44

* Wed Mar 05 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.33-3
- rebuild for new perl

* Mon Jan 07 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.33-2
- remove *.orig files from t/ (BZ#427754)

* Sat Dec 15 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.33-1
- update to 0.33

* Wed Dec 05 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.32-1
- update to 0.32

* Sun Nov 25 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.30-1
- update to 0.30

* Sat Nov 17 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.29-1
- update to 0.29
- refactor to Module::Install

* Sun Oct 14 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.26-1
- udpate to 0.26

* Sat Aug 11 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.24-1
- update to 0.24
- license tag: GPL -> GPL+
- patch t/202_...t to write to a tmpdir rather than .

* Thu May 31 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.22-1
- update to 0.22

* Fri May 04 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.21-1
- update to 0.21

* Tue May 01 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.20-2
- add t/ to %%doc
- add br for optional test #7

* Sat Apr 07 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.20-1
- update to 0.20
- add additional BR's for new optional tests

* Fri Mar 23 2007 Chris Weyl <cweyl@alumni.drew.edu> 0.18-1
- Sub::Name only needed as a br for Moose < 0.18
- update to 0.18

* Thu Nov 16 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.17-2
- add IO::File and IO::String to br's for testing

* Thu Nov 16 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.17-1
- update to 0.17

* Mon Nov 06 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.15-1
- update to 0.15

* Tue Oct 10 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.14-1
- update to 0.14
- drop some cruft from the specfile
- make %%description a touch more verbose :)

* Tue Oct 03 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.13-1
- update to 0.13

* Fri Sep 08 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.12-2
- bump

* Sat Sep 02 2006 Chris Weyl <cweyl@alumni.drew.edu> 0.12-1
- Specfile autogenerated by cpanspec 1.69.1.
