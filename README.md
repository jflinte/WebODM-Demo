# WebODM Demo
WebODM Demo is a project intended to demonstrate the capabilities of WebODM for learning and research purposes.

## Requirements
- [Docker](https://www.docker.com/products/docker-desktop/)
- [WebODM](https://github.com/OpenDroneMap/WebODM?tab=readme-ov-file#getting-started)
- [NodeODM](https://github.com/OpenDroneMap/NodeODM/blob/master/docs/index.adoc)
- [PyODM library](https://pyodm.readthedocs.io/en/latest/)
- [requests library](https://docs.python-requests.org/en/latest/index.html)

## Usuage

For Scripts with the prefix <u>WebODM</u>, run `WebODM` using `Docker`

Note that WebODM should be available on `localhost:8000`

For Scripts with the prefix <u>NodeODM</u>, run `NodeODM` using `Docker`

Note that NodeODM should be available on `localhost:3000`

### WebODM_main.py
CLI: `quickstart.py <args> <project_name> <options_file_name> <image_files_dir>`

Additional arguments:
- `-opd` / `--options_dir <string>`: Directory path to folder containing options JSON file. If not provided, assumed to be in root directory.
- `-od` / `--output_dir <string>`: Directory path to folder where output files will be placed. If not provided, output will be placed in root directory. 
- `a` / `--asset <string>`: What asset should be downloaded. Default: `'all.zip'`
- `v` / `--video <string>`: Name of the video file to be uploaded instead of images

Additional notes:
- `username` and `password` should be placed in `.env` file
- Minimum of 5 images must be provided
- Images must be of `*.jpg` file type
- If processing with GCP, the GCP data must be included **IN** the same directory as the images. The data must be stored as a `*.txt` file. 
- If processing with SRT, the SRT file must have the **SAME** name as the video file uploaded and must be in the same directory
- Directory named after the `project_name` will be created either in the root directory or in the specified output directory, where the output will be stored. 

### WebODM_delete_project.py
CLI: `delete_project.py <name of project>`

Additional notes:
- Deletes **all** projects of a given name, regardless of different IDs, letting one perform mass deletions.

### WebODM_processing_nodes.py
CLI: `processing_nodes.py <arguments>`

Additional arguments:
- `hn` / `--hostname <string>`: Hostname of processing node
- `p` / `--port <integer>`: Port of processing node
- `id` / `--identification <integer>`: ID of processing node
- `d` / `--delete`: Set delete to true

Additional notes
- To add a processing node, simply provide the `hostname` and the `port` as arguments
- To delete a processing node, provide either the `hostname` **and** the `port` as arguments or provide only the `id`
- When deleting, `id` is given priority over `hostname` and `port`
- If only `hostname` and `port` are provided, **all** processing nodes with given specifications will be deleted, regardless of differing `ids`

### NodeODM_main.py
CLI: `NodeODM_main.py <path to directory containing images>`

Additional notes
- Still under development

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
- [PyODM Documentation](https://pyodm.readthedocs.io/en/latest/)
- [ClusterODM Documentation](https://github.com/OpenDroneMap/ClusterODM/tree/master)
- [Multispectral Data Binner](https://github.com/OpenDroneMap/ODM/tree/master/contrib/exif-binner)


