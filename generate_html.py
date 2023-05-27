#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# Set the directory where the pictures are located
dir_path = os.getcwd()

# Create a list of pictures in the directory
pics = [pic for pic in os.listdir(dir_path) if pic.endswith('.jpg') or pic.endswith('.png')]
pics = sorted(pics, key=lambda x: int(x.split('.')[0]))

# Create the HTML file
with open('0.html', 'w') as f:
    # Write the HTML header
    f.write('<html>\n<head>\n<title>Combined Pictures</title>\n</head>\n<body>\n')

    # Write the image tags for each picture
    for pic in pics:
        f.write(f'<img src="{pic}" />\n')

    # Write the HTML footer
    f.write('</body>\n</html>')

print('HTML file generated!')