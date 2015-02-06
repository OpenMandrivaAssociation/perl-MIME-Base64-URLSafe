%define upstream_name    MIME-Base64-URLSafe
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Perl version of Python's URL-safe base64 codec
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/MIME/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(MIME::Base64)
BuildArch:	noarch

%description
This module is a perl version of python's URL-safe base64 encoder /
decoder.

When embedding binary data in URL, it is preferable to use base64 encoding.
However, two characters ('+' and '/') used in the standard base64 encoding
have special meanings in URLs, often leading to re-encoding with
URL-encoding, or worse, interoperability problems.

To overcome the problem, the module provides a variation of base64 codec
compatible with python's urlsafe_b64encode / urlsafe_b64decode.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/MIME/

%changelog
* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 0.10.0-1mdv2010.1
+ Revision: 541083
- import perl-MIME-Base64-URLSafe


* Fri Apr 30 2010 cpan2dist 0.01-1mdv
- initial mdv release, generated with cpan2dist
