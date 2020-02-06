import os

# 获取当前目录下所有png文件
def all_file(dirname):
    result = []
    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            if filename.endswith('.rmvb'):
                apath = os.path.join(maindir, filename)
                result.append(apath)
    return result

cur_dir = os.path.split(os.path.realpath(__file__))[0]
    # print(cur_dir)
file_list = all_file(cur_dir)


for fname in file_list:


    # #设置新文件名
    # newname= fname[:-8]
    newname = fname.replace('dream2008.cn@','')
    print(newname)

    #用os模块中的rename方法对文件改名
    os.rename(fname,newname)
    print(fname,'======>',newname)

