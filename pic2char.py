# -*- coding: utf-8 -*-
"""
@autour yyt
"""
import os
import imageio
from PIL import Image, ImageDraw, ImageFont

SOURCE_PATH = r'./webwxgetmsgimg.jpg'
OUTPUT_PATH = r'./imgs/'
FRAMES_PATH = r'./outimg/'

def create_dir():
    if (os.path.exists(OUTPUT_PATH)):
        for file in os.listdir(OUTPUT_PATH):
            os.remove(''.join((OUTPUT_PATH, file)))
    else:
        os.makedirs(FRAMES_PATH)
    if (os.path.exists(FRAMES_PATH)):
        for file in os.listdir(FRAMES_PATH):
            os.remove(''.join((FRAMES_PATH, file)))
    else:
        os.makedirs(FRAMES_PATH)

def processImage(path):
    credits()
    img = Image.open(path)
    index = 0
    print('\r正在解析....')
    try:
        while True:
            img.seek(index)
            if (index % 3 == 0):
                img.save('./imgs/%d.png' % (index / 3))
            index += 1
    except EOFError:
        print('\r解析完成！')

def createImg(path):
    STRS = '0123456789!@#$%^&*()_+-=~`abcdefghigklmnopqlstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ '
    progress = 0
    unit = len(os.listdir('./imgs/')) / 100
    for file in os.listdir(path):
        progress += int(unit + 1)
        # print('\r' + '转字符图处理：%s%.f' % ('>' * int(progress / unit)), (progress / unit))
        with Image.open(''.join((path, file))) as img:
            wide, high = img.size
            if img.mode != 'RGB': img = img.convert('RGB')
            new_img = Image.new('1', (wide * 2, high * 2), color=255)
            draw = ImageDraw.Draw(new_img)
            for i in range(1, high, 4):
                for j in range(1, wide, 4):
                    R, G, B = img.getpixel((j, i))
                    sum = R + G + B
                    index = int(sum / 25)
                    draw.text((j * 2, i * 2), STRS[index])
            new_img.save('./outimg/' + file)
    print()

def create_gif(path, filename):
    print('\r正在生成GIF。。。。')
    image_list = []
    num = len(os.listdir(path))
    for i in range(num):
        image_list.append('./outimg/'+ str(i) + '.png')
    frames = []
    for image_name in image_list:
        frames.append(imageio.imread(image_name))
    imageio.mimsave(filename, frames, 'GIF', duration = 0.1)
    print('\r已生成GIF！')

def main():
    create_dir()
    processImage(SOURCE_PATH)
    createImg(OUTPUT_PATH)
    create_gif(FRAMES_PATH, '002.gif')

if __name__ == '__main__':
    main()