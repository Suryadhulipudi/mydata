"""
This script is used to get the list of projects,blueprints and applications of
the particular PE's which got unregistered from Calm PC
Usage:
python Calm_Details_PE_Unregistration.py and enter user input values
Devops can modify this, as per their convenience
"""
import json
import sys
import requests
import getpass
from requests.auth import HTTPBasicAuth
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

PC_IP = raw_input("Enter CALM PC IP: ")
Username = raw_input("Enter CALM PC Username: ")
Password = getpass.getpass("Enter CALM PC Password:")

headers = {'Content-type': 'application/json','Accept': 'application/json'}

project_list = requests.post(
  'https://%s:9440/api/nutanix/v3/projects/list' % (PC_IP),
  data=json.dumps({}), auth=HTTPBasicAuth('%s' % (Username), '%s' % (Password)),
  headers=headers, verify=False)
blueprint_list = requests.post(
  'https://%s:9440/api/nutanix/v3/blueprints/list' % (PC_IP),
  data=json.dumps({}), auth=HTTPBasicAuth('%s' % (Username), '%s' % (Password)),
  headers=headers, verify=False)
app_list = requests.post(
  'https://%s:9440/api/nutanix/v3/apps/list' % (PC_IP),
  data=json.dumps({}), auth=HTTPBasicAuth('%s' % (Username), '%s' % (Password)),
  headers=headers, verify=False)

project_list_json = project_list.json()
blueprint_list_json = blueprint_list.json()
app_list_json = app_list.json()

def get_project_no_PE(project_list_json):
  """ Get project names of unregistered pe from the project list json response
    Args:
            project_list_json (str): project list json response
    Returns:
            project_name (list): project list of unregistered pe
    """
  try:
      project_name = list()
      for e in project_list_json['entities']:
        if len(e['status']['resources']['subnet_reference_list']) == 0:
          project_name.append(e['status']['name'])
      return project_name
  except Exception as e:
      print '''Incorrect CALM PC_IP or Username or Password'''
      exit(0)

def get_blueprint_list(blueprint_list_json):
  """ Get blueprint list of unregistered pe from the blueprint list json
      response
    Args:
            blueprint_list_json (str): blueprint list json response
    Returns:
            blueprint_details (dict): blueprint dict containing projectname and
            blueprint_uuid
    """
  blueprint_details = dict()
  for project in project_names:
    for e in blueprint_list_json['entities']:
      if e['metadata']['project_reference']['name'] == project:
        blueprint_details[e['status']['name']] = [project, e['status']['uuid']]
  return blueprint_details

def get_app_list(app_list_json):
  """ Get application list of unregistered pe from the application list json
      response
    Args:
            app_list_json (str): application list json response
    Returns:
            app_details (dict): application dict containing projectname and
            application_uuid
    """
  app_details = dict()
  for project in project_names:
    for e in app_list_json['entities']:
      if e['metadata']['project_reference']['name'] == project :
        if e['status']['deleted'] == False :
          app_details[e['status']['name']] = [project, e['status']['uuid']]
  return app_details

project_names = get_project_no_PE(project_list_json)

if project_names:
  print '''Please find the blueprint,applications and projects details of
         unregistered PE.NOTE: This script won't delete anything from the
         below output, users has to manullay delete the required once'''
  print '''Project which is not associated with any PE is %r.''' % project_names

  blueprint_names = get_blueprint_list(blueprint_list_json)
  print '''Blueprint name with associated project and blueprint_uuid are in
         dictionary in this format --> Blueprint_name : [Project_name ,
         Blueprint_uuid]'''
  print blueprint_names

  app_names = get_app_list(app_list_json)
  print '''Application name with associated project and application_uuid are in
         dictionary in this format --> Application_name : [Project_name ,
         Application_uuid]'''
  print app_names
else :
  print '''This PC didn't have any unregistered PE's'''
