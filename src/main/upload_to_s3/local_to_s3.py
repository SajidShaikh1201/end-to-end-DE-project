import os
import sys

from src.main.Utility.encrypt_decrypt import *
from src.main.Utility.s3_client import *
from src.main.Utility.logger import *

s3Provider = S3Provider(decrypt(config.aws_access_key_id), decrypt(config.aws_secret_access_key))
s3_client = s3Provider.get_client()

res = s3_client.list_buckets()

# for bucket in res["Buckets"]:
#     print(f"{bucket['Name']}")

# Uploading local data to bucket
"""
1. check data available or not
2. if available then upload it to s3
3. delete data from local 
"""

# checking file availability
file_path = config.local_file_location

if os.listdir(file_path):
    logger.info(f"File '{file_path}' Exist")
else:
    logger.error(f"File '{file_path}' Not Exist")

# Sorting of files
csv_files = []
other_file = []

for file in os.listdir(config.local_file_location):
    if file.endswith(".csv"):
        csv_files.append(file)
        logger.info(f"CSV files - {csv_files}")
    else:
        other_file.append(file)
        logger.warning(f"Other files - {other_file}")
        logger.info("Deleting other files except CSV.....")

        for files in other_file:
            filepath = os.path.join(config.local_file_location, files)
            try:
                if os.path.isfile(filepath):
                    os.remove(filepath)
                    logger.info("Other files are deleted permanently...")
            except:
                logger.error("Error while deleting files....")
