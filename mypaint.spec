%define use_ccache 1
%define ccachedir~/.ccache-OOo%{mdvsuffix}
%{?_with_ccache: %global use_ccache 1}
%{?_without_ccache: %global use_ccache 0}
%define date	    %(echo `LC_ALL="C" date +"%a %b %d %Y"`)

%define name mypaint
%define version 0.8.0
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
# the Options class is deprecated; use the Variables class instead
sed -i 's|PathOption|PathVariable|g' SConstruct
sed -i 's|Options|Variables|g' SConstruct
# for 64 bit
sed -i 's|lib/mypaint|%{_lib}/mypaint|g' SConstruct mypaint.py
# fix menu icon
sed -i 's|mypaint_48|mypaint|g' desktop/%{name}.desktop

%build
scons

%install
rm -rf %{buildroot}
scons prefix=%{buildroot}/usr install
%find_lang %{name}
desktop-file-install \
  --remove-key="Encoding" \
  --add-category="RasterGraphics;GTK;" \
  --dir=%{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/%{name}.desktop



%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
rm -rf %{buildroot}

%post
%{update_desktop_database}

%postun
%{clean_desktop_database}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc README LICENSE COPYING changelog
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/mypaint.*
%{_libdir}/%{name}/_mypaintlib.so

