# c++ project template

This example shows how the google naming convetion
and use of google test

[Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html#Header_Files)

# Using google test

get googletest from your favorite package maneger or build it from source

## build google test from source 

``` bash
git clone https://github.com/google/googletest.git -b release-1.11.0
cd googletest        # Main directory of the cloned repository.
mkdir build          # Create a directory to hold the build output.
cd build
cmake ..             # Generate native build scripts for GoogleTest.
make
```

## Building and test examples

``` bash
cd path/to/repo-template/examples/cpp
mkdir build
cd build
cmake ..
make
ctest
```

## learn more about googletest
[GoogleTest User’s Guide](https://google.github.io/googletest/)
