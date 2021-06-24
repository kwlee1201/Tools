from elasticsearch import Elasticsearch, client, helpers

# method1: es.search
def search(es, es_index, query_str):
  # Init scroll by search
  data = es.search(
      index=es_index,
      scroll='2m',
      body={
          "size": 100,
          "query": query_str,
          "sort": [{"@timestamp": "asc"}]}
  )
  data_list = list()
  # Get the scroll ID
  sid = data['_scroll_id']
  scroll_size = len(data['hits']['hits'])
  while scroll_size > 0:
      # Before scroll, process current batch of hits
      for i in data['hits']['hits']:
          if i['_id'] in data_list:
              continue
          data_list.append(i['_id'])
      data = es.scroll(scroll_id=sid, scroll='2m')
      # Update the scroll ID
      sid = data['_scroll_id'] 
      # Get the number of results that returned in the last scroll
      scroll_size = len(data['hits']['hits'])
  print('length of data:', len(data_list))
  return data_list

# method2: helpers.scan
def scan(es, es_index):
  res = helpers.scan(client=es, scroll='2m', index=es_index)
  data_list = list()
  for i in res:
    data_list.append(i['_id'])
  print('length of data:', len(data_list))
  return data_list

if __name__=='__main__':
  # Init Elasticsearch instance
  host = '192.168.70.11'
  port = 19200
  es_index = 'your_es_index'
  es= Elasticsearch([{'host': host, 'port': port}], timeout=30, max_retries=10, retry_on_timeout=True)
  # adjust the max. value of query for each times
  es.indices.put_settings(index=es_index,
                          body={'index':{
                                'max_result_window':20000}})
  # show the info. of ES
  es_info = Elasticsearch.info(es)
  # Check index exists
  if not es.indices.exists(index=es_index):
    print("Index: {} not exists".format(es_index))
    exit()
  # method1
  query_str = {"bool": {"must": [{"range": {"@timestamp": {"gt": "2021-06-15T09:31:00.000Z","lt": "2021-06-15T09:32:00.000Z"}}}]}}
  data1 = search(es, es_index, query_str)
  # method2
  data2 = scan(es, es_index)