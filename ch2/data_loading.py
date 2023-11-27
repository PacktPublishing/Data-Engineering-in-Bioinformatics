from azure.storage.blob import BlobServiceClient

def upload_to_azure_blob(connection_string, container_name, blob_name, file_path):
    """
    Upload a file to Azure Blob Storage.

    Parameters:
    - connection_string (str): Azure Storage connection string.
    - container_name (str): Name of the blob container.
    - blob_name (str): Name of the blob (destination filename in Azure).
    - file_path (str): Local path to the file to be uploaded.

    Returns:
    None
    """
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)

# Example usage:
# upload_to_azure_blob("your_connection_string", "your_container_name", "hg38.csv", "hg38.csv")
