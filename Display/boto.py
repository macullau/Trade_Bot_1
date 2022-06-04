import boto3

s3 = boto3.resource('s3')
s3.meta.client.upload_file('Data/pie_charts.png', 'mc-display-charts-bucket', 'pie_charts.png', ExtraArgs={'ACL':'public-read'})