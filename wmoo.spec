# TODO: CC and optflags
Summary:	OpenOffice start acceleration applet for WindowMaker
Summary(pl):	Aplet przyspieszający uruchamianie OpenOffice dla WindowMakera
Name:		wmoo
Version:	0.1
Release:	1
License:	GPL
Vendor:		Piera "Vampiera" Poggio piera@metodo.net
Group:		X11/Window Managers/Tools
Source0:	http://www.vampiera.net/download/%{name}-%{version}.tgz
Patch0:		%{name}.patch
URL:		http://www.vampiera.net/wmoo.html
BuildRequires:	XFree86-devel
BuildRequires:	libgtop-devel 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
wmoo is WindowMaker dockable applet that can make OpenOffice start
faster.

%description -l pl
wmsysmon jest dokowalnym apletem dla WindowMakera przyspieszającym
ładowanie OpenOffice.

%prep
%setup -q
%patch0 -p1

%build
%{__make}
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_bindir}

install icons/* $RPM_BUILD_ROOT%{_pixmapsdir}
install wmoo $RPM_BUILD_ROOT%{_bindir}

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README sample.wmoorc
%attr(755,root,root) %{_bindir}/wmoo
%{_pixmapsdir}/*
