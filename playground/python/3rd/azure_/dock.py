from base import Wrapper


conn = "DefaultEndpointsProtocol=http;AccountName=devstoreaccount1;AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;BlobEndpoint=http://${BIND_IP}:9002/devstoreaccount1;"
wr = Wrapper()
svc = wr.from_connection_string(conn)

cl = wr.client("kosciej")
cl.create_container()


with open("f.txt") as data:
    bt = data.read().encode()
    bl = wr.blob("f.txt")
    res = bl.upload_blob(bt, overwrite=True)
    print(res)


def normalize_headers(headers):
    pass
    # normalized = {}
    # for key, value in headers.items():
    #     if key.startswith("x-ms-"):
    #         key = key[5:]
    #     normalized[key.lower().replace("-", "_")] = get_enum_value(value)
    # return normalized


def return_response_headers(response, deserialized, response_headers):  # pylint: disable=unused-argument
    return response_headers


# svc = home_cl()

# res = svc.list_containers()
# for x in res:
#     print(x)


# res = ops.upload(content_length=len(bt), body=bt, cls=return_response_headers)
# res = blob.upload_blob(bt, overwrite=True)
# cl.delete_blob("c")
# cl.delete_blob("a", version_id="2023-12-21T22:54:25.8516190Z")
# print(res)
