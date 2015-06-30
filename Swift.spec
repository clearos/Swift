Name:		Swift
Version:	3.3.3
Release:	3.1%{dist}
Summary:	Swift Mailer is a basic PHP Mailer class
License:	LGPL
Group:		System Environment/Base
Packager:	ClearFoundation
URL:		http://www.swiftmailer.org/
Source:		%{name}-%{version}-php5.tar.gz
Patch:      Swift-3.3.3-php5-split.patch
BuildRoot:	%{_builddir}/%{name}-%{version}-root
Requires:	webconfig-php >= 5.3.3
BuildArch:  noarch

%description
Swift Mailer is a basic PHP Mailer class intended to do nothing
more than handle sending emails from PHP scripts.

The Swift Mailer library can handle
pretty much everything you'd want when sending emails.

 * Attachments
 * Multipart Messaging
 * Basic, single part messaging
 * Custom Headers
 * Encoding
 * Inline images
 * Embedded files
 * Redundant connections
 * Rotating connections
 * Silent recipient denied handling
 * TLS Encryption
 * Bcc Sending
 * Batch Mailing
 * Custom SMTP commands
 * SSL Connections
 * Pluggable SMTP Authentication
 * Plugin Support with event handling features

%prep
%setup -q -n %{name}-%{version}-php5
%patch -p1 
%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p -m 755 $RPM_BUILD_ROOT/usr/clearos/sandbox/usr/share/pear/Swift
cp -r * $RPM_BUILD_ROOT/usr/clearos/sandbox/usr/share/pear/Swift
rm -rf $RPM_BUILD_ROOT/usr/clearos/sandbox/usr/share/pear/Swift/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc docs
/usr/clearos/sandbox/usr/share/pear

%changelog
* Wed Dec 05 2012 - ClearFoundation <developer@clearfoundation.com> - 3.3.3-3.1
- Added patch for changing deprecated split to explode
