## Introduction

A small Conan/CMake scaffold project to build a variety of the [curl API Examples] C programs, and a couple of
variations thereof in C++, in order to explore how the [curl multi interface] works.

[curl API Examples]: https://curl.se/libcurl/c/example.html
[curl multi interface]: https://curl.se/libcurl/c/libcurl-multi.html

## Debugging

Diagnose segfaults on MacOS:

```shell
$ lldb --file /path/to/program
...
(lldb) r
Process 89510 launched
...
(lldb) bt
* thread #1, queue = 'com.apple.main-thread', stop reason = EXC_BAD_ACCESS (code=1, address=0x726f00)
  * frame #0: 0x00007fff73856e52 libsystem_platform.dylib`_platform_strlen + 18
...
```