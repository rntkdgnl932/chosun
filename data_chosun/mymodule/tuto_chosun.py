import time
# import os
import sys
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import out_check

    try:
        print("tuto_start")
        result_out = out_check(cla, "tuto_start")
        if result_out == True:
            click_pos_2(130, 375, cla)
            for i in range(5):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\move_notisfy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 430, 500, 480, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("move_notisfy", imgs_)




    except Exception as e:
        print(e)
        return 0



def way_click(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("way_click")

        way_btn = True
        way_btn_count = 0
        while way_btn is True:
            way_btn_count += 1
            if way_btn_count > 7:
                way_btn = False

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\down_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("down_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y + 55, cla)
                if way_btn_count > 1:
                    way_btn_count -= 1

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\right_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("right_1", imgs_)
                click_pos_reg(imgs_.x + 70, imgs_.y, cla)
                if way_btn_count > 1:
                    way_btn_count -= 1

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\left_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("left_1", imgs_)
                click_pos_reg(imgs_.x - 70, imgs_.y, cla)
                if way_btn_count > 1:
                    way_btn_count -= 1

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\up_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("left_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y - 50, cla)
                if way_btn_count > 1:
                    way_btn_count -= 1

            QTest.qWait(500)



    except Exception as e:
        print(e)

def reward(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("reward")

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\reward\\reward_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("reward_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)



    except Exception as e:
        print(e)

