import time
# import os
import sys

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def get_item_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2

    try:
        print("get_item_start")
        get_post(cla)
        get_event(cla)
        get_upjuk(cla)


    except Exception as e:
        print(e)
        return 0


def get_post(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import menu_open
    from clean_screen_chosun import clean_screen

    try:
        print("get_post")

        get_ = False
        get_count = 0

        while get_ is False:
            get_count += 1
            if get_count > 7:
                get_ = True

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\post.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(790, 270, 900, 350, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : post", imgs_)
                get_ = True
                click_pos_2(845, 765, cla)
                time.sleep(1)
                clean_screen(cla)

            else:
                menu_open(cla)

                for i in range(5):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\post.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 270, 900, 350, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\get_item\\menu_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(720, 730, 750, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_1", imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.5)
            time.sleep(1)


    except Exception as e:
        print(e)
        return 0


def get_event(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import menu_open
    from clean_screen_chosun import clean_screen

    try:
        print("get_event")

        get_ = False
        get_count = 0

        while get_ is False:
            get_count += 1
            if get_count > 7:
                get_ = True

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\event.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(790, 270, 900, 350, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : event", imgs_)
                get_ = True
                for i in range(4):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\get_item\\join_reward.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(140, 320, 450, 420, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("join_reward", imgs_)
                        break
                    else:
                        click_pos_2(55, 405, cla)
                    time.sleep(1)
                for i in range(20):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\get_item\\join_reward_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(120, 710, 880, 780, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("join_reward_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        break
                    QTest.qWait(500)
                clean_screen(cla)

            else:
                menu_open(cla)

                for i in range(5):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\event.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 270, 900, 350, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\get_item\\menu_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(775, 730, 805, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_1", imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.5)
            time.sleep(1)


    except Exception as e:
        print(e)
        return 0


def get_upjuk(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import menu_open
    from clean_screen_chosun import clean_screen

    try:
        print("get_upjuk")

        get_ = False
        get_count = 0

        while get_ is False:
            get_count += 1
            if get_count > 7:
                get_ = True

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\mission.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(790, 270, 900, 350, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("title : mission", imgs_)
                get_ = True
                for i in range(20):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\get_item\\mission_ilgwal_get_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 750, 900, 790, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("mission_ilgwal_get_btn", imgs_)
                        click_pos_reg(imgs_.x - 15, imgs_.y + 7, cla)
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\get_item\\mission_point_1.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(505, 325, 535, 355, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("mission_point_1", imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y + 7, cla)
                    QTest.qWait(500)
                clean_screen(cla)

            else:
                menu_open(cla)

                for i in range(5):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\mission.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(790, 270, 900, 350, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\get_item\\menu_point_2.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 330, 830, 350, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_point_2", imgs_)
                            click_pos_reg(imgs_.x - 15, imgs_.y + 15, cla)
                    time.sleep(0.5)
            time.sleep(1)


    except Exception as e:
        print(e)
        return 0
