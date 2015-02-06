%define	oname	ruby-yadis

Summary:	A library for performing Yadis service discovery
Name:		rubygem-%{oname}
Version:	0.3.4
Release:	3
License:	Apache License
Group:		Development/Ruby
URL:		http://%{oname}.rubyforge.org/
Source0:	http://gems.rubyforge.org/gems/%{oname}-%{version}.gem
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ruby-RubyGems
Requires:	ruby
BuildArch:	noarch

%description
Echoe is a Rubygems packaging tool that provides Rake tasks for documentation,
extension compiling, testing, and deployment.

%prep

%build

%install
rm -rf %{buildroot}
gem install --local --install-dir %{buildroot}/%{ruby_gemdir} --force %{SOURCE0}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/gems/%{oname}-%{version}
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec



%changelog
* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.4-2mdv2011.0
+ Revision: 614797
- the mass rebuild of 2010.1 packages

* Tue Feb 02 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.4-1mdv2010.1
+ Revision: 499411
- import rubygem-ruby-yadis


* Mon Feb  2 2010 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.3.4-1
- initial release
