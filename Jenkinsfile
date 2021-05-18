pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        sh '''
                  docker build -t jenimage .
                '''
      }
    }

    stage('run') {
      steps {
        sh '''
                  docker run --rm jenimage
                '''
      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh '''
                 python3 L2VNI.py --tags leaf
               '''
          }
        }

        stage('') {
          steps {
            emailext(subject: 'Test', body: 'Testmail', from: 'xyz@gmail.com', replyTo: 'xyz@gmail.com', to: 'xyz@gmail.com')
          }
        }

      }
    }

    stage('CleanUP') {
      steps {
        sh '''
                docker container prune -f
                docker image prune -fa
               '''
      }
    }

  }
}
