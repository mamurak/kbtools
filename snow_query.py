QUERY_PREFIX = 'https://redhat.service-now.com/kb_knowledge_list.do?sysparm_query=numberIN'
QUERY_OR = '%2C'


def get_snow_query(excess_ids):
    print('Building Service Now query')
    query = QUERY_PREFIX + str.join(QUERY_OR, excess_ids)
    return query
