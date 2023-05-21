%global optflags %optflags -Ofast

Name:		mypaint
Version:	2.0.1
Release:	2
Summary:	A simple paint program
Group:		Graphics
License:	GPLv2+
URL:		http://mypaint.org
Source0:	https://github.com/mypaint/mypaint/releases/download/v%{version}/%{name}-%{version}.tar.xz
#Patch0:		mypaint-2.0.0-fix-ginsanity-gtk-devs-are-crackpots.patch

BuildRequires:	python-scons scons
BuildRequires: swig
BuildRequires:	desktop-file-utils
BuildRequires: python3dist(numpy)
BuildRequires:	protobuf-compiler
BuildRequires:	pkgconfig(lapack)
BuildRequires: pkgconfig(py3cairo)
BuildRequires: python
BuildRequires: pkgconfig(python)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: python3egg(distribute)
BuildRequires: python3dist(pygobject)
BuildRequires: pkgconfig(pygobject-3.0)
#BuildRequires: pkgconfig(json)
BuildRequires: pkgconfig(json-c)
BuildRequires: pkgconfig(lcms2)
BuildRequires: pkgconfig(libmypaint)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(mypaint-brushes-2.0) >= 2.0.2

Requires:     mypaint-brushes
Requires:     python3dist(protobuf)

%description
Mypaint is a fast and easy/simple painter app focused on the painter, 
so you can only focus on the art and not the program itself. 
Currently MyPaint does not have a layer system, also mypaint is using 
pygtk with C extensions.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

%find_lang %{name}
desktop-file-install \
  --remove-key="Encoding" \
  --add-category="RasterGraphics;GTK;" \
  --dir=%{buildroot}%{_datadir}/applications \
   %{buildroot}%{_datadir}/applications/%{name}.desktop

%files -f %{name}.lang
%defattr(-,root,root,-)
%license COPYING
%{_bindir}/%{name}
%{_bindir}/mypaint-ora-thumbnailer
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*
%{_prefix}/lib/mypaint
%{_datadir}/metainfo/*.xml
%{_datadir}/thumbnailers/*.thumbnailer
