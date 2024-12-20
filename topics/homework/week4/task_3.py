# Introduction to OOP
"""Create a multiple inheritance example:
Write a class that inherits from multiple parent classes (e.g., BaseTest and a custom mixin class),
and check how MRO impacts method calls."""


class BaseTest:
    def run(self):
        print("Running the base test")


class CustomMixin:
    def run(self):
        print("Running the custom mixin")

    def teardown(self):
        print("Cleaning up the test")


class MultipleInheritanceTest(CustomMixin, BaseTest):
    pass


test = MultipleInheritanceTest()
test.run()

print(MultipleInheritanceTest.mro())
