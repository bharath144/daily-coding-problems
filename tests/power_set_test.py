import unittest

from easy.power_set import power_set


class TestPowerSet(unittest.TestCase):
    def test_power_set_empty(self):
        self.assertEquals(len(power_set([])), 1, "Power set for '[]' should be 1")

    def test_power_set_single(self):
        self.assertEquals(len(power_set([1])), 2, "Power set for '[1]' should be 2")

    def test_power_set_many(self):
        input1 = [1, 2, 3]
        len1 = int(pow(2, len(input1)))
        self.assertEquals(
            len(power_set(input1)), len1, f"Power set for {input1} must be {len1} long"
        )
