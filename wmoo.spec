Summary:	Window Maker
Summary(pl):	WindowMakera/
Name:		wmoo
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.vampiera.net/download/%{name}-%{version}.tgz
Patch0:     %{name}.patch
URL:		http://www.vampiera.net/wmoo.html
Vendor:     Piera "Vampiera" Poggio piera@metodo.net
BuildRequires:	XFree86-devel,libgtop-devel 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description

%description -l pl
wmsysmon jest dokowalnym apletem dla WindowMakera przyspieszaj±cym
³adowanie OpenOffice.

%prep
%setup -q
%patch0 -p1

%build

%{__make}


install -d $RPM_BUILD_ROOT/usr/X11R6/{share/icons,bin}
install icons/* $RPM_BUILD_ROOT/usr/X11R6/share/icons
install wmoo $RPM_BUILD_ROOT/usr/X11R6/bin

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf CHANGELOG README sample.wmoorc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGELOG,README,sample.wmoorc}.gz
%attr(755,root,root) %{_bindir}/wmoo
%attr(644,root,root) /usr/X11R6/share/icons

#%{_applnkdir}/DockApplets/wmoo.desktop
