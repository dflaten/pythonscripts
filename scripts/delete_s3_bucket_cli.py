#!/usr/bin/env python3
"""
This tool assumes you have the aws CLI installed and have credentials to an 
aws account active and valid before running.
"""
import subprocess
import json

#For Reference
RETRIEVE_S3_BUCKETS_CMD = "aws s3api list-buckets"

# Retrieve all buckets in an account. 
bucket_list_cmd = subprocess.Popen(['aws', 's3api', 'list-buckets'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT)

stdout, stderr = (bucket_list_cmd.communicate())
bucket_list_result = stdout.decode('UTF-8')

# Save list of buckets for reference
bucket_list_file = open('s3bucketlist.json', 'w')
bucket_list_file.write(bucket_list_result)
bucket_list_file.close()

buckets_to_delete = {}
bucket_list_json = json.loads(bucket_list_result)

for s3dict in bucket_list_json['Buckets']:
    if s3dict['Name'].startswith("first-bucket"):
        buckets_to_delete[s3dict['Name']] = s3dict['CreationDate']

# Print and write list of buckets to delete:
print("S3 buckets to be deleted:")
with open('s3bucketlisttodelete.txt', mode = 'w') as results:
    for key, value in buckets_to_delete.items():
        line = key + ' : ' + value
        print(line)
        results.write(line)
        results.write('\n')
    results.close()

print('\n')
print("List of buckets to be deleted has been saved in \'s3bucketlisttodelete.txt\'. Please review.")
print("Please confirm you want all of these buckets deleted. This is not reversable. Type \"Yes\" to confirm. Anything else to cancel.")
print('\n')

try:
      confirmation = str(input("Enter Confirmation: "))
      if confirmation == "Yes":
        print("Deleting all buckets listed in \'s3bucketlisttodelete.txt\'")
        for key, value in buckets_to_delete.items():
            print("Attempting to delete bucket: " + key)
            delete_call_cmd = subprocess.Popen(['aws','s3api','delete-bucket','--bucket', key],
                                                  stdout=subprocess.PIPE,
                                                  stderr=subprocess.STDOUT)
            stdout, stderr = (delete_call_cmd.communicate())
        print("Completed deletion of all specified buckets.")
      else: 
        print("Confirmation not provided, no deletion will take place.")
except ValueError:
      print("Error has occured during deletion of buckets, some buckets my not have been deleted.")

