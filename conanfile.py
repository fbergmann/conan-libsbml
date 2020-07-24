#!/usr/bin/env python
# -*- coding: utf-8 -*-
from conans import ConanFile, tools, CMake


class LibSBMLConan(ConanFile):

    name = "libsbml"
    version = "5.18.1"
    url = "http://github.com/fbergmann/conan-libsbml"
    homepage = "https://sbml.org"
    author = "SBML Team"
    license = "LGPL"

    description = ("LibSBML is a library for reading, writing and "
                   "manipulating the Systems Biology Markup Language "
                   "(SBML).  It is written in ISO C and C++, supports "
                   "SBML Levels 1, 2 and 3, and runs on Linux, Microsoft "
                   "Windows, and Apple MacOS X.  For more information "
                   "about SBML, please see http://sbml.org.")

    settings = "os", "arch", "compiler", "build_type"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "comp": [True, False],
        "fbc": [True, False],
        "groups": [True, False],
        "layout": [True, False],
        "multi": [True, False],
        "qual": [True, False],
        "render": [True, False],
        "cpp_namespaces": [True, False]
    }

    default_options = (
        "shared=False",
        "fPIC=True",
        "comp=True",
        "fbc=True",
        "groups=True",
        "layout=True",
        "multi=True",
        "qual=True",
        "render=True",
        "cpp_namespaces=False"
    )

    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

        self.requires("bzip2/1.0.8@conan/stable")
        self.options['bzip2'].shared = self.options.shared
        self.requires("zlib/1.2.11@conan/stable")
        self.options['zlib'].shared = self.options.shared
        self.requires("Expat/2.2.7@pix4d/stable")
        self.options['Expat'].shared = self.options.shared

        if self.settings.compiler == 'Visual Studio' and 'MT' in self.settings.compiler.runtime:
            self.options['Expat'].static_crt = True

    def source(self):
        git = tools.Git("src")
        git.clone("https://github.com/sbmlteam/libsbml")
        
        tools.replace_in_file('src/CMakeLists.txt', "project(libsbml)", '''project(libsbml)

include(${CMAKE_BINARY_DIR}/../conanbuildinfo.cmake)
conan_basic_setup()''')

    def _configure(self, cmake):
        args = ['-DWITH_LIBXML=OFF', '-DWITH_EXPAT=ON']
        if self.options.comp:
            args.append('-DENABLE_COMP=ON')
        if self.options.fbc:
            args.append('-DENABLE_FBC=ON')
        if self.options.groups:
            args.append('-DENABLE_GROUPS=ON')
        if self.options.layout:
            args.append('-DENABLE_LAYOUT=ON')
        if self.options.multi:
            args.append('-DENABLE_MULTI=ON')
        if self.options.qual:
            args.append('-DENABLE_QUAL=ON')
        if self.options.render:
            args.append('-DENABLE_RENDER=ON')
        if self.options.cpp_namespaces:
            args.append('-DWITH_CPP_NAMESPACE=ON')
        if self.settings.compiler == 'Visual Studio' and 'MT' in self.settings.compiler.runtime:
            args.append('-DWITH_STATIC_RUNTIME=ON')
        if not self.options.shared:
            args.append('-DLIBSBML_SKIP_SHARED_LIBRARY=ON')
        else: 
            args.append('-DLIBSBML_SKIP_STATIC_LIBRARY=ON')

        cmake.configure(build_folder="build", args=args, source_folder="src")

    def build(self):
        cmake = CMake(self)
        self._configure(cmake)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        self._configure(cmake)
        cmake.install()
        cmake.patch_config_paths()
        self.copy("*.lib", dst="lib", keep_path=False)
        if self.options.shared: 
          if self.settings.os == "Windows":
              self.copy("*.dll", dst="bin", keep_path=False)
          self.copy("*.so", dst="lib", keep_path=False)
          self.copy("*.dylib", dst="lib", keep_path=False)
        else:
          self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):

        libfile = "libsbml"

        if not self.settings.os == "Windows":
            if self.options.shared:
                if self.settings.os == "Linux":
                    libfile += ".so"
                if self.settings.os == "Macos":
                    libfile += ".dylib"
            else:
                libfile += "-static.a"
        else:
            if self.options.shared:
                libfile += ".dll"
            else:
                libfile += "-static.lib"

        self.cpp_info.libs = [libfile]

        if not self.options.shared:
            self.cpp_info.defines = ["LIBSBML_STATIC", "LIBLAX_STATIC"]
