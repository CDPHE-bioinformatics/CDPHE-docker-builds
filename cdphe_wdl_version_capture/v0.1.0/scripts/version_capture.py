import argparse
import json
import pandas as pd
import sys
import docker

def get_options(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--analysis_date', help='date to add to the analysis_date column in the output CSV')
    parser.add_argument('--project_name', help='project name of batch being analyzed (e.g. cov_2022_grid)')
    parser.add_argument('--versions_json', help='JSON file with an array of version_info objects (keys should be "software", "docker", and "version")')
    parser.add_argument('--workflow_name', help='workflow name (e.g. SC2_ont_assembly)')
    parser.add_argument('--workflow_version', help='workflow version without periods (e.g. v2-2-0)')
    options = parser.parse_args(args)
    return options

def create_version_df(options):
    with open(options.versions_json) as f:
        records = json.load(f)['versions']

    client = docker.from_env()
    docker_name = client.images.labels['name']
    docker_full_name = client.images.labels['host'] + '/' + docker_name
    docker_version = client.images.labels['dockerfile.version']

    version_capture_docker_record = {
        'software': docker_name,
        'docker': docker_full_name,
        'version': docker_version
    }

    records.insert(0, version_capture_docker_record)
    df = pd.DataFrame(records)
    df.insert(0, 'project_name', options.project_name)
    df.insert(1, 'analysis_date', options.analysis_date)
    df = df.rename(columns={'docker': 'associated_docker_container'})  # backwards-compat naming
    
    return df

if __name__ == '__main__':
    options = get_options()
    df = create_version_df(options)
    outfile = f"version_capture_{options.workflow_name}_{options.project_name}_{options.workflow_version}.csv"
    df.to_csv(outfile, index=False)
