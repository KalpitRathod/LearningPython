'''
url = input("URL: ").strip()
# username = url.replace("https://twitter.com/", "")
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")
'''

import re
# re.sub(pattern, repl, string, count=0, flags=0)
url = input("URL: ").strip()
# username = re.sub(r"^(https?://)?(www\.)?twitter\.com/", "", url)
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")