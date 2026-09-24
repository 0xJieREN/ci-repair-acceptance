import unittest

from calc.report import summary


class ReportTests(unittest.TestCase):
    def test_interval_summary(self):
        # Slug input is already lowercase: this job depends only on inclusive_sum.
        self.assertEqual(summary("totals", 1, 4), "totals: 10")
