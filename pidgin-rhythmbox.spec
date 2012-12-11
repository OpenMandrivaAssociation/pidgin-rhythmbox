%define	version	2.0
%define release	%mkrel 8

%define pidgin_version 2.2.1

Summary:	Update Pidgin user info with music info playing in Rhythmbox
Name:		pidgin-rhythmbox
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://jon.oberheide.org/projects/pidgin-rhythmbox/
Source:		http://jon.oberheide.org/projects/pidgin-rhythmbox/downloads/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	pidgin-devel >= %{pidgin_version}
BuildRequires:	gtk2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	automake
Requires:	pidgin >= %{pidgin_version}
Requires:	rhythmbox
Provides: gaim-rhythmbox
Obsoletes: gaim-rhythmbox

%description
The Pidgin-Rhythmbox plugin will automatically update your Pidgin user
info and/or away message with the currently playing music in Rhythmbox.

If the artist and title are known, it will also attempt to create
a link to the song's lyrics by using Google's "I'm Feeling Lucky"
feature.

Pidgin-Rhythmbox will replace %%rb in your user info and/or away message
with the song information. As of version 1.5.0.1, only oscar protocol
(i.e. AIM/ICQ) is supported, though it is expected to support every
protocol in 2.0.

%prep
%setup -q -n %name-%version
autoreconf -fi

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}%{_libdir}/pidgin/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/pidgin/*.so




%changelog
* Thu Aug 04 2011 Götz Waschk <waschk@mandriva.org> 2.0-8mdv2012.0
+ Revision: 693154
- update build deps
- rebuild

* Sun Aug 02 2009 Götz Waschk <waschk@mandriva.org> 2.0-7mdv2011.0
+ Revision: 407655
- update license
- fix build

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 2.0-6mdv2009.0
+ Revision: 259037
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.0-5mdv2009.0
+ Revision: 246967
- rebuild

* Thu Mar 13 2008 Andreas Hasenack <andreas@mandriva.com> 2.0-3mdv2008.1
+ Revision: 187589
- rebuild for 2008.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Oct 03 2007 Funda Wang <fwang@mandriva.org> 2.0-2mdv2008.0
+ Revision: 95090
- rebuild for pidgin 2.2.1

* Thu May 03 2007 Götz Waschk <waschk@mandriva.org> 2.0-1mdv2008.0
+ Revision: 20885
- new version
- rename

