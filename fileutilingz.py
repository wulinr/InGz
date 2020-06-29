import zipfile
import rarfile
import tarfile
import gzip
import os
import re

class FileUtilInGz():
    def __init__(self):
        pass
    def uncompressfile(self,source_file,des_path):
        #print(des_path)
        basename=os.path.basename(source_file)
        try:
            is_tar_gz=re.compile(r"tar.gz")
            result=is_tar_gz.findall(basename)
            filetype=basename.split('.')[-1]
            if filetype == "rar":
                rar_file=rarfile.RarFile(source_file)
                os.chdir(des_path)
                rar_file.extractall()
                rar_file.close()
            if filetype in ['tar','gz'] and result:
                tar_file=tarfile.open(source_file)
                #tar_file=tarfile.open("rarfile-2.4.tar.gz")
                for name in tar_file.getnames():
                    print(name)
                os.chdir(des_path)
                tar_file.extractall()
                tar_file.close()
            elif filetype == 'zip':
                zip_file=zipfile.ZipFile(source_file)
                os.chdir(des_path)
                zip_file.extractall()
                zip_file.close()
            elif filetype == "gz":
                gz_file=gzip.GzipFile(source_file)
                realdes=des_path+"/"+basename
                open(realdes,'wb+').write(gz_file.read())
                gz_file.close()

        except Exception as error:
            print(error)
            print("解压失败，请重新选择文件！")

    def compressfile(self,source_file,des_path):
        print("开发中，敬请期待")

if __name__=="__main__":
    fileutil=FileUtilInGz()
    #os.chdir("E:\Java相关资料\java\day01\code")
    #测试zip文件
    #fileutil.uncompressfile(r"C:\Users\Administrator\Desktop\Desktop.zip",r"C:\Users\Administrator\Desktop\wd")
    #测试tar.gz文件
    fileutil.uncompressfile(r"C:\Users\Administrator\Desktop\rarfile-2.4.tar.gz",r"C:\Users\Administrator\Desktop")

