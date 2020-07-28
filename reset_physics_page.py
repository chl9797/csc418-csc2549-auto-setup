from __future__ import print_function
import pickle
import os.path
import sys
import json

# github stuff
import getpass
import github
from github import Github
from github import GithubException

from reset_physics_readme import reset_readme

def main():
    #create github repo for paper 
    #github login
    username = input("Github Username:")
    pw = getpass.getpass()
    g = Github(username, pw)
    user = g.get_user() #get user
    
    # get repo
    repo = user.get_repo("CSC2549-physics-based-animation")

    open_issues = repo.get_issues(state='open')
    for issue in open_issues:
        issue.edit(state='closed')

    old_branch = input("Branch of the last term(e.g., fall_2019) :")
    master_branch = repo.get_branch(branch="master")
    repo.create_git_ref(ref='refs/heads/' + old_branch, sha=master_branch.commit.sha)
  
    print("Print all branches in repo %s:" % repo.name)
    for branch in repo.get_branches():
      print("\t%s" % branch.name)

    # delete old lecture slides
    old_slides = repo.get_contents("/lectures", ref=old_branch)  
    for old_slide in old_slides:
        repo.delete_file(old_slide.path, "remove old slide", old_slide.sha, branch=old_branch)

    # reset readme locally
    with open('setting_cg.json', 'r') as f:
        setting_dict = json.load(f)
    reset_readme(setting_dict)
    # update readme in the repo
    readme = repo.get_contents("README.md", ref=old_branch)
    readme_contents = open("course_readme/csc2549_readme.md").read()
    repo.update_file(readme.path, "update readme", readme_contents, readme.sha, branch=old_branch)

    for new_collaborator in setting_dict['collaborators']:
        repo.add_to_collaborators(new_collaborator, 'admin')

if __name__ == '__main__':
    main()
