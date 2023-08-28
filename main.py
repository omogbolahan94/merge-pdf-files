import PyPDF2


def merge_files(pdf1, pdf2):
    # Create a PdfFileReader object for each file
    pdf_reader1 = PyPDF2.PdfReader(pdf1)
    pdf_reader2 = PyPDF2.PdfReader(pdf2)

    # Create a new PdfFileWriter object
    pdf_writer = PyPDF2.PdfWriter()

    # Add the pages of the first PDF to the new PDF
    for page in range(len(pdf_reader1.pages)):
        pdf_writer.add_page(pdf_reader1.pages[page])

    # Add the pages of the second PDF to the new PDF
    for page in range(len(pdf_reader2.pages)):
        pdf_writer.add_page(pdf_reader2.pages[page])

    # Save the merged PDF to a file
    output_pdf = open('merged.pdf', 'wb')
    pdf_writer.write(output_pdf)

    # Close all the open files
    output_pdf.close()
    pdf1.close()
    pdf2.close()
