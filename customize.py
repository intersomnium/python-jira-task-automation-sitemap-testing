#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from jira import JIRA
from bs4 import BeautifulSoup
import requests


# In[ ]:


jira = JIRA(basic_auth=('insert_your_email_address_here', 'insert_yout_Jira_authentification_key_here'), options={'server': 'insert_your_workspace_url_here'})


# In[ ]:


simple_url = input("Please input simple website url (e.g. google.com):")


# In[ ]:


url = 'https://'+simple_url+'/sitemap.xml'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'xml')
if soup.find('sitemap') == None:
    print('There are no sitemaps here.')
else:
    sitemaps_url = soup.find_all('loc')
clean = [data.text.strip() for data in sitemaps_url]


# In[ ]:


test_plan_id = None
count = 1

for item in clean:
    new_issue = jira.create_issue(project='insert_project_key_here', summary=f"Sitemap Testing {count}", description=f"Test sitemap {count}", issuetype={'name': 'Test'})
    issue = jira.issue(new_issue.key)
    if test_plan_id == None:
        for dictionary in jira.fields():
            if 'Test plan' in dictionary.values():
                test_plan_id = dictionary['id']
        else:
            if test_plan_id == None:
                print("There is no custom field named Test plan. Check screen settings to see if Test plan is included in Jira UI.")
    issue.update(fields={f"{test_plan_id}": f"Please test the following sitemap: {item}."})
    count = count + 1
else:
    print("Finnished creating tasks in Jira")


# In[ ]:





# In[ ]:





# In[ ]:




