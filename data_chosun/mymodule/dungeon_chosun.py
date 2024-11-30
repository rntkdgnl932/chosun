import time
import os
import sys

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def dungeon_start(cla, data):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import out_check, juljun_off, all_confirms, game_loading_check, game_loading, attack_check, juljun_on, juljun_check, attack_on
    from potion_chosun import potion_check, potion_buy
    from dead_die import dead_check, dead_recovery
    from boonhae_collection import collection_start, boonhae_start


    try:
        print("dungeon_start", data)
        # 던전_부패한읍치, 던전_음양의귀성, 던전_조용한왕궁
        # 던전_버려진동굴 x
        # 던전_수련동굴

        result_spot = data.split("_")

        if result_spot[1] == "부패한읍치" or result_spot[1] == "음양의귀성" or result_spot[1] == "조용한왕궁":

            if result_spot[1] == "부패한읍치":
                spot = "boopae"
            elif result_spot[1] == "음양의귀성":
                spot = "umyang"
            elif result_spot[1] == "조용한왕궁":
                spot = "joyong"



            # 절전모드인지 확인
            result_juljun = juljun_check(cla)
            if result_juljun == True:
                # 소지품 개수 제한 초과
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\jadong\\juljun_check\\exceeded_limit.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(330, 360, 600, 430, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("exceeded_limit", imgs_)
                    #     collection_start, boonhae_start 대기중...
                else:
                    is_spot = False
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dungeon\\spot\\" + str(spot) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 340, 920, 380, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("spot...", str(spot), imgs_)
                        is_spot = True
                    if is_spot == False:
                        dungeon_spot(cla, data)
                    else:
                        # 절전을 한 상태에서 공격하는지 체크해야함.
                        juljun_on(cla)
                        result_attack = attack_check(cla)
                        if result_attack == True:
                            v_.jadong_count = 0
                            potion_check(cla)
                            result_dead = dead_check(cla, "자동사냥")
                            if result_dead == True:
                                potion_buy(cla)
                                dead_recovery(cla)
                        else:
                            attack_on(cla)
                            juljun_on(cla)

            else:
                all_confirms(cla)
                juljun_on(cla)
        elif result_spot[1] == "수련동굴":
            dungeon_spot(cla, data)


    except Exception as e:
        print(e)
        return 0

def dungeon_spot(cla, data):
    import numpy as np
    import cv2
    import random
    from function_game import imgs_set_, click_pos_reg, click_pos_2, imgs_set_for
    from action_chosun import out_check, juljun_off, all_confirms, game_loading_check, game_loading, menu_open, juljun_on, attack_on
    from clean_screen_chosun import clean_screen
    from schedule import myQuest_play_add
    from clean_screen_chosun import clean_screen

    try:
        print("dungeon_spot", data)

        juljun_off(cla)

        all_confirms(cla)

        # 던전_부패한읍치, 던전_음양의귀성, 던전_조용한왕궁
        # 던전_버려진동굴 x
        # 던전_수련동굴

        result_spot = data.split("_")

        spot = False
        spot_count = 0
        while spot is False:
            spot_count += 1
            if spot_count > 10:
                spot = True

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\dungeon.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(800, 270, 920, 350, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("menu_dungeon_btn", imgs_)

                # 던전_부패한읍치, 던전_음양의귀성, 던전_조용한왕궁
                # 던전_버려진동굴 x
                # 던전_수련동굴
                x_reg = 0
                x_1 = 0
                x_2 = 0
                if result_spot[1] == "부패한읍치" or result_spot[1] == "음양의귀성" or result_spot[1] == "조용한왕궁":
                    # click_pos_2(70, 350, cla)
                    x_reg = 70
                    if result_spot[1] == "부패한읍치":
                        x_1 = 60
                        x_2 = 180
                    elif result_spot[1] == "음양의귀성":
                        x_1 = 270
                        x_2 = 400
                    elif result_spot[1] == "조용한왕궁":
                        x_1 = 500
                        x_2 = 610

                    # 특수던전
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dungeon\\boopae.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(55, 610, 180, 670, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("boopae", imgs_)
                        print("x_1, x_2", x_1, x_2)
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dungeon\\special_lock.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_1, 530, x_2, 610, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("special_lock", imgs_)
                            myQuest_play_add(cla, data)
                            spot = True
                        else:
                            result_confirm = all_confirms(cla)
                            if result_confirm == False:
                                result_x = (x_1 + x_2) / 2
                                print("result_x", result_x)
                                click_pos_2(int(result_x), 560, cla)
                            else:
                                for i in range(5):
                                    result_out = out_check(cla, "dungeon_spot..")
                                    if result_out == True:
                                        spot = True
                                        break
                                    else:
                                        result_loading = game_loading_check(cla)
                                        if result_loading == True:
                                            game_loading(cla)
                                        else:
                                            all_confirms(cla)
                                    time.sleep(1)

                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\clean_screen\\close_1.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(600, 320, 660, 380, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("close_1", imgs_)
                                    myQuest_play_add(cla, data)
                                    spot = True
                                    clean_screen(cla)
                                else:
                                    attack_on(cla)
                                    juljun_on(cla)
                    else:
                        click_pos_2(x_reg, 350, cla)

                elif result_spot[1] == "수련동굴":

                    # click_pos_2(360, 350, cla)

                    x_reg = 360

                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dungeon\\soolyun_in_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(680, 720, 800, 760, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("soolyun_in_btn", imgs_)
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dungeon\\zero_five.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 720, 800, 760, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("zero_five", imgs_)
                            spot = True
                            myQuest_play_add(cla, data)
                            clean_screen(cla)
                        else:
                            for i in range(10):
                                result_out = out_check(cla, "dungeon_spot..")
                                if result_out == True:
                                    spot = True
                                    break
                                else:
                                    result_loading = game_loading_check(cla)
                                    if result_loading == True:
                                        game_loading(cla)
                                    else:
                                        result_confirm_2 = all_confirms(cla)
                                        if result_confirm_2 == False:
                                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dungeon\\soolyun_in_btn.PNG"
                                            img_array = np.fromfile(full_path, np.uint8)
                                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                            imgs_ = imgs_set_(680, 720, 800, 760, cla, img, 0.85)
                                            if imgs_ is not None and imgs_ != False:
                                                print("soolyun_in_btn", imgs_)
                                                click_pos_reg(imgs_.x, imgs_.y, cla)

                                time.sleep(1)

                            click_pos_2(885, 655, cla)

                            victory = False

                            for i in range(300):

                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dungeon\\soolyun_bosang.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(360, 410, 560, 510, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("soolyun_bosang", imgs_)
                                    victory = True
                                else:
                                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dungeon\\next_step.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(815, 355, 900, 390, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("next_step", imgs_)
                                        victory = True

                                if victory == True:
                                    click_pos_2(835, 345, cla)
                                else:
                                    result_loading = game_loading_check(cla)
                                    if result_loading == True:
                                        game_loading(cla)
                                        myQuest_play_add(cla, data)
                                        break
                                    else:
                                        all_confirms(cla)
                                time.sleep(1)
                            # 나가기 click_pos_2(835, 345, cla)
                            # 다음층 click_pos_2(835, 375, cla)
                            # 로딩
                    else:
                        click_pos_2(x_reg, 350, cla)


            else:
                is_dun = False
                for i in range(10):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\dungeon.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(800, 270, 920, 350, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("menu_dungeon_btn", imgs_)
                        is_dun = True
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\dungeon\\menu_dungeon_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(680, 360, 920, 530, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_dungeon_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            menu_open(cla)
                    time.sleep(1)
                if is_dun == False:
                    spot = True
            QTest.qWait(1000)



    except Exception as e:
        print(e)
        return 0
