Name:           meson
Version:        1.4.1
Release:        1
Summary:        High productivity build system
License:        ASL 2.0
Url:            https://mesonbuild.com/
Source:         %{name}-%{version}.tar.bz2
Patch0:         patch-macros.patch
BuildArch:      noarch
BuildRequires:  python3-devel >= 3.6.0
Requires:       ninja >= 1.8.2

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
%py3_build

%install
%py3_install
install -Dpm 0644 -t %{buildroot}%{_rpmmacrodir} data/macros.%{name}

rm -rf %{buildroot}/%{_mandir}/*

%files
%license COPYING
%{_bindir}/%{name}
%{python3_sitelib}/mesonbuild/
%{python3_sitelib}/%{name}-*.egg-info/
%{_rpmmacrodir}/macros.%{name}
%dir %{_datadir}/polkit-1
%dir %{_datadir}/polkit-1/actions
%{_datadir}/polkit-1/actions/com.mesonbuild.install.policy
