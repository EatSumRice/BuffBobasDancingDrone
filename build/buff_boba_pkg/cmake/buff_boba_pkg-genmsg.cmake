# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "buff_boba_pkg: 3 messages, 0 services")

set(MSG_I_FLAGS "-Ibuff_boba_pkg:/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg;-Istd_msgs:/opt/ros/noetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(buff_boba_pkg_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg" NAME_WE)
add_custom_target(_buff_boba_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "buff_boba_pkg" "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg" ""
)

get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg" NAME_WE)
add_custom_target(_buff_boba_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "buff_boba_pkg" "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg" ""
)

get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg" NAME_WE)
add_custom_target(_buff_boba_pkg_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "buff_boba_pkg" "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/buff_boba_pkg
)
_generate_msg_cpp(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/buff_boba_pkg
)
_generate_msg_cpp(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/buff_boba_pkg
)

### Generating Services

### Generating Module File
_generate_module_cpp(buff_boba_pkg
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/buff_boba_pkg
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(buff_boba_pkg_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(buff_boba_pkg_generate_messages buff_boba_pkg_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_cpp _buff_boba_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_cpp _buff_boba_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_cpp _buff_boba_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(buff_boba_pkg_gencpp)
add_dependencies(buff_boba_pkg_gencpp buff_boba_pkg_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS buff_boba_pkg_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/buff_boba_pkg
)
_generate_msg_eus(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/buff_boba_pkg
)
_generate_msg_eus(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/buff_boba_pkg
)

### Generating Services

### Generating Module File
_generate_module_eus(buff_boba_pkg
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/buff_boba_pkg
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(buff_boba_pkg_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(buff_boba_pkg_generate_messages buff_boba_pkg_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_eus _buff_boba_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_eus _buff_boba_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_eus _buff_boba_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(buff_boba_pkg_geneus)
add_dependencies(buff_boba_pkg_geneus buff_boba_pkg_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS buff_boba_pkg_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/buff_boba_pkg
)
_generate_msg_lisp(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/buff_boba_pkg
)
_generate_msg_lisp(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/buff_boba_pkg
)

### Generating Services

### Generating Module File
_generate_module_lisp(buff_boba_pkg
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/buff_boba_pkg
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(buff_boba_pkg_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(buff_boba_pkg_generate_messages buff_boba_pkg_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_lisp _buff_boba_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_lisp _buff_boba_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_lisp _buff_boba_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(buff_boba_pkg_genlisp)
add_dependencies(buff_boba_pkg_genlisp buff_boba_pkg_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS buff_boba_pkg_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/buff_boba_pkg
)
_generate_msg_nodejs(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/buff_boba_pkg
)
_generate_msg_nodejs(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/buff_boba_pkg
)

### Generating Services

### Generating Module File
_generate_module_nodejs(buff_boba_pkg
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/buff_boba_pkg
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(buff_boba_pkg_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(buff_boba_pkg_generate_messages buff_boba_pkg_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_nodejs _buff_boba_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_nodejs _buff_boba_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_nodejs _buff_boba_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(buff_boba_pkg_gennodejs)
add_dependencies(buff_boba_pkg_gennodejs buff_boba_pkg_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS buff_boba_pkg_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/buff_boba_pkg
)
_generate_msg_py(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/buff_boba_pkg
)
_generate_msg_py(buff_boba_pkg
  "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/buff_boba_pkg
)

### Generating Services

### Generating Module File
_generate_module_py(buff_boba_pkg
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/buff_boba_pkg
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(buff_boba_pkg_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(buff_boba_pkg_generate_messages buff_boba_pkg_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/moves.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_py _buff_boba_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/Song.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_py _buff_boba_pkg_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/bhyun/buff_catkin_ws/src/buff_boba_pkg/msg/numbermoves.msg" NAME_WE)
add_dependencies(buff_boba_pkg_generate_messages_py _buff_boba_pkg_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(buff_boba_pkg_genpy)
add_dependencies(buff_boba_pkg_genpy buff_boba_pkg_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS buff_boba_pkg_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/buff_boba_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/buff_boba_pkg
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(buff_boba_pkg_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/buff_boba_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/buff_boba_pkg
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(buff_boba_pkg_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/buff_boba_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/buff_boba_pkg
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(buff_boba_pkg_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/buff_boba_pkg)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/buff_boba_pkg
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(buff_boba_pkg_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/buff_boba_pkg)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/buff_boba_pkg\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/buff_boba_pkg
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(buff_boba_pkg_generate_messages_py std_msgs_generate_messages_py)
endif()
