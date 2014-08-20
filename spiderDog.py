import urllib2
from pyquery import PyQuery as pq
import os
try:
    from PIL import Image
except ImportError:
    import Image
from multiprocessing import Process
from multiprocessing import Pool
def save_img(url, vid,type) :
    saveInfo = generate_file_path_name(str(vid),type)
    res = save_to_local(url, saveInfo["path"], saveInfo["filename"])
    return res

def generate_file_path_name(vid,type) :
    # piecePath=vid.split('_')
    # piecePath='/'.join(piecePath)
    # print piecePath
    # f = lastid[0:2]
    # e = lastid[2:4]
    name = vid + ".jpg"
    path = "tmpimg/" + type+"/"

    res = {}
    res["path"] = path
    res["filename"] = name
    return res

def save_to_local(url, path, filename) :
    try :
        if not os.path.isdir(path) :
            os.makedirs(path)
        # print "open image url:"+url
        tmpFile = path + filename

        imgInfo = urllib2.urlopen(str(url),data=None,timeout=5).read()

        temp = open(tmpFile, 'wb')
        temp.write(imgInfo)
        temp.close()
        return "0"
    except Exception, e :
        print "open image url failed:"+url
        return "1"


        return


if __name__ == '__main__':
        checkurl="http://www.petdogs.cn/fenlei/"
        checkSourceCode = urllib2.urlopen(checkurl, data=None, timeout=30).read()
        d = pq(checkSourceCode)
        orgItem = d('.p2')
        count = 0
        for x in orgItem:
            for y in d(x):
                piece = d(y)
                count=count+1
                dogpic=piece("img").attr("src")
                dogname=piece("img").attr("alt")
                save_img(dogpic,count,"dog")
                print dogpic
                print dogname
                