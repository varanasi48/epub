import os
import zipfile
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

def generate_smil_files(audio_zip_path, output_dir):
    # Create smil directory
    smil_dir = os.path.join(output_dir, 'smil')
    os.makedirs(smil_dir, exist_ok=True)
    
    with zipfile.ZipFile(audio_zip_path, 'r') as zip_ref:
        audio_files = [f for f in zip_ref.namelist() if f.endswith('.mp3')]
        zip_ref.extractall(os.path.join(output_dir, 'audio'))
        
        for audio_file in sorted(audio_files):
            page_num = audio_file.split('_')[1].split('.')[0]
            page_id = f'page{page_num.zfill(3)}'
            
            # Create SMIL structure
            smil = Element('smil', xmlns="http://www.w3.org/ns/SMIL")
            head = SubElement(smil, 'head')
            meta = SubElement(head, 'meta', name="dc:format", content="SMIL 1.0")
            layout = SubElement(head, 'layout')
            root_layout = SubElement(layout, 'root-layout', width="724", height="660")
            
            body = SubElement(smil, 'body')
            seq = SubElement(body, 'seq', id=f'seq_{page_id}', dur="indefinite")
            
            # Add par elements for each text-audio sync
            par = SubElement(seq, 'par', id=f'par_{page_id}')
            text = SubElement(par, 'text', src=f'../html/{page_id}/{page_id}.html')
            audio = SubElement(par, 'audio', src=f'../audio/{audio_file}')
            
            # Pretty print XML
            xml_str = minidom.parseString(tostring(smil)).toprettyxml(indent="  ")
            
            # Write SMIL file
            smil_path = os.path.join(smil_dir, f'{page_id}.smil')
            with open(smil_path, 'w', encoding='utf-8') as f:
                f.write(xml_str)

# Usage
audio_zip_path = r'd:\epubpdf\audio.zip'
output_dir = r'd:\epubpdf'
generate_smil_files(audio_zip_path, output_dir)