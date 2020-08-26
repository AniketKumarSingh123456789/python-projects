import os,PIL
from PIL import ImageGrab
lis1 = []
i=0
while i==i:
    lis1.append(i)
    i+=1
    if i==1000:
        break
for x in lis1:
    while x==x:
        if os.path.exists(f'Screenshot{x}.png'):
            x+=1
        else:
            break
    ImageGrab.grab().save(f'Screenshot{x}.png')
    break