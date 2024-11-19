from conan import ConanFile


class SpectatorDConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = (
        "libcurl/8.10.1",
        "libuv/1.49.2",
        "libxml2/2.13.4",
    )
    tool_requires = ()
    generators = "CMakeDeps", "CMakeToolchain"

    def configure(self):
        self.options["libcurl"].with_c_ares = True
        self.options["libcurl"].with_ssl = "openssl"
