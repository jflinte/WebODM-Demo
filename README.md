# WebODM Demo
WebODM Demo is a project intended to demonstrate the capabilities of WebODM for learning and research purposes.

## Requirements
- [Docker](https://www.docker.com/products/docker-desktop/)
- [WebODM](https://github.com/OpenDroneMap/WebODM?tab=readme-ov-file#getting-started)
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
- Minimum of 5 images must be provided
- Images must be of `*.jpg` file type
- If processing with GCP, the GCP data must be included **IN** the same directory as the images. The data must be stored as a `*.txt` file. 
- Directory named after the `project_name` will be created either in the root directory or in the specified output directory, where the output will be stored. 

`more pending`

### delete_project.py
`delete_project.py <name of project>`

Additional Notes:
- Deletes **all** projects of a given name, regardless of different IDs, letting one perform mass deletions.

`more pending`

## Adding Additional Processing Nodes
- [Set up Environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment) (if on Windows)
- [Start up NodeODM](https://github.com/OpenDroneMap/NodeODM) on new machine
- [Add Processing Node](https://docs.webodm.org/#processing-node) with WebODM API or GUI

## Adding Distributed Computing
Follow steps provided [here](https://www.opendronemap.org/clusterodm/) and [here](https://docs.opendronemap.org/large/#distributed-split-merge)

## Additional Features of WebODM
- [SSL](https://letsencrypt.org/)
- [IPv6](https://github.com/OpenDroneMap/WebODM?tab=readme-ov-file#getting-started)
- [Run (Docker Version) as Linux Service](https://github.com/OpenDroneMap/WebODM?tab=readme-ov-file#getting-started)
- [Multispectral image](https://en.wikipedia.org/wiki/Multispectral_imaging) processing

## Additional Assets
- [Hugin](https://wiki.panotools.org/Hugin#Development) can be used to stitch together Orthophotos. Supports [Python Scripts](https://hugin.sourceforge.io/docs/manual/Hugin_Scripting_Interface.html
)
- [Extract](https://github.com/fede2cr/video2webodm) stills from video file (I believe [WebODM](https://docs.webodm.net/how-to/process-video-files/) already has the feature)

## Datasets
- [ODM](https://www.opendronemap.org/odm/datasets/)
- [ArcGIS Reality](https://www.esri.com/en-us/arcgis/products/arcgis-reality/resources/sample-drone-datasets)
- [UAV-datasets](https://github.com/qiangsun89/UAV-datasets)

## Documentation
- [WebODM Documentation](https://docs.webodm.org/)
- [ODM Documentation](https://docs.opendronemap.org/)
- [NodeODM Documentation](https://github.com/OpenDroneMap/NodeODM/blob/master/docs/index.adoc) 
- [ClusterODM Documentation](https://github.com/OpenDroneMap/ClusterODM/tree/master)
- [Multispectral Data Binner](https://github.com/OpenDroneMap/ODM/tree/master/contrib/exif-binner)


