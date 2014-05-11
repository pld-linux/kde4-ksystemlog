# TODO
#   %{_pkgconfigdir}/system-tools-backends.pc
%define		_state		stable
%define		orgname		ksystemlog
%define		qtver		4.8.1

%include	/usr/lib/rpm/macros.perl

Summary:	System log viewer for KDE
Summary(pl.UTF-8):	Przeglądarka logów systemowych dla KDE
Name:		kde4-%{orgname}
Version:	4.13.0
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	b49c95c6a555863bc766107ea9856fc6
URL:		http://www.kde.org/
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kdepimlibs-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
Requires:	kde4-kdebase >= %{version}
Obsoletes:	kde4-kdeadmin-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KSystemLog is a system log viewer for KDE.

%description -l pl.UTF-8
KSystemLog to przeglądarka logów systemowych dla KDE.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksystemlog
%dir %{_datadir}/apps/ksystemlog
%{_desktopdir}/kde4/ksystemlog.desktop
%{_datadir}/apps/ksystemlog/ksystemlogui.rc
