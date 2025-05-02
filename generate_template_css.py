import os
import json

def generate_template_css():
    # Read fonts from json
    with open(r'd:\epubpdf\fonts.json', 'r', encoding='utf-8') as f:
        fonts_data = json.load(f)

    css_content = []
    
    # Generate @font-face declarations
    for font_name in fonts_data:
        clean_name = font_name.split('+')[1] if '+' in font_name else font_name
        
        # Check if font file exists
        font_path = os.path.join(r'd:\epubpdf\fonts', f"{clean_name}.otf")
        if os.path.exists(font_path):
            css_content.append(f'''@font-face {{
    font-family: "{clean_name}";
    font-style: normal;
    font-weight: normal;
    src: url('../fonts/{clean_name}.otf');
}}''')

    # Add standard CSS
    css_content.extend(['''
body {
    width: 724px;
    height: 660px;
    position: absolute;
    top: 0px;
    left: 0px;
}

img {
    width: 724px;
    height: 660px;
    position: absolute;
    top: 0px;
    left: 0px;
    z-index: 0;
}

* {
    margin: 0px;
    font-weight: normal;
}

.text-hidden {
    position: absolute;
    left: -10000px;
    top: auto;
    width: 1pt;
    height: 1px;
    overflow: hidden;
}

.-epub-media-overlay-active {
    color: #DE1717 !important;
    background-color: #f8f012 !important;
}

.para span {
    position: relative;
}

.para {
    position: absolute !important;
    margin-top: 0px;
}

.img_container {
    margin: 0;
    width: 724px;
    height: 660px;
}'''])

    # Write the CSS file
    with open(r'd:\epubpdf\css\template.css', 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(css_content))

if __name__ == "__main__":
    generate_template_css()