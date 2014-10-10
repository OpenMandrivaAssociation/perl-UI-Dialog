%define upstream_name    UI-Dialog
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	OOPerl wrapper for the various dialog applications
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/UI/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

Requires:	cdialog

%description
UI::Dialog is a OOPerl wrapper for the various dialog applications. These
dialog backends are currently supported: Zenity, GDialog, XDialog, KDialog,
CDialog, and Whiptail. There is also an ASCII backend provided as a last
resort interface for the console based dialog variants. UI::Dialog is a
class that provides a strict interface to these various backend modules.
By using UI:Dialog (with it's imposed limitations on the widgets) you can
ensure that your Perl program will function with any available interfaces.

UI::Dialog supports priority ordering of the backend detection process. So
if you'd prefer that Xdialog should be used first if available, simply
designate the desired order when creating the new object. The default order
for detecting and utilization of the backends are as follows:
  (with DISPLAY env): Zenity, GDialog, XDialog, KDialog
  (without DISPLAY): CDialog, Whiptail, ASCII

UI::Dialog is the result of a complete re-write of the UDPM CPAN module. This
was done to break away from the bad choice of name (UserDialogPerlModule) and
to implement a cleaner, more detached, OOPerl interface.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc examples README CONTRIBUTORS Changes TODO COPYRIGHT
%{perl_vendorlib}/*
%{_mandir}/*/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 1.80.0-3mdv2011.0
+ Revision: 658896
- rebuild for updated spec-helper

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.80.0-2mdv2010.0
+ Revision: 430610
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.08-7mdv2009.0
+ Revision: 258708
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.08-6mdv2009.0
+ Revision: 246668
- rebuild
- fix no-buildroot-tag

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.08-4mdv2008.1
+ Revision: 152375
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.08-3mdv2008.1
+ Revision: 152368
- rebuild
- kill (multiple!) definitions of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.08-2mdv2008.0
+ Revision: 87064
- rebuild


* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/15/06 01:50:06 (56148)
- cleanup
- mkrel
- test in %%check

* Tue Aug 15 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/15/06 01:47:12 (56147)
Import perl-UI-Dialog

* Mon Dec 12 2005 Arnaud de Lorbeau <devel@mandriva.com> 1.08-1mdk
- New package

