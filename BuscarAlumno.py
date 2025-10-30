import boto3
from boto3.dynamodb.conditions import Key

def lambda_handler(event, context):
    # Entrada (json)
    print(event)
    tenant_id = event['body']['tenant_id']
    alumno_id = event['body']['alumno_id']
    # Proceso
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('t_alumnos')
    response = table.query(
        KeyConditionExpression=Key('tenant_id').eq(tenant_id) & Key('alumno_id').eq(alumno_id)
    )
    items = response['Items']
    num_reg = response['Count']
    print(items)
    # Salida (json)
    return {
        'statusCode': 200,
        'tenant_id': tenant_id,
        'alumno_id': alumno_id,
        'num_reg': num_reg,
        'alumno': items[0] if items else None
    }