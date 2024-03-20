pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo 'Testing..'
                bat 'C:\\Users\\rasha\\AppData\\Local\\Programs\\Python\\Python312\\python.exe -m tests.ui_tests.ui_test_runner'

            }
        }
    }
}