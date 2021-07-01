#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mccabe
Version  : 0.6.1
Release  : 61
URL      : http://pypi.debian.net/mccabe/mccabe-0.6.1.tar.gz
Source0  : http://pypi.debian.net/mccabe/mccabe-0.6.1.tar.gz
Summary  : McCabe checker, plugin for flake8
Group    : Development/Tools
License  : MIT
Requires: mccabe-license = %{version}-%{release}
Requires: mccabe-python = %{version}-%{release}
Requires: mccabe-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pytest-runner

%description
=========================
        
        Ned's script to check McCabe complexity.
        
        This module provides a plugin for ``flake8``, the Python code checker.
        
        
        Installation
        ------------

%package license
Summary: license components for the mccabe package.
Group: Default

%description license
license components for the mccabe package.


%package python
Summary: python components for the mccabe package.
Group: Default
Requires: mccabe-python3 = %{version}-%{release}

%description python
python components for the mccabe package.


%package python3
Summary: python3 components for the mccabe package.
Group: Default
Requires: python3-core
Provides: pypi(mccabe)

%description python3
python3 components for the mccabe package.


%prep
%setup -q -n mccabe-0.6.1
cd %{_builddir}/mccabe-0.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603395475
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mccabe
cp %{_builddir}/mccabe-0.6.1/LICENSE %{buildroot}/usr/share/package-licenses/mccabe/9bf33315fe3a3b3f00928e6e98d067c4f762ee13
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mccabe/9bf33315fe3a3b3f00928e6e98d067c4f762ee13

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
