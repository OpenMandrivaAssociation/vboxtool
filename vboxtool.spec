%define name	vboxtool
%define version	0.4
%define release	%mkrel 3 

BuildArch:	noarch

Name:		%{name} 
Summary:	Easy control of virtual machines of VirtualBox on a Linux headless server
Version:	%{version} 
Release:	%{release}
Source0:	%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/%{name}/ 


Group:		Emulators 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:	GPLv3 


%description
Easy control of VM of VirtualBox on a Linux headless server.


%prep 
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_prefix}/bin/
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/vboxtool/
cp -f script/vboxtool $RPM_BUILD_ROOT/%{_prefix}/bin/
cp -f script/vboxtoolinit $RPM_BUILD_ROOT/%{_sysconfdir}/init.d/
cp -f conf/machines.conf $RPM_BUILD_ROOT/%{_sysconfdir}/vboxtool/
cp -f conf/vboxtool.conf $RPM_BUILD_ROOT/%{_sysconfdir}/vboxtool/


%clean
rm -rf $RPM_BUILD_ROOT


%post
%_post_service vboxtoolinit


%preun
%_preun_service vboxtoolinit


%files 
%defattr(-,root,root) 
%doc readme.txt COPYING.txt changelog.txt
%config(noreplace) %{_sysconfdir}/vboxtool/machines.conf
%config(noreplace) %{_sysconfdir}/vboxtool/vboxtool.conf 
%{_prefix}/bin/vboxtool
%{_sysconfdir}/init.d/vboxtoolinit


%changelog
* Fri Jan 08 2010 Jean-Gabriel HAYS <hays.jg@gmail.com> 0.4-3mdv
- vboxtool is now compatible with VirtualBox OSE.

* Sat Jan 02 2010 Jean-Gabriel HAYS <hays.jg@gmail.com> 0.4-2mdv
- Add the 'vboxtoolinit status' command which maps to 'vboxtool show'.

* Thu Dec 31 2009 Jean-Gabriel HAYS <hays.jg@gmail.com> 0.4-1mdv
- Vboxtool RPM creation.
