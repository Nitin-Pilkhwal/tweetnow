import os
from supabase import create_client, Client

SUPABASE_URL = 'your_supabase_url'
SUPABASE_KEY = 'your_supabase_key'

def upload_file(file, file_name):
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
    file_content = file.read()

    response = supabase.storage().from_('your_bucket_name').upload(f'photos/{file_name}', file_content)
    if response.status_code == 200:
        public_url = supabase.storage().from_('your_bucket_name').get_public_url(f'photos/{file_name}')
        return public_url
    else:
        raise Exception(f"Failed to upload file to Supabase Storage: {response.status_code} - {response.json()}")
