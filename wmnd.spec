# TODO: move config file to /etc or /etc/X11
Summary:	Network monitoring dock app
Summary(pl):	Aplet monitourj±cy sieæ
Name:		wmnd
Version:	0.4.7
Release:	0.1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	ftp://ftp.yuv.info/pub/wmnd/releases/%{name}-%{version}.tar.gz
# Source0-md5:	3378ba18557dd4477b278e4144bf32c2
Source1:	%{name}.desktop
URL:		http://www.yuv.info/wmnd/
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
Requires:	XFree86-libs
Requires:	xpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WMND is a dockapp for monitoring network interfaces under WindowMaker
and other compatible window managers.

%description -l pl
WMND jest dokowalnym apletem dla WindowMakera i innych kompatybilnych
menad¿erów okien, monitoruj±cym interfejsy sieciowe.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo
echo "Check config file: %{_datadir}/wmndrc"
echo

%files
%defattr(644,root,root,755)
%doc examples/wmndrc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_applnkdir}/DockApplets/*
%config %{_datadir}/wmndrc
