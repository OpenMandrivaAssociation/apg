
Summary:	Automated Password Generator (apg)
Name:		apg
Version:	2.2.3
Release:	%mkrel 5
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


