import time
# import os
import sys

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def clean_screen(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import out_check


    try:


        for i in range(5):

            result_out = out_check(cla, "clean_screen")
            print("clean_screen", i, result_out)
            if result_out == False:
                clean_screen_start(cla)
            else:
                break
            QTest.qWait(500)

    except Exception as e:
        print(e)
        return 0


def clean_screen_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_chosun import out_check, all_confirms, juljun_off
    from dead_die import dead_check, dead_recovery
    from potion_chosun import potion_buy

    try:
        print("clean_screen_start")

        juljun_off(cla)

        all_confirms(cla)

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\boohwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 700, 800, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            result= dead_check(cla, "clean_screen_start")
            if result == True:
                potion_buy(cla)
                dead_recovery(cla)

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\menu_open\\menu_setting.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(840, 730, 920, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("menu_setting", imgs_)
            click_pos_2(890, 300, cla)

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\clean_screen\\title_close_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(870, 270, 925, 330, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("title_close_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\clean_screen\\close_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_for = imgs_set_for(0, 270, 925, 800, cla, img, 0.9)
        if imgs_for is not None and imgs_for != False:
            print("close_1", imgs_for)

            for i in range(len(imgs_for)):
                click_pos_reg(imgs_for[i][0], imgs_for[i][1], cla)
                time.sleep(0.5)


    except Exception as e:
        print(e)
        return 0

