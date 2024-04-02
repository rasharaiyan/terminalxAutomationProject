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

