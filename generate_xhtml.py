import os

def create_xhtml_pages(images_dir):
    # Create output directories
    output_base = os.path.join(os.path.dirname(images_dir), 'html')
    os.makedirs(output_base, exist_ok=True)
    
    # Get list of images
    image_files = [f for f in os.listdir(images_dir) if f.endswith('.jpg')]
    
    for image_file in sorted(image_files):
        page_num = image_file.split('_')[1].split('.')[0]
        page_id = f'page{page_num.zfill(3)}'
        
        # Create page directory
        page_dir = os.path.join(output_base, page_id)
        os.makedirs(page_dir, exist_ok=True)
        
        # Generate XHTML content
        xhtml_content = f'''<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:ibooks="http://apple.com/ibooks/html-extensions" xmlns:epub="http://www.idpf.org/2007/ops">
<head>
<meta name="viewport" content="width=724, height=660" />
<title>page {page_num}</title>
<link rel="stylesheet" type="text/css" href="../../css/css_{page_id}.css" />
<link rel="stylesheet" type="text/css" href="../../css/template.css" />
</head>
<body>
<div class="EB_X04392_{page_id}">
<div class="page">
<div class="{page_id}Container sec">
<div class="section">
</div>
<div class="img_container bottom_fixed">
<img aria-hidden="true" src="../../images/{image_file}" alt="Page {page_num}"/>
</div>
</div>
</div>
</div>
</body>
</html>'''
        
        # Write XHTML file
        output_file = os.path.join(page_dir, f'{page_id}.html')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xhtml_content)

# Usage
images_dir = r'd:\epubpdf\images'
create_xhtml_pages(images_dir)