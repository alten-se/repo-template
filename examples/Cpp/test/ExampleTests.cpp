#include <gtest/gtest.h>
#include "Example"

TEST(ExampleTests, DemonstrateGTestMacros)

{
    EXPECT_EQ(true, true);
    const bool result = f();
    EXPECT_EQ(true, result)<< "Hello world";


}

TEST(ExampleTests, DemonstrateGTestMacros2)

{
    EXPECT_EQ(true, false);
    const bool result = f();
    EXPECT_EQ(true, result)<< "Hello world";


}

TEST(ExampleTests, DemonstrateGTestMacros3)

{
    EXPECT_EQ(true, true);
    const bool result = f();
    EXPECT_EQ(true, result)<< "Hello world";


}

