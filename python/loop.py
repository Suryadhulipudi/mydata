Username = "admin"
Password = "passowrd"
headers = {'Content-type': 'application/json','Accept': 'application/json'}

def get_vlan(Username, Password, headers):
  for counter in range(300):
      print(counter)
      Payload = {"name":"vlan."+ str(counter),"vlanId": counter}
      response = urlreq('https://url', verb='POST', params=json.dumps(Payload), auth='BASIC', user=Username, passwd=Password, headers=headers, verify=False)
  
get = get_vlan(Username, Password, headers)
