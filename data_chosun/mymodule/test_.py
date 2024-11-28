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

    from function_game import imgs_set_for, click_pos_reg, imgs_set_, text_check_get
    from clean_screen_chosun import clean_screen
    from action_chosun import juljun_off, juljun_on, attack_check
    from tuto_chosun import way_click, quest_btn
    from potion_chosun import potion_buy
    from get_item import get_item_start
    from jadong_chosun import jadong_spot

    try:

        # jadong_spot(cla)

        # attack_check(cla)

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\hp_zero.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(70, 288, 140, 310, cla, img, 0.9)
        if imgs_ is not None and imgs_ != False:
            print("hp_zero", imgs_)

        # a = 215
        # b = 312
        # c = 223
        # d = 324
        #
        # pos = (a + plus, b, c - a, d - b)
        # pyautogui.screenshot("asd.png", region=pos)
        # for i in range(10):
        #     full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\potion_num\\" + str(i) + ".PNG"
        #     img_array = np.fromfile(full_path, np.uint8)
        #     img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #     imgs_ = imgs_set_(a, b, c, d, cla, img, 0.85)
        #     if imgs_ is not None and imgs_ != False:
        #         print("potion_num => ", str(i), imgs_)

    except Exception as e:
        print(e)