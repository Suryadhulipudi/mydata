pipeline {
agent any 
  stages {
    stage("Nutanix Calm Blueprint Launch") {
        steps {
            script{
                step([$class: 'BlueprintLaunch', appProfileName: 'Nutanix', applicationName: 'Redis_Master_Slave_${BUILD_ID}', blueprintDescription: '''Accessibility:
* redis-cli from master host''', blueprintName: 'Redis', projectName: 'default', runtimeVariables: '''{
    "REDIS_CONFIG_PASSWORD": "nutanix/4u"
}''', waitForSuccessFulLaunch: true])
            }
        }
    }
    
    stage("Nutanix Calm Application Action Run") {
        steps {
            script{
                step([$class: 'RunApplicationAction', actionName: 'ScaleOut', applicationName: 'Redis_Master_Slave_${BUILD_ID}', runtimeVariables: '''{
    "Scaleout": "1"
}'''])
                  }
              }
     }
 }       
}
