# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 14:27:37 2020

@author: user1
"""
from PIL import Image
import os
 
 
def rea(path, pdf_name):
    file_list = os.listdir(path)
    pic_name = []
    im_list = []
    for x in file_list:
        if "jpg" in x or 'png' in x or 'jpeg' in x:
            pic_name.append(x)
 
    pic_name.sort()
    new_pic = []
 
    for x in pic_name:
        if "jpg" in x:
            new_pic.append(x)
 
    for x in pic_name:
        if "png" in x:
            new_pic.append(x)
 
    print("hec", new_pic)
 
    im1 = Image.open(os.path.join(path, new_pic[0]))
    new_pic.pop(0)
    for i in new_pic:
        img = Image.open(os.path.join(path, i))
        # im_list.append(Image.open(i))
        if img.mode == "RGBA":
            img = img.convert('RGB')
            im_list.append(img)
        else:
            im_list.append(img)
    im1.save(pdf_name, "PDF", resolution=100.0, save_all=True, append_images=im_list)
    print("Output file name and path:", pdf_name)
 
 
if __name__ == '__main__':
 
    pdf_name = './pdf/output.pdf'
    mypath=r"./pictures"
    if ".pdf" in pdf_name:
        rea(mypath, pdf_name=pdf_name)
    else:
        rea(mypath, pdf_name="{}.pdf".format(pdf_name))