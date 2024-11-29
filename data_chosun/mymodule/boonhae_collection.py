import time
# import os
import sys

from PyQt5.QtTest import *

import variable as v_

sys.path.append('C:/my_games/' + str(v_.game_folder) + '/' + str(v_.data_folder) + '/mymodule')



def collection_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import menu_open, all_confirms
    from clean_screen_chosun import clean_screen
    try:
        print("collection_start")

        bc = False
        bc_count = 0

        while bc is False:
            bc_count += 1
            if bc_count > 7:
                bc = True

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\jangbi_dogam.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(760, 270, 900, 340, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("title : jangbi_dogam", imgs_)
                result_confirm = all_confirms(cla)
                if result_confirm == True:
                    bc = True

                    for i in range(10):
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\boonhae_collection\\jangbi_dogam_complete.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(760, 270, 900, 340, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("jangbi_dogam_complete", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                            break
                        time.sleep(1)



                else:
                    click_pos_2(790, 765, cla)
                    time.sleep(0.5)
            else:
                menu_open(cla)

                for i in range(5):
                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\title\\jangbi_dogam.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(760, 270, 900, 340, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        break
                    else:
                        full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\boonhae_collection\\menu_jangbi_collection.PNG"
                        img_array = np.fromfile(full_path, np.uint8)
                        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                        imgs_ = imgs_set_(670, 380, 750, 460, cla, img, 0.8)
                        if imgs_ is not None and imgs_ != False:
                            print("menu_jangbi_collection", imgs_)
                            click_pos_reg(imgs_.x, imgs_.y, cla)
                    time.sleep(0.5)
            time.sleep(0.5)
        clean_screen(cla)



    except Exception as e:
        print(e)
        return 0



def boonhae_start(cla):
    import numpy as np
    import cv2
    from function_game import imgs_set_, click_pos_reg, click_pos_2
    from action_chosun import menu_open, all_confirms, bag_open
    from clean_screen_chosun import clean_screen
    try:
        print("boonhae_start")

        bc = False
        bc_count = 0

        while bc is False:
            bc_count += 1
            if bc_count > 10:
                bc = True

            full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\boonhae_collection\\boonhae_title.PNG"
            img_array = np.fromfile(full_path, np.uint8)
            img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
            imgs_ = imgs_set_(410, 330, 505, 370, cla, img, 0.8)
            if imgs_ is not None and imgs_ != False:
                print("boonhae_title", imgs_)

                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(357, 587, 385, 615, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("boonhae_checked_1", imgs_)

                    full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\boonhae_collection\\boonhae_checked.PNG"
                    img_array = np.fromfile(full_path, np.uint8)
                    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                    imgs_ = imgs_set_(357, 610, 385, 640, cla, img, 0.8)
                    if imgs_ is not None and imgs_ != False:
                        print("boonhae_checked_2", imgs_)

                        for i in range(5):
                            result_confirm = all_confirms(cla)
                            if result_confirm == True:
                                bc = True
                                break
                            else:
                                click_pos_2(530, 700, cla)
                            time.sleep(1)
                        if bc == True:
                            for i in range(10):
                                result_confirm = all_confirms(cla)
                                if result_confirm == True:
                                    break
                                time.sleep(1)

                    else:
                        click_pos_2(375, 625, cla)

                else:
                    click_pos_2(375, 600, cla)

            else:
                full_path = "c:\\my_games\\chosun\\data_chosun\\imgs\\action\\bag_open\\bag_boonhae_btn.PNG"
                img_array = np.fromfile(full_path, np.uint8)
                img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
                imgs_ = imgs_set_(715, 715, 820, 770, cla, img, 0.8)
                if imgs_ is not None and imgs_ != False:
                    print("bag_boonhae_btn", imgs_)
                    click_pos_reg(imgs_.x, imgs_.y, cla)


                else:
                    bag_open(cla)
            time.sleep(0.5)
        clean_screen(cla)



    except Exception as e:
        print(e)
        return 0

