from distutils.log import error
import glob
filename = input('filename : ')
cnt = 0
scnt = 0
home = '/Users/kuniyoshitakuma'
filelist = glob.glob(home+'/Desktop/*')
filelist += glob.glob(home+'/Downloads/*')
filelist += glob.glob(home+'/prog1/*')
filelist += glob.glob(home+'/prog2/*')
filelist += glob.glob(home+'/Lectures/*')
pyfilelist = glob.glob(home+'/'+filename)
while(len(filelist)>0):
    subfilelist=[]
    for file in filelist:
        scnt += 1
        if file[0] == 'D':
            print(file)
        path = file+'/'+filename
        pyfilelist =  glob.glob(path)
        for pyfile in pyfilelist:
            try:
                f = open(pyfile,'r')
            except error and TypeError and IsADirectoryError:
                break
            else:
                try :
                    data = f.read()
                except NameError:
                    break
                else :
                    mozi = len(data.split(" " or "\n"))
                    print(f'{mozi} {pyfile}')
                    cnt += mozi
        subfilelist += glob.glob(file+'/*')
    filelist = subfilelist
print(cnt)