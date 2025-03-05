# cdphe-wdl-version-capture container

## Description
This tool is used for creating a version capture file for both WDL workflows and task software. See the associated WDL task file to import [here](https://github.com/CDPHE-bioinformatics/CDPHE-H5-influenza/blob/main/src/wdls/version_capture_tasks.wdl).

Script parameters:

`--analysis_date` - date to add to the analysis_date column of the output CSV

`--docker_host` - the Dockerfile ENV variable `HOST` for this container

`--docker_name` - the Dockerfile ENV variable `NAME` for this container

`--docker_version` - the Dockerfile ENV variable `VERSION` for this container

`--project_name` - name of sequencing run being analyzed

`--version_capture_docker_version` - the version of this docker image

`--versions_json` - JSON file with an array of version_info objects. See below for example

`--workflow_name` - workflow name

`--workflow_version` - workflow version without periods (e.g. v2_2_0)


## Examples
### Usage
```
version_capture.py \
  --analysis_date 2024-10-19
  --project_name cov_2198_grid \
  --versions_json versions.json \
  --workflow_name SC2_ont_assembly \
  --workflow_version v2_3_6 \
```

### versions.json
```
[ 
    { 
        "docker": "staphb/samtools:1.16", 
        "software": "samtools", 
        "version": "1.16" 
    }, 
    { 
        "docker": "quay.io/biocontainers/hostile:1.0.0--pyhdfd78af_0", 
        "software": "hostile", 
        "version": "1.0.0" 
    }
]
```