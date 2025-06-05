"""
quickstart.py: Demo

Author: Jonas 
Last Updated: 2025-06-05
"""

# imports
import requests, glob, sys, os, time, json # standard libraries
from dotenv import load_dotenv 
import status_codes 
import parser_module


# environment variables
load_dotenv() # load environment variables

# defaults
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

# global variables
file_types = ("*.jpg", "*.jpeg", "*.JPG", "*.JPEG")
min_number_of_images = 5

# functions

def print_error(error_message):
    """
    Prints an error to the console and exits the system
    
    :param error_message: error message to be printed
    :return: N/A
    """
    
    print(f"ERROR: {error_message} \nexiting with status 1")
    sys.exit(1)
    
def post_authentication(username, password):
    """
    Authenticates a user
    
    :param username: username (str)
    :param password: password (str)
    :return: token or -1 if error
    """
    
    res = requests.post('http://localhost:8000/api/token-auth/',
                    data = {'username': username, 
                            'password': password}).json()
    
    # get authentication token
    if 'token' in res:
        return res['token'] 
    else:
        print_error("Invalid credentials")
        
def post_project(token, project_name):
    """
    Creates a new project
    
    :param token: authentication token (str)
    :param name: name of new project (str)
    :return: id of new project
    """
    
    res = requests.post('http://localhost:8000/api/projects/',
                        headers = {'Authorization': 'JWT {}'.format(token)}, #note, format replaces {} with token
                        data = {'name' : project_name}).json() 
    # get project id
    if 'id' in res:
        return res['id'] 
    else:
        print_error("Unable to create Project")

def post_task(token, project_id, images, options):
    """
    Sends images to WebODM
    
    :param token: authentication token
    :param project_id: ID of project
    :param images: list of images to send to server
    :param options: options for given task
    :return: ID of task
    
    """

    res = requests.post('http://localhost:8000/api/projects/{}/tasks/'.format(project_id),
                        headers ={'Authorization': 'JWT {}'.format(token)},
                        files = images,
                        data = {
                            'options': options
                        }).json()
    
    # get project id
    if 'id' in res:
        return res['id'] 
    else:
        print_error("Unable to create Task")

def delete_project(token, project_id):
    """
    delete a project
    
    :param token: authentication token
    :param project_id: ID of project to be deleted
    :return: N/A
    """
    
    res = requests.delete("http://localhost:8000/api/projects/{}/".format(project_id),
                          headers={'Authorization': 'JWT {}'.format(token)})

def get_image_paths(dir_path):
    """
    Gets all image paths from a given directory path
    
    :param dir_path: directory path to images
    :return images: list of image paths
    """
    
    # empty list
    image_paths = list()
    
    # search for all file types
    for type in file_types:
        image_paths.extend(glob.glob(os.path.join(dir_path, type))) # add file paths of given type to image paths
    
    # check length
    if len(image_paths) < min_number_of_images:
        print_error("Less than {} images provided".format(min_number_of_images))
    else:
        print(f"Found {len(image_paths)} images")
    
    # return all of the paths
    return image_paths
        
def get_images(image_paths):
    """
    Gets a list of images from a given list of file paths
    
    :param image_paths: paths to the images
    :returns: images
    """

    # create empty list of images    
    images = list()
    gcp_paths = list()
    text_file_types = ["*.txt", "*.TXT"]
    
    # iterate through each path
    for image_path in image_paths:
        # append tuple to images
        images.append(('images', (os.path.basename(image_path), open(image_path, 'rb'), 'image/jpg')))
    
    # append gcp data
    for type in text_file_types: # check for gcp files
        gcp_paths.extend(glob.glob(os.path.join(image_path, type))) # add file paths of given type to image paths

    if gcp_paths != []: # check if gcp file give
        for gcp_path in gcp_paths: # append all gcp files to end of images
            images.append(('gcp', (os.path.basename(gcp_path), open(gcp_path, 'rb'), 'gcp')))

    # return images
    return images

def get_task(token, project_id, task_id):
    """
    Gets task
    
    :param token: authentication token
    :param project_id: ID of project
    :param task_id: ID of task
    :return: task
    """
    
    # get project and task based on their respective identification
    res = requests.get('http://localhost:8000/api/projects/{}/tasks/{}/'.format(project_id, task_id),
                        headers = {'Authorization': 'JWT {}'.format(token)}).json()
    
    return res

def get_download(token, project_name, project_id, task_id, output_dir, asset):
    """
    Downloads a given asset. If output directory not found, defaults to root directory
    
    :param token: authentication token
    :param project_name: name of project
    :param project_id: ID of project
    :param task_id: ID of task
    :param output_dir: directory of where the file should be downloaded
    :param asset: what to download (ex. orthophoto.tif)
    :return: N/A
    """
    
    # get download
    res = requests.get("http://localhost:8000/api/projects/{}/tasks/{}/download/{}".format(project_id, task_id, asset), 
                        headers={'Authorization': 'JWT {}'.format(token)},
                        stream=True)

    asset_path = str()
    
    # check that output directory is valid
    if output_dir == None:
        # make directory 
        os.makedirs("{}".format(project_name), exist_ok=True) 
        
        # get path
        asset_path = os.path.join(project_name, asset)
    elif os.path.exists(output_dir) and os.path.isdir(output_dir):
        # make directory 
        os.makedirs("{}/{}".format(output_dir, project_name), exist_ok=True)
        
        # get path
        asset_path = os.path.join(output_dir, project_name)
        asset_path = os.path.join(asset_path, asset)
    else:
        print(f"\nOutput_dir invalid, downloading {asset} to root directory\n")
    
    # write to new file in chunks 
    with open(f"{asset_path}", 'wb') as f:
        for chunk in res.iter_content(chunk_size=1024): 
            if chunk:
                f.write(chunk)

    # print notification of download to console
    print(f"Saved ./{asset_path}")
    
def get_options(file_name):
    """
    Reads in a JSON file to get the various options
    
    :param file_name: file name of options (JSON)
    :return: options in raw JSON format
    """

    with open(f"{file_name}", 'r') as file:
        raw_options = file.read()

    return raw_options

def get_status(token, project_id, task_id):
    """
    Gets status of given project and task
    
    :param token: authentication token
    :param project_id: ID of project
    :param task_id: ID of task
    :return: Status (corresponds to status_code), processing time (milliseconds ellapsed)
    """
    
    # get project and task based on their respective identification
    res = requests.get('http://localhost:8000/api/projects/{}/tasks/{}/'.format(project_id, task_id),
                        headers = {'Authorization': 'JWT {}'.format(token)}).json()
    # return status
    return res['status']

def get_processing_time(token, project_id, task_id):
    """
    Gets processing time of given project and task
    
    :param token: authentication token
    :param project_id: ID of project
    :param task_id: ID of task
    :return: Status (corresponds to status_code), processing time (milliseconds ellapsed)
    """
    
    # get project and task based on their respective identification
    res = requests.get('http://localhost:8000/api/projects/{}/tasks/{}/'.format(project_id, task_id),
                        headers = {'Authorization': 'JWT {}'.format(token)}).json()
    # return status
    return res['processing_time']



# main

if __name__ == "__main__":
    
    # init parser
    parser = parser_module.create_parser() # create parser and arguments
    args = parser.parse_args() 
    args_dict = vars(args) # convert args into dictionary
    
    # variable assignment
    project_name = args_dict["project_name"] # assign project name
    options_file_name = parser_module.get_options_file_path(args_dict) # assign options file name (and path)
    image_file_location = args_dict["image_files_dir"] # assign image file location
    output_dir = args_dict["output_dir"] # assign output directory
    asset = args_dict["asset"] # assign asset to download (could be set to a default value)
    
    # get image paths 
    image_paths = get_image_paths(image_file_location)
    
    # authorize
    token = post_authentication(username, password)
    
    # notify user of being logged in
    print(f"Logged in: {username}")
    
    # create new project
    project_id = post_project(token, project_name)
    
    # notify user of created project
    print(f"Project created: {project_name}")
    
    # get image paths
    images = get_images(image_paths)
    
    # get options
    options = get_options(options_file_name)

    # send images with the given options to server
    task_id = post_task(token, project_id, images, options)
    
    # monitor task until completion or failure
    try:
        while True:
            # get status 
            status = get_status(token, project_id, task_id)
            
            # check status
            if status == status_codes.COMPLETED:
                print("Task completed")
                break
            elif status == status_codes.FAILED:
                print("Task failed")
            else:
                # processing_time = get_processing_time(token, project_id, task_id)
                res = get_task(token, project_id, task_id)
                processing_time = res['processing_time']
                progress = res['running_progress']
                # print(res.keys())
                
                # format time
                s = processing_time / 1000 # convert from milliseconds to seconds
                s = 0 if processing_time < 0 else s # set to zero if less than zero
                m, s = divmod(s, 60) # get minutes
                h, m = divmod(m, 60) # get hours

                # get time 
                elapsed_time = f'{round(h):02}:{round(m):02}:{round(s):02}'
                
                # print time
                print(f"Processing . . . ({elapsed_time}) ({progress*100:2.2f}%)")
                
                # sleep
                time.sleep(3)
    except KeyboardInterrupt:
        # delete project
        delete_project(token, project_id)
        
        # stop program 
        print_error("KeyboardInterrupt")
    
    # print total time
    print(f'Total Time: {elapsed_time}')
    
    # get available assets
    res = get_task(token, project_id, task_id) # get task
    available_assets = res['available_assets'] # get all available assets
    
    # validate chosen asset
    asset = parser_module.validate_asset(available_assets, asset)
    
    # download asset
    get_download(token, project_name, project_id, task_id, output_dir, asset)

