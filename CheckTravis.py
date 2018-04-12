#!/usr/bin/env python3

from github import Github, GithubException
import json
import sys

# sys.argv[1]: optional, name of organisation to scan

def check_org(org):
    # We iterate over all the repos
    repos = org.get_repos(type='all')
    for repo in repos:
        # Now we can finally check for the existence of the file
        try:
            travis_conf = repo.get_file_contents('.travis.yml')
            print("%s: %s - dirty" % (org.name, repo.name))
        except GithubException:
            print("%s: %s - clean" % (org.name, repo.name))

if __name__ == '__main__':
    with open('app.json', 'r') as conf:
        github_conf = json.loads(conf.read())

    try:
        git = Github(login_or_token=github_conf['githubAccessToken'], base_url=github_conf['endpoint'])
    except KeyError:
        if 'githubAccessToken' not in github_conf:
            sys.exit(1)
        elif 'endpoint' not in github_conf:
            git = Github(login_or_token=github_conf['githubAccessToken'])

    # If sys.argv[1] is specified, that is the org we use
    # Otherwise, we iterate over _every_ org
    try:
        org = git.get_organization(sys.argv[2])
        check_org(org)
    except IndexError:
        orgs = git.get_organizations()
        for org in orgs:
            check_org(org)
