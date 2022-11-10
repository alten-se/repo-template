#include "../Example.hpp"

#include <gtest/gtest.h>

TEST(ExampleTests, EMacTest   )//multiply and accumulate test 

{
int x = 42;
int y = 16;
int sum = 100; 
int oldsum = sum; 
int expectedNewSum = oldsum + x*y; 
EXPECT_EQ(
    expectedNewSum,
    MAC(x,y,sum)
);
EXPECT_EQ(
    expectedNewSum,
    sum
);

}



