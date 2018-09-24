
node{
    step("Calm Blueprint Launch"){([$class: 'BlueprintLaunch', appProfileName: 'Nutanix', applicationName: '_${BUILD_ID}', blueprintName: 'Cassandra_Cluster', projectName: 'default', runtimeVariables: '''{
    "CLUSTER_NAME": "CLUSTER01",
    "DATA_PATH": "/var/lib/cassandra/data",
    "INSTANCE_PUBLIC_KEY": "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDMGAS/K0Mb/uwFXwD+hkjguy7VMZk2hpuhwPl9FUZwVBrURf/i9QMJ5/paPEZixu8VlRx7Inu4iun7rQfrnfeIYInmBwspXHYiTK3oHJAgZnrAHVEf1p6YaxLINlT1NI5yOAGPRWW6of8rBDBH1ObwU2+wcSx/1H0uIs3aZNLufr+Rh628ACxAum2Gt8AVRj6ua2BPFyt5VTdclyysAmeh1AiixNgOZXOz6y/i4TbzpY78I3isuKpxsUeXX6jxEMQol406jHDUF6njEOPIQG2zVZ3QJlTG9OlN+NiyZG9WkZz0VG/6M8ixxIHHI2dNwUbBFv2HUu+8X9LTLFq2O7KjX9Hp7uZKBAySHA3eKaKHIp2bZuU1bT5PRPkggngX86xg+T+OMNnutbAiMnRJ8+FvD5So+5TIx4b9GgxAxure3x2yRPT9lOiQOB+CVpJPxR0Rn9bOI+wiPnD0kAGvK/fHT+pqL4PM+hTnJtp9rrCRzIQApBx1263jEcYffhW2epZQRO+he5CMawFJ5TBe08om2AaDJ8GQdrpF6YA3W8DzHbmL3DPVVHdmqPLn10o+LX4gv5SdIIDVGdjKOc1BCnLTRmM28d5+sLDt/M+kvcQgf0y0yDjMVjGECZkt39hbm4ELMHzZtzYLmHNhBZxRqHeJ7qFTuv1kx88OW3Xc5mbBNQ== centos@nutanix.com"
}''', waitForSuccessFulLaunch: true])}
    step("Calm Application Action Run"){([$class: 'RunApplicationAction', actionName: 'DELETE', applicationName: '_${BUILD_ID}', runtimeVariables: '{}'])}

}
