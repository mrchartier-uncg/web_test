import PyPDF2 as pdf

file_loc = r'C:\Users\mrchartier\Box\Enterprise Administrative Systems - Vendor Release Documentation\Ellucian Product Documentation'


def find_pdf_file(location):
    pass


def pdf_reader(pdf_file):
    """This is to open and extract the text from a pdf file.
    pdf_file = The file that will have the data extracted.
    """
    with open(pdf_file, 'rb') as open_file:
        file = pdf.PdfFileReader(open_file)
        print(pdf_file)
        print(str(file.getDocumentInfo()))
        return file

if __name__ == '__main__':
    file = r'C:\Users\mrchartier\Box\Enterprise Administrative Systems - Vendor Release Documentation\Ellucian Product Documentation\Finance\Finance 8.12 & 9.3.11\Banner_Finance_Upgrade_Guide_8.12_March_2019.pdf'
    pdf = pdf_reader(file)
