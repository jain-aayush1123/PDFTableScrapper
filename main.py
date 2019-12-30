import pdf_table_scrapper

scrapper = pdf_table_scrapper.PDFTableScrapper()
scrapper.tear_pdf('timetable.pdf')
scrapper.parse_pdf_to_csv(6, 59, 'converted_timetable.csv')
