import logging
import os
import boto3
from configparser import*
import pg8000
import json
import re

logger = logging.getLogger()
logger.setLevel(logging.INFO)

step_function_arn =os.environ['step_function_arn.py']


logger.info(f"Redshift dtabse :{rs_database}"}
logger.info(f"Redshift host :{rs_host}, Redshift Port:{rs_port_"}

def validate_tble(conn, dc, tbl):
  return result

def send_sns(Message):
  message_body ={'Msg':'DDL was just execute'}
  message_body = json.dumps(message_body)
  logger.info(message_body)
  sns.boto3.client('sns', verify=False)
  topic_arn =''
  subject='Hello this is subject'
  sns.publish(TargetArn=topic_arn, Message=message_body, Subject=subject)

def execute_step_function(arg1, arg2):
  logger.info(f"Redshift host :{rs_host}, Redshift Port:{rs_port_"}
  send_sns(Message)
  
def process_active_section(active_sessions, step_function_arn)
  logger.info(f"Redshift host :{rs_host}, Redshift Port:{rs_port_"}
  execute_step_function(arg1, arg2)

def lambda_handeler(event,context)
  active_sprints = ["event1"]
  process_activate_section(active_sessions, step_function_arn)
