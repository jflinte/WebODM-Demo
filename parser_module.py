"""
parser_module.py: parsing given from user

./ <args> <project_name> <options_file_name> <image_files_dir> 

Author: Jonas 
Last Updated: 2025-06-05
"""

# imports
import requests, sys, os, argparse, string

# functions
def create_parser():
    """
    Creates Parser and adds required arguments to it
    
    :param: N/A 
    :return: ArgumentParser object
    """
    
    parser = argparse.ArgumentParser()

    # Name of Project
    parser.add_argument("project_name", help="Name of the project to be created")

    # Name of Options File 
    parser.add_argument("options_file_name", help="Name of the JSON file containing the options to be uploaded")
    
    # Image Files Location
    parser.add_argument("image_files_dir", help="Directory path to folder of images to be uploaded (and optionally the GCP text file)")

    # Options File Location (default is in root directory)
    parser.add_argument("-opd", "--options_dir", help="Directory path to folder containing options JSON file", type=str)

    # Output directory (default is root directory)
    parser.add_argument("-od", "--output_dir", help="Directory path to folder where output files will be placed", type=str)

    # Asset to Download (default is all.zip)
    parser.add_argument("-a", "--asset", help="What asset should be downloaded", type=str, default="all.zip")
    
    return parser

def validate_asset(available_assets, asset):
    """
    Check if assets is in available assets list. If not, set to 'all.zip'
    
    :param available_assets: all assets available to download (list)
    :param asset: user inputed asset (string)
    :return: asset (string)
    """
    
    # var
    default_asset = 'all.zip'
    
    # validation
    if asset in available_assets: # check if asset available
        # asset is avaiable, so it is returned
        return asset
    else: 
        
        # notify user of availability and print available assets
        print(f"\nAsset ({asset}) not found in available assets:")
        for a in available_assets:
            print(f"\t* {a}")
        
        # notify user that asset set to default
        print(f"Setting asset to \'{default_asset}\'\n")
        
        # return the default asset
        return default_asset

def get_options_file_path(args_dict):
    """
    Get options file path if a file path is given. Otherwise, simply return options file name under the assumption that it is in the root directory
    
    :param args_dict: arguments input by user (dictionary)
    :return: options_file_path (string)
    """
    
    # var
    options_name = args_dict['options_file_name']
    options_file_path = args_dict['options_dir']
    
    # handling
    if options_file_path == None: # if path not provided, return options name
        return options_name
    else: # if path provided, return joined path and name
        return os.path.join(options_file_path, options_name)
    
    

if __name__ == "__main__":
    # var
    available_assets = ["all.zip", "orthophoto.png", "orthophoto.tiff"]
    
    # create parser
    parser = create_parser()

    # get parser arguments
    args = parser.parse_args()
    args_dict = vars(args)
    
    # I think a lot of the validation (such as if the dir exists, will be done automatically by the OS)
    
    # options
    options_file_path = get_options_file_path(args_dict)
    
    # Asset handler 
    asset = validate_asset(available_assets, args_dict['asset'])
    
    

    # note that python3 is skipped over when using argv
    
    for key, value in args_dict.items():
        print(f'{key}: {value}')

    print(f'validated asset: {asset}')
    print(f'options file path: {options_file_path}')
    