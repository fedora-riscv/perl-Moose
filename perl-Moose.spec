Name:           perl-Moose
Version:        0.94
Release:        3%{?dist}
Summary:        Complete modern object system for Perl 5
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Moose/
Source0:        http://search.cpan.org/CPAN/authors/id/D/DR/DROLSKY/Moose-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::MOP)         >= 0.98
BuildRequires:  perl(Data::OptList)
BuildRequires:  perl(Filter::Simple)
BuildRequires:  perl(List::MoreUtils)    >= 0.12
BuildRequires:  perl(Scalar::Util)       >= 1.19
BuildRequires:  perl(Sub::Exporter)      >= 0.980
BuildRequires:  perl(Sub::Install)       >= 0.92
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Task::Weaken)
BuildRequires:  perl(Test::More)         >= 0.88
BuildRequires:  perl(Test::Exception)    >= 0.27
BuildRequires:  perl(Test::LongString)
BuildRequires:  perl(UNIVERSAL::require) >= 0.10

# optional test #1 (in no particular order)
# ** moved to author tests
#BuildRequires:  perl(Test::Pod), perl(Test::Pod::Coverage)
# optional test #2
BuildRequires:  perl(DBM::Deep) >= 0.983
BuildRequires:  perl(DateTime::Format::MySQL)
# optional test #3
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(Params::Coerce)
BuildRequires:  perl(URI)
BuildRequires:  perl(Try::Tiny) >= 0.02
# optional test #4
# commented out as Locale::US's license is ambiguous at the moment, precluding
# packaging it.
#BuildRequires:  perl(Regexp::Common), perl(Locale::US)
# optional test #5
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::String)
# optional test #6
BuildRequires:  perl(Test::Deep)
# optional test #7
BuildRequires:  perl(Declare::Constraints::Simple)
# optional test #8 (as of 0.20)
BuildRequires:  perl(Module::Refresh)
# optional tests #9 (as of 0.57)
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Output)
# optional test #10
BuildRequires:  perl(DateTime::Calendar::Mayan)

Requires:  perl(Carp)
Requires:  perl(Class::MOP) >= 0.98
Requires:  perl(Data::OptList)
Requires:  perl(List::MoreUtils) >= 0.12
Requires:  perl(Scalar::Util) >= 1.19
Requires:  perl(Sub::Exporter) >= 0.980
Requires:  perl(Sub::Name)
Requires:  perl(Task::Weaken)
Requires:  perl(Try::Tiny) >= 0.02

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
Moose is an extension of the Perl 5 object system.

Moose is built on top of Class::MOP, which is a metaclass system for
Perl 5. This means that Moose not only makes building normal Perl 5
objects better, but it also provides the power of metaclass programming.
such things.  Moose is different from other Perl 5 object systems because
it is not a new system, but instead an extension of the existing one.

While Moose is very much inspired by Perl 6, it is not itself Perl
6.  Instead, it is an OO system for Perl 5. I built Moose because I was
tired or writing the same old boring Perl 5 OO code, and drooling over
Perl 6 OO. So instead of switching to Ruby, I wrote Moose :)

%package -n perl-Test-Moose
License:    GPL+ or Artistic
Group:      Development/Libraries
Summary:    Test functions for Moose specific features
Requires:   %{name} = %{version}-%{release}

%description -n perl-Test-Moose
This module provides some useful test functions for Moose based classes.
It is an experimental first release, so comments and suggestions are
very welcome.

%prep
%setup -q -n Moose-%{version}

# tidy things up...
find t/ -type f -exec perl -pi -e 's|^#!/usr/local/bin|#!/usr/bin|' {} +
find . -name '*.orig' -exec rm -v {} +
find . -type f -exec chmod -c -x {} +

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} +
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc Changes README doap.rdf
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%exclude %{perl_vendorarch}/Test
%{_mandir}/man3/*
%exclude %{_mandir}/man3/Test::Moose*

%files -n perl-Test-Moose
%defattr(-,root,root,-)
%{perl_vendorarch}/Test
%{_mandir}/man3/Test::Moose*

%changelog
* Fri Feb 05 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.94-3
- PERL_INSTALL_ROOT => DESTDIR
- add perl_default_subpackage_tests
- properly exclude vendorarch/auto/ directory
- add br on DateTime::Calendar::Mayan

* Wed Jan 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.94-2
- we're not noarch anymore :)

* Wed Jan 20 2010 Chris Weyl <cweyl@alumni.drew.edu> 0.94-1
- auto-update to 0.94 (by cpan-spec-update 0.01)
- altered br on perl(Class::MOP) (0.94 => 0.98)
- altered req on perl(Class::MOP) (0.94 => 0.98)

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 0.92-2
- rebuild against perl 5.10.1

* Sun Sep 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.92-1
- auto-update to 0.92 (by cpan-spec-update 0.01)
- altered br on perl(Class::MOP) (0.93 => 0.94)
- altered req on perl(Class::MOP) (0.93 => 0.94)

* Fri Sep 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.90-1
- switch filtering systems...
- auto-update to 0.90 (by cpan-spec-update 0.01)
- altered br on perl(Class::MOP) (0.92 => 0.93)
- altered br on perl(Test::More) (0.77 => 0.88)
- added a new br on perl(Try::Tiny) (version 0.02)
- altered req on perl(Class::MOP) (0.92 => 0.93)
- added a new req on perl(Try::Tiny) (version 0.02)

* Wed Aug 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.89-1
- auto-update to 0.89 (by cpan-spec-update 0.01)
- altered br on perl(Class::MOP) (0.89 => 0.92)
- altered req on perl(Class::MOP) (0.89 => 0.92)

* Mon Jul 27 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.88-1
- auto-update to 0.88 (by cpan-spec-update 0.01)
- altered br on perl(Class::MOP) (0.85 => 0.89)
- altered br on perl(Sub::Exporter) (0.972 => 0.980)
- added a new req on perl(Carp) (version 0)
- added a new req on perl(Class::MOP) (version 0.89)
- added a new req on perl(Data::OptList) (version 0)
- added a new req on perl(List::MoreUtils) (version 0.12)
- added a new req on perl(Scalar::Util) (version 1.19)
- added a new req on perl(Sub::Exporter) (version 0.980)
- added a new req on perl(Sub::Name) (version 0)
- added a new req on perl(Task::Weaken) (version 0)

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.81-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.81-2
- split off Test::Moose

* Tue Jun 09 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.81-1
- auto-update to 0.81 (by cpan-spec-update 0.01)
- altered br on perl(Class::MOP) (0.83 => 0.85)

* Sun Jun 07 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.80-1
- auto-update to 0.80 (by cpan-spec-update 0.01)

* Tue May 19 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.79-1
- auto-update to 0.79 (by cpan-spec-update 0.01)

* Wed May 13 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.78-1
- auto-update to 0.78 (by cpan-spec-update 0.01)
- altered br on perl(Test::Exception) (0.21 => 0.27)
- altered br on perl(ExtUtils::MakeMaker) (0 => 6.42)
- added a new br on perl(Sub::Name) (version 0)
- altered br on perl(Class::MOP) (0.81 => 0.83)
- altered br on perl(Sub::Exporter) (0.954 => 0.972)
- added a new br on perl(Carp) (version 0)

* Mon May 04 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.74-2
- switch filtering to a cleaner system

* Sat Apr 18 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.74-1
- update to 0.74

* Wed Apr 01 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.73-1
- update to 0.73

* Sun Mar 08 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.72-1
- update to 0.72

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.71-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Feb 22 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.71-1
- update to 0.71

* Sun Jan 04 2009 Chris Weyl <cweyl@alumni.drew.edu> 0.64-1
- update to 0.64

* Sun Dec 28 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.63-1
- update to 0.63
- bump br versions on Moose, List::MoreUtils

* Sat Dec 06 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.62-1
- update to 0.62
- new Task::Weaken and Class::MOP requirements

* Sat Nov 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.61-4
- aaaand drop them again, as it was really perl-Class-MOP's issue.

* Sat Nov 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.61-3
- same with Devel::GlobalDestruction (same RT as below)

* Sat Nov 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.61-2
- add Sub::Name as a build dep (RT#40772)

* Sat Nov 08 2008 Chris Weyl <cweyl@alumni.drew.edu> 0.61-1
- update to 0.61
- update BR's

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
