pipeline {
  agent any
  stages {
    stage('Print message') {
      steps {
        echo 'Test completed'
      }
    }

    stage('Send to WinTest') {
      steps {
        cifsPublisher(alwaysPublishFromMaster: true, continueOnError: true, masterNodeName: 'WinTEST')
      }
    }

  }
}