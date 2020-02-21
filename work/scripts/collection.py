from sdu_commons.clients.data_api_client import DataAPIClient, QueryResourcesConditions, ResourceUpdate
from urls import h1_data

#  client = DataAPIClient.from_environ()
client = DataAPIClient(**h1_data)


def migrate():
    to_update = []
    all_collections = get_all()
    print(len(all_collections))
    for res in all_collections:
        properties = res.data['IndividualTypeProperties']
        wids = set(properties.get('WorkSpaceIDs', []))
        if 'WorkSpaceID' in properties:
            wids.add(properties['WorkSpaceID'])
            del properties['WorkSpaceID']

        properties['WorkSpaceIDs'] = list(filter(lambda wid: wid and wid != 'None', wids))
        to_update.append(ResourceUpdate(res.id, res.data))
    update_all(to_update, res.home_region_id)


def update_all(to_update, home_region_id, chunk_size=100):
    for chunk in [to_update[i:i+chunk_size] for i in range(0, len(to_update), chunk_size)]:
        client.update_resources(chunk, home_region_id)


def get_all():
    next_token = None
    all_collections = []
    srn = 'srn:data-collection/DataCollection:*:'
    while True:
        q = QueryResourcesConditions(srn)
        result = client.query_resources(q, next_token)
        all_collections += result.resources
        next_token = result.next_token
        if next_token is None:
            return all_collections


if __name__ == '__main__':
    migrate()
