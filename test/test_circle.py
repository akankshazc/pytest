import pytest

import source.shapes as shapes
import math


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        # for every test the following circle object will be created
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")
        # not necessary but can be used to clean up after each test
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected
