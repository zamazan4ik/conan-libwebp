from conans import ConanFile, CMake, tools

class libwebpConan(ConanFile):
    name = 'libwebp'
    version = 'next'
    license = 'AGPL'
    description = 'library to encode and decode images in WebP format'
    url = 'http://developers.google.com/speed/webp'
    settings = 'os', 'compiler', 'build_type', 'arch'
    options = {
        'shared': [True, False]
    }
    default_options = 'shared=False'
    generators = 'cmake'

    def source(self):
        self.run('git clone --depth 1 https://chromium.googlesource.com/webm/libwebp')
        tools.replace_in_file('libwebp/CMakeLists.txt', 'project(libwebp C)', '''project(libwebp C)
            include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
            conan_basic_setup()''')

    def configure(self):
        del self.settings.compiler.libcxx

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_dir='libwebp', build_dir='./')
        cmake.build()

    def package(self):
        self.copy('webp/types.h', dst='include', src='libwebp/src')
        self.copy('webp/decode.h', dst='include', src='libwebp/src')
        self.copy('webp/encode.h', dst='include', src='libwebp/src')
        self.copy('libwebp*.a', dst='lib', src='lib')
        self.copy('webp*.lib', dst='lib', src='lib')
        self.copy('libwebp*.so*', dst='lib')
        self.copy('libwebp*dylib', dst='lib')
        self.copy('*.dll', dst='bin')

    def package_info(self):
        self.cpp_info.libs = ['webp']
