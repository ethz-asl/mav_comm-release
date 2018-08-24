Name:           ros-melodic-mav-comm
Version:        3.3.2
Release:        0%{?dist}
Summary:        ROS mav_comm package

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/ethz-asl/mav_comm
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-melodic-mav-msgs
Requires:       ros-melodic-mav-planning-msgs
BuildRequires:  ros-melodic-catkin

%description
Contains messages and services for MAV communication

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Aug 24 2018 Rik Bähnemann <brik@ethz.ch> - 3.3.2-0
- Autogenerated by Bloom

* Tue Aug 21 2018 Rik Bähnemann <brik@ethz.ch> - 3.3.1-0
- Autogenerated by Bloom

* Mon Aug 20 2018 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 3.3.0-1
- Autogenerated by Bloom

* Mon Aug 20 2018 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 3.3.0-0
- Autogenerated by Bloom

