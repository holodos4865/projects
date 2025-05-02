import time
from random import randint
from colorama import Fore

users_date = {


}
login_and_paswords_users_date = {

}
promo_for_mon = {
    "Welcome":5000,
    "I_UDXie9G":75000,
    "1bhQ!-x%s":5000000
}
promo_for_level = {
    "S'UB't8_&F":50
}
promo_for_buisness = {
    "Casino_TUdbI9T>u_FVYBX{12C$#gaf&]":"казино"
}
city = ["0.Москва","1.Пермь","2.Сочи","3.Питер-бург","4.Владивосток"]
maps={
    "0": "Москва",
    "1": "Пермь",
    "2": "Сочи",
    "3": "Питер-бург",
    "4": "Владивосток"
}
From_Moscow = {
    "1":19,
    "2":14,
    "3":9,
    "4":16
}
From_Perm ={
    "0":19,
    "2":5,
    "3":10,
    "4":3
}
From_Sochi = {
    "0":14,
    "3":5,
    "4":2,
    "1":5,
}
From_Piter_Burg = {
    "0":9,
    "1":10,
    "2":5,
    "4":7
}
From_Vladivostok = {
    "0":16,
    "1":3,
    "2":2,
    "3":7

}
color_casino = {
    '0': 'green', 
    '1': 'red', '2': 'black', '3': 'red', '4': 'black', '5': 'red', '6': 'black',
    '7': 'red', '8': 'black', '9': 'red', '10': 'black', '11': 'black', '12': 'red',
    '13': 'black', '14': 'red', '15': 'black', '16': 'red', '17': 'black', '18': 'red',
    '19': 'red', '20': 'black', '21': 'red', '22': 'black', '23': 'red', '24': 'black',
    '25': 'red', '26': 'black', '27': 'red', '28': 'black', '29': 'black', '30': 'red',
    '31': 'black', '32': 'red', '33': 'black', '34': 'red', '35': 'black', '36': 'red'
}
automat_casino = ['🍒','🍓','🍌','🍋','🍉','🎰']
buisnesses = {
    "шаурмичная лавка":{
        "стоимость":75000,
        "прибыль в 30сек":350
    },
    "автомойка":{
        "стоимость":170000,
        "прибыль в 30сек":900
    },
    "магази продуктов":{
        "стоимость":250000,
        "прибыль в 30сек":1500
    },
    "отель(⭐⭐⭐)":{
        "стоимость":395000,
        "прибыль в 30сек":2700
    },
    "отель(⭐⭐⭐⭐)":{
        "стоимость":473000,
        "прибыль в 30сек":5100
    },
    "отель(⭐⭐⭐⭐⭐)":{
        "стоимость":600000,
        "прибыль в 30сек":8000
    },
    "казино":{
        "стоимость":850000,
        "прибыль в 30сек":12000
    },
    "торговый центр":{
        "стоимость":1000000,
        "прибыль в 30сек":17500
    }
}
nicknames= ["xuerty","rasa_ds","IWIGOFAMYGAM","DYSUROC","MEXUZI","MOCETIL","ZELUNIP","POKIZI"]
pas_hack = ['760533',
'427973',
'706537',
'588736',
'992337',
'845047',
'164436',
'786132']
pc_com = ['видеокарта','процесор','оперативная память','кулер','материнская плата','ссд накопитель','блок питания','корпус','охлаждение']
def sport_shop(login):
    while True:
        print("ты в магазине для спорта")
        print("в катологе:")
        print("1 - гири 10кг(7500р)")
        print("2 - мячи(3300р)")
        print("3 - спортивные кроссы(15000р)")
        print("4 - велосипед(35000р)")
        print("5 - самокат(11500р)")
        print("6 - баскебольное кольцо(250000р)")
        cl_us = input("введи число одежды")
        if cl_us == '1':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=7500:
                    users_date[login]["money"] -=7500
                    users_date[login]["inventary"].append("гири 10кг")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '2':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=3300:
                    users_date[login]["money"] -=3300
                    users_date[login]["inventary"].append("мячи")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '3':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=15000:
                    users_date[login]["money"] -=15000
                    users_date[login]["inventary"].append("спортивные кроссы")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '4':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=35000:
                    users_date[login]["money"] -=35000
                    users_date[login]["inventary"].append("велосипед")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '5':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=11500:
                    users_date[login]["money"] -=11500
                    users_date[login]["inventary"].append("самокат")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '6':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=250000:
                    users_date[login]["money"] -=250000
                    users_date[login]["inventary"].append("баскетбольное кольцо")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        else:
            break
def art_shop(login):
    while True:
        print("ты в магазине для творцества")
        print("в катологе:")
        print("1 - краски(750р)")
        print("2 - палитра(349р)")
        print("3 - кисточки(855р)")
        print("4 - цв карандаши(700р)")
        print("5 - фломастеры(1150р)")
        print("6 - холст(4250р)")
        cl_us = input("введи число одежды")
        if cl_us == '1':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=750:
                    users_date[login]["money"] -=750
                    users_date[login]["inventary"].append("краски")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '2':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=349:
                    users_date[login]["money"] -=349
                    users_date[login]["inventary"].append("палитра")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '3':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=855:
                    users_date[login]["money"] -=855
                    users_date[login]["inventary"].append("кисточки")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '4':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=700:
                    users_date[login]["money"] -=700
                    users_date[login]["inventary"].append("цв карандаши")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '5':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=1150:
                    users_date[login]["money"] -=1150
                    users_date[login]["inventary"].append("фломастеры")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '6':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=4250:
                    users_date[login]["money"] -=4250
                    users_date[login]["inventary"].append("холст")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        else:
            break
def food_shop(login):
    while True:
        print("ты в магазине еды")
        print("в катологе:")
        print("1 - хлеб(275р)")
        print("2 - чипсы(420р)")
        print("3 - кока кола добрый(150р)")
        print("4 - молоко(299р)")
        print("5 - овощи и фрукты(1150р)")
        print("6 - балтика 7(250р)")
        cl_us = input("введи число одежды")
        if cl_us == '1':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >= 275:
                    users_date[login]["money"] -= 275
                    users_date[login]["havchic"].append("хлеб")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '2':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >= 420:
                    users_date[login]["money"] -= 420
                    users_date[login]["havchic"].append("чипсы")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '3':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >= 150:
                    users_date[login]["money"] -= 150
                    users_date[login]["havchic"].append("кока кола добрый")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '4':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >= 299:
                    users_date[login]["money"] -= 299
                    users_date[login]["havchic"].append("молоко")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '5':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >= 1150:
                    users_date[login]["money"] -= 1150
                    users_date[login]["havchic"].append("овощи и фрукты")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '6':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >= 250:
                    users_date[login]["money"] -= 250
                    users_date[login]["havchic"].append("балтика 7")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        else:
            break
def electro_shop(login):
    while True:
        print("ты в магазине электроники")
        print("в катологе:")
        print("1 - айфон(75000р)")
        print("2 - пс5(67000р)")
        print("3 - мега ультра ноутбук игровой(15000р)")
        print("4 - комп игровой(200000р)")
        print("5 - телик 8k(115000р)")
        print("6 - эпл ватч(25000р)")
        cl_us = input("введи число одежды")
        if cl_us == '1':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=75000:
                    users_date[login]["money"] -=75000
                    users_date[login]["inventary"].append("айфон")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '2':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=67000:
                    users_date[login]["money"] -=67000
                    users_date[login]["inventary"].append("пс5")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '3':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=15000:
                    users_date[login]["money"] -=15000
                    users_date[login]["inventary"].append("мега ультра ноутбук игровой")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '4':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=200000:
                    users_date[login]["money"] -=200000
                    users_date[login]["inventary"].append("комп игровой")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '5':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=115000:
                    users_date[login]["money"] -=115000
                    users_date[login]["inventary"].append("телик 8k")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '6':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=25000:
                    users_date[login]["money"] -=25000
                    users_date[login]["inventary"].append("эпл ватч")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        else:
            break
def clothes_shop(login):
    while True:
        print("ты в магазине одежды")
        print("в катологе:")
        print("1 - шорты найк(1350р)")
        print("2 - оверсайз футболка от абибас(750р)")
        print("3 - мега ультра обтягивающийся джинсы(1000р)")
        print("4 - кофта ноунэйм брэнд(200р)")
        print("5 - кепка найк абибас гучис лавилаз лувсис тонс не паль(9500р)")
        print("6 - куртка пума(25000р)")
        cl_us = input("введи число одежды")
        if cl_us == '1':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=1350:
                    users_date[login]["money"] -=1350
                    users_date[login]["shmot"].append("шорты найк")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '2':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=750:
                    users_date[login]["money"] -=750
                    users_date[login]["shmot"].append("оверсайз футболка от абибас")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '3':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=1000:
                    users_date[login]["money"] -=1000
                    users_date[login]["shmot"].append("мега ультра обтягивающийся джинсы")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '4':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=200:
                    users_date[login]["money"] -=200
                    users_date[login]["shmot"].append("кофта ноунэйм брэнд")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '5':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=9500:
                    users_date[login]["money"] -=9500
                    users_date[login]["shmot"].append("кепка найк абибас гучис лавилаз лувсис тонс не паль")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        elif cl_us == '6':
            if input("купить? да/нет") == 'да':
                if users_date[login]["money"] >=25000:
                    users_date[login]["money"] -=25000
                    users_date[login]["shmot"].append("куртка пума")
                    print("ты успешно купил")
                else:
                    print("у тя нет стока бабла")
        else:
            break

def earn_money_from_buisness(login):
    if users_date[login]["buisnesses"] == []:
        print("у вас нет ни какого бизнеса")
    else:
        for business_name in users_date[login]["buisnesses"]:
            profit_per_minute = buisnesses[business_name]["прибыль в 30сек"]
            users_date[login]["money"] += profit_per_minute
            print(f"Вы заработали {profit_per_minute} рублей от бизнеса '{business_name}'!")
            time.sleep(30)
def buisness(login):
    while True:
        print("Здесь ты можешь купить бизнес")
        if input("Хочешь продолжить? да/нет: ").lower() == 'нет':
            break

        while True:
            print(f"Ты можешь купить бизнесы такие как: {buisnesses}")
            fs = input("Введи какой бизнес хочешь купить (скопируй название бизнеса и введи его): ")

            if fs not in buisnesses:
                print("Такого бизнеса нет из доступных для покупки.")
            else:
                print(f"Этот бизнес стоит: {buisnesses[fs]['стоимость']} рублей.")
                if input("Вы точно хотите приобрести этот бизнес? да/нет: ").lower() == 'да':
                    if users_date[login]["money"] >= buisnesses[fs]["стоимость"]:
                        users_date[login]["money"] -= buisnesses[fs]["стоимость"]
                        if fs not in users_date[login]["buisnesses"]:
                            print(f"Отлично, вы купили свой первый бизнес: {fs}.")
                            users_date[login]["buisnesses"].append(fs)
                        else:
                            print(f"Вы уже владеете бизнесом: {fs}.")
                    else:
                        print("У вас недостаточно денег для покупки этого бизнеса.")
            break
        if input("Вы хотите выйти из этого раздела? да/нет: ").lower() == 'нет':
            break


def casino(login):
    while True:
        print("ты в казино куда хочешь пойти")
        print("1. Рулетка")
        print("2. игровой автомат")
        print("3. выход")
        inp = input("напишите цифру")
        if inp == '3':
            break
        elif inp == '1':
            print("ты в игре рулетка")
            if input("хотите продолжить")== 'нет':
                break
            while True:
                input_ = input("напишите свою ставку")
                if users_date[login]["money"]<=int(input_):
                    print("у тя нет стока бабок")
                elif not input_.isdigit():
                    print("вы ввели не число")
                    break
                else:
                    users_date[login]["money"]-=int(input_)
                    inpu = input("хорошо а теперь на что будешь ставить (red/black/zero)")
                    red_black_randint = randint(0,36)
                    for i in range(5):
                        print("крутим")
                        time.sleep(1)
                    if color_casino[str(red_black_randint)]!=inpu:
                        print("к сожалению ты проиграл")
                        print(f"выпало {red_black_randint}- {color_casino[str(red_black_randint)]}")
                    else:
                        print("поздравляю ты виграл")
                        print(f"выпало {red_black_randint}- {color_casino[str(red_black_randint)]}")
                        print("сумма выиграша X2")
                        users_date[login]["money"] += int(input_)*2
                    if input("желаете ли вы продолжить играть в рулетка да/нет") == 'нет':
                        break
        elif inp == '2':
            print("ты в игровом автомате")
            while True:
                input__ = input("напишите свою ставку")
                if users_date[login]["money"] <= int(input__):
                    print("у тя нет стока бабок")
                else:
                    users_date[login]["money"] -= int(input__)
                    if input("крутить? да/нет") == 'да':
                        rand_1 = randint(0,5)
                        rand_2 = randint(0,5)
                        rand_3 = randint(0,5)
                        for i in range(5):
                            print("крутим")
                            time.sleep(1)
                        if rand_1 == rand_2 and rand_1 == rand_3:

                            if rand_1 == 5:
                                print("поздравляю ты выиграл джекпот!!!!")
                                print(f"выпало {automat_casino[rand_1]}{automat_casino[rand_2]}{automat_casino[rand_3]}")
                                print("сумма выиграша X10")
                                users_date[login]["money"] += int(input__) * 10
                            else:
                                print("поздравляю ты выиграл")
                                print(f"выпало {automat_casino[rand_1]}{automat_casino[rand_2]}{automat_casino[rand_3]}")
                                print("сумма выиграша X3")
                                users_date[login]["money"] += int(input__) * 3
                        else:
                            print("к сожаление ты проиграл")
                            print(f"выпало {automat_casino[rand_1]}{automat_casino[rand_2]}{automat_casino[rand_3]}")
                        if input("желаете ли вы продолжить играть в автомат да/нет") == 'нет':
                            break

def world_map(login):
    print("здесь ты можешь путешествовать по России")
    while True:
        print(f"доступные места: {city} только не пиши город в которм ты находишсья")
        if input("желаете ли вы продолжить да/нет") == 'нет':
            break
        m_inp_not_int = input("куда хочешь поехать (скопируй номер города и вставь сюда --->)")
        m_inp = m_inp_not_int
        if m_inp not in maps:
            print("такого города нет из доступных")
        else:
            if input("поехали? да/нет") == 'да':
                print("как будем ехать на автобусе или на лт(личный транспорт) автобу - 1, лт - 2")
                bus_or_car = input("1 или 2")
                if bus_or_car == '2':
                    if users_date[login]["cars"] == {}:
                        print("у вас нет лт")
                    else:
                        car_km_sek = users_date[login]["cars"]["km/sek"]
                        if users_date[login]["map"]== city[0]:
                            t_dr = From_Moscow[m_inp]/car_km_sek
                            print(f"время поездки {t_dr} минут")
                            time.sleep(t_dr*60)
                            print("мы приехали")
                            users_date[login]["map"] = city[int(m_inp)]
                        elif users_date[login]["map"]== city[1]:
                            t_dr = From_Perm[m_inp]/car_km_sek
                            print(f"время поездки {t_dr} минут")
                            time.sleep(t_dr*60)
                            print("мы приехали")
                            users_date[login]["map"] = city[int(m_inp)]
                        elif users_date[login]["map"]== city[2]:
                            t_dr = From_Sochi[m_inp]/car_km_sek
                            print(f"время поездки {t_dr} минут")
                            time.sleep(t_dr*60)
                            print("мы приехали")
                            users_date[login]["map"] = city[int(m_inp)]
                        elif users_date[login]["map"]== city[3]:
                            t_dr = From_Piter_Burg[m_inp]/car_km_sek
                            print(f"время поездки {t_dr} минут")
                            time.sleep(t_dr*60)
                            print("мы приехали")
                            users_date[login]["map"] = city[int(m_inp)]
                        elif users_date[login]["map"]== city[4]:
                            t_dr = From_Vladivostok[m_inp]/car_km_sek
                            print(f"время поездки {t_dr} минут")
                            time.sleep(t_dr*60)
                            print("мы приехали")
                            users_date[login]["map"] = city[int(m_inp)]
                elif bus_or_car == '1':
                    car_km_sek = 3
                    if users_date[login]["map"] == city[0]:
                        t_dr = From_Moscow[m_inp] / car_km_sek
                        print(f"время поездки {t_dr} минут")
                        time.sleep(t_dr*60)
                        print("мы приехали")
                        users_date[login]["map"] = city[int(m_inp)]
                    elif users_date[login]["map"] == city[1]:
                        t_dr = From_Perm[m_inp] / car_km_sek
                        print(f"время поездки {t_dr} минут")
                        time.sleep(t_dr*60)
                        print("мы приехали")
                        users_date[login]["map"] = city[int(m_inp)]
                    elif users_date[login]["map"] == city[2]:
                        t_dr = From_Sochi[m_inp] / car_km_sek
                        print(f"время поездки {t_dr} минут")
                        time.sleep(t_dr*60)
                        print("мы приехали")
                        users_date[login]["map"] = city[int(m_inp)]
                    elif users_date[login]["map"] == city[3]:
                        t_dr = From_Piter_Burg[m_inp] / car_km_sek
                        print(f"время поездки {t_dr} минут")
                        time.sleep(t_dr*60)
                        print("мы приехали")
                        users_date[login]["map"] = city[int(m_inp)]
                    elif users_date[login]["map"] == city[4]:
                        t_dr = From_Vladivostok[m_inp] / car_km_sek
                        print(f"время поездки {t_dr} минут")
                        time.sleep(t_dr*60)
                        print("мы приехали")
                        users_date[login]["map"] = city[int(m_inp)]

def leave_acc():
    start_game()
def leave_game():
    print("тебе это не нужно")
def promocode(login):
    while True:
        print("здесь тебе нужны промокоды которые будут давать тебе бонусы")
        if input("выйти? да/нет")== 'нет':
            break
        user_promo = input("введите промокод")
        if user_promo not in promo_for_mon:
            if user_promo not in promo_for_level:
                if user_promo not in promo_for_buisness:
                    print("такого промокода не существует")
                else:
                    if user_promo not in users_date[login]["users_promo"]:
                        print("промокод успешно введен")
                        users_date[login]["buisnesses"].append(promo_for_buisness[user_promo])
                        users_date[login]["users_promo"].append(user_promo)
                    else:
                        print("промокод недоступен(ты уже вводил этот промокод)")
            else:
                if user_promo not in users_date[login]["users_promo"]:
                    print("промокод успешно введен")
                    users_date[login]["level"]+= promo_for_level[user_promo]
                    users_date[login]["users_promo"].append(user_promo)
                else:
                    print("промокод недоступен(ты уже вводил этот промокод)")
        else:
            if user_promo not in users_date[login]["users_promo"]:
                print("промокод успешно введен")
                users_date[login]["money"]+=promo_for_mon[user_promo]
                users_date[login]["users_promo"].append(user_promo)
            else:
                print("промокод недоступен(ты уже вводил этот промокод)")
def imall(login):
    while True:
        if input("хочешь уйти") == 'да':
            break
        print("ты в торговом центре imall")
        print("здесь есть разные магазины:")
        print("1- магазин одежды ")
        print("2- магазин электроники")
        print("3- магазин еды")
        print("4- магазин для творчества")
        print("5- магазин для спорта")
        sh_us = input("введи номер магазина")
        if sh_us == '1':
            clothes_shop(login)
        elif sh_us == '2':
            electro_shop(login)
        elif sh_us == '3':
            food_shop(login)
        elif sh_us == '4':
            art_shop(login)
        elif sh_us == '5':
            sport_shop(login)
        else:
            print("такого нет попробуй ввести еще раз")
def bank():
    pass
def car_dealership():
    pass
def bandit_group():
    pass
def work_on_buisness(login):
    print("здесь ты будешь зарабатывать благодаря своему бизнесу")
    print("чтобы получать деньги ты не можешь просто стоять афк тебе надо потверждать что ты работаешь каждые 30 сек")
    while True:
        if input("потвердите что вы тут чтобы продолжить просто нажми на Enter, а чтобы уйти напиши 'стоп'") == 'стоп':
            break
        else:
            earn_money_from_buisness(login)
def work(login):
    while True:
        ot = input("введите на какую работу вы хотите пойти"
            "1.- таксист"
            "2.- хакер"
            "3.- комп-мастер"
            "4. - главное меню")
        if ot == '1':
            while True:
                ov = input("ты на работе таксиста хотите начать работу да/нет")
                if ov == 'нет':
                    print("иди тогда на другую работу")
                elif ov == 'да':
                    print("к вам сел/села посажир")
                    t_expectations = randint(21,101)
                    print(f"время поездки {t_expectations} секунд")
                    for w in range(t_expectations):
                        print(t_expectations-w)
                        time.sleep(1)
                    if t_expectations <= 63:
                        print("поездка закончена, вы получили 2500 рублей")
                        users_date[login]["money"]+= 2500
                    elif t_expectations <= 94 :
                        print("поездка закончена, вы получили 4350 рублей")
                        users_date[login]["money"]+= 4350
                    elif t_expectations <= 101:
                        print("поездка закончена, вы получили 7000 рублей")
                        users_date[login]["money"] += 7000
                    oa = input("Хотите продолжить работу да/нет")
                    if oa == 'нет':
                        break
                    elif oa != 'да':
                        print("это означает как 'да'")
        elif ot == '2':
            while True:
                ov = input("ты на работе хакера хотите начать работу да/нет")
                if ov == 'нет':
                    print("иди тогда на другую работу")
                    break
                elif ov == 'да':
                    print("на этой работе тебе надо будет выполнять заказы взламывая аккаунты")
                    gax = input("начать первый заказ да/нет")
                    if gax == "да":
                        print("заказ:")
                        ran = randint(0,7)
                        rand = randint(0,7)
                        print(f"логин:{nicknames[ran]} его пароль один из {pas_hack} этих паролей")
                        while True:
                            us_p = input("подберите пароль")
                            if us_p == pas_hack[rand]:
                                coin_ra = randint(1000, 25000)
                                print(f"молодец, ты угадал пароль и взломал аккаунт тебе на счет переведут рандомное количественное денег: {coin_ra}")
                                users_date[login]["money"] += coin_ra
                                break
                            else:
                                print("не правильно попробуй еще раз")
                        if input("жилаете ли вы продолжить работать да/нет") == 'нет':
                            break

        elif ot == '3':
            while True:
                ov = input("ты на работе компьютерного мастера хотите начать работу да/нет")
                if ov == 'нет':
                    print("иди тогда на другую работу")
                    break
                elif ov == 'да':
                    print("привет,ты на работе компьютерного мастера")
                    print()
                    print()
                    print("на этой работе тебе будут приходить заказы")
                    print("в заказах у клиентов в компьютере не будет одного комплетующего из тех которые обязательно нужны в пк")
                    print(f"например {pc_com} вот эти комплектующие должны быть в пк")
                    while True:
                        if input("желаети ли вы начать свой заказ да/нет") == 'да':
                            pc_com_rand = randint(0,8)
                            dse = pc_com
                            ds = dse.copy()
                            efs = ds.pop(pc_com_rand)
                            print(f"у клиента проблемы, в его пк вот такие комплектующие {ds}")
                            print(f"для этой задачи вам поможет вот этот список {pc_com}")
                            while True:
                                op = input("напишите какого комплектующего не хватает в этом компьютере")
                                if op == efs:
                                    print("да это правильно")
                                    print("за этот заказ вы получили 6500 руб")
                                    users_date[login]["money"] += 6500
                                    break
                                else:
                                    print("не верно попробуйте еще раз")
                            if input("хотити ли вы продолжить да/нет") == 'нет':
                                break
        elif ot == '4':
            break
def play_game():
    while True:
        login = input("введите пожалуйста свой логин")
        pasword = input("введите пожалуйста свой пароль от акк")
        if login in login_and_paswords_users_date:
            if pasword == login_and_paswords_users_date[login]:
                print("вы успешно вошли в свой аккаунт")

                if users_date[login]["map"] == city[2]:
                    print()
                    print("Ты в главном меню.")
                    print()
                    print("Выберите действие:")
                    print("1. Работа")
                    print("2. Бизнес")
                    print("3. Казино")
                    print("4. Карта мира")
                    print("5. Выйти из аккаунта")
                    print("6. Выйти из игры")
                    print("7. Промокоды")
                    print("8. Проверить счет")
                    print("9. работать в своем бизнесе")
                    print("10. посмотреть весь инвентарь")
                    ve_0 = input("введи куда хочешь пойти")
                    if ve_0 == '1':
                        work(login)
                    elif ve_0 == '2':
                        buisness(login)
                    elif ve_0 == '3':
                        casino(login)
                    elif ve_0 == '4':
                        world_map(login)
                    elif ve_0 == '5':
                        leave_acc()
                    elif ve_0 == '6':
                        leave_game()
                    elif ve_0 == '7':
                        promocode(login)
                    elif ve_0 == '8':
                        print(f"вас счет в данный момент равен: {users_date[login]["money"]} рублей")
                    elif ve_0 == '9':
                        work_on_buisness(login)
                    elif ve_0 == '10':
                        print(f"{users_date[login]["inventary"]} - это все твои вещи")
                        print(f"{users_date[login]["shmot"]} - это вся твоя одежда")
                        print(f"{users_date[login]["havchic"]} - это вся твоя еда")
                elif users_date[login]["map"] == city[1]:
                    print()
                    print("Ты в главном меню.")
                    print()
                    print("Выберите действие:")
                    print("1. Работа")
                    print("2. Бизнес")
                    print("3. imall")
                    print("4. Карта мира")
                    print("5. Выйти из аккаунта")
                    print("6. Выйти из игры")
                    print("7. Промокоды")
                    print("8. Проверить счет")
                    print("9. работать в своем бизнесе")
                    print("10. посмотреть весь инвентарь")
                    ve_1 = input("введи куда хочешь пойти")

                    if ve_1 == '1':
                        work(login)
                    elif ve_1 == '2':
                        buisness(login)
                    elif ve_1 == '3':
                        imall(login)
                    elif ve_1 == '4':
                        world_map(login)
                    elif ve_1 == '5':
                        leave_acc()
                    elif ve_1 == '6':
                        leave_game()
                    elif ve_1 == '7':
                        promocode(login)
                    elif ve_1 == '8':
                        print(f"вас счет в данный момент равен: {users_date[login]["money"]} рублей")
                    elif ve_1 == '9':
                        work_on_buisness(login)
                    elif ve_1 == '10':
                        print(f"{users_date[login]["inventary"]} - это все твои вещи")
                        print(f"{users_date[login]["shmot"]} - это вся твоя одежда")
                        print(f"{users_date[login]["havchic"]} - это вся твоя еда")
                elif users_date[login]["map"] == city[0]:
                    print()
                    print("Ты в главном меню.")
                    print()
                    print("Выберите действие:")
                    print("1. Работа")
                    print("2. Бизнес")
                    print("3. банк")
                    print("4. Карта мира")
                    print("5. Выйти из аккаунта")
                    print("6. Выйти из игры")
                    print("7. Промокоды")
                    print("8. Проверить счет")
                    print("9. работать в своем бизнесе")
                    print("10. посмотреть весь инвентарь")
                    ve_2 = input("введи куда хочешь пойти")
                    if ve_2 == '1':
                        work(login)
                    elif ve_2 == '2':
                        buisness(login)
                    elif ve_2 == '3':
                        bank()
                    elif ve_2 == '4':
                        world_map(login)
                    elif ve_2 == '5':
                        leave_acc()
                    elif ve_2 == '6':
                        leave_game()
                    elif ve_2 == '7':
                        promocode(login)
                    elif ve_2 == '8':
                        print(f"вас счет в данный момент равен: {users_date[login]["money"]} рублей")
                    elif ve_2 == '9':
                        work_on_buisness(login)
                    elif ve_2 == '10':
                        print(f"{users_date[login]["inventary"]} - это все твои вещи")
                        print(f"{users_date[login]["shmot"]} - это вся твоя одежда")
                        print(f"{users_date[login]["havchic"]} - это вся твоя еда")
                elif users_date[login]["map"] == city[3]:
                    print()
                    print("Ты в главном меню.")
                    print()
                    print("Выберите действие:")
                    print("1. Работа")
                    print("2. Бизнес")
                    print("3. автосалон")
                    print("4. Карта мира")
                    print("5. Выйти из аккаунта")
                    print("6. Выйти из игры")
                    print("7. Промокоды")
                    print("8. Проверить счет")
                    print("9. работать в своем бизнесе")
                    print("10. посмотреть весь инвентарь")
                    ve_3 = input("введи куда хочешь пойти")
                    if ve_3 == '1':
                        work(login)
                    elif ve_3 == '2':
                        buisness(login)
                    elif ve_3 == '3':
                        car_dealership()
                    elif ve_3 == '4':
                        world_map(login)
                    elif ve_3 == '5':
                        leave_acc()
                    elif ve_3 == '6':
                        leave_game()
                    elif ve_3 == '7':
                        promocode(login)
                    elif ve_3 == '8':
                        print(f"вас счет в данный момент равен: {users_date[login]["money"]} рублей")
                    elif ve_3 == '9':
                        work_on_buisness(login)
                    elif ve_3 == '10':
                        print(f"{users_date[login]["inventary"]} - это все твои вещи")
                        print(f"{users_date[login]["shmot"]} - это вся твоя одежда")
                        print(f"{users_date[login]["havchic"]} - это вся твоя еда")
                elif users_date[login]["map"] == city[4]:
                    print()
                    print("Ты в главном меню.")
                    print()
                    print("Выберите действие:")
                    print("1. Работа")
                    print("2. Бизнес")
                    print("3. бандитская группировка")
                    print("4. Карта мира")
                    print("5. Выйти из аккаунта")
                    print("6. Выйти из игры")
                    print("7. Промокоды")
                    print("8. Проверить счет")
                    print("9. работать в своем бизнесе")
                    print("10. посмотреть весь инвентарь")
                    ve_4 = input("введи куда хочешь пойти")
                    if ve_4 == '1':
                        work(login)
                    elif ve_4 == '2':
                        buisness(login)
                    elif ve_4 == '3':
                        bandit_group()
                    elif ve_4 == '4':
                        world_map(login)
                    elif ve_4 == '5':
                        leave_acc()
                    elif ve_4 == '6':
                        leave_game()
                    elif ve_4 == '7':
                        promocode(login)
                    elif ve_4 == '8':
                        print(f"вас счет в данный момент равен: {users_date[login]["money"]} рублей")
                    elif ve_4 == '9':
                        work_on_buisness(login)
                    elif ve_4 == '10':
                        print(f"{users_date[login]["inventary"]} - это все твои вещи")
                        print(f"{users_date[login]["shmot"]} - это вся твоя одежда")
                        print(f"{users_date[login]["havchic"]} - это вся твоя еда")
            else:
                print("неправильный пароль")
        else:
            print("неверный логин")

def start_game():
    while True:
        print("О привет, ты зашел в 'симулятор миллионера'")
        print()
        s = input("хотите начать игру (да/нет)")
        if s  == 'нет':
            print("ну ладно пока")

        elif s == 'да':
            while True:
                quiree = input("хорошо вы желаете зарегистрироваться или войти")
                if quiree == 'войти':
                    log = input("тогда напишите свой логин")
                    pas = input("а здесь напишите свой пароль")
                    if log in login_and_paswords_users_date:
                        if pas == login_and_paswords_users_date[log]:
                            print("вы успешно вошли в свой аккаунт")
                            break
                        else:
                            print("неправильный пароль")
                    else:
                        print("неверный логин")



                elif quiree == "зарегистрироваться":
                    login = input("придумайте и введите свой логин здесь")
                    password = input('придумайте и введите свой пароль здесь')
                    login_and_paswords_users_date[login]= password
                    users_date[login] = {
                        "money": 0,
                        "level": 0,
                        "map": city[1],
                        "buisnesses":[],
                        "cars":{},
                        "inventary":[],
                        "users_promo":[],
                        "shmot":[],
                        "havchic":[]
                    }
                    print("ты успешно зарегистрировался")
                    break
            break
def main_game():
    while True:
        start_game()
        play_game()
main_game()