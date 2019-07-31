
## Conan package recipe for [*libSBML*](https://sbml.org)



## Issues
All conan specific issues should be tracked in this projects 

issue tracker

To report possible libSBML bugs or other issues:

* [libSBML issue tracker](http://sbml.org/Software/libSBML/issue-tracker)

To ask questions:

* [sbml-interoperability](https://groups.google.com/forum/#!forum/sbml-interoperability) is where people discuss development, use, and interoperability of software that supports SBML. LibSBML questions and other topics are perfectly acceptable here.

* [libsbml-development](https://groups.google.com/forum/#!forum/libsbml-development) is for more technical discussions about libSBML, including requests for new facilities and features, questions about the internals of libSBML, and discussions about ongoing development of libSBML.

To contact the libSBML Team directly:

libsbml-team(at)caltech.edu

## For Users

### Basic setup

    $ conan install libsbml/5.18.1@fbergmann/stable

### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*

    [requires]
    libsbml/5.18.1@fbergmann/stable

    [generators]
    cmake

Complete the installation of requirements for your project running:

    $ mkdir build && cd build && conan install ..

Note: It is recommended that you run conan install from a build directory and not the root of the project directory.  This is because conan generates *conanbuildinfo* files specific to a single build configuration which by default comes from an autodetected default profile located in ~/.conan/profiles/default .  If you pass different build configuration options to conan install, it will generate different *conanbuildinfo* files.  Thus, they should not be added to the root of the project, nor committed to git.


## Build and package

The following command both runs all the steps of the conan file, and publishes the package to the local system cache.  This includes downloading dependencies from "build_requires" and "requires" , and then running the build() method.

    $ conan create . conan/stable


### Available Options

| Option        | Default | Possible Values  |
| ------------- |:----------------- |:------------:|
| shared      | False |  [True, False] |
| fPIC      | True |  [True, False] |
|comp| True| [True, False] |
|fbc| True| [True, False] |
|groups| True| [True, False] |
|layout| True| [True, False] |
|multi| True| [True, False] |
|qual| True| [True, False] |
|render| True| [True, False] |
|cpp_namespaces| False| [True, False] | 
              
## Add Remote

You might need to add the Conan Center repo before installing the package:

    $ conan remote add conan-center "https://conan.bintray.com"


## Conan Recipe License

NOTE: The conan recipe license applies only to the files of this recipe, which can be used to build and package zlib.
It does *not* in any way apply or is related to the actual software being packaged.

[MIT](LICENSE)
