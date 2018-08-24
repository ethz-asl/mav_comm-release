Name:           ros-indigo-mav-comm
Version:        3.3.2
Release:        0%{?dist}
Summary:        ROS mav_comm package

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/ethz-asl/mav_comm
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-mav-msgs
Requires:       ros-indigo-mav-planning-msgs
BuildRequires:  ros-indigo-catkin

%description
Contains messages and services for MAV communication

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Aug 24 2018 Rik Bähnemann <brik@ethz.ch> - 3.3.2-0
- Autogenerated by Bloom

* Tue Aug 21 2018 Rik Bähnemann <brik@ethz.ch> - 3.3.1-0
- Autogenerated by Bloom

* Mon Aug 20 2018 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 3.3.0-1
- Autogenerated by Bloom

* Fri Aug 17 2018 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 3.3.0-0
- Autogenerated by Bloom

* Fri Apr 07 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 3.2.0-1
- Autogenerated by Bloom

* Fri Apr 07 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 3.2.0-0
- Autogenerated by Bloom

* Sun Aug 09 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 3.0.0-0
- Autogenerated by Bloom

* Fri May 22 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.0.3-0
- Autogenerated by Bloom

* Mon Apr 20 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.0.2-0
- Autogenerated by Bloom

* Fri Apr 10 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 2.0.1-0
- Autogenerated by Bloom

* Thu Apr 09 2015 Markus Achtelik <markus.achtelik_devel@mavt.ethz.ch> - 2.0.0-0
- Autogenerated by Bloom

