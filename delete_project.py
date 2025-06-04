"""
delete_project.py: delete ALL projects of a given name

Author: Jonas 
Last Updated: 2025-06-03
"""

# imports
import quickstart
import requests

# variables
name = "quickstart_demo"
token = quickstart.post_authentication(quickstart.username, quickstart.password)
project_ids = list()

res = requests.get('http://localhost:8000/api/projects/?name={}'.format(name), 
                   headers={'Authorization': 'JWT {}'.format(token)}).json()

for result in res:
    project_ids.append(result['id'])
    
for project_id in project_ids:

    requests.delete("http://localhost:8000/api/projects/{}/".format(project_id), 
                        headers={'Authorization': 'JWT {}'.format(token)})

    