cmake_minimum_required(VERSION 3.25.0)

set(This ExampleTests)

set(Sources 
    ExampleTests.cpp
)

add_executable(Example Example.cpp)
target_link_libraries(${This} PUBLIC
    gtest_main
   
)


add_test(
    NAME ${This}
    COMMAND ${This}
)