import os, zipfile

ROOT = r'C:\Users\huang\Desktop\IoT\DIC4\DIC4'

def pack_latex_dir(src_dir_name, out_zip_name):
    src_dir = os.path.join(ROOT, src_dir_name)
    out_zip = os.path.join(ROOT, out_zip_name)
    items = ['main.tex', 'references.bib', 'fig1_architecture.png']
    with zipfile.ZipFile(out_zip, 'w', zipfile.ZIP_DEFLATED) as zf:
        for item in items:
            p = os.path.join(src_dir, item)
            zf.write(p, arcname=item)
        sec_dir = os.path.join(src_dir, 'sections')
        for fn in sorted(os.listdir(sec_dir)):
            if fn.endswith('.tex'):
                zf.write(os.path.join(sec_dir, fn), arcname=f'sections/{fn}')
    with zipfile.ZipFile(out_zip, 'r') as zf:
        names = zf.namelist()
    print(f'{out_zip_name}: {os.path.getsize(out_zip)} bytes, {len(names)} files -> {names}')

pack_latex_dir('paper_good', 'DIC4_Paper_Overleaf_Package.zip')
pack_latex_dir('paper_bad', 'DIC4_Bad_Draft_Overleaf_Package.zip')
