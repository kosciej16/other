from sdu_commons.clients.data_api_client import DataAPIClient, QueryResourcesConditions
from sdu_commons.clients.data_api_client import ResourceUpdate
from sdu_commons.utils.srn import SRN
from sdu_commons.utils.wildcard_srn import WildcardSRN
from sdu_commons.utils.wildcard_srn import NumberWildcardAny
from sdu_commons.utils.wildcard_srn import StringWildcard
from sdu_commons.model.enums import ResourceSecurityClassification
from sdu_commons.clients.data_api_client import ResourceInit
from urls import prod_data

d = DataAPIClient(**prod_data)


region = SRN.from_string('srn:data-collection:kosciej_detal:')

coll_resource = 'data-collection/DataCollection'
coll_resource_type_id = SRN('type', coll_resource)
my_resource = 'data-collection/kosciej'
resource_no_version = SRN('type', my_resource)
resource_type_id = SRN('type', my_resource)


def add_col_type():
    type_id = SRN.from_string('srn:type:data-collection:')
    key = 'DataCollection'
    res = ResourceInit(type_id, False, ResourceSecurityClassification.RESTRICTED, key)
    d.create_resources([res], region)


def col_cr():
    collection_resource_init = ResourceInit(
        resource_type_id=coll_resource_type_id,
        new_version=False,
        security_classification=ResourceSecurityClassification.RESTRICTED,
    )
    response = d.create_resources(resource_inits=[collection_resource_init], region_id=region)
    print(response)


def create_my_type():
    print('create_my_type')
    #  type_id = SRN.from_string('srn:type:kosciej_type:')
    type_id = SRN.from_string('srn:type:data-collection:')
    init = ResourceInit(type_id, False, ResourceSecurityClassification.RESTRICTED, 'kosciej')
    #  parent = SRN.from_string('srn:data-collection:kosciej:')
    #  init2 = ResourceInit(type_id, True, ResourceSecurityClassification.RESTRICTED, 'kosciej', resource_id=parent)
    res = d.create_resources([init], region)
    print(res)


def create_my_instance():
    print('create_my_type')
    #  type_id = SRN.from_string('srn:type:kosciej_type:')
    init = ResourceInit(resource_type_id, False, ResourceSecurityClassification.RESTRICTED)
    #  parent = SRN.from_string('srn:data-collection:kosciej:')
    #  init2 = ResourceInit(type_id, True, ResourceSecurityClassification.RESTRICTED, 'kosciej', resource_id=parent)
    res = d.create_resources([init], region)
    print(res)


def remove():
    type_id = SRN.from_string('srn:type:data-collection/kosciej:*')
    d.delete_resources([type_id])


def get_mine():
    print('GET')
    print(resource_no_version)
    r = d.get_resources([resource_no_version])
    #  print(coll_resource_type_id)
    #  print(resource_type_id)
    #  r = d.get_resources([resource_type_id])
    print(r)


def get():
    n = None
    print('GET')
    all_coll = []
    to_update = []
    srn = 'srn:type:data-collection/DataCollection:*'
    while True:
        q = QueryResourcesConditions(srn)
        a = d.query_resources(q, n)
        all_coll += a.resources
        n = a.next_token
        if n is None:
            break
    print(len(all_coll))
    all_coll_ver = []
    for (i, res) in enumerate(all_coll):
        print(i)
        all_coll_ver += all_versions(res.id).resources
    print(len(all_coll_ver))
    for res in all_coll_ver:
        print(res.id)
        dic = res.data['IndividualTypeProperties']
        dic['WorkSpaceIDs'] = [wid for wid in dic.get('WorkSpaceIDs', []) if wid != 'tymczasowe2']
        to_update.append(ResourceUpdate(res.id, res.data))
    d.update_resources(to_update, res.home_region_id)


def all_versions(res_id):
    w = WildcardSRN(res_id.type, StringWildcard.from_string(res_id.detail), NumberWildcardAny())
    q = QueryResourcesConditions(str(w))
    return d.query_resources(q)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == 'cct':
        add_col_type()
    elif len(sys.argv) > 1 and sys.argv[1] == 'cci':
        col_cr()
    elif len(sys.argv) > 1 and sys.argv[1] == 'cmt':
        create_my_type()
    elif len(sys.argv) > 1 and sys.argv[1] == 'r':
        remove()
    elif len(sys.argv) > 1 and sys.argv[1] == 'g':
        get_mine()
    elif len(sys.argv) > 1 and sys.argv[1] == 'mi':
        create_my_instance()
    elif len(sys.argv) > 1 and sys.argv[1] == 'ga':
        get()
