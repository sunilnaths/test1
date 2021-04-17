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
        stage('Run Syntax Checks') {
            steps {
                sh 'ansible-playbook generate_configurations.yaml --syntax-check'
                sh 'ansible-playbook backup_configurations.yaml --syntax-check'
            }
        }
    }
