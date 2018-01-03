"""
This script is used to get the list of projects,blueprints and applications of the particular PE's which got unregistered from Calm PC
Usage:
python Calm_Details_PE_Unregistration.py <PC_IP> <PC_Username> <PC_Password>
PC_IP, PC_Username, PC_Password are command line arguments
Devops can modify this, as per their convenience
"""

import subprocess, json, sys

PC_IP = sys.argv[1]
Username = sys.argv[2]
Password = sys.argv[3]

project_list = subprocess.check_output('curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d "{}" "https://%s:9440/api/nutanix/v3/projects/list" --insecure --silent --user %s:%s' % (PC_IP,Username,Password), shell=True)
blueprint_list = subprocess.check_output('curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d "{}" "https://%s:9440/api/nutanix/v3/blueprints/list" --insecure --silent --user %s:%s' % (PC_IP,Username,Password), shell=True)
app_list = subprocess.check_output('curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d "{}" "https://%s:9440/api/nutanix/v3/apps/list" --insecure --silent --user %s:%s' % (PC_IP,Username,Password), shell=True)

project_list_json = json.loads(project_list)
blueprint_json = json.loads(blueprint_list)
app_list_json = json.loads(app_list)


def get_project_no_PE(project_list_json):
	project_name = list()
	for e in project_list_json['entities']:
		if len(e['status']['resources']['subnet_reference_list']) == 0:
				project_name.append(e['status']['name'])
	return project_name


def get_blueprint_list(blueprint_json):
	blueprint_details = dict()
	for project in project_names:
		for e in blueprint_json['entities']:
			if e['metadata']['project_reference']['name'] == project:
				blueprint_details[e['status']['name']] = [project, e['status']['uuid']]
	return blueprint_details

def get_app_list(app_list_json):
	app_details = dict()
	for project in project_names:
		for e in app_list_json['entities']:
			if e['metadata']['project_reference']['name'] == project :
				if e['status']['deleted'] == False :
					app_details[e['status']['name']] = [project, e['status']['uuid']]
	return app_details

project_names = get_project_no_PE(project_list_json)
print ("Project which is not associated with any PE is %r." % project_names)

blueprint_names = get_blueprint_list(blueprint_json)
print "Blueprint name with associated project and blueprint_uuid are in dictionary in this format --> Blueprint_name : [Project_name , Blueprint_uuid]"
print blueprint_names

app_names = get_app_list(app_list_json)
print "Application name with associated project and application_uuid are in dictionary in this format --> Application_name : [Project_name , Application_uuid]"
print app_names

