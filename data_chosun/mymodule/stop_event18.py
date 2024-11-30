import time
# import os
import sys

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def _stop_please(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("_stop_please")
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\18_event\\18_close_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 270, 920, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("18_close_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            time.sleep(0.5)
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\18_event\\18_close_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 270, 920, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("18_close_2", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        for i in range(10):
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\18_event\\apk_open_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 0, 920, 1030, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("apk_open_title", imgs_)
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\18_event\\apk_open_cancle.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 0, 920, 1030, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("apk_open_cancle", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            else:
                break
            time.sleep(0.5)





    except Exception as e:
        print(e)
        return 0



