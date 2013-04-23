Name:		puppet-cobbler	
Version:	0.1
Release:	1cisco%{?dist}
Summary:	Puppet module to configure cobbler

Group:		System Environment/Base
License: 	Apache License 2.0	
URL:		https://github.com/CiscoSystems/puppet-cobbler.git
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This module can be used to flexibly configure cobbler. It is recommended to use the openstack module as a starting place.

%prep
%setup -q


%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_usr}/share/puppet/modules/%{name}/
cp -R * %{buildroot}/%{_usr}/share/puppet/modules/%{name}/

%files
%dir %{_usr}/share/puppet/modules/%{name}/
%{_usr}/share/puppet/modules/%{name}/*


%defattr(-,root,root,-)
%doc README.md examples/

%clean
rm -rf %{buildroot}

%changelog
* Tue Apr 23 2013 Pradeep Kilambi <pkilambi@cisco.com> - 0.1-1cisco
- Initial package.

