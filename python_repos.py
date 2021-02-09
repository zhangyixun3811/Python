import requests

# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code", r.status_code)

# 将API相应存储到变量
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("repositories returned:", len(repo_dicts))

# 研究第一个仓库
repo_dict = repo_dicts[0]

print("\ninformation for first repository:")
print("name:", repo_dict['name'])
print("owner:", repo_dict['owner']['login'])
print("Stars:", repo_dict['stargazers_count'])
print("url:", repo_dict['html_url'])
print("Descrip:", repo_dict['description'])