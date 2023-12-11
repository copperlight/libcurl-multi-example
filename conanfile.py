from conans import ConanFile


class SpectatorDConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    requires = (
        "libcurl/8.4.0",
        "libuv/1.47.0",
        "libxml2/2.12.2",
    )
    generators = "cmake"
    default_options = {}

    def configure(self):
        self.options["libcurl"].with_c_ares = True
