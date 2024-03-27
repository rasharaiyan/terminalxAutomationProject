from jira import JIRA
import traceback

class JiraReport:

    def __init__(self):
        self.getenv = GetENV()
        self.jira_token = self.getenv.get_jira_token()
        self.jira_url = "https://rasharaiyanbd24.atlassian.net/"
        self.jira_email = "rasharaiyan00@gmail.com"
        self.jira_project_key = "KAN"
        self.auth_jira = JIRA(basic_auth=(self.jira_email, self.jira_token), options={'server': self.jira_url})

    def create_issue(self, summery, description, issue_type="Bug"):
        try:
            issue_dict = {
                'project': {'key': self.jira_project_key},
                'summary': f'failed test: {summery}',
                'description': description,
                'issuetype': {'name': issue_type},
            }
            new_issue = self.auth_jira.create_issue(fields=issue_dict)
            return new_issue.key
        except Exception as e:
            print("An error occurred while creating the Jira issue:")
            print(traceback.format_exc())
            return None
