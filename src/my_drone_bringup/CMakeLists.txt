cmake_minimum_required(VERSION 3.14)
project(my_drone_bringup)

set(my_drone_bringup_MAJOR_VERSION 0)
set(my_drone_bringup_MINOR_VERSION 0)
set(my_drone_bringup_PATCH_VERSION 0)
set(my_drone_bringup_VERSION
  ${my_drone_bringup_MAJOR_VERSION}.${my_drone_bringup_MINOR_VERSION}.${my_drone_bringup_PATCH_VERSION})

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)
find_package(ament_cmake REQUIRED)
install(DIRECTORY
launch
DESTINATION share/${PROJECT_NAME}/
)
ament_package()