from bottle import (
    route, run, template, request, redirect
)

from scrapper import get_news
from db import News, session
from bayes import NaiveBayesClassifier


@route("/news")
def news_list():
    s = session()
    rows = s.query(News).filter(News.label == None).all()
    return template('news_template', rows=rows)


@route("/add_label/")
def add_label():
    # 1. Получить значения параметров label и id из GET-запроса
    # 2. Получить запись из БД с соответствующим id (такая запись только одна!)
    # 3. Изменить значение метки записи на значение label
    # 4. Сохранить результат в БД
    s = session()
    label = request.query.label
    row_id = request.query.id
    row = s.query(News).filter(News.id == row_id).one()
    row.label = label
    s.commit()
    redirect("/news")


@route("/update")
def update_news():
    # 1. Получить данные с новостного сайта
    # 2. Проверить, каких новостей еще нет в БД. Будем считать,
    #    что каждая новость может быть уникально идентифицирована
    #    по совокупности двух значений: заголовка и автора
    # 3. Сохранить в БД те новости, которых там нет
    s = session()

    last_news = get_news()

    for n in last_news:
        check = s.query(News).filter(News.author == n['author'], News.title == n['title']).count()
        if check == 0:
            new = News(title=n['title'], author=n['author'], url=n['url'], comments=n['comments'], points=n['points'])
            s.add(new)
    s.commit()
    redirect("/news")



@route("/classify")
def classify_news():
    # 1. Получить список неразмеченных новостей из БД
    # 2. Получить прогнозы для каждой новости
    # 3. Вывести ранжированную таблицу с новостями

    s.session()
    classifier = NaiveBayesClassifier()

    news_lable = s.query(News).filter(News.label != None).all()
    x_train = [row.title for row in news_lable] 
    y_train = [row.label for row in news_lable]
    classifier.fit(x_train, y_train)

    news_lable_none = s.query(News).filter(News.label == None).all()
    x = [row.title for row in news_lable_none]
    label = classifier.predict(x)

    classified_news[0] = [news_lable_none[i] for i in range(len(news_lable_none)) if label[i]=='good']
    classified_news[1] = [news_lable_none[i] for i in range(len(news_lable_none)) if label[i]=='maybe']
    classified_news[2] = [news_lable_none[i] for i in range(len(news_lable_none)) if label[i]=='never']
    return template('news_recommendations', rows=classified_news)



if __name__ == "__main__":
    s = session()
    run(host="localhost", port=8080)
