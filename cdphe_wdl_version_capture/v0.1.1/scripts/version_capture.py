import argparse
import json
import pandas as pd
import sys

def get_options(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()
    parser.add_argument('--analysis_date', 
                        help = 'date to add to the analysis_date column in the output CSV',
                        required = True)
    parser.add_argument('--project_name', 
                        help = 'project name of batch being analyzed (e.g. cov_2022_grid)',
                        required = True)
    parser.add_argument('--versions_json', 
                        help = 'JSON file with an array of version_info objects (keys should be "software", "docker", and "version")',
                        required = True)
    parser.add_argument('--workflow_name', 
                        help = 'workflow name (e.g. SC2_ont_assembly)',
                        required = True)
    parser.add_argument('--workflow_version', 
                        help = 'workflow version without periods (e.g. v2-2-0)',
                        required = True)
    parser.add_argument('--docker_name', 
                        help = 'the Dockerfile ENV variable "NAME" for this container',
                        required = True)
    parser.add_argument('--docker_host', 
                        help = 'the Dockerfile ENV variable "HOST" for this container',
                        required = True)
    parser.add_argument('--docker_version', 
                        help = 'the Dockerfile ENV variable "VERSION" for this container',
                        required = True)
    parser.add_argument('--sample_name', 
                        help = 'provide only when calling from a sample-level workflow', 
                        required = False,
                        default = None)
    options = parser.parse_args(args)
    return options

def create_version_df(options):
    with open(options.versions_json) as f:
        records = json.load(f)['versions']

    docker_full_name = options.docker_host + '/' + options.docker_name

    version_capture_docker_record = {
        'software': options.docker_name,
        'docker': docker_full_name,
        'version': options.docker_version
    }
    records.insert(0, version_capture_docker_record)

    df = pd.DataFrame(records)
    df = df.rename(columns={'docker': 'associated_docker_container'})  # backwards-compat naming
    
    if options.sample_name is not None:
        insert_dict = {'sample_name': options.sample_name}
    else:
        insert_dict = {}
    insert_dict.update({'project_name': options.project_name, 
                        'analysis_date': options.analysis_date})
    for i, (k, v) in enumerate(insert_dict.items()):
        df.insert(i, k, v)
    
    return df

def create_out_fn(options):
    prefix = 'version_capture_'
    suffix = f'{options.workflow_name}_{options.project_name}_{options.workflow_version}.csv'
    if options.sample_name is not None:
        out_fn = prefix + options.sample_name + '_' + suffix
    else:
        out_fn = prefix + suffix
    
    return out_fn
        
if __name__ == '__main__':
    options = get_options()
    df = create_version_df(options)
    out_fn = create_out_fn(options)
    df.to_csv(out_fn, index=False)
