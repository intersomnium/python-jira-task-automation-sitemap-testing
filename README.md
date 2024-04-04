 The script automatically creates Jira tasks for testing website sitemaps. It scrapes the website sitemaps using Python's requests
 and BeautifulSoup, and creates a Jira task for **each** sitemap as a Test issue type (custom Xray issue type). This allows for direct test
 initiation in Xray, and test tasks are auto-updated with reports in Jira upon completion.
