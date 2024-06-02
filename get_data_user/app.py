import json
import pymysql

rds_host = 'integradora-desarrollo.cd4gi2og06nk.us-east-2.rds.amazonaws.com'
name = 'root'
password = 'superroot'
db_name = 'coauto'


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
            cursor.execute("SELECT * FROM user")
            result = cursor.fetchall()

            for row in result:
                user = {
                    'id': row[0],
                    'name': row[1],
                    'email': row[2]
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
