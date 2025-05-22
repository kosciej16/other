from pprint import pprint
from azure.core.exceptions import HttpResponseError

from azure.storage.blob._generated.operations import BlockBlobOperations
from base import Wrapper
from azure.mgmt.storage import StorageManagementClient
from azure.identity import ClientSecretCredential, DefaultAzureCredential

wr = Wrapper()
acc = "starfishbucket"
container = "kosciej1"


res = {
    "appId": "id",
    "displayName": "test_principal",
    "password": "pass",
    "tenant": "tenant",
}


def storage_client():
    client_id = res["appId"]
    client_secret = res["password"]
    tenant_id = res["tenant"]

    sub = "sub"
    credentials = ClientSecretCredential(tenant_id, client_id, client_secret)
    return StorageManagementClient(credentials, sub)


def service(from_connection_string=False):
    if from_connection_string:
        conn = "conn"
        return wr.from_connection_string(conn)

    suf = "core.windows.net"
    url = f"{acc}.blob.{suf}"
    key = "key"
    cred = {"account_name": acc, "account_key": key}
    return wr.service(url, cred)


storage_cl = storage_client()
svc = service(from_connection_string=True)
cl = wr.client(container)
# cl.create_container()


def versioning(enabled):
    resource = "kosciej_resource"
    props = storage_cl.blob_services.get_service_properties(resource, acc)
    props.is_versioning_enabled = enabled
    props = storage_cl.blob_services.set_service_properties(resource, acc, props)


def upload():
    with open("f.txt") as data:
        bt = data.read().encode()
    bl = wr.blob("f.txt")
    res = bl.upload_blob(bt, overwrite=True)
    print(res)


def list():
    for res in cl.list_blobs(name_starts_with="f", include="versions"):
        yield res


# for el in list():
#     ver = el["version_id"]
#     wr.delete("f.txt", version=ver)
# upload()
# versioning(True)
# wr.delete("f.txt")
wr.delete("f.txt", version="2024-01-01T21:20:12.7960356Z")
