import os
a = os.listdir('input files')
print('%a' % (a))
for name in a:
    if name.endswith('.foo'):
        os.remove(f'.\input files\{name}')
        os.remove(f'.\output files\{name}')
    else:
        command = f'ffmpeg -i ".\input files\{name}" -vf scale=1024x576 -b:v 1M ".\output files\output{name}"'
        os.system(command) 

    