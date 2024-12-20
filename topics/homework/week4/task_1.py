# Introduction to OOP
# Write a TestCase class with methods for setup(), run(), and teardown().
# Create objects of the TestCase class to represent individual test cases.

class TestCase:
    def setup(self):
        print("Setting up the test")

    def run(self):
        print("Running login test")

    def teardown(self):
        print("Cleaning up the test")


test_case1 = TestCase()  # TestCase class object creation
test_case2 = TestCase()  # TestCase class object creation
test_case3 = TestCase()  # TestCase class object creation

test_case1.setup()  # Output: Setting up common tasks
test_case1.run()  # Output: Running login test
test_case1.teardown()  # Output: Cleaning up the test

test_case2.setup()  # Output: Setting up common tasks
test_case2.run()  # Output: Running login test
test_case2.teardown()  # Output: Cleaning up the test

test_case3.setup()  # Output: Setting up common tasks
test_case3.run()  # Output: Running login test
test_case3.teardown()  # Output: Cleaning up the test
