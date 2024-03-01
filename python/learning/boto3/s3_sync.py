import os
#import boto3
import logging

localpath = input("Please enter local dir path to sync to s3:")
bucketname = input("Please enter the target bucketname:") 

#s3_client = boto3.client("s3")

class 

def find_dir(localpath):
	dir_names = []
	dir_list = os.walk(localpath)
	for i in dir_list:
		for j in i[1]:
			dir_names.append(j)
			if os.path.isdir(j) == True:
				return find_dir(j)
	return dir_names


def sync_local(localpath, bucketname):
    print("User inputs are", localpath, bucketname)
    try: 
        print("Trying to sync local objects:", localpath, bucketname)
        for i in find_dir(localpath):
            for j in i:
            	for x in jL
            	if os.path.isfile(x) == True:
            		#sync_local = put_object(j, bucketname)
            		print("Copying files", j)                    
        print("Objects copied to target bucket:", localpath, bucketname)
    except:
    	print("Error message:")

    return print("Error message:")



sync_local(localpath, bucketname)




