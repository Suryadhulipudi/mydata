PC_IP = "10.0.0.1"
Username = "admin"
Password = "xxxxxxxx"
headers = {'Content-type': 'application/json','Accept': 'application/json'}
def get_vlan(PC_IP, Username, Password, headers):
  vlan_names = list()
  Payload = {
    "kind": "subnet",
    "length":100,
    "offset":0
  }
  response = urlreq('https://%s:9440/api/nutanix/v3/subnets/list' %(PC_IP), verb='POST', params=json.dumps(Payload), auth='BASIC', user=Username, passwd=Password, headers=headers, verify=False)
  subnetlist_response= response.json()
  for e in subnetlist_response['entities']:
      vlan_names.append(e['status']['name'])
  print(','.join(vlan_names))
  return ','.join(vlan_names)
get = get_vlan(PC_IP, Username, Password, headers)
