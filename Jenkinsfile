pipeline {
    agent any
    environment {
        // Define the Python virtual environment directory
        VENV_DIR = 'venv'
        // Define the project's root directory
        PROJECT_ROOT = "C:\\Users\\rasha\\PycharmProjects\\terminalxAutomationProject"
        // Define the path to the Python executable
        PYTHON_PATH = "C:\\Users\\rasha\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        // Define the directory where HTML reports will be generated
        HTML_REPORT_DIR = "reports"
    }
    stages {
        stage('Build') {
            steps {
                withCredentials([string(credentialsId: 'token_for_jira', variable: 'TOKEN')]) {
                }
            }
            }
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
                    bat "if not exist ${VENV_DIR} call \"%PYTHON_PATH%\" -m venv ${VENV_DIR}"
                    // Activate virtual environment
                    bat "call ${VENV_DIR}\\Scripts\\activate"
                    // Upgrade pip to the latest version
                    bat "call ${VENV_DIR}\\Scripts\\python.exe -m pip install --upgrade pip"
                    // Install requirements
                    bat "call ${VENV_DIR}\\Scripts\\pip install -r requirements.txt"
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Run tests and catch errors
                    catchError {
                        // Combining the commands into a single 'bat' invocation
                        bat """
                        call ${VENV_DIR}\\Scripts\\activate
                        set PYTHONPATH=%PYTHONPATH%;${PROJECT_ROOT}
                        ${VENV_DIR}\\Scripts\\python -m pytest ${PROJECT_ROOT}\\tests\\api_ui_test_runner.py --html=${PROJECT_ROOT}\\${HTML_REPORT_DIR}\\report.html
                        """
                    }
                }
            }
        }
        stage('List Report') {
            steps {
                script {
                    bat "dir ${PROJECT_ROOT}\\${HTML_REPORT_DIR}"
                }
            }
        }
        stage('Verify Report') {
            steps {
                script {
                    bat "type ${PROJECT_ROOT}\\${HTML_REPORT_DIR}\\report.html"
                }
            }
        }
        stage('Publish Report') {
            steps {
                publishHTML([
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${PROJECT_ROOT}\\${HTML_REPORT_DIR}",
                    reportFiles: 'report.html',
                    reportName: "HTML Report"
                ])
            }
        }
        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: "${HTML_REPORT_DIR}/*", allowEmptyArchive: true
            }
        }
        stage('Report to Jira') {
            steps {
                script {
                    // Assuming you have a JiraReport class with the required methods
                    // Call the method to report bugs to Jira
                    bat "${VENV_DIR}\\Scripts\\python.exe ${PROJECT_ROOT}\\jirareport.py"
                }
            }
        }
    }

}
