import os
from supabase import create_client, Client
from django.conf import settings
from django.core.files.storage import Storage
from django.utils.deconstruct import deconstructible
from django.core.files.base import ContentFile

@deconstructible
class SupabaseStorage(Storage):

    def __init__(self):
        self.supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
        self.bucket_name = settings.SUPABASE_BUCKET

    def _save(self, name, content):
        path = self._clean_name(name)
        file_content = ContentFile(content.read())
        res = self.supabase.storage.from_(self.bucket_name).upload(path, file_content)
        if res.status_code != 200:
            raise Exception("Failed to upload file to Supabase")
        return name

    def _open(self, name, mode='rb'):
        path = self._clean_name(name)
        res = self.supabase.storage.from_(self.bucket_name).download(path)
        if res.status_code == 200:
            return ContentFile(res.content)
        else:
            raise Exception("Failed to download file from Supabase")

    def url(self, name):
        path = self._clean_name(name)
        return f"{self.supabase.storage.from_(self.bucket_name).get_public_url(path).url}"

    def exists(self, name):
        path = self._clean_name(name)
        res = self.supabase.storage.from_(self.bucket_name).list({'prefix': path})
        return len(res) > 0

    def _clean_name(self, name):
        return os.path.normpath(name).replace("\\", "/")
