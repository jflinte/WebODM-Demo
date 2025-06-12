"""
WebODM_processing_nodes.py: add processing nodes

Author: Jonas 
Last Updated: 2025-06-10
"""

# imports
import os, sys, time
import argparse
import requests
import WebODM_main

# functions
def create_parser():
    """
    Creates Parser and adds required arguments to it
    
    :param: N/A 
    :return: ArgumentParser object
    """
    
    # create parser    
    parser = argparse.ArgumentParser()

    # hostname
    parser.add_argument('-hn', '--hostname', help='Hostname of processing node', type=str)
    
    # port
    parser.add_argument('-p', '--port', help='Port of processing node', type=int)
    
    # id
    parser.add_argument('-id', '--identification', help='ID of processing node', type=int)
    
    # d
    parser.add_argument('-d', '--delete', help='Set delete to true', action='store_true', default=False)
    
    return parser

def post_processing_node(token, hostname, port):
    """
    adds a processing node
    
    :param token: authentication token
    :param hostname: hostname of the processing node wanting to be added
    :param port: port of the processing node wanting to be added
    :return: processing node ID
    """
    
    res = requests.post('http://localhost:8000/api/processingnodes/', 
                        headers={'Authorization' : 'JWT {}'.format(token)}, 
                        data = {
                            'hostname' : hostname,
                            'port' : port
                            }).json()
    
    if res['id']:
        print(f'Processing node added at host {hostname} port {port}')
        return(res['id'])
    else:
        print(f'Could not add processing node at host {hostname} port {port}')
               
def get_all_processing_nodes(token):
    """
    gets all processing nodes
    
    :param token: authentication token
    :return: list of processing nodes
    """
    
    res = requests.get('http://localhost:8000/api/processingnodes/', 
                       headers={'Authorization' : 'JWT {}'.format(token)}).json()
    
    # for node in res:
    #     # print(node['id'])
    #     print('label: {}'.format(node['label']))
    
    return res

def get_processing_nodes_ids(token, hostname, port):
    """
    gets processing node ids based on hostname and port
    
    :param token: authentication token
    :param hostname: hostname of the processing node wanting to be added
    :param port: port of the processing node wanting to be added
    :return: processing node IDs
    """
    
    # var
    ids = list()
    
    # get processing nodes
    processing_nodes = get_all_processing_nodes(token)
    
    for pn in processing_nodes:
        if (hostname == pn['hostname']) and (int(port) == pn['port']):
            ids.append(pn['id'])
    
    return ids

def delete_processing_node(token, id):
    """
    deletes a processing node based on id
    
    :param token: authentication token
    :param hostname: hostname of the processing node wanting to be added
    :param port: port of the processing node wanting to be added
    :return: N/A
    """  
    
    if (pnid == 1):
        WebODM_main.print_error('Not allowed to delete default processing node')
        
    
    res = requests.delete('http://localhost:8000/api/processingnodes/{}/'.format(id), 
                          headers={'Authorization' : 'JWT {}'.format(token)})
    
    # print(res.status_code)
    if res.status_code == 204:
        print(f'Deletion of proccess node {id} successful')
    else:
        print(f'Deletion of proccess node {id} failure')

def delete_processing_nodes(token, ids):
    """
    deletes processing nodes of given ids
    
    :param hostname: authorization token 
    :param ids: list of ids to delete
    :return: N/A
    """
    
    for id in ids:
        delete_processing_node(token, id)

def check_if_pn_added(hostname, port, processing_nodes):
    """
    checks if given hostname and port have been added to the processing of processing nodes
    
    :param hostname: hostname of processing node
    :param port: port of processing node
    :param processing_nodes: list of processing nodes (list of dictionaries)
    :return: True if processing node has been added, False otherwise
    """
    
    # iterate through processing nodes, checking if BOTH the hostname AND the port match
    for pn in processing_nodes:

        
        if (hostname == pn['hostname']) and (int(port) == pn['port']):
            print('Processing node of hostname {} and port {} has already been added under the label {}'.format(pn['hostname'], pn['port'], pn['label']))
            return True
    
    # neither match, so it hasn't been added yet
    print('Processing node of hostname {} and port {} has not yet been added'.format(hostname, port))
    return False
        
# var
username = WebODM_main.username
password = WebODM_main.password

# main

if __name__ == "__main__":
    
    # init parser
    parser = create_parser()
    args = parser.parse_args()
    args_dict = vars(args)
    
    # get arguments
    hostname = args_dict['hostname']
    port = args_dict['port']
    pnid = args_dict['identification']
    
    
    # get authentication token
    token = WebODM_main.post_authentication(username, password)
    
    if not ((args.hostname and args.port) or args.identification):
        WebODM_main.print_error('Not enough arguments')
    
    # delete
    if args_dict['delete'] == True:
        
        if args.identification: # delete by ID
            # delete processing node
            delete_processing_node(token, pnid)
        elif args.hostname and args.port: # delte by hostname and port
            # get ids based on hostname and port
            ids = get_processing_nodes_ids(token, hostname, port)
            
            # delete processing nodes with given ids
            delete_processing_nodes(token, ids)  
        else:
            WebODM_main.print_error('Error deleting processing node')
        
    elif args.hostname and args.port: # create
        # get processing nodes
        processing_nodes = get_all_processing_nodes(token)
        
        # check if processing node already exists
        if not (check_if_pn_added(hostname, port, processing_nodes)): 
            # add processing node
            pnid = post_processing_node(token, hostname, port)
            print(f'Processing Node {pnid} added')
        else:
            # print error message
            WebODM_main.print_error('Processing Node already exists')
    else:
        WebODM_main.print_error('Not enough arguments provided')
            
        

   
    
    
        
    
        
    
    
    