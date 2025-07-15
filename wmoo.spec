Summary:	OpenOffice start acceleration applet for WindowMaker
Summary(pl.UTF-8):	Aplet przyspieszający uruchamianie OpenOffice dla WindowMakera
Name:		wmoo
Version:	0.1
Release:	1
License:	GPL
Vendor:		Piera "Vampiera" Poggio <piera@metodo.net>
Group:		X11/Window Managers/Tools
Source0:	http://www.vampiera.net/download/%{name}-%{version}.tgz
# Source0-md5:	1a3a53ae3e76731746dabd4a5ab9f481
Patch0:		%{name}.patch
URL:		http://www.vampiera.net/wmoo.html
BuildRequires:	XFree86-devel
BuildRequires:	libgtop-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmoo is WindowMaker dockable applet that can make OpenOffice start
faster.

%description -l pl.UTF-8
wmoo jest dokowalnym apletem dla WindowMakera przyspieszającym
ładowanie OpenOffice.

%prep
%setup -q
%patch -P0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_bindir}}

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
