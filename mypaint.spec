%define use_ccache 1
%define ccachedir~/.ccache-OOo%{mdvsuffix}
%{?_with_ccache: %global use_ccache 1}
%{?_without_ccache: %global use_ccache 0}
%define date	    %(echo `LC_ALL="C" date +"%a %b %d %Y"`)

%define name mypaint
%define version 0.7.1
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A simple paint program
Group:		Graphics
License:	GPLv2+
URL:		http://mypaint.intilinux.com/
Source0:	http://download.gna.org/mypaint/%{name}/%{name}-%{version}.tar.bz2
Source1:	mypaint.desktop
BuildRoot:	%{_tmppath}/%{name}-buildroot

BuildRequires:	%mklibname gtk+2.0_0-devel
BuildRequires:	python-devel pygtk2.0-devel python-numpy-devel scons swig desktop-file-utils

Requires:	gtk+2.0 pygtk2.0 python python-numpy python-gobject python-cairo

%description
Mypaint is a fast and easy/simple painter app focused on the painter, 
so you can only focus on the art and not the program itself. 
Currently MyPaint does not have a layer system, also mypaint is using 
pygtk with C extensions.

%prep
%setup -q

%build
scons

%install
rm -rf $RPM_BUILD_ROOT
scons prefix=$RPM_BUILD_ROOT/usr install

install -m 0644 %SOURCE1 $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_desktop_database}

%postun
%{clean_desktop_database}

%files
%defattr(-,root,root,-)
%doc README LICENSE COPYING changelog
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
/usr/lib/%{name}/_mypaintlib.so

