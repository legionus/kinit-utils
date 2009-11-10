Name: kinit-utils
Version: 1.5.15
Release: alt1

Summary: Small utilities built with klibc
License: BSD/GPL
Group: System/Base

Packager: Alexey Gladkov <legion@altlinux.ru>

Source0: %name-%version.tar
Patch0:  klibc.patch
Patch1:  md_run.patch
Patch2:  replace.patch
Patch3:  showenv.patch

# Automatically added by buildreq on Wed Nov 11 2009
BuildRequires: libcap-devel zlib-devel

%description
This package contains a collection of programs that are linked against
klibc.  These duplicate some of the functionality of a regular Linux
toolset, but are typically much smaller than their full-function
counterparts.  They are intended for inclusion in initramfs images and
embedded systems.

%prep
%setup -q
%patch0 -p0 -b .fix0
%patch1 -p0 -b .fix1
%patch2 -p0 -b .fix2
%patch3 -p0 -b .fix3

%build
%make_build

%install
%make_install \
	bindir=%buildroot/lib/initrd/bin \
	install

%files
/lib/initrd

%changelog
* Tue Nov 10 2009 Alexey Gladkov <legion@altlinux.ru> 1.5.15-alt1
- First build for Sisyphus.

