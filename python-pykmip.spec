%global pypi_name PyKMIP
%global sname pykmip

%if 0%{?fedora}
%global with_python3 1
%endif

Name:           python-%{sname}
Version:        0.5.0
Release:        3%{?dist}
Summary:        Python implementation of the Key Management Interoperability Protocol

License:        ASL 2.0
URL:            https://github.com/OpenKMIP/PyKMIP
Source0:        https://pypi.python.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The
standard is governed by the `Organization for the Advancement of
Structured InformationStandards`_ (OASIS).

%package -n python2-%{sname}
Summary:        Python implementation of the Key Management Interoperability Protocol
%{?python_provide:%python_provide python2-%{sname}}

BuildRequires:       python2-devel
BuildRequires:       python-enum34
BuildRequires:       python-six
BuildRequires:       python-setuptools

Requires:     python-enum34
Requires:     python-six

%description -n python2-%{sname}
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The
standard is governed by the `Organization for the Advancement of
Structured InformationStandards`_ (OASIS).

%if 0%{?with_python3}
%package -n python3-%{sname}
Summary:        Python implementation of the Key Management Interoperability Protocol
%{?python_provide:%python_provide python3-%{sname}}


BuildRequires:       python3-devel
BuildRequires:       python3-six
BuildRequires:       python3-setuptools

Requires:     python3-six

%description -n python3-%{sname}
PyKMIP is a Python implementation of the Key Management Interoperability
Protocol (KMIP). KMIP is a client/server communication protocol for the
storage and maintenance of key, certificate, and secret objects. The
standard is governed by the `Organization for the Advancement of
Structured InformationStandards`_ (OASIS).

%endif

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build

%if 0%{?with_python3}
%py3_build
%endif

%install
%py2_install

%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{sname}
%doc README.rst
%license LICENSE.txt
%if !0%{?with_python3}
%{_bindir}/pykmip-server
%endif
%{python2_sitelib}/kmip
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%if 0%{?with_python3}
%files -n python3-%{sname}
%doc README.rst
%license LICENSE.txt
%{_bindir}/pykmip-server
%{python3_sitelib}/kmip
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%endif

%changelog
* Fri Jul 28 2017 Jan Beran <jberan@redhat.com> 0.5.0-3
- Fix of python3-pykmip requiring both Python 2 and Python 3

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 05 2017 Haikel Guemar <hguemar@fedoraproject.org> 0.5.0-1
- Update to 0.5.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.0-5
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5
- Remove python3-enum34 as enum is now part of stdlib in python3

* Wed Sep 30 2015 chandankumar <chkumar246@gmail.com> - 0.4.0-1
- Initial package.
