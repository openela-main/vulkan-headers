%global __python %{__python3}
Name:           vulkan-headers
Version:        1.3.250.1
Release:        1%{?dist}
Summary:        Vulkan Header files and API registry

License:        ASL 2.0
URL:            https://github.com/KhronosGroup/Vulkan-Headers
Source0:        %url/archive/sdk-%{version}.tar.gz#/Vulkan-Headers-sdk-%{version}.tar.gz

BuildRequires:  cmake
BuildArch:      noarch       

%description
Vulkan Header files and API registry

%prep
%autosetup -n Vulkan-Headers-sdk-%{version}


%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} .
%make_build


%install
%make_install


%files
%license LICENSE.txt
%doc README.md
%{_includedir}/vulkan/
%{_includedir}/vk_video/
%dir %{_datadir}/vulkan/
%{_datadir}/vulkan/registry/
%dir %{_datadir}/cmake/VulkanHeaders/
%{_datadir}/cmake/VulkanHeaders/*.cmake

%changelog
* Wed Jul 12 2023 Dave Airlie <airlied@redhat.com> - 1.3.250.1-1
- Update to 1.3.250.1 SDK release

* Fri Feb 10 2023 Dave Airlie <airlied@redhat.com> - 1.3.239.0-1
- Update to 1.3.239.0 SDK release

* Wed Aug 24 2022 Dave Airlie <airlied@redhat.com> - 1.3.224.0-1
- Update to 1.3.224.0 SDK release

* Mon Jun 20 2022 Dave Airlie <airlied@redhat.com> - 1.3.216.0-1
- Update to 1.3.216.0 SDK release

* Mon Feb 21 2022 Dave Airlie <airlied@redhat.com> - 1.3.204.0-1
- Update to 1.3.204.0 headers

* Fri Jan 29 2021 Dave Airlie <airlied@redhat.com> - 1.2.162.0-1
- Update to 1.2.162.0 headers

* Tue Aug 04 2020 Dave Airlie <airlied@redhat.com< - 1.2.148.0-1
- Update to 1.2.148.0 headers

* Fri May 22 2020 Dave Airlie <airlied@redhat.com> - 1.2.135.0-1
- Update to 1.2.135.0 headers

* Wed Jan 29 2020 Dave Airlie <airlied@redhat.com> - 1.2.131.1-1
- Update to 1.2.131.1 headers

* Tue Nov 12 2019 Dave Airlie <airlied@redhat.com> - 1.1.126.0-1
- Update to 1.1.126.0 headers

* Sat Aug 03 2019 Dave Airlie <airlied@redhat.com> - 1.1.114.0-1
- Update to 1.1.114.0 headers

* Wed Mar 06 2019 Dave Airlie <airlied@redhat.com> - 1.1.101.0-1
- Update to 1.1.101.0 headers

* Tue Aug 07 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.82.0-1
- Update to 1.1.82.0

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.77.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 22 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.1.77.0-1
- Initial package
