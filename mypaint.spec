%define use_ccache 1
%define ccachedir~/.ccache-OOo%{mdvsuffix}
%{?_with_ccache: %global use_ccache 1}
%{?_without_ccache: %global use_ccache 0}
%define date	    %(echo `LC_ALL="C" date +"%a %b %d %Y"`)

Name:		mypaint
Version:	1.0.0
Release:	4
Summary:	A simple paint program
Group:		Graphics
License:	GPLv2+
URL:		http://mypaint.intilinux.com/
Source0:	http://download.gna.org/mypaint/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	pygtk2.0-devel
BuildRequires:	python-scons scons
BuildRequires:	swig
BuildRequires:	desktop-file-utils
BuildRequires:	python-numpy-devel
BuildRequires:	protobuf-compiler
BuildRequires:	pkgconfig(lapack)
Requires:	pygtk2.0
Requires:	python-protobuf

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
scons prefix=%{buildroot}/usr install
%find_lang %{name}
desktop-file-install \
  --remove-key="Encoding" \
  --add-category="RasterGraphics;GTK;" \
  --dir=%{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/%{name}.desktop



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
%{_iconsdir}/hicolor/*
%{_libdir}/%{name}/_mypaintlib.so


%changelog
* Thu Nov 24 2011 Александр Казанцев <kazancas@mandriva.org> 1.0.0-1
+ Revision: 733232
- new version 1.0.0

* Fri May 06 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.9.1-1
+ Revision: 669917
- new version 0.9.1

* Mon Nov 08 2010 Matthew Dawkins <mattydaw@mandriva.org> 0.9.0-1mdv2011.0
+ Revision: 595124
- new version 0.9.0

* Sun May 02 2010 Frederik Himpe <fhimpe@mandriva.org> 0.8.2-2mdv2010.1
+ Revision: 541622
- Fix Requirs (does not start without python-protobuf installed:
  bug #58792)

* Mon Mar 01 2010 Frederik Himpe <fhimpe@mandriva.org> 0.8.2-1mdv2010.1
+ Revision: 513067
- Update to new version 0.8.2

* Mon Feb 22 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.8.1-1mdv2010.1
+ Revision: 509579
- update to 0.8.1

* Sat Jan 30 2010 Frederik Himpe <fhimpe@mandriva.org> 0.8.0-1mdv2010.1
+ Revision: 498503
- Add protobuf-compiler BuildRequires
- Remove useless BuildRequires and Requires, because they are
  already implicity required by other (Build)Requires
- Update to new version 0.8.0
- Use scons hacks from Fedora, makes it use correct libdir on 64 bit
- Use upstream desktop file

* Thu Oct 01 2009 Stéphane Téletchéa <steletch@mandriva.org> 0.7.1-2mdv2010.0
+ Revision: 452147
- fix library path
- import mypaint


* Thu Oct 1 2009 Stephane Teletchea <steletch@mandriva.org> mypaint-0.7.1-1mdv2010.0
- Correct desktop file
- Clean spaces in spec, simplify BR

* Mon Sep 28 2009 Donald Stewart <watersnowrock@gmail.com> mypaint-0.7.1-1djbs2010.0
- Import .spec from MIB
- Clean .spec 
