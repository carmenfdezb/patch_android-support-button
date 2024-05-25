Name:       android-support-button

BuildArch: noarch

Summary:    Android Support button
Version:    1.1.0
Release:    1
Group:      Qt/Qt
License:    WTFPL
Source0:    %{name}-%{version}.tar.bz2
Requires:   patchmanager
Requires:	aliendalvik
URL:        https://github.com/carmenfdezb

%description
Toggle Android Support button for starting and stopping Android Support

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/patchmanager/patches/%{name}
cp -r patch/* %{buildroot}/usr/share/patchmanager/patches/%{name}

%pre
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%preun
if [ -d /var/lib/patchmanager/ausmt/patches/%{name} ]; then
/usr/sbin/patchmanager -u %{name} || true
fi

%files
%defattr(-,root,root,-)
%{_datadir}/patchmanager/patches/%{name}

%changelog
* Sat May 25 2024 Carmen Fdez. B. 1.1.0-1
- Support for sfos 4.6

* Sun Feb 19 2023 Carmen Fdez. B. 1.0.0-1
- Initial release
