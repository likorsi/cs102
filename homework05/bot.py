import requests
import config
import telebot
import datetime
from datetime import date
from bs4 import BeautifulSoup
from typing import Optional, Tuple


bot = telebot.TeleBot(config.access_token)
day_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
rus_day = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']

def get_page(group ='K3140', week=''):
    if week:
        week = str(week) + '/'
    url = '{domain}/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        domain=config.domain,
        week=week,
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page


def parse_schedule_for_a_day(web_page: str, day: str) -> Optional[Tuple[list, list, list, list]]:
    soup = BeautifulSoup(web_page, "html5lib")

    need_day = ''

    if day in day_list:
        need_day = str(day_list.index(day) + 1) +'day'
    # Получаем таблицу с расписанием на понедельник
    schedule_table = soup.find("table", attrs={"id": need_day})

    # Время проведения занятий
    try:
        times_list = schedule_table.find_all("td", attrs={"class": "time"})
    except AttributeError:
        return None
    try:
        times_list = [time.span.text for time in times_list]
    except AttributeError:
        return None
    
    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations = [room.span.text for room in locations_list]

    #Аудитория
    aud_list = [room.dd.text for room in locations_list]
  

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split() for lesson in lessons_list]
    lessons_list = [' '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]


    return times_list, locations, aud_list, lessons_list 


@bot.message_handler(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])
def get_schedule(message: telebot.types.Message) -> telebot.types.Message:
    """ Получить расписание на указанный день """

    need_day, week, group = message.text.split()

    web_page = get_page(group, str(int(week)+1))
    answer = parse_schedule_for_a_day(web_page, need_day[1:])

    if answer is None:
        resp = 'В этот день нет совпадающих пар либо у вас выходной'
    else:
        times_list, aud_list, locations_list, lessons_list  = answer
        resp = ''
        for time, location, aud, lession in zip(times_list, locations_list, aud_list, lessons_list):
            if time == 'День':
                resp += '<b>{}</b>\n{}'.format(time, lession)
            else:
                resp += '<b>{}</b>\n\n{}\n{}\n{}\n\n'.format(time, location, aud, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['near'])
def get_near_lesson(message:telebot.types.Message) -> telebot.types.Message:
    """ Получить ближайшее занятие """
    _, group = message.text.split()

    near_day = int(datetime.datetime.today().weekday())
    week = (int(datetime.datetime.now().isocalendar()[1])+1) % 2
    if week ==0:
        week = 2
    real_hour = int(datetime.datetime.now().hour)
    real_min = int(datetime.datetime.now().minute)


    need_time = {1:'8:20-9:50', 2:'10:00-11:30', 3:'11:40-13:10', 
    4:'13:30-15:00', 5:'15:20-16:50', 6:'17:00-18:30', 7:'18:40-20:10'}


    hour = [8, 10 , 11, 13, 15, 17, 18]
    minute = [20, 0, 40, 30, 20, 0, ]

    pare = 1
    for i in range(0,6):
        if real_hour <= hour[i]:
            if real_min < minute[i]:
                pare = i + 1
                break
        else:
            pare += 1

    resp = 'Ближайшее занятие - '
    need_day = day_list[near_day]
    web_page = get_page(group, week)
    answer = parse_schedule_for_a_day(web_page, need_day)

    all_pare = 0
    if answer != None:
        times_list, aud_list, locations_list, lessons_list = answer
        all_pare = len(times_list)

    if pare > all_pare:
        near_day += 1
        need_day = day_list[near_day]
        web_page = get_page(group, str(week))
        answer = parse_schedule_for_a_day(web_page, need_day) 
        while answer is None:
            if near_day == 6:
                near_day = 0
                week = (week + 1) % 2
                if week == 0:
                    week = 2   
            need_day = day_list[near_day]
            web_page = get_page(group, str(week))
            answer = parse_schedule_for_a_day(web_page, need_day)  
        times_list, aud_list, locations_list, lessons_list = answer
        resp += '{}\n\n<b>{}</b>\n{}\n{}\n{}\n'.format(rus_day[near_day], times_list[0], 
            locations_list[0], aud_list[0], lessons_list[0])
    else:
        pare -= 1
        resp += '{}\n\n<b>{}</b>\n{}\n{}\n{}\n\n'.format(rus_day[near_day], times_list[pare], 
            locations_list[pare], aud_list[pare], lessons_list[pare])        

    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['tomorrow'])
def get_tommorow(message: telebot.types.Message) -> telebot.types.Message:
    """ Получить расписание на следующий день """
    _, group = message.text.split()

    near_day = int(datetime.datetime.today().weekday())
    week = (int(datetime.datetime.now().isocalendar()[1])+1) % 2
    if week == 0:
        week = 2
    if near_day == 6:
        near_day = 0
        week = (week + 1) % 2
        if week == 0:
            week = 2
    else:
        near_day += 1


    need_day = day_list[near_day]
    web_page = get_page(group, str(week))
    answer = parse_schedule_for_a_day(web_page, need_day)

    if answer is None:
        resp = 'Завтра выходной!'
    else:
        times_list, aud_list, locations_list, lessons_list  = answer
        resp = ''
        for time, location, aud, lession in zip(times_list, locations_list, aud_list, lessons_list):
            if aud is None:
                resp += '<b>{}</b>\n{}'.format(time, lession)
            else:
                resp += '<b>{}</b>\n{}\n{}\n{}\n\n'.format(time, location, aud, lession)


    bot.send_message(message.chat.id, resp, parse_mode='HTML')


@bot.message_handler(commands=['all'])
def get_all_schedule(message: telebot.types.Message) -> telebot.types.Message:
    """ Получить расписание на всю неделю для указанной группы """
    _, week, group = message.text.split()
    web_page = get_page(group, week)

    resp = 'Расписание на неделю:\n--------\n'
    for one_of_need_day in range(0, 6):
        day = ''
        need_day = day_list[one_of_need_day]
        answer = parse_schedule_for_a_day(web_page, need_day[0:])
        if answer is None:
            day += '{} - выходной! \n'.format(rus_day[one_of_need_day])
        else:
            day += rus_day[one_of_need_day] + ':\n\n'
            times_list, aud_list, locations_list, lessons_list  = answer
            for time, location, aud, lession in zip(times_list, locations_list, aud_list, lessons_list):
                day += '<b>{}</b>\n\n{}\n{}\n{}\n\n'.format(time, location, aud, lession)
                if time == 'День':
                    day = rus_day[one_of_need_day] + ':\n\n'
                    day += '<b>{}</b>\n{}\n'.format(time, lession)
        resp += '\n' + day + '\n--------\n' 
  
    bot.send_message(message.chat.id, resp, parse_mode='HTML')


if __name__ == '__main__':
    bot.polling(none_stop=True)