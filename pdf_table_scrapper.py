import tabula
import pandas
import os
import PyPDF2


class PDFTableScrapper:
    def __init__(self):
        super().__init__()

    def tear_pdf(self, pdf_name):
        # tear the pdf into individual pages
        pdf_file = open(pdf_name, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        for page in range(number_of_pages):
            p = read_pdf.getPage(page)
            write_file = PyPDF2.PdfFileWriter()
            write_file.addPage(p)

            output = 'Pages/%02d.pdf' % page
            with open(output, 'wb') as f:
                write_file.write(f)

    def parse_pdf_to_csv(self, starting_page, ending_page, output_file):
        # parse data
        split_pdf_files = os.listdir("Pages")
        split_pdf_files.sort()
        for file in split_pdf_files:
            page_no = int(file.split('.')[0])
            if(page_no >= starting_page and page_no <= ending_page):
                data = tabula.read_pdf(
                    'Pages/' + file,
                    pandas_options={
                        'header': 0,
                        'keep_default_na': False,
                        'skiprows': [0],
                        # 'usecols': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
                        'usecols': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

                    }
                )
                csv_file = open(output_file, 'a')
                data.to_csv(csv_file, index=None)
                print("done: " + str(page_no))
