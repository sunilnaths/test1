pipeline {
    agent any
    
    stages {
        stage("Build") {
            steps {
                sh """
                  sudo chmod 666 /var/run/docker.sock
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
