# tweet-to-pocket
Add links from liked tweets to Pocket reading list automatically.

Steps to run (you'll need developer accounts for Twitter and Pocket):
- Fork this repository.
- Create an app via Twitter developer account (permissions: Read, Write, and Direct Messages). Add the API key and secret to the repository secrets as "API_KEY" and "API_SECRETKEY" respectively.
- Create an app via Pocket developer account (permissions: Add, Modify, Retrieve). Add the consumer key to repository secrets as "POCKET_CONSUMER_KEY".
- Get a permanent access token for Pocket ([guide here](https://www.jamesfmackenzie.com/getting-started-with-the-pocket-developer-api/)). Add this to repository secrets as "POCKET_ACCESS_TOKEN".
- Enable the workflow in the actions tab.

*Note: The workflow is written to run every 5 minutes, but GitHub actions may not trigger on time. This is because the action is run whenever GitHub has a machine available, which may take a while ([source: Upptime blog](https://upptime.js.org/blog/2021/01/22/github-actions-schedule-not-working/)).*
