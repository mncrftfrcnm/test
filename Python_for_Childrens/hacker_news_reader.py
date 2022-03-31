from operator import itemgetter
import requests
from pprint import pprint
import requests
from plotly.graph_objs import Bar
from plotly import offline 
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)

print(f'status code: {r.status_code}')
submission_ids = r.json()

sub_dicts = []
titles, coms, links = [], [], []

for submission_id in submission_ids[:30]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    r = requests.get(url)
    print(f'id: {submission_id}\tstatus: {r.status_code}')
    resp_dict = r.json()
    try:
        sub_dict = {'title': resp_dict['title'],
                    'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
                    'comments': {resp_dict['descendants']}}
    except KeyError:
        sub_dict = {'title': resp_dict['title'],
                    'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
                    'comments': {resp_dict['score']}}
    sub_dicts.append(sub_dict)
sub_dicts = sorted(sub_dicts, key=itemgetter('comments'), reverse=True)
print(sub_dicts)
for sub_dict in sub_dicts:
    print(sub_dict)
    print(f'Title: {sub_dict["title"]}')
    print(f'Discussion link: {sub_dict["hn_link"]}')
    print(f'Comments: {sub_dict["comments"]}')
    titles.append(f"<a href='{sub_dict['hn_link']}'>{sub_dict['title']}</a>")
    links.append(sub_dict["hn_link"])
    
    for cvg in sub_dict["comments"]:
        coms.append(cvg)
    
data = [{'type': 'bar', 'x': titles, 'y': coms,
            'marker': {
                 'color': 'rgb(25, 120, 100)',
                 'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}},
             'opacity': 0.6,
             'hovertext': links,
             'name':'blablabla'}]
my_layout = {'title': 'the top stories in hacker news',
             'xaxis': {'title': 'Repository'},
             'yaxis': {'title': 'Stars'}}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='hacker_news_reader.html')
