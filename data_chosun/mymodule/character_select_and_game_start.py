import sys
import os
import time

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')

def game_start_screen(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from massenger import line_to_me


    try:

        # 실수로 새 캐릭터 클릭시...
        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\game_start\\create_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:
            # 이건 잘못 클릭시 나가기
            print("create_btn", imgs_)

            for i in range(10):
                full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\game_start\\start_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    break
                else:
                    full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                        v_.data_folder) + "\\imgs\\game_start\\create_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        # 이건 잘못 클릭시 나가기
                        click_pos_2(90, 305, cla)
                time.sleep(0.5)
        else:

            text_apply = False

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\text_apply.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(340, 740, 580, 800, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("text_apply", imgs_)
                text_apply = True
                text_apply_count = 0
                text_apply_count_second = 0
                while text_apply is True:
                    text_apply_count_second += 1
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\text_apply.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 740, 580, 800, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("text_apply : 로딩중", text_apply_count_second, "초")
                        if text_apply_count > 0:
                            text_apply_count -= 1
                    else:
                        text_apply_count += 1
                        if text_apply_count > 3:
                            text_apply = False
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\screen_touch_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(360, 630, 560, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                text_apply = False
                            else:
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\start_skip.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(740, 270, 930, 370, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    text_apply = False
                    time.sleep(1)
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\start_skip.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(740, 270, 930, 370, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("start_skip", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

                start_skip = True
                start_skip_count = 0
                start_skip_count_second = 0
                while start_skip is True:
                    start_skip_count_second += 1
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\start_skip.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(340, 740, 580, 800, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("start_skip : 로딩중", start_skip_count_second, "초")
                        click_pos_reg(imgs_.x, imgs_.y, cla)
                        if start_skip_count > 0:
                            start_skip_count -= 1
                    else:
                        start_skip_count += 1
                        if start_skip_count > 3:
                            start_skip = False
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\screen_touch_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(360, 630, 560, 700, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                start_skip = False
                    time.sleep(1)

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\screen_touch_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(360, 630, 560, 700, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("screen_touch_btn", imgs_)
                click_pos_reg(imgs_.x, imgs_.y, cla)

                screen_touch_btn = True
                screen_touch_btn_count = 0
                while screen_touch_btn is True:
                    screen_touch_btn_count += 1
                    if screen_touch_btn_count > 7:
                        screen_touch_btn = False
                        why = "게임선택 시작에 문제 있다."
                        line_to_me(cla, why)
                    full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                        v_.data_folder) + "\\imgs\\game_start\\start_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        screen_touch_btn = False
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\screen_touch_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(360, 630, 560, 700, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("screen_touch_btn", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                        else:
                            game_ready(cla)
                    time.sleep(1)
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\join_ready_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(420, 430, 520, 480, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                game_ready(cla)

        # 캐릭터 선택 화면
        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
            v_.data_folder) + "\\imgs\\game_start\\start_btn.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
        if imgs_ is not None and imgs_ != False:

            character_change(cla, character_id)

        else:
            dir_path = "C:\\my_games\\" + str(v_.game_folder) + ""
            if cla == 'one':
                file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
            if cla == 'two':
                file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
            if cla == 'three':
                file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
            if cla == 'four':
                file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"

            same = False

            if os.path.isfile(file_path) == True:
                with open(file_path, "r", encoding='utf-8-sig') as file:
                    read_id = file.read()
                    if str(character_id) == str(read_id):
                        # 메뉴 안 열어도 됨
                        same = True
            if same == False:
                character_change(cla, character_id)


    except Exception as e:
        print(e)

def character_change(cla, character_id):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2

    from action_chosun import game_loading_check, out_check, menu_open, game_loading
    from clean_screen_chosun import clean_screen

    from massenger import line_to_me
    try:



        print(str(character_id), "번으로 캐릭터 체인지")


        cha_select = False
        cha_select_count = 0
        while cha_select is False:
            cha_select_count += 1
            if cha_select_count > 10:
                cha_select = True
                line_to_me(cla, "처음 스타트 화면에 문제가 있다.")

            # 실수로 새 캐릭터 클릭시...
            full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                v_.data_folder) + "\\imgs\\game_start\\create_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                # 이건 잘못 클릭시 나가기
                print("create_btn", imgs_)

                for i in range(10):
                    full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                        v_.data_folder) + "\\imgs\\game_start\\start_btn.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                            v_.data_folder) + "\\imgs\\game_start\\create_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            # 이건 잘못 클릭시 나가기
                            click_pos_2(90, 305, cla)
                    time.sleep(0.5)

            # 저장된 캐릭 번호 불러오기
            dir_path = "C:\\my_games\\" + str(v_.game_folder) + ""
            if cla == 'one':
                file_path = dir_path + "\\mysettings\\myschedule\\one_now_id.txt"
            if cla == 'two':
                file_path = dir_path + "\\mysettings\\myschedule\\two_now_id.txt"
            if cla == 'three':
                file_path = dir_path + "\\mysettings\\myschedule\\three_now_id.txt"
            if cla == 'four':
                file_path = dir_path + "\\mysettings\\myschedule\\four_now_id.txt"

            # 캐릭터 선택 화면

            full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                v_.data_folder) + "\\imgs\\game_start\\start_btn.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                x_reg = imgs_.x
                y_reg = imgs_.y

                # select 1 (780, 360)
                # select 2 (780, 425)490...

                character_id_y = 295 + (int(character_id) * 65)

                click_pos_2(780, character_id_y, cla)
                time.sleep(0.1)
                click_pos_2(780, character_id_y, cla)

                time.sleep(0.5)
                click_pos_reg(x_reg, y_reg, cla)
                time.sleep(0.1)

                #진입 버튼 누르면서 캐릭번호 저장하기
                save = False
                save_count = 0
                while save is False:
                    save_count += 1
                    if save_count > 15:
                        save = True
                    if os.path.isfile(file_path) == True:
                        with open(file_path, "r", encoding='utf-8-sig') as file:
                            read_id = file.read()
                            if str(character_id) == str(read_id):
                                save = True
                            else:
                                with open(file_path, "w", encoding='utf-8-sig') as file:
                                    file.write(str(character_id))
                            time.sleep(0.3)
                    else:
                        with open(file_path, "w", encoding='utf-8-sig') as file:
                            file.write(str(character_id))

                # 대기 화면 있는지 확인하면서 진입확인하기
                joined = False
                joined_count = 0
                while joined is False:
                    joined_count += 1
                    if joined_count > 15:
                        joined = True

                    result_out = out_check(cla, "character_change")
                    if result_out == True:
                        joined = True
                        cha_select = True

                        print("게임 접속 끝")
                        time.sleep(0.1)

                        # 먼저 물약부터 채우기

                       # # 1번 캐릭은 이벤트 받기
                        # full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(v_.data_folder) + "\\imgs\\get_items\\event_title.PNG"
                        # img_array = np.fromfile(full_path, np.uint8)
                        # img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        # imgs_ = imgs_set_(400, 300, 545, 345, cla, img, 0.8)
                        # if imgs_ is not None and imgs_ != False:
                        #
                        #     if int(character_id) == 1:
                        #         get_event(cla)
                        #
                        #     else:
                        #         get_event_sub(cla)

                    else:
                        # 로딩중 확인

                        result_loading = game_loading_check(cla)
                        if result_loading == True:
                            game_loading(cla)
                    time.sleep(1)
            else:
                # 캐릭 번호와 체인지 하려는 번호 비교하기

                same = False

                if os.path.isfile(file_path) == True:
                    with open(file_path, "r", encoding='utf-8-sig') as file:
                        read_id = file.read()
                        if str(character_id) == str(read_id):
                            # 메뉴 안 열어도 됨
                            same = True
                            cha_select = True
                if same == False:

                    # # 포션만 채우기(수집 분해도 함)
                    # maul_potion_small_only(cla)
                    #
                    # # 장비 빼기
                    # chango_action(cla, "jangbi_in")

                    # 메뉴 열기
                    menu_open(cla)

                    # 캐릭선택화면까지...
                    for t in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\setting.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(800, 280, 900, 350, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("title_setting", imgs_)

                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\setting_character_select_btn.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(640, 740, 770, 790, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("setting_character_select_btn", imgs_)
                                c_s_btn_x = imgs_.x
                                c_s_btn_y = imgs_.y
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\tuto\\tuto_start\\move_notisfy_confirm.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(0, 270, 925, 800, cla, img, 0.85)
                                if imgs_ is not None and imgs_ != False:
                                    print("move_notisfy_confirm", imgs_)
                                    click_pos_reg(imgs_.x, imgs_.y, cla)

                                    for i in range(10):
                                        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                                            v_.data_folder) + "\\imgs\\game_start\\start_btn.PNG"
                                        img_array = np.fromfile(full_path, np.uint8)
                                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                        imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
                                        if imgs_ is not None and imgs_ != False:
                                            break
                                        time.sleep(1)
                                else:
                                    click_pos_reg(c_s_btn_x, c_s_btn_y, cla)


                            else:
                                click_pos_2(505, 350, cla)
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\menu_open\\menu_setting.PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(840, 730, 920, 800, cla, img, 0.8)
                            if imgs_ is not None and imgs_ != False:
                                print("menu_setting", imgs_)
                                click_pos_reg(imgs_.x, imgs_.y, cla)
                            else:
                                full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                                    v_.data_folder) + "\\imgs\\game_start\\start_btn.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    break

                        time.sleep(1)

                else:
                    print("같은 번호의 캐릭이라서 체인지 안함")

    except Exception as e:
        print(e)

def game_ready(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_
    from action_chosun import game_loading_check, out_check, game_loading
    from massenger import line_to_me

    try:

        # 접속대기일 경우 기다리기
        print("game_ready")

        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\join_ready_title.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(420, 430, 520, 480, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("join_ready_title", imgs_)
            game_ready = True
            game_ready_count = 0
            while game_ready is True:

                game_ready_count += 1

                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\game_start\\join_ready_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(420, 430, 520, 480, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("기다리는중...", game_ready_count, "초")
                else:
                    result_loading = game_loading_check(cla)
                    if result_loading == True:
                        game_loading(cla)

                    else:
                        full_path = "c:\\my_games\\" + str(v_.game_folder) + "\\" + str(
                            v_.data_folder) + "\\imgs\\game_start\\start_btn.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(700, 730, 820, 800, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            game_ready = False
                            why = str(game_ready_count) + "초 기다리고 접속했다."
                            line_to_me(cla, why)
                time.sleep(1)



    except Exception as e:
        print(e)