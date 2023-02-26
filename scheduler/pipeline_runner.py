import os
import kfp
import kfp.dsl as dsl
import kfp.components as component

# Building the component from text instead of a yaml file
component_template = """
    name: $job_name
    description: $job_type
    inputs:
    - {name: job_id, type: String, description: 'Job index for job_runner'}
    implementation:
        container:
            image: $image
            command: [
                git fetch; git checkout $branch_name; git pull; $env_vars; python3 scheduler/pipeline_runner.py,
                --job_id,
                
            ]
"""

def job_runner(job_id):
    pass


if __name__=="__main__":

    
    pass
