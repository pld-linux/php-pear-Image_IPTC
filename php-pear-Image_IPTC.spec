%include	/usr/lib/rpm/macros.php
%define		_class		Image
%define		_subclass	IPTC
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - extract, modify, and save IPTC data
Summary(pl.UTF-8):	%{_pearname} - wyciąganie, modyfikowanie i zapisywanie danych IPTC
Name:		php-pear-%{_pearname}
Version:	1.0.2
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	7095a4abb7cd666f1245c21576683e25
URL:		http://pear.php.net/package/Image_IPTC/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a mechanism for modifying IPTC header
information. The class abstracts the functionality of iptcembed() and
iptcparse() in addition to providing methods that properly handle
replacing IPTC header fields back into image files.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet dostarcza mechanizm do modyfikowania informacji w
nagłówkach IPTC. Klasa abstrahuje funkcjonalność iptcembed() i
iptcparse() jako dodatek do metod właściwie obsługujących podstawianie
pól nagłówka IPTC w plikach obrazków.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
