from auth import auth
#uploading from s3 bucket
def upload_file(object_key, filename):
  s3_resource, s3_bucket = auth('config.ini')
  try:
    bucket = s3_resource.Bucket(s3_bucket)
    # Replace the string with your local path to the file
    bucket.upload_file(f'data/input/{filename}', object_key)
    return True
  except Exception as e:
    print(f'Error uploading file to S3: {str(e)}')
    return False