import json
import boto3
import urllib3
import datetime

# REPLACE WITH YOUR DATA FIREHOSE NAME
FIREHOSE_NAME = 'PUT-S3-Zmiqf'

def lambda_handler(event, context):
    http = urllib3.PoolManager()

    r = http.request("GET",
                     "https://api.stockdata.org/v1/data/quote?symbols=SPY,QQQ,DIA&api_token=ORxC2vjwqqUQNckhKcpluiPLqB1WXNxvLX2adHOx")

    # turn it into a dictionary
    r_dict = json.loads(r.data.decode(encoding='utf-8', errors='strict'))

    # Create a list to store processed stock data
    processed_data_list = []

    # Iterate over the list of stock data
    for stock in r_dict['data']:
        # extract pieces of the dictionary
        processed_dict = {}
        processed_dict['ticker'] = stock['ticker']
        processed_dict['name'] = stock.get('name')
        processed_dict['price'] = stock['price']
        processed_dict['day_high'] = stock['day_high']
        processed_dict['day_low'] = stock['day_low']
        processed_dict['day_open'] = stock['day_open']
        processed_dict['52_week_high'] = stock['52_week_high']
        processed_dict['52_week_low'] = stock['52_week_low']
        processed_dict['previous_close_price'] = stock['previous_close_price']
        processed_dict['day_change'] = stock['day_change']
        processed_dict['volume'] = stock['volume']
        processed_dict['row_ts'] = str(datetime.datetime.now())

        # Add the processed dictionary to the list
        processed_data_list.append(processed_dict)

    # Create a boto3 Firehose client
    fh = boto3.client('firehose')

    # Send each processed dictionary as a separate record to the Firehose delivery stream
    for data in processed_data_list:
        msg = json.dumps(data) + '\n'
        fh.put_record(
            DeliveryStreamName=FIREHOSE_NAME,
            Record={
                'Data': msg
            }
        )

    return {
        'statusCode': 200,
        'body': json.dumps('Data successfully sent to Firehose')
    }
