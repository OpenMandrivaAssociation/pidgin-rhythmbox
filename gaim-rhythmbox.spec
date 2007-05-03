%define	version	2.0
%define pre beta5
%define release	%mkrel 0.%pre.2

%define gaim_version 1:2.0.0

Summary:	Update Gaim user info with music info playing in Rhythmbox
Name:		gaim-rhythmbox
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Networking/Instant messaging
URL:		http://jon.oberheide.org/projects/gaim-rhythmbox/
Source:		http://jon.oberheide.org/projects/gaim-rhythmbox/downloads/%{name}-%{version}%pre.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	gaim-devel >= %{gaim_version}
BuildRequires:	gtk2-devel
BuildRequires:	dbus-glib-devel
Requires:	gaim >= %{gaim_version}
Requires:	rhythmbox

%description
The Gaim-Rhythmbox plugin will automatically update your Gaim user
info and/or away message with the currently playing music in Rhythmbox.

If the artist and title are known, it will also attempt to create
a link to the song's lyrics by using Google's "I'm Feeling Lucky"
feature.

Gaim-Rhythmbox will replace %%rb in your user info and/or away message
with the song information. As of version 1.5.0.1, only oscar protocol
(i.e. AIM/ICQ) is supported, though it is expected to support every
protocol in 2.0.

%prep
%setup -q -n %name-%version%pre
aclocal
autoconf

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}%{_libdir}/gaim/*.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_libdir}/gaim/*.so


