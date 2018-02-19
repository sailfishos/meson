%global __python %{__python3}

%define _name   mesonbuild
Name:           meson
Version:        0.44.0
Release:        0
Summary:        Python-based build system
License:        ASL 2.0
Group:          Development/Tools/Building
Url:            http://mesonbuild.com/
Source:         https://github.com/mesonbuild/meson/releases/download/%{version}/meson-%{version}.tar.gz

BuildRequires:  python3-base
BuildArch:      noarch

%description
Meson is a build system designed to optimise programmer productivity.
It aims to do this by providing support for software development
tools and practices, such as unit tests, coverage reports, Valgrind,
CCache and the like. Supported languages include C, C++, Fortran,
Java, Rust. Build definitions are written in a non-turing complete
Domain Specific Language.

%prep
%setup -q -n meson-%{version}/meson

# Remove static boost tests from test cases/frameworks/1 boost (can't use patch due to spaces in dirname)
sed -i "/static/d" test\ cases/frameworks/1\ boost/meson.build

# Disable test of llvm-static libs
sed -i "s/foreach static : \[true, false\]/foreach static : \[false\]/" test\ cases/frameworks/15\ llvm/meson.build

# We do not have gmock available at this moment - can't run the test suite for it
rm -rf "test cases/frameworks/3 gmock" \
       "test cases/objc/2 nsstring"

# Remove hashbang from non-exec script
sed -i '1{/\/usr\/bin\/env/d;}' ./mesonbuild/rewriter.py

%build
python3 setup.py build

%install
python3 setup.py install \
  --root=%{buildroot} --prefix=%{_prefix}

install -Dpm 0644 data/macros.meson \
  %{buildroot}%{_rpmconfigdir}/macros.d/macros.meson

rm -rf %{buildroot}/%{_mandir}/*

%files
%doc COPYING
%{_bindir}/meson
%{_bindir}/mesonconf
%{_bindir}/mesonintrospect
%{_bindir}/mesontest
%{_bindir}/wraptool
%{python_sitelib}/%{_name}/
%{python_sitelib}/meson-*
%{_rpmconfigdir}/macros.d/macros.meson
