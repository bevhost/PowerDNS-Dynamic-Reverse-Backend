Summary: PowerDNS Dynamic Reverse Backend
Name: pdns-dynrev
Version: 0.9
Release: 2
License: MIT
Group: System Environment/Daemons
Source: https://github.com/bevhost/PowerDNS-Dynamic-Reverse-Backend/archive/master.zip
Packager: David Beveridge <dave@bevhost.com>
Requires: python-netaddr py-radix python-IPy PyYAML pdns-backend-pipe
BuildRequires: /usr/bin/pathfix.py
BuildArch: noarch

%description
PowerDNS pipe backend for generating reverse DNS entries and their
forward lookup.

%prep
%autosetup -n PowerDNS-Dynamic-Reverse-Backend-master
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" . 

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_sysconfdir}/pdns
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_docdir}/%{name}
install -m 0755 pdns-dynamic-reverse-backend.py %{buildroot}%{_sbindir}/pdns-dynamic-reverse-backend.py
install -m 0644 dynrev.yml %{buildroot}%{_sysconfdir}/pdns/dynrev.yml
install -m 0644 README.md %{buildroot}%{_docdir}/%{name}/README

%clean
rm -rf %{buildroot}

%pre 

%post

%files
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/pdns/dynrev.yml
%attr(0755,root,root) %{_sbindir}/pdns-dynamic-reverse-backend.py
%attr(0644,root,root) %{_docdir}/%{name}/README

%changelog
* Thu Jun 27 2024 David Beveridge <dave@bevhost.com>
- Use pathfix.py to set the shebang to python version

* Sat Nov 09 2019 David Beveridge <dave@bevhost.com>
- initial build

