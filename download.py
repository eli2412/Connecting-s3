from auth import auth
#downloading from s3 bucket
def download_file(object_key, new_file_name):
  s3_resource, s3_bucket = auth('config.ini')
  try:
    bucket = s3_resource.Bucket(s3_bucket)
    # Replace with the path where you want your file to be saved!
    bucket.download_file(object_key, f'data/output/{new_file_name}')
    return True
  except Exception as e:
    print(f'Error downloading file to S3: {str(e)}')
    return False