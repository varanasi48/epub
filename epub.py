import os
import shutil
from PyPDF2 import PdfReader
from ebooklib import epub

def convert_pdf_to_text(pdf_path):
    reader = PdfReader(pdf_path)
    pages = [page.extract_text() or "" for page in reader.pages]
    return pages

def create_html_page(text, page_id):
    html_template = f'''<?xml version="1.0" encoding="utf-8"?>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head><title>{page_id}</title></head>
  <body><p>{text.replace('\n', '<br/>')}</p></body>
</html>'''
    return html_template

def build_epub_from_pdf(pdf_path, output_epub, title="Untitled Book", author="Unknown"):
    texts = convert_pdf_to_text(pdf_path)

    book = epub.EpubBook()
    book.set_identifier("id123456")
    book.set_title(title)
    book.set_language("en")
    book.add_author(author)

    spine = ['nav']
    toc = []

    for idx, text in enumerate(texts):
        page_id = f'page{idx+1:03}'
        html_content = create_html_page(text, page_id)
        item = epub.EpubHtml(title=page_id, file_name=f'{page_id}.xhtml', content=html_content)
        book.add_item(item)
        spine.append(item)
        toc.append(item)

    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    book.spine = spine
    book.toc = toc

    epub.write_epub(output_epub, book)

# Example usage:
build_epub_from_pdf("X05545.pdf", "mybook.epub", title="My Book", author="John Doe")
