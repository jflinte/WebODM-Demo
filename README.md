# WebODM Demo
A project intended to demonstrate the capabilities of WebODM for learning and research purposes.

## Requirements
- docker
- WebODM
- [requests library](https://docs.python-requests.org/en/latest/index.html)

`more pending`

## Usuage

### Quickstart.py
`quickstart.py <args> <project_name> <options_file_name> <image_files_dir>`

Additional arguments:
- `-opd` / `--options_dir <string>`: Directory path to folder containing options JSON file. If not provided, assumed to be in root directory.
- `-od` / `--output_dir <string>`: Directory path to folder where output files will be placed. If not provided, output will be placed in root directory. 
- `a` / `--asset`: What asset should be downloaded. Default: `'all.zip'`

Additional notes:
- `username` and `password` should be placed in `.env` file



## Documentation
- [WebODM Documentation](https://docs.webodm.org/)
- [ODM Documentation](https://docs.opendronemap.org/)
- [NodeODM Documentation](https://github.com/OpenDroneMap/NodeODM/blob/master/docs/index.adoc) 
- [Multispectral Data Binner](https://github.com/OpenDroneMap/ODM/tree/master/contrib/exif-binner)

`more pending`
