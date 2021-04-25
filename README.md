# pinpoint-renewal-reminder
A mechanism to send renewal reminders to your customers using Pinpoint

**Use-cases**

1) Subscription/Contract renewal
2) Appointment reminder

**Background**

Companies want to have the ability to remind their customers for upcoming activities related to their products or services. Such cases include subscription renewal or appointment reminder and both have a monetary value attached to them. In the subscription case, if customers receive a reminder X days before the subscription there is a higher probability of them renewing and consequently the company decreasing the churn rate. In the case of appointment reminder, it helps companies to ensure that their resources are being utilised 100% by decreasing the number of no-show appointments.

**Solution**

This solution allows Pinpoint customers to assess and qualify customers who are X days away from the end of their subscription or appointment and add them to a segment. The segment works as the entry point for a Pinpoint Journey that sends out reminders. Every day (frequency can be changed) a Lambda is being executed and updates the segment mentioned above to include customers whose renewal date is TODAY + X days. The X days is a variable that can be changed when deploying the solution and refers to the number of days that you would like to send the first reminder to your customers who are up for renewal or an appointment. 

**Considerations**

1) All customers will need to have a User Attribute with their renewal date stored in there
2) Pinpoint Journeys with segments as an entry point, review the segment at a maximum frequency of 1 hour

**Incorporating timezone - !!!NOT PART OF THIS SOLUTION**

To incorporate timezone to this solution, three changes will need to take place:
1) The CloudWatch event will need to take place every hour
2) The "Renewal_Reminder" segment criteria will be a list of date-times for all the timezones of your customers. The format will include date, time (up to hour) and the timezone symbol e.g. 2021-04-20_10:00:00UTC. Ensure that the segment criteria Attribute operator is "Contains" and all date-times generated are in a form of a list
3) The User Attribute "renewal_date" should also follow the format of date, time (up to hour) and timezone symbol as shown on point 2

**Architectural diagram**

![alt text](https://github.com/Pioank/pinpoint-renewal-reminder/blob/main/Images/Architecture_Diagram.JPG)

**How to implement**

**First step:** Ensure that your Pinpoint users have a Pinpoint User Attribute renewal_date that includes the renewal date of their subscription or the date of the appointment

**Second step:** Create a segment with a name "Renewal_Reminder" and configure its criteria like the screenshot below. Once the segment is created then obtain its segment ID, which is required for the next step

![alt text](https://github.com/Pioank/pinpoint-renewal-reminder/blob/main/Images/Create_Renewal_Segment.JPG)

**Third step:** Navigate to CloudFormation on AWS console and create a new stack with new resources. Upload the [yaml file in this repository](https://github.com/Pioank/pinpoint-renewal-reminder/blob/main/Pinpoint_Renewal_Reminder.yaml) and fill the fields as shown on the screenshot below. Note that you will need to obtain your own Pinpoint Project ID and the Segment ID from the segment you created on the second step.

![alt text](https://github.com/Pioank/pinpoint-renewal-reminder/blob/main/Images/Cloudformation_Input.JPG)

**Fourth step:** At this point the Lambda on the third step will be triggered daily, which you can change by navigating to CloudWatch. To start sending reminders to your customers, create a Pinpoint Journey - see an example below:

![alt text](https://github.com/Pioank/pinpoint-renewal-reminder/blob/main/Images/Pinpoint_Renewal_Journey.JPG)


