from os import write

import PIL
from PIL import Image
import os
a = os.listdir('input files')
print('%a' % (a))
for x in a:
    name = x
    command = f'ffmpeg -i ".\input files\{name}" -vf scale=1024x576 -b:v 1M ".\output files\output{name}"'
    os.system(command)


