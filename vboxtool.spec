%define name	vboxtool
%define version	0.4
%define release	%mkrel 1 

BuildArch:	noarch

Name:		%{name} 
Summary:	Easy control of virtual machines of VirtualBox on a Linux headless server
Version:	%{version} 
Release:	%{release}
Source0:	%{name}-%{version}.zip
Source1:	machines.conf
Source2:	vboxtool.conf
Patch0:		vboxtool.patch
Patch1:		vboxtoolinit.patch
URL:		http://sourceforge.net/projects/%{name}/ 


Group:		Emulators 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:	GPLv3 


%description
Easy control of VM of VirtualBox on a Linux headless server.


%prep 
%setup -q -T -a0 -c
%patch0 -p1
%patch1	-p1


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

%clean
rm -rf $RPM_BUILD_ROOT


%post
%_post_service vboxtoolinit


%preun
%_preun_service vboxtoolinit


%files
%defattr(-,root,root) 
%attr(644,root,root)%doc readme.txt COPYING.txt changelog.txt
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/vboxtool/machines.conf
%attr(644,root,root) %config(noreplace) %{_sysconfdir}/vboxtool/vboxtool.conf 
%attr(755,root,root)%{_prefix}/bin/vboxtool
%attr(755,root,root)%{_sysconfdir}/init.d/vboxtoolinit
