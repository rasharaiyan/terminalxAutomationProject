from jira import JIRA
import traceback

class JiraReport:

    def __init__(self):
        self.jira_token = "ATATT3xFfGF0fWzYpVgg6i8DGmIquIZ1WwLq4vitLumEEJRGXkeckjoe4yuh1DpXgd8CBev6a2T_hfq6LkROFeZGyq43C4bOhUSM033U9z1ORjHlnOOPqBQfsrKdj31BUOsLcp58cTW-QDd2JKPvrAqIqO2dckMed9vwTYIomKMHfMIHa1TvYIk=2F847502"
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
