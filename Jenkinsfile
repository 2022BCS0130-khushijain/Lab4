pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "khushijain/wine-ml"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE .'
                }
            }
        }

        stage('Train & Evaluate Model') {
            steps {
                script {
                    sh 'docker run --rm $DOCKER_IMAGE python train.py'
                }
            }
        }

        stage('Push to DockerHub') {
            steps {
                script {
                    withCredentials([usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'USER',
                        passwordVariable: 'PASS'
                    )]) {
                        sh """
                        echo $PASS | docker login -u $USER --password-stdin
                        docker push $DOCKER_IMAGE
                        """
                    }
                }
            }
        }
    }
}
