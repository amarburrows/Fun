
import unittest
from main import *
class FunTests(unittest.TestCase):




    def test_books(self):
        books = [Book('harry potter and the sorcerers stone', 'jk rowling'),
                 Book('pride and prejudice', 'jane austen'),
                 Book('harry potter and the prisoner of azkaban', 'jk rowling')]
        expected = [
            Book('harry potter and the prisoner of azkaban', 'jk rowling'),
            Book('harry potter and the sorcerers stone', 'jk rowling'),
            Book('pride and prejudice', 'jane austen')]
        self.assertEqual(selection_sort_books(books), expected)

    def test_books_2(self):
        books = [Book('naur', 'me'),
                 Book('bruhoof', 'you'),
                 Book('whatever man', 'everyone')]
        expected = [Book('bruhoof', 'you'),
                 Book('naur', 'me'),
                 Book('whatever man', 'everyone')]
        self.assertEqual(selection_sort_books(books), expected)

    def test_swap(self):
        original = 'AHHHH'
        expected = 'ahhhh'
        self.assertEqual(swap_case(original), expected)

    def test_swap_2(self):
        original = 'AmAr iS CoOl'
        expected = 'aMaRIscOoL'
        self.assertEqual(swap_case(original), expected)

    def test_translate(self):
        og = ('amar')
        letter_1 = 'a'
        letter_2 = 'o'
        expected = 'omor'
        self.assertEqual(str_translate(og, letter_1, letter_2), expected)

    def test_translate_2(self):
        og = ('oooohhhh nooooo')
        letter_1 = 'o'
        letter_2 = 'e'
        expected = 'eeeehhhh neeeee'
        self.assertEqual(str_translate(og, letter_1, letter_2), expected)