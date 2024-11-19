## Introduction

A small Conan/CMake scaffold project to build a variety of the [curl API Examples] C programs, and a couple of
variations thereof in C++, in order to explore how the [curl multi interface] works.

[curl API Examples]: https://curl.se/libcurl/c/example.html
[curl multi interface]: https://curl.se/libcurl/c/libcurl-multi.html

## Local Development

```shell
# install necessary build tools
brew install cmake

# setup python venv and activate, to gain access to conan cli
./setup-venv.sh
source venv/bin/activate

./build.sh  # [clean|clean --confirm|skiptest]

# run the examples
./cmake-build/bin/10-at-a-time
./cmake-build/bin/crawler
```
