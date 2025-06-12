"""
NodeODM_main.py: 

Author: Jonas 
Last Updated: 2025-06-12
"""

# imports
import os, sys, glob, time
import WebODM_main
from pyodm import Node
from pyodm.types import TaskStatus

# variables
def get_images(dir_path):
    """
    Gets all image paths from a given directory path
    
    :param dir_path: directory path to images
    :return images: list of image paths
    """
    
    # list of file image paths
    images = list() 
    min_num_images = 2
    
    # allowed file types
    file_types = ("*.jpg", "*.jpeg", "*.JPG", "*.JPEG") 
    
    # check if valid directory path
    if not os.path.isdir(dir_path):
        WebODM_main.print_error('Invalid Path')
        
    # get all image paths for given directory path and allowed file types
    for type in file_types:
        images.extend(glob.glob(os.path.join(dir_path, type)))
        
    # check if enough images found/provided
    if len(images) < min_num_images:
        WebODM_main.print_error(f'Less than {min_num_images} images found')
        
    # return image paths
    return images


if __name__ == '__main__':
    
    if len(sys.argv) < 2:
        WebODM_main.print_error('Invalid number of arguments')
    
    # var
    dir_path = sys.argv[1] # path to images
    options = {
        'fast-orthophoto': True
    }

    # create node
    n = Node('localhost', 3000)
    print('Node connected')
    
    # get images
    images = get_images(dir_path)
    print('Images retrieved')

    # create task
    task = n.create_task(images, options)
    print('Task created')

    # wait for the task to be completed
    task_info = task.info()
    while task_info.status != TaskStatus.COMPLETED:
        print(f'Task processing . . .  ({task_info.status})')
        task_info = task.info() # reretrieve info
        time.sleep(3)

    # Task completed!
    print('Task Completed')
    
    # download assets and list first 2
    os.listdir(task.download_assets("output/NodeODM"))[0:2]
    print('Assets downloaded')

    # Note, this is essentially just the first script run in the documentation
    # More features and error handling to come