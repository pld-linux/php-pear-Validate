%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_status		beta
%define		_pearname	%{_class}

Summary:	%{_pearname} - Validation class
Summary(pl):	%{_pearname} - klasa sprawdzaj±ca poprawno¶æ danych
Name:		php-pear-%{_pearname}
Version:	0.6.2
Release:	1
Epoch:		0
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	127b233b3d42b33a3030a6f6bcff2111
URL:		http://pear.php.net/package/Validate/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# It's in a comment block
%define		_noautoreq	'pear(FR_insee_country_codes.php)' 'pear(Date.*)'

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

%description -l pl
Pakiet do sprawdzania poprawno¶ci ró¿nych danych:
- liczb (minimalna/maksymalna, dziesiêtne czy nie),
- adresy e-mail (sk³adnia, sprawdzanie domeny),
- ³añcuchy znaków (predefiniowane typy alfanumeryczne z du¿ymi i
  ma³ymi literami, numeryczne...),
- daty (minimalna, maksymalna),
- karty kredytowe,
- mo¿liwe sprawdzenie wiêkszej ilo¶ci danych wywo³aniem pojedynczej
  metody (::multiple).

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
