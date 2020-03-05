from passporteye.mrz.image import read_mrz


import os
from shutil import copyfile

# base_directory = '/home/kia/Desktop/passs/'
# succ_directory = '/home/kia/Desktop/succ/'
# none_directory = '/home/kia/Desktop/none/'

# base_directory = '/home/kia/Desktop/none/'
# succ_directory = '/home/kia/Desktop/non_suc/'
# none_directory = '/home/kia/Desktop/trash/'
#
# import time
# st=time.time()
# for filename in os.listdir(base_directory):
#
#     to_open = os.path.join (base_directory, filename)
#     mrz = read_mrz(to_open)
#
#     if mrz:
#         to_go = os.path.join(succ_directory, filename)
#     else:
#         to_go = os.path.join(none_directory, filename)
#
#     copyfile(to_open, to_go)
#
#     if (mrz):
#         print(to_open, "  :")
#         print(mrz)
#     print ("-------------")
#     print ()
#
#
# print("----%.2f----"%(time.time()-st))

test = "/home/kia/Desktop/trash/5hjhypot.5jr.jpeg"
print (read_mrz(test, save_roi=False, extra_cmdline_params="--oem 1 -l ocrb"))
# print (read_mrz(test, save_roi=True))
