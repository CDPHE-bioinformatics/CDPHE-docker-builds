# CDPHE_docker_builds
docker builds for cdphe workflows

## Contributors
| GitHub                  | Docker Hub      |
| ----------------------- | --------------- |
| arianna-smith           | ariannaesmith   |
| danpolanco              | danthecoloradan |
| laura-bankers           | laurabankers    |
| molly-hetheringtonrauth | mchether        |
| sam-baird               | sambaird        |

*Next generation sequencing and bioinformatic and genomic analysis at CDPHE is not CLIA validated at this time. These workflows and their outputs are not to be used for diagnostic purposes and should only be used for public health action and surveillance purposes. CDPHE is not responsible for the incorrect or inappropriate use of these workflows or their results.

## Dockerfile requirements
All Dockerfiles need to have the following labels included:
| label        | Description                                  | Example                                                                          |
| ------------ | -------------------------------------------- | -------------------------------------------------------------------------------- |
| maintainer   | Maintainer's name and email                  | `LABEL maintainer "Arianna Smith <arianna.smith@state.co.us>"`                   |
| registry     | Registry the container is hosted on          | `LABEL registry "Docker Hub"`                                                    |
| namespace    | Registry namespace                           | `LABEL namespace "ariannaesmith"`                                                |
| repository   | Registry repository (container name)         | `LABEL repository "cdphe_h5_influenza"`                                          |
| source_code  | GitHub repository where Dockerfile is hosted | `LABEL source_code "https://github.com/CDPHE-bioinformatics/CDPHE-H5-influenza"` |
