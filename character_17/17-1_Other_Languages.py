""" Modify the API call in python_repos.py so it generates a chart showing the 
most popular projects in other languages. Try languages such as JavaScript, Ruby, 
C, Java, Perl, Haskell, and Go. """


import requests


base_url = "https://api.github.com/search/repositories"
headers = {"Accept": "application/vnd.github.v3+json"} 
languages = ['JavaScript', 'Ruby', 'C', 'Java', 'Perl', 'Haskell', 'Go']
for language in languages:
    url_parameter = "?q=language:" + language + "+sort:stars+stars:>10000" 
    request = base_url + url_parameter
    respond = requests.get(request, headers=headers)
    print(f"{language}: {respond.json()}")