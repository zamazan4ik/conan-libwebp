[![badge](https://img.shields.io/badge/conan.io-libwebp%2Fnext-green.svg?logo=data:image/png)](http://www.conan.io/source/libwebp/next/nunojpg/ci)
[![Build Status](https://travis-ci.org/nunojpg/conan-libwebp.svg?branch=master)](https://travis-ci.org/nunojpg/conan-libwebp)
[![Build status](https://ci.appveyor.com/api/projects/status/id8h0aq9myiqjt7o/branch/master?svg=true)](https://ci.appveyor.com/project/nunojpg/conan-libwebp/branch/master)

# conan-libwebp

## Reuse the packages

### Basic setup

    $ conan install libwebp/next@nunojpg/ci
    
### Project setup

If you handle multiple dependencies in your project is better to add a *conanfile.txt*
    
    [requires]
    libwebp/next@nunojpg/ci

    [options]
    #libwebp:shared=true # default is false
    
    [generators]
    txt
    cmake

Complete the installation of requirements for your project running:</small></span>

    conan install .

Project setup installs the library (and all his dependencies) and generates the files *conanbuildinfo.txt* and *conanbuildinfo.cmake* with all the paths and variables that you need to link with your dependencies.
