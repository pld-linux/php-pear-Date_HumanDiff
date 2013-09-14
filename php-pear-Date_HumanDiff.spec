%define		status		alpha
%define		pearname	Date_HumanDiff
%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - Generate textual time differences that are easily understandable by humans
Name:		php-pear-Date_HumanDiff
Version:	0.4.0
Release:	1
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	c7442bc2bb8e10167ac2350048875448
URL:		http://pear.php.net/package/Date_HumanDiff/
BuildRequires:	php-packagexml2cl
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(date)
Requires:	php(pcre)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Generate textual time differences that are easily understandable by
humans ("5 minutes ago"). The package supports minutes, hours, days,
weeks, months and years. A time difference of 65 seconds gets
converted to "a minute ago".

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%build
packagexml2cl package.xml > ChangeLog

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog install.log
%doc docs/Date_HumanDiff/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Date/HumanDiff.php
%dir %{php_pear_dir}/Date/HumanDiff
%{php_pear_dir}/Date/HumanDiff/Locale.php
%{php_pear_dir}/Date/HumanDiff/LocaleArray.php
%dir %{php_pear_dir}/Date/HumanDiff/Locale
%lang(de) %{php_pear_dir}/Date/HumanDiff/Locale/de.php
%lang(el) %{php_pear_dir}/Date/HumanDiff/Locale/el.php
%lang(fa) %{php_pear_dir}/Date/HumanDiff/Locale/fa.php
