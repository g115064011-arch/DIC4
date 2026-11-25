import shutil, os
ROOT = r'C:\Users\huang\Desktop\IoT\DIC4\DIC4'
os.makedirs(os.path.join(ROOT, 'deliverables'), exist_ok=True)
pairs = [
    ('paper_good/main.pdf', 'DIC4_Good_Final_IEEE_Conference.pdf'),
    ('paper_bad/main.pdf',  'DIC4_Bad_Draft_Erroneous.pdf'),
    ('paper_good/main.pdf', 'deliverables/DIC4_Good_Final_IEEE_Conference.pdf'),
    ('paper_bad/main.pdf',  'deliverables/DIC4_Bad_Draft_Erroneous.pdf'),
    ('paper_good/main.log', 'deliverables/DIC4_Good_Final.log'),
    ('paper_bad/main.log',  'deliverables/DIC4_Bad_Draft.log'),
]
for src_rel, dst_rel in pairs:
    src = os.path.join(ROOT, src_rel)
    dst = os.path.join(ROOT, dst_rel)
    shutil.copy2(src, dst)
    print(f'{dst_rel}: {os.path.getsize(dst)} bytes')
print('Done.')
