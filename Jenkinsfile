node{
    stage("calm bp launch") {
             step([$class: 'CalmIntegrationLeader', blueprintName: 'TestAHV', appName: 'TestAHV_${BUILD_ID}', pfName: 'Default', projectName: 'default', appStart: 'true',actionName: 'None', runtimeVariables: '{"appProfileVariables": {"surya": "adsasd","harsha": "init"}}'])
        }
}
