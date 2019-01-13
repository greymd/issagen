Name:       issagen
Summary:    Issa generator
Version:    1.0.0
Group:      Applications
License:    MIT
Release:    %(date '+%'s)
URL:        https://github.com/greymd/issagen
Source:     https://github.com/greymd/issagen/archive/v%{version}.tar.gz
BuildArch:  noarch
Vendor:     Yamada, Yasuhiro <greengregson at gmail dot com>
Requires:   imagemagick
Provides:   issagen

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Issa Generator.
Generate issagen.gif on the current directory.

%prep
%setup

%install
install -d -m 0755 %{buildroot}%{_bindir}
%{__cp} -a bin/* %{buildroot}%{_bindir}/

%files
%defattr(0644, root, root, 0755)
%doc README.md
%license LICENSE
%attr(0755, root, root) %{_bindir}/*

%clean
%{__rm} -rf %{buildroot}

