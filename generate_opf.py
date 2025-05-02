import os
import json
from datetime import datetime

def generate_opf():
    # Read fonts data
    with open(r'd:\epubpdf\fonts.json', 'r', encoding='utf-8') as f:
        fonts_data = json.load(f)

    # Get HTML files
    html_dir = r'd:\epubpdf\html'
    html_files = []
    for root, dirs, files in os.walk(html_dir):
        for file in files:
            if file.endswith('.html'):
                rel_path = os.path.relpath(os.path.join(root, file), r'd:\epubpdf')
                page_id = os.path.splitext(file)[0]
                html_files.append((page_id, rel_path.replace('\\', '/')))

    # Get CSS files
    css_dir = r'd:\epubpdf\css'
    css_files = []
    for file in os.listdir(css_dir):
        if file.endswith('.css'):
            css_id = os.path.splitext(file)[0]
            css_files.append((css_id, f"css/{file}"))

    # Generate OPF content
    opf_content = '''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" xml:lang="en" unique-identifier="epub978-1-4108-6040-8" prefix="rendition: http://www.idpf.org/vocab/rendition/#">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
    <dc:title>Book Title</dc:title>
    <dc:identifier id="epub978-1-4108-6040-8">978-1-4108-6040-8</dc:identifier>
    <dc:language>en-US</dc:language>
    <dc:creator>Author Name</dc:creator>
    <dc:publisher>Publisher Name</dc:publisher>
    <dc:rights>© Publisher Name</dc:rights>
    <meta name="cover" content="cover-image" />
    <meta property="rendition:layout">pre-paginated</meta>
    <meta property="rendition:orientation">landscape</meta>
    <meta property="rendition:spread">both</meta>
    <meta property="media:active-class">-epub-media-overlay-active</meta>
    <meta property="dcterms:modified">{datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")}</meta>
</metadata>

<manifest>
    <!-- Navigation -->
    <item id="toc1" href="html/nav.xhtml" properties="nav" media-type="application/xhtml+xml"/>
    
    <!-- HTML Pages -->'''

    # Add HTML items
    for page_id, page_path in html_files:
        opf_content += f'''
    <item id="{page_id}" href="{page_path}" media-type="application/xhtml+xml"/>'''

    # Add CSS items
    opf_content += '''
    
    <!-- CSS Files -->'''
    for css_id, css_path in css_files:
        opf_content += f'''
    <item id="{css_id}" href="{css_path}" media-type="text/css"/>'''

    # Add Font items
    opf_content += '''
    
    <!-- Fonts -->'''
    for font_name in fonts_data:
        clean_name = font_name.split('+')[1] if '+' in font_name else font_name
        font_id = clean_name.lower().replace(' ', '_').replace('-', '_')
        opf_content += f'''
    <item id="{font_id}" href="fonts/{clean_name}.otf" media-type="application/vnd.ms-opentype"/>'''

    # Add Images
    opf_content += '''
    
    <!-- Images -->
    <item id="cover-image" href="images/cover.jpg" media-type="image/jpeg"/>'''

    # Close manifest and add spine
    opf_content += '''
</manifest>

<spine>'''

    # Add spine items
    for page_id, _ in html_files:
        opf_content += f'''
    <itemref idref="{page_id}"/>'''

    opf_content += '''
</spine>
</package>'''

    # Write the OPF file
    with open(r'd:\epubpdf\content.opf', 'w', encoding='utf-8') as f:
        f.write(opf_content)

if __name__ == "__main__":
    generate_opf()