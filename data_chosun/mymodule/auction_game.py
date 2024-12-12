import sys
import os
import time
import requests

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')




def mine_check(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number
    try:

        result_dia = 0
        result_silver = 0

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\dia_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("dia_reg", imgs_)

            result_text = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 45, imgs_.y + 8)
            result_text = change_number(result_text)
            result_dia = int_put_(result_text)
            result_dia_num = in_number_check(result_dia)
            print("result_text", result_dia_num, result_dia)

        full_path = "c:\\my_games\\arthdal\\data_arthdal\\imgs\\auction\\silver_reg.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(680, 30, 900, 80, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("silver_reg", imgs_)
            result_text2 = text_check_get_reg(imgs_.x + 8, imgs_.y - 10, imgs_.x + 70, imgs_.y + 8)
            result_text2 = change_number(result_text2)
            result_silver = int_put_(result_text2)
            result_silver_num = in_number_check(result_silver)
            print("result_text2", result_silver_num, result_silver)

        if result_dia_num == True:

            return result_silver, result_dia

    except Exception as e:
        print(e)


def auction_start(cla):
    import numpy as np
    import cv2

    from boonhae_collection import collection_start, boonhae_start
    try:
        # 아이템부터 정리 후
        collection_start(cla)
        boonhae_start(cla)

        # 거래소 들어가서 정산 후
        auction_in(cla)
        # 아이템 판매 등록 활성화하고 판매한다
        auction_sell_start(cla)

        # 다했으면 나간다.

    except Exception as e:
        print(e)

def auction_low_num(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number

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

    try:

        # text_check_get(365, 520, 433, 533, cla)

        is_point = False
        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\point.PNG"
        img_array = np.fromfile(full_path, np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        imgs_ = imgs_set_(365, 520, 433, 533, cla, img, 0.85)
        if imgs_ is not None and imgs_ != False:
            print("point", imgs_)
            is_point = True
            point_x = imgs_.x
        else:
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\point_2.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(365, 520, 433, 533, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print("point", imgs_)
                is_point = True
                point_x = imgs_.x
        num_find_front = False
        num_find_front_count = 0
        num_find_back = False
        num_find_back_count = 0

        x_reg_1 = 0
        this_price = ""
        if is_point == True:

            front_first_num = 0

            print("소수점 앞 자리, 가장 앞에 숫자 찾기")
            # 숫자 있는지 파악하기..
            print("숫자 있는지 파악하기..")
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(365, 512, point_x - plus, 533, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    x_reg_1 = imgs_.x
                    num_find_front = True
                    break
                else:
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(365, 512, point_x - plus, 533, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print(str(i), imgs_)
                        x_reg_1 = imgs_.x
                        num_find_front = True
                        break
            # 맨 앞 숫자 위치 파악하기
            print("맨 앞 숫자 위치 파악하기", x_reg_1)
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(365, 512, point_x - plus, 533, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    if x_reg_1 > imgs_.x:
                        x_reg_1 = imgs_.x
                else:
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(365, 512, point_x - plus, 533, cla, img, 0.88)
                    if imgs_ is not None and imgs_ != False:
                        print(str(i), imgs_)
                        if x_reg_1 > imgs_.x:
                            x_reg_1 = imgs_.x


            # 맨앞부터 숫자 찾아 돌려서 숫자 파악하기..
            print("맨앞부터 숫자 찾아 돌려서 숫자 파악하기..")
            while num_find_front is True:
                num_find_front_count += 1
                is_num = False

                if num_find_front_count == 1:
                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(
                            i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 5, 533, cla, img, 0.88)
                        if imgs_ is not None and imgs_ != False:
                            print("앞 1: ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                            if point_x > imgs_.x:
                                this_price += str(i)
                                x_reg_1 = imgs_.x + 4
                                is_num = True
                                break
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\" + str(
                            i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 5, 533, cla, img, 0.88)
                            if imgs_ is not None and imgs_ != False:
                                print("앞 2: ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                                if point_x > imgs_.x:
                                    this_price += str(i)
                                    x_reg_1 = imgs_.x + 4
                                    is_num = True
                                    break
                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 7, 533, cla, img, 0.88)
                        if imgs_ is not None and imgs_ != False:
                            print("앞 1: ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                            if point_x > imgs_.x:
                                this_price += str(i)
                                x_reg_1 = imgs_.x + 4
                                is_num = True
                                break
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\" + str(
                            i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 7, 533, cla, img, 0.88)
                            if imgs_ is not None and imgs_ != False:
                                print("앞 2: ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                                if point_x > imgs_.x:
                                    this_price += str(i)
                                    x_reg_1 = imgs_.x + 4
                                    is_num = True
                                    break
                if is_num == False:
                    num_find_front = False
                QTest.qWait(1000)

            #######
            this_price += str(".")
            back_first_num = 0
            ######
            print("소수점 뒷 자리, 가장 앞에 숫자 찾기")

            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(point_x - plus, 512, 433, 533, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    x_reg_1 = imgs_.x
                    num_find_back = True
                    break
            # 소수점 뒷자리 중 가장 앞 숫자 찾기
            print("소수점 뒷자리 중 가장 앞 숫자 찾기")
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(point_x - plus, 512, 433, 533, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    if x_reg_1 > imgs_.x:
                        x_reg_1 = imgs_.x

            # 소수점 뒷자리 중 맨앞부터 숫자 찾아 돌려서 숫자 파악하기..
            print("소수점 뒷자리 중 맨앞부터 숫자 찾아 돌려서 숫자 파악하기..", x_reg_1)
            while num_find_back is True:
                num_find_back_count += 1
                is_num = False

                if num_find_back_count == 1:
                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(
                            i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(point_x - plus, 512, x_reg_1 - plus + 4, 533, cla, img, 0.88)
                        if imgs_ is not None and imgs_ != False:
                            print("뒤 1: ", num_find_back_count, "번째 숫자 =>", str(i), imgs_)
                            x_reg_1 = imgs_.x + 4
                            this_price += str(i)
                            is_num = True
                            break
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\" + str(
                            i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(point_x - plus, 512, x_reg_1 - plus + 4, 533, cla, img, 0.88)
                            if imgs_ is not None and imgs_ != False:
                                print("뒤 2: ", num_find_back_count, "번째 숫자 =>", str(i), imgs_)
                                x_reg_1 = imgs_.x + 4
                                this_price += str(i)
                                is_num = True
                                break
                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 7, 533, cla, img, 0.88)
                        if imgs_ is not None and imgs_ != False:
                            print("뒤 1: ", num_find_back_count, "번째 숫자 =>", str(i), imgs_)
                            x_reg_1 = imgs_.x + 4
                            this_price += str(i)
                            is_num = True
                            break
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\" + str(i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 7, 533, cla, img, 0.88)
                            if imgs_ is not None and imgs_ != False:
                                print("뒤 2: ", num_find_back_count, "번째 숫자 =>", str(i), imgs_)
                                x_reg_1 = imgs_.x + 4
                                this_price += str(i)
                                is_num = True
                                break
                if is_num == False:
                    num_find_back = False
                QTest.qWait(1000)

        else:
            print("소수점 없을 경우 가장 앞에 숫자 및 가장 뒷 숫자 찾기")
            # 숫자 있는지 파악하기..
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(365, 512, 433, 533, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    x_reg_1 = imgs_.x
                    num_find_front = True
                    break
            # 맨 앞 숫자 위치 파악하기
            print("맨 앞 숫자 위치 파악하기")
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(365, 512, 433, 533, cla, img, 0.88)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    if x_reg_1 > imgs_.x:
                        x_reg_1 = imgs_.x

            # 맨앞부터 숫자 찾아 돌려서 숫자 파악하기..
            print("맨앞부터 숫자 찾아 돌려서 숫자 파악하기..")
            while num_find_front is True:
                num_find_front_count += 1
                is_num = False

                if num_find_front_count == 1:
                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(
                            i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 5, 533, cla, img, 0.88)
                        if imgs_ is not None and imgs_ != False:
                            print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                            x_reg_1 = imgs_.x + 4
                            this_price += str(i)
                            is_num = True
                            break
                else:

                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\low_price_num\\" + str(i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 8, 533, cla, img, 0.88)
                        if imgs_ is not None and imgs_ != False:
                            print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                            x_reg_1 = imgs_.x + 4
                            this_price += str(i)
                            is_num = True
                            break
                        else:
                            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\low_price_num\\" + str(
                            i) + ".PNG"
                            img_array = np.fromfile(full_path, np.uint8)
                            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                            imgs_ = imgs_set_(x_reg_1 - plus - 4, 512, x_reg_1 - plus + 8, 533, cla, img, 0.88)
                            if imgs_ is not None and imgs_ != False:
                                print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                                x_reg_1 = imgs_.x + 4
                                this_price += str(i)
                                is_num = True
                                break
                if is_num == False:
                    num_find_front = False
                QTest.qWait(1000)


        print("this_price", this_price)
        return this_price
    except Exception as e:
        print(e)


def auction_qun_num(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, text_check_get_reg, in_number_check, int_put_, change_number

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

    try:
        print("auction_qun_num")
        # text_check_get(365, 520, 433, 533, cla)

        num_find_front = False
        num_find_front_count = 0

        x_reg_1 = 0
        this_price = ""
        # 숫자 있는지 파악하기..
        for i in range(10):
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\qun_price_num\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(500, 400, 615, 430, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print(str(i), imgs_)
                x_reg_1 = imgs_.x
                num_find_front = True
                break
            else:
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\qun_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(500, 400, 615, 430, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    x_reg_1 = imgs_.x
                    num_find_front = True
                    break
        # 맨 앞 숫자 위치 파악하기
        print("맨 앞 숫자 위치 파악하기")
        for i in range(10):
            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\qun_price_num\\" + str(i) + ".PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(555, 400, 615, 430, cla, img, 0.85)
            if imgs_ is not None and imgs_ != False:
                print(str(i), imgs_)
                if x_reg_1 > imgs_.x:
                    x_reg_1 = imgs_.x
            else:
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\qun_price_num\\" + str(i) + ".PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(555, 400, 615, 430, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print(str(i), imgs_)
                    if x_reg_1 > imgs_.x:
                        x_reg_1 = imgs_.x

        # 맨앞부터 숫자 찾아 돌려서 숫자 파악하기..
        print("맨앞부터 숫자 찾아 돌려서 숫자 파악하기..")
        while num_find_front is True:
            num_find_front_count += 1
            is_num = False

            if num_find_front_count == 1:
                for i in range(10):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\qun_price_num\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_reg_1 - plus - 4, 400, x_reg_1 - plus + 5, 430, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                        x_reg_1 = imgs_.x + 4
                        this_price += str(i)
                        is_num = True
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\qun_price_num\\" + str(
                            i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 400, x_reg_1 - plus + 5, 430, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                            x_reg_1 = imgs_.x + 4
                            this_price += str(i)
                            is_num = True
                            break

            else:

                for i in range(10):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\qun_price_num\\" + str(i) + ".PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(x_reg_1 - plus - 4, 400, x_reg_1 - plus + 11, 430, cla, img, 0.85)
                    if imgs_ is not None and imgs_ != False:
                        print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                        x_reg_1 = imgs_.x + 4
                        this_price += str(i)
                        is_num = True
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\etc\\qun_price_num\\" + str(
                            i) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(x_reg_1 - plus - 4, 400, x_reg_1 - plus + 11, 430, cla, img, 0.85)
                        if imgs_ is not None and imgs_ != False:
                            print("소수점없음 : ", num_find_front_count, "번째 숫자 =>", str(i), x_reg_1, imgs_)
                            x_reg_1 = imgs_.x + 4
                            this_price += str(i)
                            is_num = True
                            break

            if is_num == False:
                num_find_front = False
            QTest.qWait(1000)


        print("this_qun", this_price)



        return this_price
    except Exception as e:
        print(e)



def auction_in(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action_chosun import menu_open

    try:
        print("auction_in")

        air = False
        air_count = 0
        while air is False:
            air_count += 1
            print("auction_in : air_count", air_count)
            if air_count > 10:
                air = True


            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 280, 900, 330, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                # 정산
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\all_get.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(510, 750, 630, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.2)
                    click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
                    click_pos_2(880, 390, cla)
                    air = True

                else:
                    click_pos_2(220, 350, cla)

            else:

                menu_open(cla)


                for i in range(5):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\auction.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 280, 900, 330, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\menu_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(810, 380, 920, 460, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

            QTest.qWait(1000)
    except Exception as e:
        print(e)


def auction_sell_start(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action_chosun import menu_open

    my_item = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\list_item"
    file_list = os.listdir(my_item)

    try:
        print("auction_sell_start")

        air = False
        air_count = 0
        while air is False:
            air_count += 1
            print("auction_sell_start : air_count", air_count)
            if air_count > 10:
                air = True


            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\auction.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(750, 280, 900, 330, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:

                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\all_get.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(510, 750, 630, 800, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(880, 390, cla)
                    QTest.qWait(1000)
                    click_pos_2(880, 390, cla)
                    QTest.qWait(1000)
                    click_pos_2(880, 390, cla)
                    QTest.qWait(1000)
                    air = True

                    for i in range(len(file_list)):
                        result_file_list = file_list[i].split(".")
                        read_data = result_file_list[0]

                        is_jangbi = False

                        # 종류 쭈욱 시작
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\list_item\\" + str(
                            read_data) + ".PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(750, 130, 950, 1000, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("item...", str(read_data), imgs_)
                            x_reg_item = imgs_.x
                            y_reg_item = imgs_.y
                            is_jangbi = True

                        if is_jangbi == True:
                            print("팔자")

                            for s in range(5):
                                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\auction_sell_title.PNG"
                                img_array = np.fromfile(full_path, np.uint8)
                                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                                imgs_ = imgs_set_(410, 330, 510, 380, cla, img, 0.8)
                                if imgs_ is not None and imgs_ != False:
                                    sell_registery(cla)
                                    break
                                else:
                                    click_pos_reg(x_reg_item, y_reg_item, cla)
                                time.sleep(0.5)

                            QTest.qWait(1000)


                else:
                    click_pos_2(220, 350, cla)

            else:

                menu_open(cla)


                for i in range(5):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\auction.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(750, 280, 900, 330, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\menu_auction.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(810, 380, 920, 460, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)

            QTest.qWait(1000)
    except Exception as e:
        print(e)


def sell_registery(cla):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action_chosun import menu_open, all_confirms

    my_item = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\list_item"
    file_list = os.listdir(my_item)

    try:
        print("sell_registery")

        s_r = True
        s_r_count = 0

        while s_r is True:

            s_r_count += 1
            if s_r_count > 5:
                s_r = False

            # 최대수량 적기
            for i in range(10):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\auction_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(830, 730, 920, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("auction_confirm", imgs_)
                    click_pos_2(660, 615, cla)
                    time.sleep(0.5)
                    click_pos_2(660, 615, cla)
                    break
                else:
                    click_pos_2(380, 595, cla)
                QTest.qWait(1000)

            click_pos_2(660, 615, cla)
            time.sleep(0.5)
            click_pos_2(660, 615, cla)

            result_auction_low_num = auction_low_num(cla)
            result_auction_qun_num = auction_qun_num(cla)

            result = float(result_auction_low_num) * float(result_auction_qun_num)
            print("result", result)
            result = int(result)
            print("result", result)
            result_str = str(result)

            # 산정한 판매금액 입력하기
            for i in range(5):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\auction_confirm.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(830, 730, 920, 800, cla, img, 0.85)
                if imgs_ is not None and imgs_ != False:
                    print("auction_confirm", imgs_)
                    click_pos_2(505, 620, cla)
                    time.sleep(0.5)
                    click_pos_2(505, 620, cla)
                    break
                else:
                    click_pos_2(380, 635, cla)
                QTest.qWait(1000)

            if result > 10:
                result_equl = sell_registery_price(cla, result_str)

                if result_equl == True:
                    s_r = False
                QTest.qWait(1000)
            else:
                for s in range(5):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\auction_sell_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 330, 510, 380, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        click_pos_2(385, 705, cla)
                    else:
                        s_r = False
                        break
                    QTest.qWait(1000)

        if s_r == False:
            for s in range(5):
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\auction_sell_title.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(410, 330, 510, 380, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    click_pos_2(385, 705, cla)
                else:
                    break
                QTest.qWait(1000)
    except Exception as e:
        print(e)


def sell_registery_price(cla, result_str):
    import numpy as np
    import cv2

    from function_game import imgs_set_, click_pos_reg, click_pos_2, int_put_, change_number
    from action_chosun import menu_open, all_confirms

    my_item = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\list_item"
    file_list = os.listdir(my_item)

    try:
        print("sell_registery_price")

        equl_price = False
        equl_price_count = 0

        while equl_price is False:
            equl_price_count += 1
            if equl_price_count > 7:
                equl_price = True

            for i in range(len(result_str)):
                print("가격 누르자", i + 1, result_str[i])

                if result_str[i] == "0":
                    x_reg = 585
                    y_reg = 615
                else:
                    # x 값 구하기
                    if result_str[i] == "1" or result_str[i] == "4" or result_str[i] == "7":
                        x_reg = 505
                    elif result_str[i] == "2" or result_str[i] == "5" or result_str[i] == "8":
                        x_reg = 585
                    elif result_str[i] == "3" or result_str[i] == "6" or result_str[i] == "9":
                        x_reg = 665

                    # y 값 구하기
                    if result_str[i] == "1" or result_str[i] == "2" or result_str[i] == "3":
                        y_reg = 570
                    elif result_str[i] == "4" or result_str[i] == "5" or result_str[i] == "6":
                        y_reg = 520
                    elif result_str[i] == "7" or result_str[i] == "8" or result_str[i] == "9":
                        y_reg = 470
                click_pos_2(x_reg, y_reg, cla)
                QTest.qWait(1000)
            # 가격 수정 후 맞는지 최종확인
            if int(result_str) == int(auction_qun_num(cla)):
                print("등록 누르면 된다.")
                for r in range(7):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\auction_sell_title.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(410, 330, 510, 380, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        all_confirms(cla)
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\auction\\registery_confirm_title.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(410, 400, 510, 440, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            all_confirms(cla)
                        else:
                            equl_price = True
                            break
                    time.sleep(0.5)

            else:
                print("가격 다시 누르자...")
                click_pos_2(505, 620, cla)
                QTest.qWait(1000)
            QTest.qWait(1000)
        return equl_price
    except Exception as e:
        print(e)