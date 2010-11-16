%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_status		beta
%define		_pearname	%{_class}
Summary:	%{_pearname} - Validation class
Summary(pl.UTF-8):	%{_pearname} - klasa sprawdzająca poprawność danych
Name:		php-pear-%{_pearname}
Version:	0.8.4
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f8b3a163980f920fb3e498bff37b14be
URL:		http://pear.php.net/package/Validate/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Suggests:	php-pear-Date
Suggests:	php-pear-Net_IDNA
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# It's in a comment block
%define		_noautoreq	'pear(FR_insee_country_codes.php)' 'pear(Date.*)' pear(Net/IDNA.*)

%description
Package to validate various data. It includes:
- numbers (min/max, decimal or not),
- email (syntax, domain check),
- string (predifined type alpha upper and/or lowercase, numeric,...),
- date (min, max),
- Credit cards,
- possibility valid multiple data with a single method call
  (::multiple).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet do sprawdzania poprawności różnych danych:
- liczb (minimalna/maksymalna, dziesiętne czy nie),
- adresy e-mail (składnia, sprawdzanie domeny),
- łańcuchy znaków (predefiniowane typy alfanumeryczne z dużymi i
  małymi literami, numeryczne...),
- daty (minimalna, maksymalna),
- karty kredytowe,
- możliwe sprawdzenie większej ilości danych wywołaniem pojedynczej
  metody (::multiple).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{version}-%{release}
AutoProv:	no
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
