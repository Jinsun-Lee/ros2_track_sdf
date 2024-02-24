cmake_minimum_required(VERSION 3.8)
project(debugging_pkg)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(ament_cmake_python REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/StudentSpec.msg"
)

install(PROGRAMS
  scripts/student_pub.py
  scripts/ta_sub.py
  
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()



