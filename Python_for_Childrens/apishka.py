from pprint import pprint
import requests
from plotly.graph_objs import Bar
from plotly import offline 
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')
responce_dict = r.json()
print(f'Total repositories: {responce_dict["total_count"]}')
repo_dicts = responce_dict['items']
print(f'repositories returned: {len(repo_dicts)}')
print('\nSelected information from every repository')
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    # print(f'\nName: {repo_dict["name"]}')
    # repo_names.append(repo_dict["name"])
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_names.append(repo_link)
    
    # print(f' Owner: {repo_dict["owner"]["login"]}')
    # print(f' Stars: {repo_dict["stargazers_count"]}')
    stars.append(repo_dict["stargazers_count"])
    owner = repo_dict["owner"]["login"]
    description = repo_dict["description"]
    created = repo_dict["created_at"]
    labels.append(f'{owner}<br />{description}<br />{created}')
    # print(f' Repository: {repo_dict["html_url"]}')
    # print(f' Description: {repo_dict["description"]}')
    # print(f' Created at {repo_dict["created_at"]}')
    # print(f' Watchers count: {repo_dict["watchers_count"]}')
data = [{'type': 'bar', 'x': repo_names, 'y': stars,
            'marker': {
                 'color': 'rgb(25, 120, 100)',
                 'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}},
             'opacity': 0.6,
             'hovertext': labels}]
my_layout = {'title': 'most starred python projects on Git Hub',
             'xaxis': {'title': 'Repository'},
             'yaxis': {'title': 'Stars'}}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repositories.html')
