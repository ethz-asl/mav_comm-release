Name:           ros-jade-mav-comm
Version:        3.2.0
Release:        1%{?dist}
Summary:        ROS mav_comm package

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/ethz-asl/mav_comm
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-jade-mav-msgs
Requires:       ros-jade-planning-msgs
BuildRequires:  ros-jade-catkin

%description
Contains messages and services for MAV communication

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Fri Apr 28 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 3.2.0-1
- Autogenerated by Bloom

* Fri Apr 07 2017 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 3.2.0-0
- Autogenerated by Bloom

* Thu Aug 13 2015 Fadri Furrer <fadri.furrer@mavt.ethz.ch> - 3.0.0-0
- Autogenerated by Bloom

