%define name		vboxtool
%define version		0.4
%define release		%mkrel 1 

BuildArch:		noarch

Name:			%{name} 
Summary:		Easy control of virtual machines of VirtualBox on a Linux headless server
Version:		%{version} 
Release:		%{release}
Source0:		%{name}-%{version}.zip
Source1:		machines.conf
Source2:		vboxtool.conf
Patch0:			vboxtool.patch
Patch1:			vboxtoolinit.patch
URL:			http://sourceforge.net/projects/%{name}/ 


Group:			Emulators 
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:		GPLv3 
Requires(pre):		rpm-helper
Requires(preun):	rpm-helper


%description
Easy control of VM of VirtualBox on a Linux headless server.


%prep 
%setup -q -T -a0 -c
%patch0 -p0 -b .patch
%patch1	-p0 -b .patch

chmod 644 readme.txt 
chmod 644 COPYING.txt 
chmod 644 changelog.txt


%build
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_prefix}/bin/
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/
cp -f script/vboxtool $RPM_BUILD_ROOT/%{_prefix}/bin/
cp -f script/vboxtoolinit $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/
cp -f %{SOURCE1} $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/
cp -f %{SOURCE2} $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/
chmod 644 $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}/*


%clean
rm -rf $RPM_BUILD_ROOT


%post
%_post_service vboxtoolinit



%preun
%_preun_service vboxtoolinit


%files
%defattr(-,root,root)
%doc readme.txt COPYING.txt changelog.txt
%config(noreplace) %{_sysconfdir}/%{name}/machines.conf
%config(noreplace) %{_sysconfdir}/%{name}/vboxtool.conf 
%{_prefix}/bin/%{name}
%{_sysconfdir}/init.d/vboxtoolinit
