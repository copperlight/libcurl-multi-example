
## Example Listing

This is a curated set of examples from the [libcurl examples] page, intended to highlight the multi interface and how
that contrasts with basic usage.

[libcurl examples]: https://curl.se/libcurl/c/example.html

| Filename            | Description                                                                                                           |
|---------------------|-----------------------------------------------------------------------------------------------------------------------|
| 10-at-a-time        | Download many files in parallel, in the same thread.                                                                  |
| chkspeed            | Show transfer timing info after download completes.                                                                   |
| crawler             | Web crawler based on curl and libxml2 to stress-test curl with hundreds of concurrent connections to various servers. |
| debug               | Show how CURLOPT_DEBUGFUNCTION can be used.                                                                           |
| http-post           | simple HTTP POST using the easy interface.                                                                            |
| multi-app           | A basic application source code using the multi interface doing two transfers in parallel.                            |
| multi-debugcallback | multi interface and debug callback                                                                                    |
| multi-double        | multi interface code doing two parallel HTTP transfers                                                                |
| multi-post          | using the multi interface to do a multipart formpost without blocking                                                 |
| multi-single        | using the multi interface to do a single download                                                                     |
| multi-uv            | multi_socket API using libuv                                                                                          |
| multithread         | A multi-threaded program using pthreads to fetch several files at once                                                |
| simple              | Very simple HTTP GET                                                                                                  |
| simplepost          | Very simple HTTP POST                                                                                                 |
| simplessl           | Shows HTTPS usage with client certs and optional ssl engine use.                                                      |

## Observed Issues

* chkspeed
  * You need to provide your own URL which hosts the files of the specified sizes.
* http-post
  * The URL provided does not resolve.
  * Swap to http://httpbin.org/post.
* multi-app
  * The program hangs. Suspect ftp is the issue.
* multi-double
  * Only one download is printed to the screen.
* multi-single
  * Hangs for about 1 second after receiving the page.
* multi-uv
  * CLion does not find the uv library, despite the Conan requirement and compilation succeeding.
  * Nothing happens.
* multithread
  * Two of four threads appear to complete successfully, then it hangs.
* simplepost
  * The URL provided resolves, but the response is does not seem to show anything about the form.
  * Swap to http://httpbin.org/post.
* simplessl
  * Several things need to be done for this to work, including client certificates and your own URL.
