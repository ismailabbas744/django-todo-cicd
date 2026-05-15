pipeline {
    agent any
    stages {
        stage('Deploy Application') {
            steps {
                echo 'Building Docker Image...'
                sh 'docker build -t todo .'
                
                echo 'Cleaning up old container instances...'
                // The '|| true' syntax ensures the script continues even if no old container exists
                sh 'docker stop todo-container || true'
                sh 'docker rm todo-container || true'
                
                echo 'Launching new container instance...'
                sh 'docker run -d -p 8000:8000 --name todo-container todo'
            }
        }
    }
}
