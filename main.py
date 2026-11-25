# Verified entry line: exactly 96 characters (UTF-8: 96 bytes), no trailing newline.
LINE = "My code works on my machine. It does not work on yours. I have decided this is your problem now."

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
output_path = os.path.join(output_dir, 'entry.txt')

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))
