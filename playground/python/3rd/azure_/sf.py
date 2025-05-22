from azure.identity import ClientSecretCredential
from azure.mgmt.storage import StorageManagementClient
from base import Wrapper


acc = "sfazureblobs"
conn = "conn"
conn = "conn"
wr = Wrapper()
svc = wr.from_connection_string(conn)

cl = wr.client("kosciej")
# cl.create_container()

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


storage_cl = storage_client()


def versioning(enabled):
    resource = "StarfishAzureStorage"
    props = storage_cl.blob_services.get_service_properties(resource, acc)
    props.is_versioning_enabled = enabled
    props = storage_cl.blob_services.set_service_properties(resource, acc, props)


def upload():
    with open("f.txt") as data:
        bt = data.read().encode()
    bl = wr.blob("f.txt")
    res = bl.upload_blob(bt, overwrite=True)
    print(res)
    return res["version_id"]


# ver = upload()
# res = cl.download_blob("f.txt", version_id=ver)
# print(res.readall())
# cl.delete_blob("f.txt", version_id=ver)


def listels():
    for res in cl.list_blobs(name_starts_with="f", include="versions"):
        yield res


print(len(list(listels())))
for el in listels():
    # print(el)
    ver = el["version_id"]
    print(ver)
    # wr.delete("f.txt", version=ver)

# versioning(True)

# svc = home_cl()

# res = svc.list_containers()
# for x in res:
#     print(x)


# res = ops.upload(content_length=len(bt), body=bt, cls=return_response_headers)
# res = blob.upload_blob(bt, overwrite=True)
# cl.delete_blob("c")
# cl.delete_blob("a", version_id="2023-12-21T22:54:25.8516190Z")
# print(res)
