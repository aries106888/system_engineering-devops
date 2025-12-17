import os

files = ['0-current_working_directory', '1-listit', '2-bring_me_home', '3-listfiles', '4-listmorefiles']
for f in files:
    path = os.path.join(os.getcwd(), f)
    if os.path.exists(path):
        with open(path, 'rb') as fin:
            content = fin.read()
        content = content.replace(b'\r\n', b'\n')
        with open(path, 'wb') as fout:
            fout.write(content)
        print(f"Fixed {f}")
    else:
        print(f"Skipping {f} (not found)")
