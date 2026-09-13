#!/usr/bin/env python3

import contextlib
import io
import unittest

from src.multiplication_table import main


class MultiplicationTable(unittest.TestCase):

    def test_lines(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main()
        result = buf.getvalue().strip().split("\n")
        self.assertEqual(
            len(result), 10,
            msg="The output should contain ten lines (one per row of the "
                "table)! Got %d line(s)." % len(result))

    def test_content(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            main()
        result = buf.getvalue().strip().split("\n")
        for i, line in enumerate(result):
            j = i + 1
            numbers = list(map(int, line.split()))
            self.assertEqual(
                numbers, list(range(j, 11 * j, j)),
                msg="Row %d should be the multiples of %d from %d to %d. "
                    "Got %r." % (i, j, j, 10 * j, numbers))


if __name__ == '__main__':
    unittest.main()
