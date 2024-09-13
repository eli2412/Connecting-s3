import configparser
import boto3

def auth(config_filename):
  config = configparser.ConfigParser()

  # Read the configuration file
  credentials = config.read(config_filename)

   # AWS credentials
  service_name = config.get('aws_s3', 'service_name')
  region_name = config.get('aws_s3', 'region_name')
#   aws_access_key_id = config.get('aws_s3', 'aws_access_key_id')
#   aws_secret_access_key = config.get('aws_s3', 'aws_secret_access_key')
  s3_bucket = config.get('aws_s3', 's3_bucket')

  s3_resource = boto3.resource(
    service_name=service_name,
    region_name=region_name,
    # aws_access_key_id=aws_access_key_id,
    # aws_secret_access_key=aws_secret_access_key
  )

  return s3_resource, s3_bucket

test = auth('config.ini')
print(test[0]) # Prints s3.ServiceResource()
print(test[1]) # Prints the name of the s3_bucket you are connecting to