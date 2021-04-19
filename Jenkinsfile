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
                 python3 L2VNI_nornir.py --tags leaf
               """
          }
       }
        
    } 
}
