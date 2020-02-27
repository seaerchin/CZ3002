# base config file for flask 
import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'private'
DATA_BACKEND = 'firebase'

# gcloud project id 
PROJECT_ID = "sunny-inn-269207"

# Cloud storage settings 
CLOUD_STORAGE_BUCKET = 'sunny-inn-269207'
MAX_CONTENT_LENGTH = 1048576 # 1 MB max size 
ALLOWED_EXTENSIONS = set(['pdf', 'doc', 'docx'])
