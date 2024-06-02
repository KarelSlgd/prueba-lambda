import json
import pymysql
import os

rds_host = os.environ['RDS_HOST']
name = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']
db_name = os.environ['DB_NAME']

def lambda_handler(event, context):
    connection = pymysql.connect(
        host=rds_host,
        user=name,
        password=password,
        database=db_name
    )

    users = []

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, email, phone_number, profile_image_url, role FROM user")
            result = cursor.fetchall()

            for row in result:
                user = {
                    'id': row[0],
                    'email': row[1],
                    'phone_number': row[2],
                    'profile_image_url': row[3],
                    'role': row[4]
                }
                users.append(user)

    finally:
        connection.close()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "get users",
            "data": users
        }),
    }
