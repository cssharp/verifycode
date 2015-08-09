#coding:utf-8
import os,itertools,re,urllib

'''分析得到验证码'''
def getVerify_Code(fileName):
    r=r'^[a-zA-Z0-9]{5}$'
    cmdList=['-colorspace gray','-monochrome']
    scaleList=[i*100 for i in range(1,6)]

    for s,c in itertools.product(scaleList,cmdList):
        cmds='convert.exe -compress none -depth 8 -alpha off -scale {0} {1} {2} code.tif '.format(s,c,fileName)
        print cmds
        os.system(cmds)
        os.system('tesseract -l eng code.tif rr')
        strx=open('rr.txt','r').read().replace(' ','').replace('_','').strip()
        print strx
        m = re.search('\d+[\+\-\*\/]\d+',strx)
        if m:
            strx=m.group(0)
            strx=eval(strx)
            return strx
        elif re.match(r,strx):
            return strx
    return ''


if __name__=='__main__':
    #uri='http://support.58.com/firewall/code/3739103579/a3aa8eed.do?rnd=0.7356960084289312'
    #urllib.urlretrieve(uri,'code.jpg')
    xxx=getVerify_Code('code.jpg')
    print u'找到了，{0}'.format(xxx) if xxx!='' else u'没有找到'