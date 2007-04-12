%define realname        UI-Dialog
Name:           perl-%realname
Version:        1.08
Release:        %mkrel 1
License:        GPL

Group:          Development/Perl
Summary:        OOPerl wrapper for the various dialog applications
Source0:        %{realname}-%{version}.tar.bz2
Url:            http://www.cpan.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:       perl cdialog
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-root

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
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc examples README CONTRIBUTORS Changes TODO COPYRIGHT
%{perl_vendorlib}/*
%{_mandir}/*/*

