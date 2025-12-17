import os

# Files to process
files = [
    '0-iam_betty',
    '1-who_am_i',
    '2-groups',
    '3-new_owner',
    '4-empty',
    '5-execute',
    '8-James_Bond',
    '9-John_Doe',
    '11-directories_permissions',
    '12-directory_permissions',
    '13-change_group'
]

# Write LF directly
for f in files:
    path = os.path.join(os.getcwd(), f)
    if os.path.exists(path):
        with open(path, 'rb') as fin:
            content = fin.read()
        # remove CR
        content = content.replace(b'\r\n', b'\n')
        with open(path, 'wb') as fout:
            fout.write(content)
        print(f"Fixed {f}")
    else:
        print(f"Skipping {f} (not found)")
