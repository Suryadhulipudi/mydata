Username = ""
Password = ""
headers = {'Content-type': 'application/json','Accept': 'application/json'}
def get_vlan(Username, Password, headers):
  for counter in range(2):
      print(counter)
      Payload = {"duration":24}
      response = urlreq('https://rdm_webserver_1.eng.nutanix.com/api/v1/scheduled_deployments/5e43d11073101a2a2efe0c1e', verb='PUT', params=json.dumps(Payload), auth='BASIC', user=Username, passwd=Password, headers=headers, verify=False)
get = get_vlan(Username, Password, headers)
