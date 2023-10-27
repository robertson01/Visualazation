# На основании данных из hn_submissions.py постройте столбцовую диаграмму
# самых активных обсуждений, проходящих на Hacker News. Высота каждого
# столбца должна соответствовать количеству комментариев к каждой статье. Метка столбца
# должна включать заголовок статьи, а сам столбец должен служить ссылкой на страницу
# обсуждения этой публикации.

from operator import itemgetter
from plotly.graph_objs import Bar
from plotly import offline

import requests

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:5]:
    # Создание отдельного вызова API для каждой статьи.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Построение словаря для каждой статьи.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)


article_links, article_comments = [], []
for submission_dict in submission_dicts:
    article_url = submission_dict['hn_link']
    article_title = submission_dict['title']
    article_link = f"<a href='{article_url}'>{article_title}</a>"
    article_comment = submission_dict['comments']
    article_links.append(article_link)
    article_comments.append(article_comment)
    # print(f"\nTitle: {submission_dict['title']}")
    # print(f"Discussion link: {submission_dict['hn_link']}")
    # print(f"Comments: {submission_dict['comments']}")


data = [{
    'type': 'bar',
    'x': article_links,
    'y': article_comments,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
}]

my_layout = {
    'title': 'Most-comment',
    'xaxis': {
        'title': 'Artile',
    },
    'yaxis': {
        'title': 'Comments'
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hn_submissions_comments.html')
