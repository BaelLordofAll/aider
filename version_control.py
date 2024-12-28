import git
import os

def commit_changes(message):
    repo = git.Repo(os.getcwd())
    repo.git.add(A=True)
    repo.index.commit(message)
    origin = repo.remote(name='origin')
    origin.push()

def create_branch(branch_name):
    repo = git.Repo(os.getcwd())
    repo.git.checkout('-b', branch_name)

def merge_branch(branch_name):
    repo = git.Repo(os.getcwd())
    repo.git.checkout('master')
    repo.git.merge(branch_name)

# Example usage:
# commit_changes("Updated system integration")
# create_branch("feature/new_functionality")
# merge_branch("feature/new_functionality")
