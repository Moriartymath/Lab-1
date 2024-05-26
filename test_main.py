import unittest
import os
from main import IsContainNestedFormating, convertToAnsi,FindTextInRow, read_file, save_to_file, convert_to_html

class TestIsContainNestedFormating(unittest.TestCase):

    def test1(self):
        text = "This is a **_test_** string"
        result = IsContainNestedFormating(text, ['_','`','```'], 12, 17)
        self.assertTrue(result)
       

    def test2(self):
        text = "This is a _**test**_ string"
        result = IsContainNestedFormating(text, ['_','**','```'], 11, 18)
        self.assertTrue(result)

    def test3(self):
        text = "This is a **test** string"
        result = IsContainNestedFormating(text, ['_','**','```'], 12, 15)
        self.assertFalse(result)


class TestConvertToAnsi(unittest.TestCase):

    def test_convertToAnsi(self):
   
        html_text = "<b>bold</b> <i>italic</i> <tt>monospaced</tt> <pre>Preformatted text</pre>"

       
        expected_output = "\033[1mbold\033[0m \033[3mitalic\033[0m \033[2mmonospaced\033[0m \033[4mPreformatted text\033[0m"

       
        actual_output = convertToAnsi(html_text)
        
        self.assertEqual(actual_output, expected_output)


class TestFindTextInRow(unittest.TestCase):

    def test_FindTextInRow(self):
    
        text = "Some text\nwith new line\nand more text\n"

        start_counter_1 = 0
        expected_output_1 = True
        self.assertEqual(FindTextInRow(text, start_counter_1), expected_output_1)

   
        start_counter_2 = 10
        expected_output_2 = True
        self.assertEqual(FindTextInRow(text, start_counter_2), expected_output_2)

        
        start_counter_3 = 15
        expected_output_3 = True
        self.assertEqual(FindTextInRow(text, start_counter_3), expected_output_3)


class TestFileOperations(unittest.TestCase):

    def setUp(self):
      
        self.temp_file_path = "temp_file.txt"
        with open(self.temp_file_path, 'w') as temp_file:
            temp_file.write("Test content")

    def tearDown(self):
      
        os.remove(self.temp_file_path)

    def test_read_file(self):
     
        expected_content = "Test content"
        self.assertEqual(read_file(self.temp_file_path), expected_content)

      
        with self.assertRaises(FileNotFoundError):
            read_file("nonexistent_file.txt")

    def test_save_to_file(self):
  
        content_to_save = "Content to save"
        save_to_file(content_to_save, self.temp_file_path)
        with open(self.temp_file_path, 'r') as temp_file:
            saved_content = temp_file.read()
        self.assertEqual(saved_content, content_to_save)



class TestConverToHTML(unittest.TestCase):

    def test_convert_to_html(self):

        md_text = '**BOLD** _ITALIC_'
        expectedResult = '<p><b>BOLD</b> <i>ITALIC</i></p>'
        result = convert_to_html(md_text)
       
        self.assertEqual(result,expectedResult)

        md_text2 = 'This is my path\n_some_\n**other**'
        expectedResult2 = '<p>This is my path\n<i>some</i>\n<b>other</b></p>'

        result2 = convert_to_html(md_text2);

        self.assertEqual(result2,expectedResult2)
       


if __name__ == '__main__':
    unittest.main()
