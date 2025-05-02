import os

def create_css_files(output_dir):
    css_dir = os.path.join(output_dir, 'css')
    os.makedirs(css_dir, exist_ok=True)
    
    # Create template.css
    template_css = '''@font-face {font-family: "Agenda"; font-style: normal; font-weight:normal; src: url('../fonts/Agenda.otf'); }
@font-face {font-family: "AgendaBold"; font-style: normal; font-weight:normal; src: url('../fonts/AgendaBold.otf'); }
@font-face {font-family: "AgendaBoldCondensed"; font-style: normal; font-weight:normal; src: url('../fonts/AgendaBoldCondensed.otf'); }
@font-face {font-family: "AgendaMedium"; font-style: normal; font-weight:normal; src: url('../fonts/AgendaMedium.otf'); }
@font-face {font-family: "AgendaMediumCondensed"; font-style: normal; font-weight:normal; src: url('../fonts/AgendaMediumCondensed.otf'); }
@font-face {font-family: "AvantGardeCondBold"; font-style: normal; font-weight:normal; src: url('../fonts/AvantGardeCondBold.otf'); }
@font-face {font-family: "AvantGardeDemi"; font-style: normal; font-weight:normal; src: url('../fonts/AvantGardeDemi.otf'); }
@font-face {font-family: "futura-book-bt"; font-style: normal; font-weight:normal; src: url('../fonts/futura-book-bt.otf'); }
@font-face {font-family: "TextileRegular"; font-style: normal; font-weight:normal; src: url('../fonts/TextileRegular.otf'); }
@font-face {font-family: "Aragon-Sans-SC"; font-style: normal; font-weight:normal; src: url('../fonts/Aragon-Sans-SC.otf'); }

body {
    width:724px;
    height:660px;
    position:absolute;
    top:0px;
    left:0px;
}
img {width: 724px;height: 660px;position:absolute;top: 0px;left: 0px;z-index:0;}
* {margin: 0px;font-weight:normal;}
a {
    text-decoration: none;
    color: inherit;
}
.text-hidden{
    position: absolute;
    left: -10000px;
    top: auto;
    width: 1pt;
    height: 1px;
    overflow: hidden;
}
.-epub-media-overlay-active { color: #DE1717 !important;  background-color: #f8f012 !important;}
.-epub-media-overlay-active *{ color: #DE1717 !important;  background-color: #f8f012 !important;}
.para span {position: relative;}
.para {position: absolute!important;margin-top: 0px;}

.img_container {margin: 0;width: 724px;height: 660px;}

.even_text_1 {font-family: "Orbitron-Medium_3mo";font-style: normal;font-weight: normal;word-spacing: 0px;color: #000000;font-size: 11px;top: 35.7px;height: 0px;left: 71.7px;z-index: 1;position: absolute;letter-spacing: 2px;text-align: left;}
.even_text_2 {font-family: "Orbitron-Medium_3mo";font-style: normal;font-weight: normal;word-spacing: 0px;color: #FFFFFF;font-size: 11px;top: 35.7px;height: 0px;left: 71.7px;z-index: 1;position: absolute;letter-spacing: 2px;text-align: left;}
.even_odd_1 {font-family: "Orbitron-Medium_3mo";font-style: normal;font-weight: normal;word-spacing: 0px;color: #8F499C;font-size: 11px;top: 35.8px;height: 0px;left: 401.7px;z-index: 1;position: absolute;letter-spacing: 1.9px;text-align: left;}
.even_odd_3 {font-family: "Orbitron-Medium_3mo";font-style: normal;font-weight: normal;word-spacing: 0px;color: #8F499C;font-size: 11px;top: 35.8px;height: 0px;left: 417.7px;z-index: 1;position: absolute;letter-spacing: 1.9px;text-align: left;}
.even_odd_21 {font-family: "Orbitron-Medium_3mo";font-style: normal;font-weight: normal;word-spacing: 0px;color: #8F499C;font-size: 11px;top: 35.8px;height: 0px;left: 362.7px;z-index: 1;position: absolute;letter-spacing: 1.9px;text-align: left;}

.page_odd{font-family: "AgendaMedium";letter-spacing: px;position: absolute;top: 575px;left: 646px;color: #8F499C;font-size: 28px;z-index: 1; color:black;}
.page_even{font-family: "AgendaMedium";letter-spacing: px;position: absolute;top: 575px;left: 63px;color: #8F499C;font-size: 28px;z-index: 1; color:black;}
.page_odd_1{font-family: "AgendaMedium";letter-spacing: px;position: absolute;top: 575px;left: 643px;color: #8F499C;font-size: 28px;z-index: 1; color:black;}
.page_even_1{font-family: "AgendaMedium";letter-spacing: px;position: absolute;top: 575px;left: 57px;color: #8F499C;font-size: 28px;z-index: 1; color:black;}'''
    
    with open(os.path.join(css_dir, 'template.css'), 'w', encoding='utf-8') as f:
        f.write(template_css)
    
    # Continue with the page-specific CSS generation
    html_dir = os.path.join(output_dir, 'html')
    page_dirs = [d for d in os.listdir(html_dir) if d.startswith('page')]
    
    for page_dir in sorted(page_dirs):
        page_id = page_dir  # e.g., 'page001'
        
        css_content = f'''.section {{
    height: 1031px;
    width: 715px;
    position: absolute;
    padding: 0;
    margin: 0;
    top: 19px;
    left: 0;
    display: contents;
    overflow: hidden;
}}

img {{
    width: 715px;
    height: 1031px;
    position: absolute;
    top: 0px;
    left: 0px;
    z-index: 0;
}}

.{page_id}Container {{
    width: 715px;
    height: 1031px;
    position: absolute;
    left: 0px;
    top: 0px;
    z-index: 0;
}}

.para1 {{
    font-family: Futura;
    font-size: 50px;
    position: absolute;
    top: 30px;
    left: 65px;
    width: 724px;
    word-spacing: 0px;
    letter-spacing: 0.9px;
    z-index: 1;
    height: 24px;
    color: #E52B33;
}}

.para2 {{
    font-family: "AgendaBold";
    font-size: 19px;
    position: absolute;
    top: 588.7px;
    left: 294px;
    width: 393px;
    word-spacing: 0px;
    letter-spacing: 0px;
    z-index: 1;
    line-height: 19.7px;
    height: 24px;
}}

.para2 .speaking {{
    color: yellow;
    background: transparent !important;
}}

.para3 {{
    font-family: "BerkeleyStd-Medium_px";
    font-size: 16px;
    position: absolute;
    top: 218.4px;
    left: 60px;
    width: 480px;
    word-spacing: 0px;
    letter-spacing: 0px;
    z-index: 1;
    line-height: 19.7px;
    height: 24px;
    color: #ffffff;
}}

.para4, .para5, .para6, .para7 {{
    font-family: "BerkeleyStd-Medium_px";
    font-size: 16px;
    position: absolute;
    word-spacing: 0px;
    letter-spacing: 0px;
    z-index: 1;
    line-height: 20px;
    height: auto;
    color: #000000;
}}

.para4 {{
    top: 69.7px;
    left: 227px;
    text-indent: 25.1px;
}}

.para5 {{
    top: 268.9px;
    left: 363px;
    text-indent: 23.1px;
}}

.para6 {{
    top: 568.9px;
    left: 228px;
}}

.para7 {{
    top: 708.9px;
    left: 228px;
    text-indent: 23.3px;
}}'''
        
        css_file = os.path.join(css_dir, f'css_{page_id}.css')
        with open(css_file, 'w', encoding='utf-8') as f:
            f.write(css_content)

# Usage
output_dir = r'd:\epubpdf'
create_css_files(output_dir)