#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from chars import CHChars
# for char in CHChars:
#     print(char)
bad_char = b'\xF0\x9D\x91\x9B'.decode('utf-8')
print(bad_char)


if __name__ == '__main__':
    from deal_with_data import DIR,File

    # dirs = DIR('/home/huawenjin/learning_materials/python学习资料/html/')
    # dirs.getFileName()
    # i = 0
    # for f in dirs.files:
    #     if  i < 10000:
    #        os.popen('cp /home/huawenjin/learning_materials/python学习资料/html/%s  /home/huawenjin/tmp/' %f).readlines()
    #        i += 1


