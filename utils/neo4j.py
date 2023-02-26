
'''
    Contains all neo4j helper functions
'''
import os
from py2neo import Graph
from constants.compute_constants import JOB_NOT_STARTED

url = os.environ.get('NEO4J_URL')
username = os.environ.get('NEO4J_USERNAME')
passwd = os.environ.get('NEO4J_PASSWORD')

g = Graph(url = url, user=username, password=passwd)

def get_jobs():
    ''' 
        Fetches all jobs from the job node that have not been processed 
    '''
    query = """
        MATCH (j:job)
        WHERE j.status = $status or NOT EXISTS(j.status)
        RETURN j.id as id, j.status as status, j.type as type
    """
    res = g.run(query, status=JOB_NOT_STARTED)
    return res

def get_job_data(job_id: str):
    
    query = """
        MATCH (j:job)
        WHERE j.id = $job_id
        RETURN j.params as params, j.id as id, j.status as status
    """
    res = g.run(query, job_id=job_id)
    return res

def update_node(node: str, identifier: str, update_dict: dict):

    update_dict = ["n.{}={}".format(k,v) for k,v in update_dict.items()]
    sub_query = ','.join(update_dict)

    query = """
        MATCH (n:$node)
        WHERE n.id = $identifier
        SET $sub_query
    """

    g.run(query, node=node, identifier=identifier, sub_query=sub_query)

