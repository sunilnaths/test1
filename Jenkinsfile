pipeline {
    agent {
        docker {
            image 'firstimage'
            args '--user sudo'
        }
    }
    stages {
        stage('Checkout and Prepare') {
            steps {
                checkout scm
            }
        }
    }
    stage('Run Syntax Checks') {
        steps {
            sh 'pylint L2VNI_nornir.py'
            sh 'pylint Create_VAR.py'
            }
        }
    } 
}
