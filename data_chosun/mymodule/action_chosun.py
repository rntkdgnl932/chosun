import sys
import os
import time
import requests

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')


def game_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg
    from massenger import line_to_me
    from character_select_and_game_start import game_start_screen
    from schedule import myQuest_play_check
    try:

        is_checked = False
        is_start = False

        print("game_check")

        print("game_check before all_confirms")
        all_confirms(cla)

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\check\\game_check\\server_out_1.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 480, 570, 570, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("server_out_1", imgs_)
            is_checked = True
            why = "서버 연결 끊어짐"
        else:
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\check\\game_check\\server_out_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 480, 570, 570, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("server_out_2", imgs_)
                is_checked = True
                why = "서버 연결 끊어짐"
            else:
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\check\\game_check\\server_fix.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(360, 480, 570, 570, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("server_fix", imgs_)
                    is_checked = True
                    why = "서버 점검 중"

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\check\\game_check\\fix_complete.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 340, 540, 400, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("fix_complete", imgs_)
            is_checked = True
            why = "서버 점검 완료"

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\text_apply.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(340, 740, 580, 800, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("text_apply", imgs_)
            is_start = True
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\start_skip.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(740, 270, 930, 370, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("start_skip", imgs_)
            is_start = True

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\screen_touch_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(360, 630, 560, 700, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("screen_touch_btn", imgs_)
            is_start = True
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\join_ready_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(420, 430, 520, 480, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("join_ready_title", imgs_)
            is_start = True

        if is_checked is True:
            line_to_me(cla, why)
            dir_path = "C:\\my_games\\load\\" + str(v_.game_folder)
            file_path = dir_path + "\\start.txt"
            # cla.txt
            cla_data = str(cla) + "cla"
            file_path2 = dir_path + "\\" + cla_data + ".txt"
            with open(file_path, "w", encoding='utf-8-sig') as file:
                data = 'no'
                file.write(str(data))
                time.sleep(0.2)
            with open(file_path2, "w", encoding='utf-8-sig') as file:
                data = cla
                file.write(str(data))
                time.sleep(0.2)
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif is_start == True:

            result_schedule = myQuest_play_check(cla, "game_check")
            character_id = result_schedule[0][1]

            game_start_screen(cla, character_id)

    except Exception as e:
        print(e)

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
        imgs_ = imgs_set_(800, 580, 900, 650, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skip_1", imgs_)
            is_skip = True

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\skip\\skip_2.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(800, 580, 900, 650, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            print("skip_2", imgs_)
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
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\skip\\skip_2.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(800, 580, 900, 650, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("skip_2", imgs_)
                    is_skip = True
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
    from clean_screen_chosun import clean_screen
    from function_game import imgs_set_, click_pos_reg
    try:

        print("menu_open...game_check, clean_screen")

        game_check(cla)
        clean_screen(cla)

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
        game_check(cla)
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


def attack_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, text_check_get
    try:

        print("attack_check")

        is_attack = False

        result_out = out_check(cla, "attack_check")

        if result_out == True:


            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\attack_check\\auto_on.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 580, 500, 620, cla, img, 0.7)
                if imgs_ is not None and imgs_ != False:
                    print("auto_on", imgs_)
                    is_attack = True
                    break
                time.sleep(0.5)
        else:
            result_juljun = juljun_check(cla)
            if result_juljun == True:
                print("금화 등 비교하기")

                result_text_1 = text_check_get(825, 446, 888, 460, cla)
                # print("result_text_1", result_text_1)

                for i in range(20):
                    result_text_2 = text_check_get(825, 446, 888, 460, cla)
                    # print("result_text_2", result_text_2)
                    if result_text_1 != result_text_2:
                        print("사냥중이다.", result_text_1)
                        print("사냥중이다.", result_text_2)
                        is_attack = True
                        break
                    else:
                        print("사냥중인지 체크중")
                    time.sleep(0.5)

        return is_attack

    except Exception as e:
        print(e)


def attack_on(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_2, text_check_get
    from clean_screen_chosun import clean_screen
    try:

        print("attack_on")

        clean_screen(cla)
        click_pos_2(885, 655, cla)

        attack_start = False
        attack_start_count = 0

        while attack_start is False:
            attack_start_count += 1
            if attack_start_count > 10:
                attack_start = True

            is_attack = False

            result_out = out_check(cla, "attack_on")

            if result_out == True:


                for i in range(10):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\attack_check\\auto_on.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(420, 580, 500, 620, cla, img, 0.7)
                    if imgs_ is not None and imgs_ != False:
                        print("auto_on", imgs_)
                        is_attack = True
                        break
                    time.sleep(0.5)
            else:
                result_juljun = juljun_check(cla)
                if result_juljun == True:
                    print("금화 등 비교하기")

                    result_text_1 = text_check_get(825, 446, 888, 460, cla)
                    # print("result_text_1", result_text_1)

                    for i in range(20):
                        result_text_2 = text_check_get(825, 446, 888, 460, cla)
                        # print("result_text_2", result_text_2)
                        if result_text_1 != result_text_2:
                            print("사냥중이다.", result_text_1)
                            print("사냥중이다.", result_text_2)
                            is_attack = True
                            break
                        else:
                            print("사냥중인지 체크중")
                        time.sleep(0.5)

            if is_attack == False:
                result_juljun = juljun_check(cla)
                if result_juljun == False:
                    clean_screen(cla)
                    click_pos_2(885, 655, cla)
                else:
                    juljun_off(cla)
                    click_pos_2(885, 655, cla)
            else:
                attack_start = True

            QTest.qWait(1000)

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
            is_juljun = True


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