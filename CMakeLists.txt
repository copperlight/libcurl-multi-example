cmake_minimum_required(VERSION 3.23)

project(libcurl-multi-example)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)
set(CMAKE_CXX_EXTENSIONS OFF)
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

find_package(CURL REQUIRED)
find_package(libuv REQUIRED)
find_package(libxml2 REQUIRED)

add_compile_options(-pedantic -Werror -Wall -Wno-missing-braces -fno-omit-frame-pointer "$<$<CONFIG:Debug>:-fsanitize=address>")

include(CTest)

#-- examples
add_executable(10-at-a-time "src/examples/10-at-a-time.c")
target_link_libraries(10-at-a-time CURL::libcurl)

add_executable(chkspeed "src/examples/chkspeed.c")
target_link_libraries(chkspeed CURL::libcurl)

add_executable(crawler "src/examples/crawler.c")
target_link_libraries(crawler CURL::libcurl LibXml2::LibXml2)

add_executable(debug "src/examples/debug.c")
target_link_libraries(debug CURL::libcurl)

add_executable(http-post "src/examples/http-post.c")
target_link_libraries(http-post CURL::libcurl)

add_executable(multi-app "src/examples/multi-app.cpp")
target_link_libraries(multi-app CURL::libcurl)

add_executable(multi-debugcallback "src/examples/multi-debugcallback.c")
target_link_libraries(multi-debugcallback CURL::libcurl)

add_executable(multi-double "src/examples/multi-double.c")
target_link_libraries(multi-double CURL::libcurl)

add_executable(multi-post "src/examples/multi-post.c")
target_link_libraries(multi-post CURL::libcurl)

add_executable(multi-single "src/examples/multi-single.c")
target_link_libraries(multi-single CURL::libcurl)

add_executable(multi-uv "src/examples/multi-uv.c")
target_link_libraries(multi-uv CURL::libcurl uv)

add_executable(multithread "src/examples/multithread.c")
target_link_libraries(multithread CURL::libcurl)

add_executable(simple "src/examples/simple.c")
target_link_libraries(simple CURL::libcurl)

add_executable(simplepost "src/examples/simplepost.c")
target_link_libraries(simplepost CURL::libcurl)

add_executable(simplessl "src/examples/simplessl.c")
target_link_libraries(simplessl CURL::libcurl)

#-- variations
add_executable(multi-download "src/multi-download.cpp")
target_link_libraries(multi-download CURL::libcurl)
