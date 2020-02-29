from passporteye.mrz.image import read_mrz


import os
from shutil import copyfile

base_directory = '/home/kia/Desktop/passs/'
succ_directory = '/home/kia/Desktop/succ/'
none_directory = '/home/kia/Desktop/none/'
for filename in os.listdir(base_directory):

    to_open = os.path.join (base_directory, filename)
    mrz = read_mrz(to_open)

    if mrz:
        to_go = os.path.join(succ_directory, filename)
    else:
        to_go = os.path.join(none_directory, filename)

    copyfile(to_open, to_go)

    if (mrz):
        print(to_open, "  :")
        print(mrz)
    print ("-------------")
    print ()

# test = "/home/kia/Desktop/fail/14y1lnwh.i03.jpg"
# print (read_mrz(test, save_roi=False, extra_cmdline_params="--oem 1 -l ocrb").__dict__)
# # print (read_mrz(test, save_roi=True))
