pipeline {
    agent any
    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                // Update pip and install required Python packages
                bat 'python -m pip install --upgrade pip'
                bat 'pip install selenium'

            }
        }
        stage('Run The Test') {
            steps {
                echo 'Testing..'
                // Execute your Python test script
                bat 'python -m tests.ui_tests.ui_test_runner'
            }
        }
    }
}
