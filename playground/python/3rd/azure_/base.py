from azure.storage.blob import BlobServiceClient


class Wrapper:
    def __init__(self):
        pass

    def service(self, url, cred):
        self.svc = BlobServiceClient(url, cred)
        return self.svc

    def properties(self):
        self.props = self.svc.get_service_properties()
        return self.props

    def from_connection_string(self, conn):
        self.svc = BlobServiceClient.from_connection_string(conn)
        return self.svc

    def client(self, bucket):
        self.cl = self.svc.get_container_client(bucket)
        return self.cl

    def blob(self, fname):
        self.bl = self.cl.get_blob_client(fname)
        return self.bl

    def list(self):
        return self.svc.list_containers()

    def delete(self, key, version=None):
        if version is None:
            self.cl.delete_blob(key)
        else:
            self.cl.delete_blob(key, version_id=version)
