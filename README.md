# WebODM Demo
WebODM Demo is a project intended to demonstrate the capabilities of WebODM for learning and research purposes.

## Requirements
- [Docker](https://www.docker.com/products/docker-desktop/)
- [WebODM](https://opendronemap.org/webodm/)
- [requests library](https://docs.python-requests.org/en/latest/index.html)

## Usuage

### Quickstart.py
`quickstart.py <args> <project_name> <options_file_name> <image_files_dir>`

Additional arguments:
- `-opd` / `--options_dir <string>`: Directory path to folder containing options JSON file. If not provided, assumed to be in root directory.
- `-od` / `--output_dir <string>`: Directory path to folder where output files will be placed. If not provided, output will be placed in root directory. 
- `a` / `--asset <string>`: What asset should be downloaded. Default: `'all.zip'`

Additional notes:
- `username` and `password` should be placed in `.env` file

`more pending`

### delete_project.py
`delete_project.py <name of project>`

Additional Notes:
- Deletes **all** projects of given name, regardless of different IDs, letting one perform mass deletions.

`more pending`

## Documentation
- [WebODM Documentation](https://docs.webodm.org/)
- [ODM Documentation](https://docs.opendronemap.org/)
- [NodeODM Documentation](https://github.com/OpenDroneMap/NodeODM/blob/master/docs/index.adoc) 
- [Multispectral Data Binner](https://github.com/OpenDroneMap/ODM/tree/master/contrib/exif-binner)

