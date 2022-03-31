from operator import itemgetter
import requests
url = 'https://en.wikipedia.org/wiki/List_of_best-selling_Nintendo_Switch_video_games'
headers = {'Accept': 'Reitingu+json'}
r = requests.get(url)
print()
print()
print()
print()
print()
print()
print(f'status code: {r.status_code}')
print(r.content)

# submission_ids = r
# sub_dicts = []
# for submission_id in submission_ids[:30]:
#     pass
    #print(submission_id)
    # url = f'https://hacker-news.firebaseio.com/v0/item/{submission_id}.json'
    # r = requests.get(url)
    # print(f'id: {submission_id}\tstatus: {r.status_code}')
    # resp_dict = r.json()
    # try:
    #     sub_dict = {'title': resp_dict['title'],
    #                 'hn_link': f'https://news.ycombinator.com/item?id={submission_id}',
    #                 'comments': {resp_dict['descendants']}}
    # except KeyError:
    #     pass
    # sub_dicts.append(sub_dict)
# sub_dicts = sorted(sub_dicts, key=itemgetter('comments'), reverse=True)
# print(sub_dicts)
# for sub_dict in sub_dicts:
#     print(f'Title: {sub_dict["title"]}')
#     print(f'Discussion link: {sub_dict["hn_link"]}')
#     print(f'Comments: {sub_dict["comments"]}')
