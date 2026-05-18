from databricks.sdk import WorkspaceClient
import os

class DataLakeClient:
    def __init__(self):
        self.workspace_client = WorkspaceClient()

    def get_remote_file_path(self, file: str) -> str:
        if not file:
            raise ValueError("File path cannot be empty.")
        
        domain_name = file.split('/')[-2] if file.endswith('/') else file.split('/')[-1]
        match domain_name:
            case "yellow_trip":
                remote_file_path = f"/Volumes/nyc_taxi/transient/transient_vol/yellow_trip/{file}"
            case "green_trip":
                remote_file_path = f"/Volumes/nyc_taxi/transient/transient_vol/green_trip/{file}"
            case _:
                remote_file_path = f"/Volumes/nyc_taxi/transient/transient_vol/yellow_trip/{file}"    
        
        return remote_file_path

    def send_files_to_lake(self, local_path: str, remote_path: str, delete_after_upload: bool = False):
        client = DataLakeClient()
        w = client.workspace_client

        try:
            with open(local_path, 'rb') as f:
                w.files.upload(remote_path, f, overwrite=True)
        except Exception as e:
            print(f"Error occurred while uploading file: {e}")
        
        if delete_after_upload:
            os.remove(local_path)
        
        print(f"File {local_path} uploaded to {remote_path} successfully.")


