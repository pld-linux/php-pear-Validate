%include	/usr/lib/rpm/macros.php
%define		_class		Validate
%define		_status		alpha
%define		_pearname	%{_class}

Summary:	%{_pearname} - Validation class
Summary(pl):	%{_pearname} - klasa validuj±ca
Name:		php-pear-%{_pearname}
Version:	0.4.1
Release:	3
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6203c4285dc8ff0736b823fa6e991de4
URL:		http://pear.php.net/package/Validate/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# It's in a comment block
%define		_noautoreq	'pear(FR_insee_country_codes.php)'

%description
Package to validate various datas. It includes :
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
- liczby (min/max, dziesiêtne czy nie),
- email (sk³adnia, sprawdzanie domeny),
- stringi (predefiniowane typy alfanumeryczne z du¿ymi i ma³ymi
  literami, numeryczne,...),
- daty (min, max),
- karty kredytowe,
- mo¿liwe sprawdzenie wiêkszej ilo¶ci danych wywo³aniem pojedynczej
  metody (::multiple).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Finance

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/%{_class}/Finance/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Finance

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{tests,docs/*}
%dir %{php_pear_dir}/%{_class}/Finance
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/Finance/*.php
