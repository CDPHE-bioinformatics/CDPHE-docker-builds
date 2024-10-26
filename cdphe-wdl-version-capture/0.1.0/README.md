# cdphe-wdl-version-capture container

## Description
This tool is used for creating a version capture file for both workflow and tools. It was originally written for the [`CDPHE-bioinformatics/CDPHE-SARS-CoV-2`](https://github.com/CDPHE-bioinformatics/CDPHE-SARS-CoV-2) Github repository but has been transferred to a Docker container.

Script parameters:

`--analysis_date` - date to add to the analysis_date column of the output CSV

`--project_name` - project name of batch being analyzed

`--version_capture_docker_version` - the version of this docker image

`--versions_json` - JSON file with an array of version_info objects 
- keys should be `software`, `docker`, and `version`

`--workflow_name` - workflow name

`--workflow_version` - workflow version with dashes (e.g. v2-2-0)


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
        "docker": "genomicpariscentre/guppy:6.4.6", 
        "software": "guppy", 
        "version": "6.4.6+ae70e8f" 
    }, 
    { 
        "docker": "staphb/artic:1.2.4-1.11.1", 
        "software": "artic", 
        "version": "artic 1.2.4" 
    }, 
    { 
        "docker": "staphb/artic:1.2.4-1.11.1", 
        "software": "medaka", 
        "version": "medaka 1.11.1" 
    }, 
    { 
        "docker": "staphb/samtools:1.16", 
        "software": "samtools", 
        "version": "1.16" 
    }, 
    { 
        "docker": "chrishah/pyscaf-docker", 
        "software": "pyScaf", 
        "version": "0.12a" 
    }, 
    { 
        "docker": "staphb/bcftools:1.16", 
        "software": "bcftools", 
        "version": "1.16" 
    }, 
    { 
        "docker": "quay.io/biocontainers/hostile:1.0.0--pyhdfd78af_0", 
        "software": "hostile", 
        "version": "1.0.0" 
    } 
]
```