%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_status		alpha
%define		_pearname	%{_class}
Summary:	%{_pearname} - Validation class
Summary(pl):	%{_pearname} - klasa validuj�ca
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
# Source0-md5:	b83b758d52e359ac802001bf159fa3bf
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Package to validate various datas. It includes :
 - numbers (min/max, decimal or not),
 - email (syntax, domain check),
 - string (predifined type alpha upper and/or lowercase, numeric,...),
 - date (min, max),
 - Credit cards,
 - possibility valid multiple data with a single method call
   (::multiple).

This class has in PEAR status: %{_status}.

%description -l pl
Pakiet do sprawdzania poprawno�ci r�nych danych:
 - liczby (min/max, dziesi�tne czy nie),
 - email (sk�adnia, sprawdzanie domeny),
 - stringi (predefiniowane typy alfanumeryczne z du�ymi i ma�ymi
   literami, numeryczne,...),
 - daty (min, max),
 - karty kredytowe,
 - mo�liwe sprawdzenie wi�kszej ilo�ci danych wywo�aniem pojedynczej
   metody (::multiple).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{tests,docs/*}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
