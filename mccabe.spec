#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mccabe
Version  : 0.6.1
Release  : 36
URL      : http://pypi.debian.net/mccabe/mccabe-0.6.1.tar.gz
Source0  : http://pypi.debian.net/mccabe/mccabe-0.6.1.tar.gz
Summary  : McCabe checker, plugin for flake8
Group    : Development/Tools
License  : MIT
Requires: mccabe-python3
Requires: mccabe-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pytest-runner
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=========================
        
        Ned's script to check McCabe complexity.
        
        This module provides a plugin for ``flake8``, the Python code checker.
        
        
        Installation
        ------------

%package python
Summary: python components for the mccabe package.
Group: Default
Requires: mccabe-python3

%description python
python components for the mccabe package.


%package python3
Summary: python3 components for the mccabe package.
Group: Default
Requires: python3-core

%description python3
python3 components for the mccabe package.


%prep
%setup -q -n mccabe-0.6.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1519051604
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
