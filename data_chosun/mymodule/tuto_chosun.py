import time
# import os
import sys
from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def tuto_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import out_check, skip_start, skip_check, game_loading_check, game_loading
    from clean_screen_chosun import clean_screen_start

    try:
        print("tuto_start")

        result_loading = game_loading_check(cla)

        if result_loading == True:
            game_loading(cla)
        else:

            result_way = way_click_check(cla)
            if result_way == True:
                way_click(cla)
            else:

                result_out = out_check(cla, "tuto_start")
                if result_out == True:

                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\all_confirms\\notify_confirm.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(0, 270, 925, 800, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("notify_confirm", imgs_)
                        click_pos_reg(imgs_.x, imgs_.y, cla)

                    friend(cla)

                    result_q_btn = quest_btn(cla)
                    if result_q_btn == True:
                        for i in range(5):
                            result_skip = skip_check(cla)
                            if result_skip == True:
                                skip_start(cla)
                                break
                            else:
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\move_notisfy_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 270, 925, 800, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_notisfy_confirm", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)
                            time.sleep(0.5)
                    else:
                        is_attack = False
                        for i in range(5):
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\attack_check\\auto_on.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(420, 580, 500, 620, cla, img, 0.7)
                            if imgs_ is not None and imgs_ != False:
                                print("auto_on", imgs_)
                                is_attack = True
                                break
                            time.sleep(0.5)
                        if is_attack == True:
                            is_attack_count = 0
                            is_attack_countup = 0
                            while is_attack is True:
                                is_attack_countup += 1
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\attack_check\\auto_on.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(420, 580, 500, 620, cla, img, 0.7)
                                if imgs_ is not None and imgs_ != False:
                                    print("퀘스트 자동사냥 중", is_attack_countup, "초")
                                    time.sleep(0.5)
                                    if is_attack_count > 0:
                                        is_attack_count = 0
                                else:
                                    is_attack_count += 1
                                    if is_attack_count > 3:
                                        is_attack = False
                                time.sleep(0.5)
                        else:
                            for i in range(5):
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\move_notisfy.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(420, 430, 500, 480, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_notisfy", imgs_)
                                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\move_notisfy_confirm.PNG"
                                    img_array = np.fromfile(full_path, np.uint8)
                                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                    imgs_ = imgs_set_(0, 270, 925, 800, cla, img, 0.85)
                                    if imgs_ is not None and imgs_ != False:
                                        print("move_notisfy_confirm", imgs_)
                                        click_pos_reg(imgs_.x, imgs_.y, cla)
                                        break
                                else:
                                    click_pos_2(130, 375, cla)
                                time.sleep(0.5)
                else:
                    result_skip = skip_check(cla)
                    if result_skip == True:
                        skip_start(cla)
                    else:
                        result_reward = reward(cla)
                        if result_reward == False:
                            result_out = out_check(cla, "tuto_start, result_reward == False")
                            if result_out == False:
                                clean_screen_start(cla)


    except Exception as e:
        print(e)
        return 0


def way_click_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("way_click_check")

        way_btn = False


        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\down_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("down_1", imgs_)
            way_btn = True

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\right_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("right_1", imgs_)
            way_btn = True

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\left_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("left_1", imgs_)
            way_btn = True

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\up_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("left_1", imgs_)
            way_btn = True

        return way_btn

    except Exception as e:
        print(e)

def way_click(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("way_click")

        way_btn = True
        way_btn_count = 0
        while way_btn is True:
            way_btn_count += 1
            if way_btn_count > 7:
                way_btn = False

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\down_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("down_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y + 55, cla)
                if way_btn_count > 1:
                    way_btn_count -= 1

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\right_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("right_1", imgs_)
                click_pos_reg(imgs_.x + 65, imgs_.y, cla)
                if way_btn_count > 1:
                    way_btn_count -= 1

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\left_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("left_1", imgs_)
                click_pos_reg(imgs_.x - 70, imgs_.y, cla)
                if way_btn_count > 1:
                    way_btn_count -= 1

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\way_click\\up_1.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("left_1", imgs_)
                click_pos_reg(imgs_.x, imgs_.y - 50, cla)
                if way_btn_count > 1:
                    way_btn_count -= 1

            QTest.qWait(500)



    except Exception as e:
        print(e)

def reward(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    try:

        print("reward")

        is_reward = False

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\reward\\reward_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 260, 930, 820, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("reward_1", imgs_)
            click_pos_reg(imgs_.x, imgs_.y, cla)
            is_reward = True

        return is_reward



    except Exception as e:
        print(e)


def quest_btn(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_reg

    q_btn = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\quest_btn"
    q_btn_list = os.listdir(q_btn)

    try:

        print("quest_btn", len(q_btn_list))

        is_quest_btn = False

        for i in range(len(q_btn_list)):
            result_list = q_btn_list[i].split(".")
            read_data = result_list[0]

            print("quest_btn[i]", q_btn_list[i])

            # 종류 쭈욱 시작

            if str(read_data) != "2":
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\quest_btn\\" + str(read_data) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 270, 925, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("quest_btn_", str(read_data), imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_quest_btn = True
                    break
            else:
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\quest_btn\\" + str(
                    read_data) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(0, 270, 925, 800, cla, img, 0.9)
                if imgs_ is not None and imgs_ != False:
                    print("quest_btn_", str(read_data), imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    is_quest_btn = True
                    break



        return is_quest_btn



    except Exception as e:
        print(e)

def friend(cla):
    import numpy as np
    import cv2
    import os

    from function_game import imgs_set_, click_pos_2



    try:



        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\friend.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(0, 270, 925, 800, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("friend", imgs_)
            click_pos_2(465, 605, cla)
            time.sleep(0.5)


    except Exception as e:
        print(e)

