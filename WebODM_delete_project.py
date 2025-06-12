"""
delete_project.py: delete ALL projects of a given name

Author: Jonas 
Last Updated: 2025-06-04
"""

# imports
import os, sys
import quickstart
import requests

# functions
def get_project_ids(token, project_name):
    """
    Gets list of project IDs based on inputed project_name
    
    :param token: authentication token
    :param project_name: name of project to get ID/s for
    :return: list of project IDs
    """
    
    # var
    project_ids = list()
    
    # get project IDs of name project_name
    res = requests.get('http://localhost:8000/api/projects/?name={}'.format(project_name), 
                   headers={'Authorization': 'JWT {}'.format(token)}).json()

    # get id for each
    for result in res:
        project_ids.append(result['id'])
    
    # return list of IDs
    return project_ids

def delete_projects(token, project_id):
    """
    Deletes projects based on list of ids
    
    :param token: authentication token
    :param project_id: list of ID having project name
    :return: list of project IDs
    """
    
    for project_id in project_ids:
        requests.delete("http://localhost:8000/api/projects/{}/".format(project_id), 
                            headers={'Authorization': 'JWT {}'.format(token)})

    
if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        quickstart.print_error("Must provide name of project. Usuage ./delete_project.py <name of project>")
    else:
        project_name = sys.argv[1]
        
    
    # name of project to be deleted
    print(f'Deleting {project_name}')
    
    # get token
    token = quickstart.post_authentication(quickstart.username, quickstart.password)
    
    # get project IDs
    project_ids = get_project_ids(token, project_name)
    
    # delete all projects of name
    delete_projects(token, project_ids)
    
    

    