# coding:utf-8
# version 1.0
import os.path
import sys
import base64
import re
import io
from PIL import Image


class ImageSolidifier():
    def __init__(self) -> None:
        self.srcfile = ''
        self.destfile = ''
        self.content = ''
        self.ratiolimit = 0.3
        self.qualitylimit = 50
        self.qualitylimitmax = 80
        self.datalenlimit = 72000
        self.progress=0
        self.indicator=None

    def setsrcfile(self, filepath):
        self.srcfile = filepath

    def setdestfile(self, filepath):
        self.destfile = filepath

    def conv_callback(self):
        pass

    def callback(self):
        #self.indicator.updatestate()
        pass

    def convert(self, imgfile, targefile , format, resize):
        with Image.open(imgfile) as im:
            #im.save(targefile, format=format)
            # image_data = list(im.getdata())
            # image_without_exif = Image.new(im.mode, im.size)
            # image_without_exif.putdata(image_data)
            ratio = 1
            q = self.qualitylimitmax
            sizeok = False
            loopcount = 1
            while ratio>=self.ratiolimit and q >= self.qualitylimit and not sizeok:
                with io.BytesIO() as output:
                    rzim = im.resize( [int(ratio * s) for s in im.size] )
                    rzim = rzim.convert('RGB')
                    rzim.save(output, format="JPEG", quality=q)
                    # my_palette = (20, 20, 20, 40, 40, 40, 200, 200, 200)
                    # rzim = rzim.convert('P', colors=16)
                    # rzim.save(output, format="GIF", optimize=True, bits=2)
                    self.content = output.getvalue()
                    
                    loopcount = loopcount+1
                    if len(self.content) < self.datalenlimit:
                        sizeok = True
                    else:
                        q=q-5
                        if q<self.qualitylimit:
                            ratio = ratio - 0.1
                            q=self.qualitylimitmax
            #print(loopcount, ratio, q ,'content len:',len(self.content))
            self.conv_callback()

    def solidify(self):
        self.progress = 0
        content = ''
        with open(self.srcfile, 'r') as f:
            content = f.read()
        images = re.findall(r'\!\[.*\]\(.+\)', content)
        #print(images)
        htmlimgs = []
        for image in images:
            imgpath = re.findall(r'\((.+?)\)', image)[0]
            self.convert(imgpath, '','','')
            self.progress=int((images.index(image)+1)/len(images)*100)
            self.callback()
            # with open(imgpath, 'rb') as f:
            #     self.content = f.read()
            r = base64.b64encode(self.content)
            imgcode = '<img src="data:image/gif;base64,%s" />' % r.decode('ascii')
            #imgcode = '![](data:image/png;base64,%s)' % r.decode('ascii')
            htmlimgs.append(imgcode)
        for i in range(len(images)):
            content = content.replace(images[i], htmlimgs[i])
        #print(content)
        #print(htmlimgs)
        with open(self.destfile, 'w') as f:
            f.write(content)


if __name__ == '__main__':
    aa = ImageSolidifier()
    if len(sys.argv) !=3:
        print('usage:\nmdingsolidifer.py src.md dest.md\n')
    else:
        aa.setsrcfile(sys.argv[1])
        aa.setdestfile(sys.argv[2])
        aa.solidify()
