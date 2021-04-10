import unittest
from quality import urlExists

class testurlExists(unittest.TestCase):
    def testFunction(self):
        self.assertEqual(urlExists("https://www.google.ca/"), True)
        self.assertEqual(urlExists("https://www.facebook.com/"), True)
        self.assertEqual(urlExists("https://www.facdkfjdkfdkfjdfebook.com/"), False)
        self.assertEqual(urlExists("https://d35p9e4fm9h3wo.cloudfront.net/latestData.json"), True)
        self.assertEqual(urlExists("https://d35p9e4fmf9h3wo.cloudfront.net/latestData.json"), False)

         
if __name__ == '__main__':
    unittest.main()


    