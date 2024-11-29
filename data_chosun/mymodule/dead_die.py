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
    from action_chosun import game_loading_check, game_loading, juljun_off, skip_start
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
        imgs_ = imgs_set_(300, 700, 800, 800, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("boohwal_btn", imgs_)

            skip_start(cla)

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

def dead_recovery(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from clean_screen_chosun import clean_screen
    from action_chosun import all_confirms, menu_open
    from massenger import line_to_me

    try:
        print("dead_recovery")
        bc = False
        bc_count = 0

        while bc is False:
            bc_count += 1
            if bc_count > 10:
                bc = True

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\dead_recorvery_experience.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(5, 335, 70, 370, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("dead_recorvery_experience", imgs_)

                bc = True

                # 첫번째
                click_pos_2(60, 350, cla)
                time.sleep(0.2)

                click_pos_2(60, 350, cla)
                time.sleep(0.2)

                click_pos_2(60, 350, cla)
                time.sleep(0.2)

                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\not_recorvery.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 500, 250, 565, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("not_recorvery", imgs_)

                else:
                    not_free = False
                    for i in range(10):

                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\not_recorvery.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 500, 250, 565, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("not_recorvery", imgs_)
                            break
                        else:
                            result_confirm = all_confirms(cla)
                            if result_confirm == False:
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\free_recorvery_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(100, 720, 190, 760, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("free_recorvery_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                else:
                                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\not_free_recorvery_btn.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(100, 720, 190, 760, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("not_free_recorvery_btn", imgs_)

                                        not_free = True

                                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\gold_checked.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(225, 690, 270, 730, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            print("gold_checked", imgs_)
                                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\not_free_recorvery_btn.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(100, 720, 190, 760, cla, img, 0.8)
                                            if imgs_ is not None and imgs_ != False:
                                                click_pos_reg(imgs_.x, imgs_.y, cla)
                                        else:
                                            click_pos_2(260, 710, cla)



                        QTest.qWait(1000)
                    # if not_free == True:
                    #     why = "경험치 무료복구 없다!!!"
                    #     line_to_me(cla, why)

                # 두번째
                click_pos_2(140, 350, cla)
                time.sleep(0.2)
                click_pos_2(140, 350, cla)
                time.sleep(0.2)

                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\not_recorvery.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(40, 500, 250, 565, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("not_recorvery", imgs_)

                else:
                    for i in range(8):

                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\not_recorvery.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(40, 500, 250, 565, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("not_recorvery", imgs_)
                            break
                        else:
                            result_confirm = all_confirms(cla)
                            if result_confirm == False:
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\not_free_recorvery_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(100, 720, 190, 760, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    print("not_free_recorvery_btn..2", imgs_)

                                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\gold_checked.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(225, 690, 270, 730, cla, img, 0.8)
                                    if imgs_ is not None and imgs_ != False:
                                        print("gold_checked", imgs_)
                                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\not_free_recorvery_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(100, 720, 190, 760, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            click_pos_reg(imgs_.x, imgs_.y, cla)
                                    else:
                                        click_pos_2(260, 710, cla)
                        QTest.qWait(1000)
            else:
                menu_open(cla)

                is_recorvery = False

                for i in range(5):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\dead_recorvery_experience.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(5, 335, 70, 370, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\google_play.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(45, 290, 170, 370, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            bc = True
                            break
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\menu_open\\menu_setting.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(840, 730, 920, 800, cla, img, 0.85)
                            if imgs_ is not None and imgs_ != False:
                                print("dead_recorvery : menu_setting", imgs_)
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\recorvery_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(640, 270, 700, 330, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("recorvery_btn", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                                    is_recorvery = True
                    time.sleep(0.5)

                if is_recorvery == False:
                    bc = True

            time.sleep(0.5)
        for i in range(10):
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dead_die\\google_play.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(45, 290, 170, 370, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                click_pos_2(940, 915, cla)
            else:
                break
            time.sleep(1)

        clean_screen(cla)



    except Exception as e:
        print(e)
        return 0

