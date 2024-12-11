# Introduction to OOP
# Implement method overriding in a test automation context.
# Override a method in the child test class to customize the test execution.

class TestCase:
    def setup(self):
        print("Setting up the test")

    def run(self):
        print("Running login test")

    def teardown(self):
        print("Cleaning up the test")


class CustomTestCase(TestCase):
    def run(self):
        print("Customized test execution")


test_case1 = CustomTestCase()  # CustomTestCase class object creation
test_case2 = CustomTestCase()  # CustomTestCase class object creation

test_case1.setup()
test_case1.run()
test_case1.teardown()

test_case2.setup()
test_case2.run()
test_case2.teardown()
