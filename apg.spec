
Summary:	Automated Password Generator (apg)
Name:		apg
Version:	2.2.3
Release:	%mkrel 6
License:	BSD
Group:		System/Configuration/Other
Source0:	%{name}-%{version}.tar.bz2
URL:		http://www.adel.nursat.kz/apg/
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Apg generates several random passwords. It uses several password
generation algorithms (currently two) and a built-in pseudo random
number generator.


%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	FLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install apg apgbfm $RPM_BUILD_ROOT%{_bindir}
install doc/man/{apgbfm,apg}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README CHANGES THANKS TODO doc/APG_TIPS
%attr(755,root,root) %{_bindir}/apg
%attr(755,root,root) %{_bindir}/apgbfm
%{_mandir}/man1/*




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.3-6mdv2011.0
+ Revision: 616593
- the mass rebuild of 2010.0 packages

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 2.2.3-5mdv2010.0
+ Revision: 423984
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 2.2.3-4mdv2009.0
+ Revision: 226161
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 2.2.3-3mdv2008.1
+ Revision: 135823
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Feb 01 2007 Nicolas Lécureuil <neoclust@mandriva.org> 2.2.3-3mdv2007.0
+ Revision: 115798
- Rebuild
- Import apg

* Thu Apr 22 2004 Marcel Pol <mpol@mandriva.org> 2.2.3-2mdk
- rebuild

* Mon Feb 16 2004 Marcel Pol <mpol@mandrake.org> 2.2.3-1mdk
- 2.2.3

