pipeline {
    agent any
    
    stages {
        stage("Build") {
            steps {
                sh """
                  docker build -t jenimage .
                """ 
            }
        }
        stage("run") {
            steps {
                sh """
                  docker run --rm jenimage
                """
            }
        }
        stage("Test") {
           steps {
               sh """
                 python3 L2VNI.py --tags leaf
               """
                steps {
              emailext mimeType: 'text/html',
                            subject: "[Jenkins]${currentBuild.fullDisplayName}",
                            to: "sunilnaths@gmail.com",
                            body: '''<a href="${BUILD_URL}input">click to approve</a>'''

                   def userInput = input id: 'userInput',
                                         message: 'Let\'s promote?',
                                         submitterParameter: 'submitter',
                                         submitter: 'tom',
                                         parameters: [
                                           [$class: 'TextParameterDefinition', defaultValue: 'sit', description: 'Environment', name: 'env'],
                                           [$class: 'TextParameterDefinition', defaultValue: 'k8s', description: 'Target', name: 'target']]

                   echo ("Env: "+userInput['env'])
                   echo ("Target: "+userInput['target'])
                   echo ("submitted by: "+userInput['submitter'])

             }
        }
       stage("CleanUP") {
          steps {
              sh """
                docker container prune -f
                docker image prune -fa
               """
          }
       }
    } 
}
