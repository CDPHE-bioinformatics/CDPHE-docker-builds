# terra-jupyter-python image
This repo contians a dockerfile for the docker image used for jupyter notebooks in the terra workspace.

This repo contains the terra-jupyter-python image that is compatible with notebook service in [Terra]("https://app.terra.bio/") called Leonardo. For example, use `us.gcr.io/broad-dsp-gcr-public/terra-jupyter-python:{version}` in terra. the dockerfile was origianlly cloned from https://github.com/DataBiosphere/terra-docker.git

In addtition to the docker image this repo also contains a set of scripts and SARS-CoV-2 genome references. See below for more detail.

## Image contents

The terra-jupyter-python image extends the [terra-jupyter-base](../terra-jupyter-base) image, supported in this repo.

To see the complete contents of this image please see the [Dockerfile](./Dockerfile).

I have appended iqtree (for maximum likelihood phylogenetic analysis) and the python module ete3 (for phylogenetic tree visualization) to the base python dockerfile.

See https://support.terra.bio/hc/en-us/articles/360037143432 for more info on creating a custom jupyter notebook environment for terra workspace.

## to launch a terra notebook with this docker image:
https://support.terra.bio/hc/en-us/articles/360037143432
see the section on launching a notebook with your custom docker image.
The container image name is: mchether/terra_jupyter_docker_seq_analysis:v1

## Scripts and references
The scripts and refereces are kept in this repository for archival purposes. The original purpose of this repo was to run analysis on a jupyter notebook within the terra workspace environment; however we no longer do that and instead have incorporated that analysis into our SC2_lineage_calling_and_results.wdl workflow. It is advised that if you want to use the scripts found in here to use the up to date versions. The most update indel finder version can be found in the SC2_indel_finder repo and the nextclade json parser can be found in the SC2 workflows repo under python scripts.
