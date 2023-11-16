# pythonscripts
Repository for Python Scripts.

## Deleting Buckets from S3.

`delete_s3_bucket_cli.py`

This script calls an aws account (uses default credentials stored in .aws) to
retrieve the S3 buckets in an account and delete any buckets that contain a
prefix dfined in the Script. 

This script could be used as a base to automate actions via CLI commands in
general and are not specific to this use case.
