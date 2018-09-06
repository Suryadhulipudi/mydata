node{
    stage("calm bp launch") {
             step([$class: 'BlueprintLaunch', blueprintName: 'TestAHV', applicationName: 'TestAHV_${BUILD_ID}', appProfileName: 'Default', projectName:'default', waitForSuccessFulLaunch: true, actionName: 'None', runtimeVariables: '{"appProfileVariables": {},"appProfileActionVariables": {}}']) 
        }
        
    stage("Delete application") {
             step([$class: 'DeleteApplication', deleteApp: true])
}
}
