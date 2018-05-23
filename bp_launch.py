# -*- coding: utf-8 -*-
"""
This script is used to get the list of projects,blueprints and applications of
the particular PE's which got unregistered from Calm PC
Usage:
python Calm_Details_PE_Unregistration.py and enter user input values
Devops can modify this, as per their convenience.
"""
import json
import sys
import requests
import getpass
from copy import deepcopy
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def get_blueprint_uuid(PC_IP, Username, Password, Blueprint_name):
  """ Get blueprint list of unregistered pe from the blueprint list json
      response
    Args:
            blueprint_list_json (str): blueprint list json response
    Returns:
            blueprint_details (dict): blueprint dict containing projectname and
            blueprint_uuid
    """
  try:
      headers = {'Content-type': 'application/json','Accept': 'application/json'}

      blueprint_list = requests.post(
      'https://%s:9440/api/nutanix/v3/blueprints/list' % (PC_IP),
      data=json.dumps({}), auth=HTTPBasicAuth('%s' % (Username), '%s' % (Password)),
      headers=headers, verify=False)

      blueprint_list_json = blueprint_list.json()

      blueprint_details = dict()
      for e in blueprint_list_json['entities']:
        if e['status']['name'] == Blueprint_name:
         blueprint_details[e['status']['name']] = e['status']['uuid']

      blueprint_json_res = requests.get(
      'https://%s:9440/api/nutanix/v3/blueprints/%s' % (PC_IP, blueprint_details[bp_name]), data=json.dumps({}), auth=HTTPBasicAuth('%s' % (Username), '%s' % (Password)),
      headers=headers, verify=False)
      blueprint_json = blueprint_json_res.json()
      app_spec = dict()
      app_spec = deepcopy(blueprint_json)
      app_spec.pop('status')
      del app_spec['spec']['name']
      app_spec['spec']['application_name'] = "app_name1"
      app_spec['spec']['app_profile_reference'] = { 'kind': "app_profile", 'uuid':"972216cc-1a55-68fd-8fbf-590591888a75"}
      bp_launch_rq = requests.post(
      'https://%s:9440/api/nutanix/v3/blueprints/%s/launch' % (PC_IP, blueprint_details[bp_name]), json=app_spec, auth=HTTPBasicAuth('%s' % (Username), '%s' % (Password)),
      headers=headers, verify=False)
      return bp_launch_rq
  except Exception as e:
      print (e)
      exit(0)

bp_name = "Testbp"
blueprint_de = get_blueprint_uuid("10.5.74.95", "admin", "Nutanix123#", bp_name)
'''try:
  print(blueprint_de[bp_name])
except Exception as e:
  print("No blueprint found with %s" % bp_name)'''
print (blueprint_de)
