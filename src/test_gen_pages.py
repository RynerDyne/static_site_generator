import unittest

from generate_pages import extract_title

class TestGenPages(unittest.TestCase):
    def test_extract_title(self):
        header = """
        ## This is a header

        # Title

        # not title
        """
        self.assertEqual(extract_title(header),
                         'Title')

    def test_extract_no_title(self):
        no_header = """
        ## This is a header

        ## Title

         not title
        """
        self.assertRaises(Exception, extract_title, no_header)
