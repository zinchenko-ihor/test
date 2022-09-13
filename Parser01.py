import re
import csv
import collections

import base64
from github import Github
from github import InputGitTreeElement

def log_file_reader(filename):
    # Get all IP addresses from the log file
    with open(filename) as f:
        log = f.read()
        regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        ip_list = re.findall(regex, log)
        return ip_list

# Get total count of IPs
def count_ip(ip_list):
    return collections.Counter(ip_list)

# Create
def write_to_csv(counter):
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['IP', 'Count']
        writer.writerow(header)
        for item in counter:
            writer.writerow((item, counter[item]))

#GIT
user = "zinchenko-ihor"
password = "*******"
g = Github(user,password)
repo = g.get_user().get_repo('https://github.com/zinchenko-ihor/test.git')
file_list = "C:/Users/Zinchenko Ihor/parser/"

file_names = ['output.csv']
commit_message = 'python update'
master_ref = repo.get_git_ref('heads/master')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)
#element_list = list()
#for i, entry in enumerate(file_list):
 ##      data = input_file.read()
   # if entry.endswith('.csv'):
    #    data = base64.b64encode(data)
    #element = InputGitTreeElement(file_names[i], '100644', 'blob', data)
    #element_list.append(element)
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
master_ref.edit(commit.sha)


if __name__ == "__main__":
    write_to_csv(count_ip(log_file_reader('nginx.log')))