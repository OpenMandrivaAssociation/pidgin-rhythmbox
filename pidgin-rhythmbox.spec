%define	version	2.0
%define release	%mkrel 2

%define pidgin_version 2.2.1

Summary:	Update Pidgin user info with music info playing in Rhythmbox
Name:		pidgin-rhythmbox
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Instant messaging
URL:		http://jon.oberheide.org/projects/pidgin-rhythmbox/
Source:		http://jon.oberheide.org/projects/pidgin-rhythmbox/downloads/%{name}-%{version}.tar.bz2
BuildRequires:	pidgin-devel >= %{pidgin_version}
BuildRequires:	gtk2-devel
BuildRequires:	dbus-glib-devel
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
aclocal
autoconf

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


