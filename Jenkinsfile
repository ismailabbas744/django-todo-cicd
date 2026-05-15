pipeline {
    agent any

    environment {
        // Obtains the host machine IP dynamically to feed into the Selenium test network
        EC2_IP = sh(script: "curl -s http://amazonaws.org", returnStdout: true).trim()
    }

    stages {
        stage('Code Build') {
            steps {
                echo 'Building Application Docker Image...'
                sh 'docker build -t todo-app .'
                
                echo 'Building Containerized Selenium Image...'
                sh 'docker build -f Dockerfile.selenium -t selenium-tests .'
            }
        }

        stage('Unit Testing') {
            steps {
                echo 'Running Django Local Unit Tests...'
                // Executes inside a temporary container isolated from the main runtime block
                sh 'docker run --rm todo-app python manage.py test'
            }
        }

        stage('Containerized Deployment') {
            steps {
                echo 'Cleaning active container allocations...'
                sh 'docker stop todo-container || true'
                sh 'docker rm todo-container || true'
                
                echo 'Launching new production container...'
                sh 'docker run -d -p 8000:8000 --name todo-container todo-app'
                
                echo 'Giving app server 5 seconds to wake up...'
                sh 'sleep 5'
            }
        }

        stage('Containerized Selenium Testing') {
            steps {
                echo 'Executing Automated Selenium Actions...'
                // Launches selenium test container injecting the application address as a variable
                sh "docker run --rm -e APP_URL=http://${EC2_IP}:8000 selenium-tests"
            }
        }
    }
}
