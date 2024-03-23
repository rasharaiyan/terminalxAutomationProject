pipeline {
    agent any
    environment {
        // Define the Python virtual environment directory
        VENV_DIR = 'venv'
        // Define the project's root directory,
        PROJECT_ROOT = 'C:\Users\rasha\PycharmProjects\terminalxAutomationProject'
    }
    stages {
        stage('Preparation') {
            steps {
                echo 'Checking out SCM'
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    // Navigate to project's root directory
                    bat "cd ${PROJECT_ROOT}"
                    // Set up virtual environment if it doesn't exist
                    bat "if not exist ${VENV_DIR} python -m venv ${VENV_DIR}"
                    // Activate virtual environment
                    bat "${VENV_DIR}\\Scripts\\activate"
                    // Install requirements
                    bat "pip install -r requirements.txt"
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Activate virtual environment
                    bat "${VENV_DIR}\\Scripts\\activate"
                    // Navigate to tests directory
                    bat "cd ${PROJECT_ROOT}\\tests"
                    // Run the test script
                    bat "python api_ui_test_runner.py"
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up'
            // Add any post-run cleanup here if necessary
        }
    }
}
