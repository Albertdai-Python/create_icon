from PIL import Image
from to_icns import convert
import os
import shutil
from tkinter import filedialog
dirr=os.listdir()
for i in range(len(dirr)):
        if dirr[i]=='.DS_Store':
                continue
        elif ".png" in dirr[i]:
                if dirr[i]!="folder.png":
                        os.rename(r'{}'.format(dirr[i]),r'{}'.format("target.png"))
        else:
                continue
image_dir="target.png"
bg_dir="folder.png"
img = Image.open(image_dir)
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
                newData.append((255, 255, 255, 0))
        else:
                newData.append(item)

img.putdata(newData)
w,h=img.size
background = Image.open(bg_dir)
wb,hb=background.size
img=img.resize((int(w/h*(hb/2)),int(hb/2)))
w,h=img.size
background.paste(img, (int(wb/2-w/2), int(hb/2-h/2+15)), img)
os.chdir(os.getcwd()+"/icons")
dirr=os.listdir()
a=[]
for i in range(len(dirr)):
        if dirr[i]=='.DS_Store':
                continue
        elif "**" in dirr[i]:
                a.append(int(dirr[i].split('.')[0].split("_")[1]))
        else:
                continue

if len(a)>0:
        background.save(f'**image_{max(a)+1}.png',"PNG")
        convert(os.getcwd()+f'/**image_{max(a)+1}.png')
        shutil.rmtree(os.getcwd()+f'/**image_{max(a)+1}.iconset', ignore_errors=True)
        os.remove(f'**image_{max(a)+1}.png')
else:
        background.save(f'**image_1.png',"PNG")
        convert(os.getcwd()+f'/**image_1.png')
        shutil.rmtree(os.getcwd()+f'/**image_1.iconset', ignore_errors=True)
        os.remove(f'**image_1.png')
