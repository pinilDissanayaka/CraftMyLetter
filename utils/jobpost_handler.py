import os
from langchain.document_loaders import WebBaseLoader


def get_job_description(job_description=None, job_post_url=None):
    if job_description:
        return job_description
    else:
        job_post_url_data=WebBaseLoader(job_post_url).load()
        return job_post_url_data
    