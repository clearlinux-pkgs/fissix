#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : fissix
Version  : 21.6.6
Release  : 3
URL      : https://files.pythonhosted.org/packages/45/0f/d2d0a61c5b3bb1a2d5e677996ee12f3a3505551f70c3bad17cc1a2a631bb/fissix-21.6.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/45/0f/d2d0a61c5b3bb1a2d5e677996ee12f3a3505551f70c3bad17cc1a2a631bb/fissix-21.6.6.tar.gz
Summary  : Monkeypatches to override default behavior of lib2to3.
Group    : Development/Tools
License  : Python-2.0
Requires: fissix-license = %{version}-%{release}
Requires: fissix-python = %{version}-%{release}
Requires: fissix-python3 = %{version}-%{release}
Requires: appdirs
BuildRequires : appdirs
BuildRequires : buildreq-distutils3

%description
fissix
======
Backport of latest lib2to3, with enhancements.
[![build status](https://travis-ci.org/jreese/fissix.svg?branch=master)](https://travis-ci.org/jreese/fissix)
[![version](https://img.shields.io/pypi/v/fissix.svg)](https://pypi.org/project/fissix)
[![license](https://img.shields.io/pypi/l/fissix.svg)](https://github.com/jreese/fissix/blob/master/LICENSE)
[![code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

%package license
Summary: license components for the fissix package.
Group: Default

%description license
license components for the fissix package.


%package python
Summary: python components for the fissix package.
Group: Default
Requires: fissix-python3 = %{version}-%{release}

%description python
python components for the fissix package.


%package python3
Summary: python3 components for the fissix package.
Group: Default
Requires: python3-core
Provides: pypi(fissix)
Requires: pypi(appdirs)

%description python3
python3 components for the fissix package.


%prep
%setup -q -n fissix-21.6.6
cd %{_builddir}/fissix-21.6.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1631477791
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/fissix
cp %{_builddir}/fissix-21.6.6/LICENSE %{buildroot}/usr/share/package-licenses/fissix/d9e4c07df8805b7ff5a20663e7b154c8dd1ddc8b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/fissix/d9e4c07df8805b7ff5a20663e7b154c8dd1ddc8b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
