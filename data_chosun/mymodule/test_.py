import sys
import os
import time
import requests

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random


    print("test")
    cla = "one"

    plus = 0


    if cla == "one":
        plus = 0
    elif cla == "two":
        plus = 960
    elif cla == "three":
        plus = 960 * 2
    elif cla == "four":
        plus = 960 * 3
    elif cla == "five":
        plus = 960 * 4
    elif cla == "six":
        plus = 960 * 5

    from function_game import imgs_set_for, click_pos_reg, imgs_set_
    from clean_screen_chosun import clean_screen
    from action_chosun import juljun_off, juljun_on
    from tuto_chosun import way_click, quest_btn


    try:
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\attack_check\\auto_on.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(420, 580, 500, 620, cla, img, 0.7)
        if imgs_ is not None and imgs_ != False:
            print("auto_on", imgs_)

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\attack_check\\auto_off.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(855, 625, 910, 680, cla, img, 0.95)
        if imgs_ is not None and imgs_ != False:
            print("auto_off", imgs_)

    except Exception as e:
        print(e)