%include	/usr/lib/rpm/macros.php
%define         _class          Image
%define         _subclass       IPTC
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - Extract, modify, and save IPTC data
Summary(pl):	%{_pearname} - wyci±ganie, modyfikowanie i zapisywanie danych IPTC
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7095a4abb7cd666f1245c21576683e25
URL:		http://pear.php.net/package/%{_pearname}/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a mechanism for modifying IPTC header
information. The class abstracts the functionality of iptcembed() and
iptcparse() in addition to providing methods that properly handle
replacing IPTC header fields back into image files.

This class has in PEAR status: %{_status}.

%description -l pl
Ten pakiet dostarcza mechanizm do modyfikowania informacji w
nag³ówkach IPTC. Klasa abstrahuje funkcjonalno¶æ iptcembed() i
iptcparse() jako dodatek do metod w³a¶ciwie obs³uguj±cych podstawianie
pól nag³ówka IPTC w plikach obrazków.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
