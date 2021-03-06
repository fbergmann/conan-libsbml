from conans import ConanFile, CMake
import os

class LibsbmlTestConan(ConanFile):
    settings = "os", "compiler", "arch", "build_type"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        self.run(os.path.join("bin", "libsbml_info"), run_environment=True)
        self.run(os.path.join("bin", "createExampleSBML"), run_environment=True)
        self.run(os.path.join("bin", "printSBML") + " enzymaticreaction.xml", run_environment=True)
        self.run(os.path.join("bin", "printSBML") + " units.xml", run_environment=True)
        self.run(os.path.join("bin", "printSBML") + " functiondef.xml", run_environment=True)
