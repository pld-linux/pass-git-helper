Summary:	A git credential helper interfacing with pass
Name:		pass-git-helper
Version:	4.0.0
Release:	1
License:	LGPL v3+
Group:		Applications
Source0:	https://github.com/languitar/pass-git-helper/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b70ff00afa81294cca135af452116151
URL:		https://github.com/languitar/pass-git-helper
BuildRequires:	python3 >= 1:3.11
BuildRequires:	python3-modules >= 1:3.11
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.11
Requires:	python3-setuptools
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A git credential helper implementation that allows using pass as the
credential backend for your https-based git repositories.

%prep
%setup -q

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/pass-git-helper
%{py3_sitescriptdir}/__pycache__/passgithelper.cpython-*.py[co]
%{py3_sitescriptdir}/passgithelper.py
%{py3_sitescriptdir}/pass_git_helper-%{version}-py*.egg-info
