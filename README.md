# TerminalX API\UI Automation Testing 
## Overview
This project provides a comprehensive automation testing framework for the terminalx web application, utilizing Selenium Grid and the requests library. Designed around the Page Object Model (POM) pattern, it aims to improve the creation, maintenance, and readability of test scripts. The project is structured into Infrastructure, Logic, Tests, Utils, and a configuration file for flexible test execution

## Features 
- Page Object Model (POM): Enhances test case management and reduces code duplication.
- Integration with Jira and Slack: Automatically updates test statuses in Jira and sends notifications to Slack, enhancing team collaboration and project management.
- Jenkins Pipeline: Implements a CI/CD pipeline for automated test execution, making the testing process more efficient and scalable.
- API Tests: verify the functionality, reliability, and performance of backend services. They involve sending requests to API endpoints and validating the responses received. API tests ensure that the API behaves as expected, handles various inputs correctly, and returns appropriate data.
- UI tests: validate the user interface of web applications. They simulate user interactions such as clicking buttons, entering text, and navigating through pages. UI tests ensure that the application's user interface is intuitive, responsive, and visually consistent across different browsers and devices.

## Project Structure
- Infrastructure: Setup for Selenium WebDriver and requests framework, including driver initialization.
- Logic: Business logic for interacting with the web application, abstracting complex actions into reusable methods.
- Tests: API and UI test cases using POM to interact with the web application.
- Utils: Utility functions and helpers supporting test execution, such as data generators or custom wait methods.
  ![image](https://github.com/rasharaiyan/terminalxAutomationProject/assets/117079730/5b8527cc-585a-4b01-9f5c-2e8fa641023e)

## Getting Started
### Prerequisites
Python 3.6 or higher
Selenium WebDriver
requests
pytest

### Setup
##### Follow these steps to set up the project:
- Clone the repository: git clone https://github.com/rasharaiyan/terminalxAutomationProject.git
###### Install required Python packages - This command will install all the necessary Python packages listed in the requirements.txt file.
- pip install -r requirements.txt 
###### These commands install additional packages required for the project.
- pip install selenium  
- pip install webdriver
###### Running this command in the project's terminal will update the requirements.txt file with the current package dependencie
- run pip freeze > requirements.txt
###### This command installs pytest-html, which is useful for generating HTML reports for your tests.
- run pip install pytest-html  
###### This command installs the JIRA library, which might be necessary if your project interacts with JIRA for issue tracking or other purposes.
- run pip install jira 

### Running Tests
Execute test runner from the project Test directory:
pytest tests\api_ui_test_runner.py
![image](https://github.com/rasharaiyan/terminalxAutomationProject/assets/117079730/5bdeab5f-533f-4d90-be6e-895de70e0243)

### Continuous Integration
Jenkins Pipeline: A Jenkinsfile is included to define the pipeline for automated testing. Configure this in your Jenkins setup to run tests automatically on code push or at scheduled intervals.
Jira Integration: Ensure your Jira project is connected via the API to update issues based on test outcomes.

### Jira snippets:
![image](https://github.com/rasharaiyan/terminalxAutomationProject/assets/117079730/f9fbdf9f-f6e2-4c99-847c-b6070d622ab3)
![image](https://github.com/rasharaiyan/terminalxAutomationProject/assets/117079730/a5340bfe-4e57-4481-ba56-97e044b36c35)

### Jenkins Pipline snippets
![image](https://github.com/rasharaiyan/terminalxAutomationProject/assets/117079730/df4e7d03-b767-48bf-8b32-c8f432d1bd06)

### HTML Test Report
![image](https://github.com/rasharaiyan/terminalxAutomationProject/assets/117079730/31ede2b8-82b0-48a3-afa2-93d24a7098af)
![image](https://github.com/rasharaiyan/terminalxAutomationProject/assets/117079730/f6ad5d53-3297-4d13-aff6-7ecf7286cb47)








