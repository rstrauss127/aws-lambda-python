from dataclasses import dataclass
import psycopg2
from psycopg2.extras import RealDictCursor
import json

host = "ccrm-internal-dev-instance-1.c2q9cwd22amo.us-east-1.rds.amazonaws.com"
username ="postgres"
password = "postgres"
database ="ccrmdev"

conn = psycopg2.connect(
    host = host,
    database = database,
    user = username,
    password = password
)

def lambda_handler(event, context):
    cur = conn.cursor(cursor_factory = RealDictCursor)
    cur.execute(""" SELECT userroleid, userroledescription, permissionindicator, lastupdatedby, active from "Truist_Lookup"."Lookup_User_Role" """) ##need these quotes because database tables are capitalized 
    results = cur.fetchall()
    json_result = json.dumps(results)
    print(json_result)
    return json_result
    
    

#lambda_handler()
