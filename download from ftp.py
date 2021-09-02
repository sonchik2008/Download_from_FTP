from ftplib import FTP
import datetime
import os
import time
import zipfile

now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

ftp = FTP()
ftp.connect('your FTP', PORT)
ftp.login("login","password")

ftp.cwd('infobase') # change to folder on ftp
filename = ((now)+'_'+'yourname.1CD') # create file

with open(filename, 'wb') as f:
    ftp.retrbinary('RETR ' + '1Cv8.1CD', f.write)

#quit from ftp
ftp.quit()

# name zip
target = now + '.zip'

test1_zip = zipfile.ZipFile(target,'w')

for folder, subfolders, files in os.walk('d:\\test1'): # add file endswith *.1CD
 
    for file in files:
        if file.endswith('.1CD'):
            test1_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'd:\\test1'), compress_type = zipfile.ZIP_DEFLATED)
 
test1_zip.close()
os.remove(filename)
