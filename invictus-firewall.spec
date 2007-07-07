%define name invictus-firewall
%define version 0.1
%define release %mkrel 4
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


