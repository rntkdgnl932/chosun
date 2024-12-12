import sys
import os
import time
import requests

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def go_test():
    import numpy as np
    import cv2
    import pyautogui
    import random

    from datetime import datetime

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

    from function_game import imgs_set_for, click_pos_reg, imgs_set_, text_check_get, click_pos_reg_double_click, click_pos_2
    from clean_screen_chosun import clean_screen
    from action_chosun import juljun_off, juljun_on, attack_check, skip_start, all_confirms
    from tuto_chosun import way_click, quest_btn
    from potion_chosun import potion_buy, go_maul
    from get_item import get_item_start
    from jadong_chosun import jadong_spot
    from boonhae_collection import collection_start, boonhae_start
    from dead_die import dead_recovery
    from dungeon_chosun import dungeon_spot
    from auction_game import auction_low_num, auction_qun_num, auction_start

    try:

        # spot = "던전_수련동굴"
        # dungeon_spot(cla, spot)

        # 최대수량 적기
        auction_start(cla)

        # auction_low_num(cla)

        # auction_qun_num(cla)

        # full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\menu_auction.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(810, 380, 920, 460, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     click_pos_reg(imgs_.x, imgs_.y, cla)

        ############################################################
        ################ auction ###########################
        #################################################################

        # text_check_get(365, 520, 433, 533, cla)

        # is_point = False
        # full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\point.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(365, 520, 433, 533, cla, img, 0.85)
        # if imgs_ is not None and imgs_ != False:
        #     print("point", imgs_)
        #     is_point = True
        #     point_x = imgs_.x
        #
        # x_reg_1 = 10000
        # x_reg_2 = 0
        # if is_point == True:
        #     print("소수점 앞 자리, 가장 앞에 숫자 찾기")
        #     for i in range(10):
        #         full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(365, 512, point_x, 533, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             print(str(i), imgs_)
        #             if x_reg_1 > imgs_.x:
        #                 x_reg_1 = imgs_.x
        #     for i in range(10):
        #         full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(x_reg_1 - 4, 512, point_x, 533, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             print(str(i), imgs_)
        #             if x_reg_1 > imgs_.x:
        #                 x_reg_1 = imgs_.x
        #
        #
        #     print("소수점 뒷 자리, 가장 앞에 숫자 찾기")
        #     for i in range(10):
        #         full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(point_x, 512, 433, 533, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             print(str(i), imgs_)
        #             if x_reg_1 > imgs_.x:
        #                 x_reg_1 = imgs_.x
        # else:
        #     print("소수점 없을 경우 가장 앞에 숫자 및 가장 뒷 숫자 찾기")
        #
        #     for i in range(10):
        #         full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(365, 512, 433, 533, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             print(str(i), imgs_)
        #             if x_reg_1 > imgs_.x:
        #                 x_reg_1 = imgs_.x
        #     for i in range(10):
        #         full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
        #         img_array = np.fromfile(full_path, np.uint8)
        #         img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        #         imgs_ = imgs_set_(x_reg_1 - 4, 512, x_reg_1 + 4, 533, cla, img, 0.85)
        #         if imgs_ is not None and imgs_ != False:
        #             print(str(i), imgs_)
        #             if x_reg_1 > imgs_.x:
        #                 x_reg_1 = imgs_.x
        #
        # print("x_reg", x_reg_1)

        ########################################################
        ######################################################
        ########################################################

        # go_maul(cla)

        # full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\gold_checked.PNG"
        # img_array = np.fromfile(full_path, np.uint8)
        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        # imgs_ = imgs_set_(225, 690, 270, 730, cla, img, 0.8)
        # if imgs_ is not None and imgs_ != False:
        #     print("gold_checked", imgs_)



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