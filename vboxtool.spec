Name:			vboxtool
Summary:		Easy control of virtual machines of VirtualBox on a Linux headless server
Version:		0.5
Release:		1
Source0:		https://sourceforge.net/projects/vboxtool/files/vboxtool/%{version}/vboxtool-%{version}.zip
Source1:		machines.conf
Source2:		vboxtool.conf
#Patch0:			vboxtool.patch
#Patch1:			vboxtoolinit.patch
URL:			https://sourceforge.net/projects/%{name}/ 
BuildArch:		noarch


Group:			Emulators 
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:		GPLv3 
Requires(pre):		rpm-helper
Requires(preun):	rpm-helper


%description
Easy control of VM of VirtualBox on a Linux headless server.


%prep 
%setup -q -T -a0 -c
#patch0 -p0 -b .patch
#patch1	-p0 -b .patch

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


%changelog
* Sun Feb 14 2010 Stéphane Téletchéa <steletch@mandriva.org> 0.4-1mdv2010.1
+ Revision: 505670
- Initial Mandriva release

  + Jean Gabriel Hays <janot@mandriva.org>
    - patch modifications
    - patchs modifications
    - spec corrections
    - New spec file
    - Spec correction
    - Patchs correction
    - MDV patches added
    - Apply MDV patches
    - chkconfig line added in intscript
    - chkconfig added in the initscript
    - Added LSB compliance
    - build corrections
    - First upload
    - import vboxtool

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Remove the changelog from the spec file


* Sat Jan 08 2010 Jean-Gabriel HAYS <hays.jg@gmail.com> 0.4-3mdv
- Vboxtool is now compatible with VirtualBox OSE edition.

* Sat Jan 02 2010 Jean-Gabriel HAYS <hays.jg@gmail.com> 0.4-2mdv
- Add the 'vboxtoolinit status' command which maps to 'vboxtool show'.

* Thu Dec 31 2009 Jean-Gabriel HAYS <hays.jg@gmail.com> 0.4-1mdv
- Vboxtool RPM creation.
