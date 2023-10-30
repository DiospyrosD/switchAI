#!/usr/bin/env python3

import boto3
import openai

def get_key():
    openai.api_key = ""
    session = boto3.Session(region_name='us-east-1')  # Replace 'your-region' with your AWS region.
    ssm_client = session.client('ssm')
    parameter_name = 'OpenAI-Key'  # Replace with the name of your parameter
    try:
        response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
        openai.api_key = response['Parameter']['Value']
    except Exception as e:
        print(f"Error retrieving parameter '{parameter_name}': {str(e)}")
    return openai.api_key