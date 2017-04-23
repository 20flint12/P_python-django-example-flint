
import unittest

# import examples.test_facebook.routines_fb as fb
import test_facebook.routines_fb as fb


class TestStringMethods(unittest.TestCase):

    # def test_simple(self):
    #     self.assertEqual(remove_unused_parentheses('esdfd((esdf)(esdf'), 'esdfd((esdf)')
    #     self.assertEqual(remove_unused_parentheses('esdfd((esdf)(es)df'), 'esdfd((esdf)(es)df')
    #
    # def test_regex(self):
    #     self.assertEqual(remove_unused_parentheses_regex('esdfd((esdf)(esdf'), 'esdfd((esdf)')
    #     self.assertEqual(remove_unused_parentheses_regex('esdfd((esdf)(efgdsfgsdf'), 'esdfd((esdf)')

    def test_simple(self):

        fb.main_routine('examples/test_facebook/data_fb.csv')
        pass


# fb.main_routine('examples/test_facebook/data_fb.csv')

if __name__ == '__main__':
    unittest.main()