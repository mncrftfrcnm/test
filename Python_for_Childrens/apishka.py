from pprint import pprint
import requests
from plotly.graph_objs import Bar
from plotly.graph_objs import Scatter

from plotly import offline 
url = 'https://api.github.com/search/repositories?q=language:Python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(r.headers)
print(f'Status code: {r.status_code}')
inputer = input('projects with more than ')
print('stars')

responce_dict = r.json()
print(f'Total repositories: {responce_dict["total_count"]}')
repo_dicts = responce_dict['items']

print('\nSelected information from every repository')

repo_names, stars, labels, colors, colors2 = [], [], [], [], []
for repo_dict in repo_dicts:
    if repo_dict["stargazers_count"] <= int(inputer):
        pass
    else:
        # print(f'\nName: {repo_dict["name"]}')
        # repo_names.append(repo_dict["name"])
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_names.append(repo_link)
        
        # print(f' Owner: {repo_dict["owner"]["login"]}')
        # print(f' Stars: {repo_dict["stargazers_count"]}')
        gh = 0
        stars.append(repo_dict["stargazers_count"])
        for x in range(160):
            if repo_dict["stargazers_count"] >= x*1000:
                colors.append(f'rgb({x*10}, {x*10}, {x*10})')  
                colors2.append(f'rgb({0}, {x*10}, {0})')

                
        # if repo_dict["stargazers_count"] >= 160000:
        #     colors.append('rgb(0, 0, 0)')
        # elif repo_dict["stargazers_count"] >= 140000:
        #     colors.append('rgb(10, 10, 10)')

        # elif repo_dict["stargazers_count"] >= 150000:
        #     colors.append('rgb(20, 20, 20)')
        # elif repo_dict["stargazers_count"] >= 50000:
        #     colors.append('rgb(30, 30, 30)')
        # elif repo_dict["stargazers_count"] >= 40000:
        #     colors.append('rgb(20, 120, 220)')
        # elif repo_dict["stargazers_count"] >= 35000:
        #     colors.append('rgb(220, 20, 120)')
        # elif repo_dict["stargazers_count"] >= 25000:
        #     colors.append('rgb(220, 230, 20)')
        # elif repo_dict["stargazers_count"] >= 20000:
        #     colors.append('rgb(200, 140, 200)')
        # else:
        #     colors.append('rgb(25, 120, 100)')
        
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
                 'color': colors,
                 'line': {'width': 0.5, 'color': colors2}},
             'opacity': 0.6,
             'hovertext': labels}]
my_layout = {'title': 'most starred python projects on Git Hub',
             'xaxis': {'title': 'Repository'},
             'yaxis': {'title': 'Stars'}}
fig = {'data': data, 'layout': my_layout}
print(f'repositories returned: {len(repo_names)}')
g = offline.plot(fig, filename='python_repositories.html')#.update_traces(marker_color='blue', selector=dict(type='scatter'))

#g.update_traces(marker_color='blue', selector=dict(type='scatter'))