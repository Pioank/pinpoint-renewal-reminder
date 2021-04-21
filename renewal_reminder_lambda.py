import os
import boto3
import json
from datetime import date
import datetime

pinpoint_id = os.environ['PINPOINT_APP_ID']
reminder_period = int(os.environ['REMINDER_PERIOD'])
segment_id = os.environ['SEGMENT_ID']
client = boto3.client('pinpoint')

def lambda_handler(event, context):
    today = date.today()
    renewal_reminder = today + datetime.timedelta(days=reminder_period)
    renewal_reminder = renewal_reminder.strftime("%Y/%m/%d")
    print("""
    The date today is """ + str(today) + """
    
    Reminder period is set to """ + str(reminder_period) + """
    
    Users whose renewal date is: """ + renewal_reminder + """ will be contacted via the renewal reminder Pinpoint Journey!
    
    Pinpoint Segment Update Response: 
    """ )
    
    
    update_segment = client.update_segment(
    ApplicationId=pinpoint_id,
    SegmentId=segment_id,
    WriteSegmentRequest={
        'Dimensions': {
            'UserAttributes': {
                'renewal_date': {
                    'AttributeType': 'CONTAINS',
                    'Values': [
                        renewal_reminder,
                    ]
                }
            }
            }
    })
    
    print(update_segment['SegmentResponse'])
    print("")
