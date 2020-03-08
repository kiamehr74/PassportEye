from passporteye.mrz.image import read_mrz


import os
from shutil import copyfile

# base_directory = '/home/kia/Desktop/passs/'
# succ_directory = '/home/kia/Desktop/succ/'
# none_directory = '/home/kia/Desktop/none/'
#
# import time
# st=time.time()
# total_cp_time = 0
#
# for filename in os.listdir(base_directory):
#
#     to_open = os.path.join (base_directory, filename)
#     mrz = read_mrz(to_open)
#
#     cp_time_start = time.time()
#     if mrz:
#         to_go = os.path.join(succ_directory, filename)
#     else:
#         to_go = os.path.join(none_directory, filename)
#
#     copyfile(to_open, to_go)
#     total_cp_time += (time.time()-cp_time_start)
#
#     if (mrz):
#         print(to_open, "  :")
#         print(mrz)
#     print ("-------------")
#     print ()
#
#
# print("total time: ","----%.2f----"%(time.time()-st))
# print("cp time: ","----%.2f----"%(total_cp_time))
# print("alg time: ","----%.2f----"%(time.time()-(st+total_cp_time)))
#
#

from pprint import pprint
test = "/home/kia/Desktop/passs/10hfavru.x3p.jpg"
mrz = read_mrz(test, save_roi=False, extra_cmdline_params="--oem 1 -l ocrb")
dict_mrz = mrz.to_dict()
for key in dict_mrz.keys():
    print (key, " : ", dict_mrz[key])


# # print (read_mrz(test, save_roi=True))
