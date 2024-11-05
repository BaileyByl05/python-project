# -*- coding: utf-8 -*-
"""
ICTPRG443 Assessment 3

Created on Mon Oct 21 18:02:42 2024

@author: Bailey Byl 20135558
"""

import PyPDF2 as pdf

# Merge 2 PDFs into one
def merge_pdf_files(path, pdf_files, save_path):
    merger = pdf.PdfFileMerger()
    for files in pdf_files:
        merger.append(path+files)
    merger.write(save_path)
    merger.close()

# Rotate a page from an existing PDF and save it as a new PDF
def rotate_pdf_page(path, page, save_path):
    file = open(path, 'rb')
    pdf_reader = pdf.PdfFileReader(file)
    pdf_page = pdf_reader.getPage(page)
    pdf_page.rotateClockwise(90)
    pdf_writer = pdf.PdfFileWriter()
    pdf_writer.addPage(pdf_page)
    result_pdf_file = open(save_path, 'wb')
    pdf_writer.write(result_pdf_file)
    result_pdf_file.close()
    file.close()
    
# Encrypt a PDF using a password
def encrypt_pdf_file(path, password, save_path):
    file = open(path, 'rb')
    pdf_reader = pdf.PdfFileReader(file)
    pdf_writer = pdf.PdfFileWriter()
    
    for pageNum in range(pdf_reader.numPages):
        pdf_writer.addPage(pdf_reader.getPage(pageNum))
        
    pdf_writer.encrypt(password)
    result_pdf = open(save_path, 'wb')
    pdf_writer.write(result_pdf)
    result_pdf.close()
    
# Decrypt a PDF using a password
def decrypt_pdf_file(path, password, save_path):
    pdf_reader = pdf.PdfFileReader(open(path, 'rb'))
    pdf_writer = pdf.PdfFileWriter()
    if pdf_reader.isEncrypted:
        try:
            pdf_reader.decrypt(password)
            for pageNum in range(pdf_reader.numPages):
                pdf_writer.addPage(pdf_reader.getPage(pageNum))
            result_pdf = open(save_path, 'wb')
            pdf_writer.write(result_pdf)
            result_pdf.close()
            return True
        except:
            return False
    else:
        return -1
    


def main():
    print('PDF Manager Program by Bailey Byl')
    
    while True:
        print('''Options:
        M - Merge two PDFs
        R - Create a new PDF which contains a rotated page from an existing PDF
        E - Encrypt a PDF
        D - Decrypt a PDF
        ENTER to exit''')

        option = input('Select option: ')
        
        # Merge PDFs
        if option == 'M' or option == 'm':
            path = input('Enter path to the folder containing the two PDFs: ')
            pdf_files = []
            pdf_files.append(input('Enter name of first PDF: '))
            pdf_files.append(input('Enter name of second PDF: '))
            save_path = input('Enter save path: ')
            
            try:
                merge_pdf_files(path, pdf_files, save_path)
                print('PDFs merged')
            except:
                 print('Error merging PDFs')
        
        # Rotate a PDF page
        elif option == 'R' or option == 'r':
            path = input('Enter PDF path: ')
            page = int(input('Enter the page to rotate: '))
            save_path = input('Enter save path: ')
            
            try:
                rotate_pdf_page(path, page, save_path)
                print('PDF page rotated')
            except:
                print('Error rotating PDF page')
        
        # Encrypt a PDF
        elif option == 'E' or option == 'e':
            path = input('Enter PDF path: ') 
            password = input('Enter password: ')
            save_path = input('Enter save path: ')
            
            try:
                encrypt_pdf_file(path, password, save_path)
                print('PDF encrypted')
            except:
                print('Error encrypting PDF')
        
        # Decrypt a PDF
        elif option == 'D' or option == 'd':
            path = input('Enter PDF path: ') 
            password = input('Enter password: ')
            save_path = input('Enter save path: ')
            
            try:
                decrypt_pdf_file(path, password, save_path)
                print('PDF decrypted')
            except:
                print('Error decrypting PDF')

        elif option == '':
            return

        else:
            print('Invalid input')



if __name__ == '__main__':
    main()
