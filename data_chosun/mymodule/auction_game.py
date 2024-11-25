import sys
import os
import time
import requests

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def mine_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number
    try:

        result_dia = 0
        result_silver = 0

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\dia_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("dia_reg", imgs_)

            result_text = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 45, imgs_.y + 8)
            result_text = change_number(result_text)
            result_dia = int_put_(result_text)
            result_dia_num = in_number_check(result_dia)
            print("result_text", result_dia_num, result_dia)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\silver_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("silver_reg", imgs_)
            result_text2 = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 70, imgs_.y + 8)
            result_text2 = change_number(result_text2)
            result_silver = int_put_(result_text2)
            result_silver_num = in_number_check(result_silver)
            print("result_text2", result_silver_num, result_silver)

        if result_dia_num == True:

            return result_silver, result_dia

    except Exception as e:
        print(e)




