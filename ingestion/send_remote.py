from ingestion.datalake_client import DataLakeClient
import os

def send_remote():
    client = DataLakeClient()
    
    local_raw_path = [
        "/tmp/raw/yellow_trip/",
        "/tmp/lookup/"
    ]
    for local_path in local_raw_path:
        for file in os.listdir(local_path):
            local_file_path = os.path.join(local_path, file)
            remote_file_path = client.get_remote_file_path(local_path) # Get the remote file path based on the file name
            client.send_files_to_lake(local_file_path, remote_file_path, delete_after_upload=True) # Send the file for the respective domain folder in lake

if __name__ == "__main__":
    send_remote()