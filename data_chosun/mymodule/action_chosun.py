import sys
import os
import time
import requests

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


def skip_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        is_skip = False

        print("skip_check")
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\skip\\skip_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 580, 900, 650, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("skip_1", imgs_)
            is_skip = True

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\skip\\next_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 750, 910, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("next_1", imgs_)
            is_skip = True

        return is_skip

    except Exception as e:
        print(e)

def skip_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    from tuto_chosun import reward
    try:

        print("skip_start")

        is_skip = True
        is_skip_count = 0

        while is_skip is True:
            is_skip_count += 1
            if is_skip_count > 5:
                is_skip = False


            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\skip\\skip_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 580, 900, 650, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("skip_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                if is_skip_count > 0:
                    is_skip_count -= 1
            else:
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\skip\\next_1.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 750, 910, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("next_1", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    if is_skip_count > 0:
                        is_skip_count -= 1
                else:
                    result_reward = reward(cla)
                    if result_reward == True:
                        if is_skip_count > 0:
                            is_skip_count -= 1
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\move_notisfy_confirm.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(0, 270, 925, 800, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("move_notisfy_confirm", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
            QTest.qWait(500)

    except Exception as e:
        print(e)

def menu_open(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("menu_open")
        for i in range(5):
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\menu_open\\menu_setting.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(840, 730, 920, 800, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("menu_setting", imgs_)
                break
            else:
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\menu_open\\out_menu_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(860, 270, 920, 340, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("out_menu_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
            QTest.qWait(500)



    except Exception as e:
        print(e)

def out_check(cla, data):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        is_out = False

        print("out_check", data)
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\menu_open\\menu_setting.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(840, 730, 920, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("menu_setting", imgs_)
        else:
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\out_check\\out_pk.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(860, 680, 905, 725, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("out_pk", imgs_)
                is_out = True

        return is_out

    except Exception as e:
        print(e)


def juljun_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        is_juljun = False


        print("juljun_check")
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\juljun_check\\juljun_off_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(375, 700, 540, 770, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("juljun_off_btn", imgs_)


        return is_juljun

    except Exception as e:
        print(e)


def juljun_off(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, drag_pos
    try:

        is_juljun = True

        print("juljun_off")

        for i in range(5):
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\juljun_check\\juljun_off_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(375, 700, 540, 770, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("juljun_off_btn", i, imgs_)
                drag_pos(420, 730, 650, 730, cla)
            else:
                is_juljun = False
                break
            time.sleep(0.5)


        return is_juljun

    except Exception as e:
        print(e)


def juljun_on(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2
    from clean_screen_chosun import clean_screen_start
    try:

        is_juljun = False

        print("juljun_on")



        for i in range(5):
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\juljun_check\\juljun_off_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(375, 700, 540, 770, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("juljun_off_btn", i, imgs_)
                is_juljun = True
                break
            else:
                result_out = out_check(cla, "juljun_on")
                if result_out == False:
                    clean_screen_start(cla)
                else:
                    click_pos_2(33, 673, cla)
            QTest.qWait(500)


        return is_juljun

    except Exception as e:
        print(e)

def game_loading_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("game_loading_check")

        loading = False
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\check\\loading\\loading_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(420, 740, 500, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("loading_1", imgs_)
            loading = True
        else:
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\check\\loading\\loading_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(190, 190, 700, 950, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("loading_2", imgs_)
                loading = True

        return loading
    except Exception as e:
        print(e)

def game_loading(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("game_loading")

        loading = True
        loading_count = 0
        loading_False_count = 0
        while loading is True:



            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\check\\loading\\loading_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 740, 500, 800, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("loading_1", imgs_)
                if loading_count > 0:
                    print("loading...", loading_count, "초")

                loading_count += 1
                if loading_False_count > 0:
                    loading_False_count -= 1

            else:
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\check\\loading\\loading_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(190, 190, 700, 950, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("loading_2", imgs_)
                    if loading_count > 0:
                        print("loading...", loading_count, "초")

                    loading_count += 1
                    if loading_False_count > 0:
                        loading_False_count -= 1
                else:
                    loading_False_count += 1
                    if loading_False_count > 2:
                        loading = False
                    else:
                        result_out = out_check(cla, "game_loading")
                        if result_out == True:
                            loading = False

            time.sleep(1)


    except Exception as e:
        print(e)


def all_confirms(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    from clean_screen_chosun import clean_screen_start
    try:
        is_confirm = False

        print("all_confirms")

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\all_confirms\\notify_confirm.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 270, 925, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("notify_confirm", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_confirm = True
        else:
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\move_notisfy_confirm.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 270, 925, 800, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("move_notisfy_confirm", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)
                is_confirm = True

        return is_confirm
    except Exception as e:
        print(e)