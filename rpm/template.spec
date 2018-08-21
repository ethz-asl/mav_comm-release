Name:           ros-indigo-mav-planning-msgs
Version:        3.3.1
Release:        0%{?dist}
Summary:        ROS mav_planning_msgs package

Group:          Development/Libraries
License:        ASL 2.0
URL:            https://github.com/ethz-asl/mav_comm
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-cmake-modules
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-mav-msgs
Requires:       ros-indigo-message-generation
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       ros-indigo-trajectory-msgs
BuildRequires:  eigen3-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cmake-modules
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-mav-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-message-runtime
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  ros-indigo-trajectory-msgs

%description
Messages specific to MAV planning, especially polynomial planning.

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
* Tue Aug 21 2018 Helen Oleynikova <helen.oleynikova@mavt.ethz.ch> - 3.3.1-0
- Autogenerated by Bloom

* Mon Aug 20 2018 Helen Oleynikova <helen.oleynikova@mavt.ethz.ch> - 3.3.0-1
- Autogenerated by Bloom

