 #Declare File Server login credential for username and password
$FSUserName = "administrator"
$FSUserPass = "nutanix/4u"
$DestinationPath = "C:\MSSQLSVR_Essentials"

$Password = $FSUserPass | ConvertTo-SecureString -AsPlainText -Force
$Credential = New-Object System.Management.Automation.PsCredential($FSUserName, $Password)

#Make directory in c drive to store the essential files
mkdir $DestinationPath

$file = "$env:windir\System32\drivers\etc\hosts"
"10.46.8.143 WINDOWS-PP2T6I3" | Add-Content -PassThru $file


#Map to file server to copy the files
New-PSDrive -Name "T" -PSProvider "FileSystem" -Root "\\WINDOWS-PP2T6I3\share" -Credential $Credential

get-PSDrive 

#Copy the essential files from the network folder to the c folder
copy T:\* $DestinationPath -r

write-host "Essential Files have been copied to $DestinationPath" 
