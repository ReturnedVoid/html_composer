import codecs
import re
import os
import base64
import platform
import shutil

# get current os (Linux or Windows considered)
OS = platform.system()


def compose():
    html_files = [file for file in os.listdir() if file.endswith('htm')]

    for hfile in html_files:
        # htmlname.files
        imgpath = '{}.files'.format(hfile.split('.')[0])

        with codecs.open(hfile, 'r',
                         encoding='windows-1251',
                         errors='ignore') as data:
            f = data.read()
            f = re.sub(r'alt=".+"', '', f)  # clear all alt
            imgs = re.findall(r'src=".+/image.+"', f)  # findall images

        def img2str(img):
            ''' Returns string image '''
            with open(img, "rb") as imageFile:
                stri = base64.b64encode(imageFile.read())
            return str(stri)[2:-1]

        for img in imgs:
            imgname = img.split('/')[-1]
            imgname = imgname[:-1]  # delete unnecessary '"'
            imgp = os.path.join(imgpath, imgname)
            stri = img2str(imgp)
            f = re.sub(img, 'src="data:image/png;base64, {}"'.format(stri), f)

        # if linux, we need utf8 charset
        if OS == 'Linux':
            f = re.sub('charset=windows-1251', 'charset=utf8', f)

        os.remove(hfile)
        shutil.rmtree(imgpath)
        with open(hfile, 'w') as htmlf:
            htmlf.write(f)


if __name__ == '__main__':
    compose()
