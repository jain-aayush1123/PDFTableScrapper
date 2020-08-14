import pdf_table_scrapper

scrapper = pdf_table_scrapper.PDFTableScrapper()
scrapper.tear_pdf('timetable_2019_draft.pdf')
scrapper.parse_pdf_to_csv(0, 45, 'converted_timetable.csv')
