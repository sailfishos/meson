%global __python %{__python3}

%define libname  mesonbuild

Name:           meson
Version:        0.54.3
Release:        1
Summary:        High productivity build system
License:        ASL 2.0
Url:            http://mesonbuild.com/
Source:         %{name}-%{version}.tar.bz2
Patch0:         0001-patch-macros.patch

BuildArch:      noarch

BuildRequires:  python3-devel >= 3.5.0
BuildRequires:  python3-setuptools
Requires:       python3-setuptools
Requires:       ninja >= 1.7.0
# Workaround ccache autodetection not working on OBS arm builds, JB#42632
Requires:       ccache

%description
Meson is a build system designed to optimise programmer productivity.
It aims to do this by providing support for software development
tools and practices, such as unit tests, coverage reports, Valgrind,
CCache and the like. Supported languages include C, C++, Fortran,
Java, Rust. Build definitions are written in a non-turing complete
Domain Specific Language.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --prefix=%{_prefix}
install -Dpm 0644 data/macros.%{name} %{buildroot}%{_sysconfdir}/rpm/macros.%{name}

rm -rf %{buildroot}/%{_mandir}/*

%files
%license COPYING
%{_bindir}/%{name}
%{python_sitelib}/%{libname}/
%{python_sitelib}/%{name}-*.egg-info/
%{_sysconfdir}/rpm/macros.%{name}
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy
