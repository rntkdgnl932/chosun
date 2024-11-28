import time
import os
import sys

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def jadong_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import out_check, juljun_off, all_confirms, game_loading_check, game_loading, attack_check, juljun_on, juljun_check, attack_on
    from potion_chosun import potion_check
    from dead_die import dead_check

    my_spot = "c:\\my_games\\chosun\\data_chosun\\imgs\\jadong\\spot"
    file_list = os.listdir(my_spot)

    try:
        print("jadong_start")

        # 절전모드인지 확인
        result_juljun = juljun_check(cla)
        if result_juljun == True:
            is_spot = False
            for i in range(len(file_list)):
                result_file_list = file_list[i].split(".")
                read_data = result_file_list[0]

                # 종류 쭈욱 시작
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\jadong\\spot\\" + str(read_data) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 130, 950, 1000, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("spot...", str(read_data), imgs_)
                    is_spot = True
            if is_spot == False:
                jadong_spot(cla)
            else:
                result_attack = attack_check(cla)
                if result_attack == True:
                    potion_check(cla)
                    dead_check(cla, "자동사냥")
                else:
                    attack_on(cla)
                    juljun_on(cla)
        else:
            all_confirms(cla)
            juljun_on(cla)



    except Exception as e:
        print(e)
        return 0

def jadong_spot(cla):
    import numpy as np
    import cv2
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_chosun import out_check, juljun_off, all_confirms, game_loading_check, game_loading, attack_check, juljun_on, attack_on
    from clean_screen_chosun import clean_screen

    try:
        print("jadong_spot")

        juljun_off(cla)

        all_confirms(cla)


        spot = False
        spot_count = 0
        while spot is False:
            spot_count += 1
            if spot_count > 10:
                spot = True

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\map_all.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 330, 110, 365, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("map_all", imgs_)

                # 즐겨찾기
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\jadong\\jadong_list.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(80, 360, 180, 400, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("jadong_list", imgs_)

                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\jadong\\star_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_for = imgs_set_for(215, 390, 265, 800, cla, img, 0.9)
                    if imgs_for is not None and imgs_for != False:
                        print("star_btn", imgs_for)

                        print("len(imgs_for)", len(imgs_for))

                        ran_y = len(imgs_for) - 1

                        result_random = random.randint(0, ran_y)

                        for i in range(4):
                            result_confirm = all_confirms(cla)
                            if result_confirm == True:
                                spot = True
                                break
                            else:
                                click_pos_2(130, imgs_for[result_random][1], cla)
                            QTest.qWait(1000)

                        if spot == True:
                            for i in range(10):
                                result_out = out_check(cla, "jadong_spot..")
                                if result_out == True:
                                    break
                                else:
                                    result_loading = game_loading_check(cla)
                                    if result_loading == True:
                                        game_loading(cla)
                                    else:
                                        all_confirms(cla)
                                time.sleep(1)
                            attack_on(cla)
                            juljun_on(cla)


                else:
                    click_pos_2(38, 388, cla)


            else:
                result_out = out_check(cla, "jadong_spot")
                print("result_out", result_out)
                if result_out == True:
                    click_pos_2(800, 385, cla)
                else:
                    clean_screen(cla)
            QTest.qWait(1000)



    except Exception as e:
        print(e)
        return 0
