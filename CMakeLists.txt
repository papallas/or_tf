cmake_minimum_required(VERSION 2.4.6)
project(or_tf)

include(CheckCXXSourceCompiles)
set(CMAKE_CXX_FLAGS "-std=c++0x ${CMAKE_CXX_FLAGS}")

find_package(catkin REQUIRED COMPONENTS
    geometry_msgs
    openrave_catkin
    std_msgs
    tf
)

include_directories(SYSTEM
    ${catkin_INCLUDE_DIRS}
    ${OpenRAVE_INCLUDE_DIRS}
    ${PROJECT_NAME}/include
)

link_directories(
    ${catkin_LIBRARY_DIRS}
    ${OpenRAVE_LIBRARY_DIRS}
)

catkin_package(
    INCLUDE_DIRS include
    LIBRARIES
        ${PROJECT_NAME}
    CATKIN_DEPENDS
        geometry_msgs
        tf
        std_msgs
)

include_directories(include/${PROJECT_NAME})

# Helper library that implements core functionality.
add_library(${PROJECT_NAME} SHARED
    src/or_tf.cpp
)

# Stub library that registers the plugins with OpenRAVE.
openrave_plugin(${PROJECT_NAME}_plugin
    src/or_tf_interface.cpp
)

target_link_libraries(${PROJECT_NAME}_plugin
    ${PROJECT_NAME}
    ${catkin_LIBRARIES}
)

install(TARGETS ${PROJECT_NAME}
    ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
    LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
    RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
