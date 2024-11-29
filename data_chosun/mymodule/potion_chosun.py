import time
# import os
import sys

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def potion_check(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import juljun_check, out_check
    try:
        print("potion_check => v_.potion_count : ", v_.potion_count)

        is_potion = True

        result_juljun = juljun_check(cla)
        result_out = out_check(cla, "potion_check")

        if result_juljun == True or result_out == True:
            is_potion = False



        if is_potion == False:

            a = 215
            b = 312
            c = 223
            d = 324

            for count in range(4):
                print("potion_check count =>", count)
                for i in range(10):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\potion_num\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(a, b, c, d, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("potion_num => ", str(i), imgs_)
                        is_potion = True
                        v_.potion_count = 0
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\potion_num\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(a, b, c, d, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("potion_num => ", str(i), imgs_)
                            is_potion = True
                            v_.potion_count = 0
                            break
                if is_potion == True:
                    break
            if is_potion == False:
                v_.potion_count += 1
                if v_.potion_count > 6:
                    potion_buy(cla)

        # 절전모드일때와 절전모드 아닐때 구분할 필요는 없네
        # result_juljun = juljun_check(cla)
        # if result_juljun == False:
        #     # 아웃
        # else:
        #     # 절전

    except Exception as e:
        print(e)
        return 0


def potion_buy(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import all_confirms, juljun_off
    from clean_screen_chosun import clean_screen
    try:
        print("potion_buy")

        juljun_off(cla)


        result_maul = go_maul(cla)
        if result_maul == True:


            buy = False
            buy_count = 0

            while buy is False:
                buy_count += 1
                print("buy_count", buy_count)
                if buy_count > 60:
                    buy = True

                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\jadong_buy.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(180, 740, 260, 780, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("jadong_buy", imgs_)
                    buy = True
                    v_.potion_count = 0

                    for i in range(3):
                        result_confirm = all_confirms(cla)
                        if result_confirm == True:
                            break
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\jadong_buy.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(180, 740, 260, 780, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                time.sleep(0.5)
                                click_pos_2(535, 755, cla)
                        time.sleep(1)
                    clean_screen(cla)
                else:
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\it_is_buy_potion.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(290, 700, 370, 740, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                    else:
                        for i in range(2):
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\potion_point_" + str(i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(0, 270, 920, 800, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("potion_point_", str(i), imgs_)
                                click_pos_reg(imgs_.x, imgs_.y + 65, cla)
                            time.sleep(1)

                QTest.qWait(1000)
            for i in range(3):
                result_confirm = all_confirms(cla)
                if result_confirm == False:
                    break
                time.sleep(1)
    except Exception as e:
        print(e)
        return 0

def go_maul(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import out_check, game_loading_check, game_loading, all_confirms
    from clean_screen_chosun import clean_screen
    try:
        print("go_maul")

        buy_ready = False

        maul_ = False
        maul_count = 0
        while maul_ is False:
            maul_count += 1
            if maul_count > 13:
                maul_ = True



            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\map_all.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(30, 330, 110, 365, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("map_all", imgs_)

                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\dungeon_special.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(750, 270, 920, 350, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("dungeon_special", imgs_)
                    clean_screen(cla)

                    for i in range(10):
                        result_loading = game_loading_check(cla)
                        if result_loading == True:
                            game_loading(cla)
                            break
                        else:
                            result_confirm = all_confirms(cla)
                            if result_confirm == False:
                                click_pos_2(630, 350, cla)
                        QTest.qWait(1000)

                else:
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\jabhwa_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(650, 380, 850, 750, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("jabhwa_btn", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        time.sleep(0.5)

                        # 그다음 로딩화면
                        for i in range(10):
                            result_loading = game_loading_check(cla)
                            if result_loading == True:
                                game_loading(cla)
                                maul_ = True
                                buy_ready = True
                                break
                            else:
                                # 이동 누르기
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\move_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(720, 750, 800, 790, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\maul_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(650, 380, 700, 750, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("maul_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\maul_1.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(50, 360, 900, 800, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("maul_1", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\potion\\maul_2.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(50, 360, 900, 800, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("maul_2", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    click_pos_2(70, 350, cla)

            else:
                result_out = out_check(cla, "go_maul")
                if result_out == True:
                    click_pos_2(800, 385, cla)
                else:
                    clean_screen(cla)
            time.sleep(1)

        # if buy_ready == True:
        #     potion_buy(cla)

        return buy_ready

    except Exception as e:
        print(e)
        return 0