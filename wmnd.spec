Summary:	Network monitoring dock app
Summary(pl.UTF-8):	Aplet monitorujący sieć
Name:		wmnd
Version:	0.4.11
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.yuv.info/wmnd/releases/%{name}-%{version}.tar.gz
# Source0-md5:	f7a57fa5b610373326007b43e341a85c
Source1:	%{name}.desktop
Patch0:		%{name}-etc.patch
URL:		http://www.yuv.info/wmnd/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMND is a dockapp for monitoring network interfaces under WindowMaker
and other compatible window managers.

%description -l pl.UTF-8
WMND jest dokowalnym apletem dla WindowMakera i innych kompatybilnych
zarządców okien, monitorującym interfejsy sieciowe.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/X11,%{_desktopdir}/docklets}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets
mv -f $RPM_BUILD_ROOT%{_datadir}/wmndrc $RPM_BUILD_ROOT%{_sysconfdir}/X11

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo
echo "Check config file: %{_sysconfdir}/X11/wmndrc"
echo

%files
%defattr(644,root,root,755)
%doc examples/wmndrc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/docklets/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/X11/wmndrc
