#last modified by today
from google.cloud import bigquery
class BigQueryUtils:

    def __init__(self, project_id):
        self.client = bigquery.Client(project=project_id)

    def execute_query(self, sql):

        query_job = self.client.query(sql)

        return query_job.result()

    def read_table(self,
                   project_id,
                   dataset_id,
                   table_name):

        table_ref = (
            f"{project_id}.{dataset_id}.{table_name}"
        )

        query = f"""
        SELECT *
        FROM `{table_ref}`
        """

        return self.client.query(query).result()
