Name:		certbot-dns-pdns
Version:	0.1.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/c/certbot_dns_pdns/certbot_dns_pdns-%{version}.tar.gz
Summary:	DNS Authenticator for certbot using the PowerDNS API
URL:		https://pypi.org/project/certbot-dns-pdns/
License:	Apache-2.0
Group:		Development/Python
Requires:	certbot
BuildRequires:	python
BuildRequires:	python%{pyver}dist(poetry-core)
BuildSystem:	python
BuildArch:	noarch

%description
DNS Authenticator for certbot using the PowerDNS API

%files
%{py_sitedir}/certbot_dns_pdns
%{py_sitedir}/certbot_dns_pdns-*.*-info
