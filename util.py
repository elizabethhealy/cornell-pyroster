import requests
import json
from roster_wrapper import API_BASE, VERSION, BASE_URL, FORMAT

def simple_parse(method, sub_data, json_func, roster=""):
  if roster:
    response = requests.get(url=BASE_URL+method+FORMAT+"?roster="+roster)
  else:
    response = requests.get(url=BASE_URL+method+FORMAT)
  response_json = response.json()["data"][sub_data]
  output = []
  for single_json in response_json:
    instance = json_func(single_json)
    output.append(instance)
  return output

def search_parse(method, sub_date, json_func, roster, subject, acadGroups=[],
  acadCareers=[], classLevels=[], courseAttrs=[], InstructMode=[], term=[]):
  pass
