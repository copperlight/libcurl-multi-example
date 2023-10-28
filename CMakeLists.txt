cmake_minimum_required(VERSION 3.13)

project(libcurl-multi-example)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

add_compile_options(-fno-omit-frame-pointer "$<$<CONFIG:Debug>:-fsanitize=address>")
add_link_options(-fno-omit-frame-pointer "$<$<CONFIG:Debug>:-fsanitize=address>")

include(CTest)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

#-- examples
add_executable(10-at-a-time "src/examples/10-at-a-time.c")
target_include_directories(10-at-a-time PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(10-at-a-time ${CONAN_LIBS})

add_executable(chkspeed "src/examples/chkspeed.c")
target_include_directories(chkspeed PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(chkspeed ${CONAN_LIBS})

add_executable(crawler "src/examples/crawler.c")
target_include_directories(crawler PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(crawler ${CONAN_LIBS})

add_executable(debug "src/examples/debug.c")
target_include_directories(debug PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(debug ${CONAN_LIBS})

add_executable(http-post "src/examples/http-post.c")
target_include_directories(http-post PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(http-post ${CONAN_LIBS})

add_executable(multi-app "src/examples/multi-app.cpp")
target_include_directories(multi-app PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(multi-app ${CONAN_LIBS})

add_executable(multi-debugcallback "src/examples/multi-debugcallback.c")
target_include_directories(multi-debugcallback PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(multi-debugcallback ${CONAN_LIBS})

add_executable(multi-double "src/examples/multi-double.c")
target_include_directories(multi-double PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(multi-double ${CONAN_LIBS})

add_executable(multi-post "src/examples/multi-post.c")
target_include_directories(multi-post PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(multi-post ${CONAN_LIBS})

add_executable(multi-single "src/examples/multi-single.c")
target_include_directories(multi-single PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(multi-single ${CONAN_LIBS})

add_executable(multi-uv "src/examples/multi-uv.c")
target_include_directories(multi-uv PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(multi-uv ${CONAN_LIBS})

add_executable(multithread "src/examples/multithread.c")
target_include_directories(multithread PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(multithread ${CONAN_LIBS})

add_executable(simple "src/examples/simple.c")
target_include_directories(simple PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(simple ${CONAN_LIBS})

add_executable(simplepost "src/examples/simplepost.c")
target_include_directories(simplepost PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(simplepost ${CONAN_LIBS})

add_executable(simplessl "src/examples/simplessl.c")
target_include_directories(simplessl PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(simplessl ${CONAN_LIBS})

#-- variations
add_executable(multi-download "src/multi-download.cpp")
target_include_directories(multi-download PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(multi-download ${CONAN_LIBS})
