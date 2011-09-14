Summary:	Egg Windows Manager
Summary(pl.UTF-8):	Menedżer Okien Egg
Name:		eggwm
Version:	0.2
Release:	1
License:	GPL
Group:		X11/Window Managers
URL:		http://code.google.com/p/eggwm/
Source0:	http://eggwm.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	3442e56d9a78a44c349f9e83f15c8eac
Source1:	%{name}.desktop
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
EggWM is a window manager based on Qt4 and Xlib.

%description -l pld.UTF-8
EggWM jest menedżerem okien bazowanym na Qt4 oraz Xlib.

%prep
%setup -q

%build
lrelease-qt4 EggWM.pro
PREFIX=%{_prefix} \
DESTDIR=$RPM_BUILD_ROOT \
qmake-qt4 EggWM.pro
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.TXT
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/xsessions/%{name}.desktop
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/%{name}.conf
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/oxygegg
%{_datadir}/%{name}/themes/oxygegg/*
%dir %{_datadir}/%{name}/themes/testtheme
%{_datadir}/%{name}/themes/testtheme/*
