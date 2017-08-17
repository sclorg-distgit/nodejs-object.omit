%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name object.omit

Summary:       Return a copy of an object excluding the given key
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       2.0.0
Release:       5%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/object.omit
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch

%description
Return a copy of an object excluding the given key, or array of keys. 
Also accepts an optional filter function as the last argument.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Mon Jul 03 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-5
- rh-nodejs8 rebuild

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 2.0.0-3
- Rebuilt with updated metapackage

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 2.0.0-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 2.0.0-1
- Initial package
