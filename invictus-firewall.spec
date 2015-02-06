%define name invictus-firewall
%define version 0.1
%define release 14
%define service ct_sync

Summary: Invictus Firewall
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{service}.init
Source1: %{service}.sysconfig
Source2: ucarp-action.sh
Source3: ucarp-up.sh
Source4: ucarp-down.sh
License: GPL
Group: System/Configuration/Networking
Url: http://www.mandriva.com/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
Requires(post):  rpm-helper
Requires(preun): rpm-helper
Requires: ucarp


%description
Invictus Firewall allows to setup a redundant firewall using ucarp to
handle failover and ct_sync to replicate connection tracking state.

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT
install -m755 -D %{SOURCE0} %{buildroot}%{_initrddir}/%{service}
install -m644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/sysconfig/%{service}
install -d %{buildroot}%{_datadir}/%{name}/
install -m755 %{SOURCE2} %{SOURCE3} %{SOURCE4} %{buildroot}%{_datadir}/%{name}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
%_post_service %{service}

%preun
%_preun_service %{service}

%files
%defattr(-,root,root)
%{_initrddir}/%{service}
%config(noreplace) %{_sysconfdir}/sysconfig/%{service}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/ucarp-*.sh




%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-11mdv2011.0
+ Revision: 665514
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-10mdv2011.0
+ Revision: 605977
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-9mdv2010.1
+ Revision: 520130
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1-8mdv2010.0
+ Revision: 425355
- rebuild

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 0.1-7mdv2009.1
+ Revision: 351252
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.1-6mdv2009.0
+ Revision: 221632
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 0.1-5mdv2008.1
+ Revision: 150290
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jul 07 2007 Adam Williamson <awilliamson@mandriva.org> 0.1-4mdv2008.0
+ Revision: 49568
- rebuild for 2008


* Sun Aug 27 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-27 16:33:11 (58225)
- fix typo

* Sun Aug 27 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-27 16:08:50 (58220)
- invictus-firewall-0.1-3mdv2007.0

* Sun Aug 27 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-27 16:07:36 (58219)
- let initscript start normally if configuration is empty

* Wed Aug 23 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-23 11:57:33 (57682)
- fix ct_sync service status

* Wed Aug 23 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-23 11:50:12 (57679)
- check that ct_sync state file is writable in /proc

* Wed Aug 23 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-23 11:46:10 (57678)
- add ucarp up/down scripts

* Tue Aug 22 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-22 23:28:42 (57532)
- initial Mandriva release

* Tue Aug 22 2006 Olivier Blin <oblin@mandriva.com>
+ 2006-08-22 19:32:43 (57519)
- Created package structure for invictus-firewall.

