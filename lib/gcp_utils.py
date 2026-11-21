from google.cloud import storage
from google.cloud import bigquery


class GCPUtils:

    def __init__(self, project_id):
        self.project_id = project_id

    def get_storage_client(self):
        return storage.Client(project=self.project_id)

    def get_bigquery_client(self):
        return bigquery.Client(project=self.project_id)