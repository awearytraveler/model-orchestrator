'''
    Contains methods to launch jobs on K8s cluster
'''
import json
import os
from utils.neo4j import get_jobs, update_node
from pipeline_runner import job_runner

def sentinel():
    '''
        Sentinel scans the job node for any queued jobs
    '''
    try:
        job_list = get_jobs()
        for job in job_list:
            job_id = job['id']
            job_type = job['type']
            job_status = job['status']


    except Exception as e:
        print(e) #TODO: Add logger