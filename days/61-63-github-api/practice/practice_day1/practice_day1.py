from collections import namedtuple
import os
from github import Github, InputFileContent
from pprint import pprint

GITHUB_TOKEN = os.environ['GITHUB_TOKEN']

code = """
Repo = namedtuple('Repo', 'name stars forks')
from collections import namedtuple
def get_repo_stats(user, n=5):
    repos = []
    for repo in user.get_repos():
        if repo.fork:
            continue
        repos.append(Repo(repo.name, repo.stargazers_count, repo.forks_count))
    return sorted(repos, key=lambda x: x.stars, reverse=True)[:n]
"""

if __name__ == '__main__':
    gh = Github(GITHUB_TOKEN)
    pb = gh.get_user()
    print(pb.name)
    repos = pb.get_repos()
    # print(get_repo_stats(pb))
    print(gh.rate_limiting)
    gist = pb.create_gist(True, {"repo_stats.py": InputFileContent(code)}, "Get GH user's most popular repos")
    print(gist)
    print(gh.get_emojis()['woman_singer'])
    # print(help(pb.create_gist))
    
