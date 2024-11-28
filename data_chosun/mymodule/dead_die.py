import time
# import os
import sys

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dead_check(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from potion_chosun import potion_buy
    from action_chosun import game_loading_check, game_loading, juljun_off
    from schedule import myQuest_play_check, myQuest_play_add

    try:
        print("dead_check")

        is_dead = False

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\hp_zero.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(70, 288, 140, 310, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("hp_zero", imgs_)
            juljun_off(cla)

            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\boohwal_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 700, 800, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    break
                time.sleep(0.5)


        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\boohwal_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(300, 700, 800, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_btn", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_dead = True

            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\boohwal_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(300, 700, 800, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                else:
                    break
                time.sleep(1)

            if data == "튜토육성":
                myQuest_play_add(cla, data)



            for i in range(10):
                result_loading = game_loading_check(cla)
                if result_loading == True:
                    game_loading(cla)
                    break
                time.sleep(1)


        return is_dead

    except Exception as e:
        print(e)
        return 0



