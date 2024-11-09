# -*- coding: utf-8 -*-
"""
ICTPRG443 Assessment 3

Created on Mon Oct 21 18:03:27 2024

@author: Bailey Byl 20135558
"""


import unittest
import os
import PyPDF2 as pdf

from PDF_manager import merge_pdf_files, rotate_pdf_page, encrypt_pdf_file, decrypt_pdf_file


class TestPdfManagerFunctions(unittest.TestCase):
    
    def compare_pdfs(self, pdf1, pdf2):
        pdf_reader_1 = pdf.PdfFileReader(pdf1)
        pdf_reader_2 = pdf.PdfFileReader(pdf2)

        self.assertEqual(pdf_reader_1.getNumPages(), pdf_reader_2.getNumPages())

        for i in range(pdf_reader_1.getNumPages()):
            page1 = pdf_reader_1.getPage(i)
            page2 = pdf_reader_2.getPage(i)

            self.assertEqual(page1.extract_text(), page2.extract_text())
            
    
    def test_merge_pdf(self):
        path = os.path.join(os.path.dirname(__file__), 'TestFiles/')
        save_path = os.path.join(os.path.dirname(__file__), 'TestFiles/test_merged.pdf')
        pdf_files = ['test_pdf1.pdf', 'test_pdf2.pdf']
        reference_path = os.path.join(os.path.dirname(__file__), 'TestFiles/reference_merged.pdf')
        
        merge_pdf_files(path, pdf_files, save_path)
        
        self.compare_pdfs(save_path, reference_path)
        
        
    def test_rotate_pdf(self):
        path = os.path.join(os.path.dirname(__file__), 'TestFiles/test_pdf1.pdf')
        page = 0
        save_path = os.path.join(os.path.dirname(__file__), 'TestFiles/test_rotated.pdf')
        reference_path = os.path.join(os.path.dirname(__file__), 'TestFiles/reference_rotatedPage.pdf')
        
        rotate_pdf_page(path, page, save_path)
        
        self.compare_pdfs(save_path, reference_path)
        
        
    def test_encrypt_pdf(self):
        path = os.path.join(os.path.dirname(__file__), 'TestFiles/test_pdf1.pdf')
        password = 'password123'
        save_path = os.path.join(os.path.dirname(__file__), 'TestFiles/test_encrypted.pdf')
        
        encrypt_pdf_file(path, password, save_path)
        
        pdf_reader = pdf.PdfFileReader(open(save_path, 'rb'))
        
        self.assertTrue(pdf_reader.isEncrypted)
    
    def test_decyrpt_pdf(self):
        path = os.path.join(os.path.dirname(__file__), 'TestFiles/test_encrypted.pdf')
        password = 'password123'
        save_path = os.path.join(os.path.dirname(__file__), 'TestFiles/test_decrypted.pdf')
        
        decrypt_pdf_file(path, password, save_path)
        
        pdf_reader = pdf.PdfFileReader(open(save_path, 'rb'))
        
        self.assertFalse(pdf_reader.isEncrypted)
        


if __name__ == '__main__':
    unittest.main()
    
