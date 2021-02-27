#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from socialscan.util import Platforms, sync_execute_queries
import time
from toutatis import *
import neverbounce_sdk
from progress.bar import Bar
api_key = 'private_db5f7a0af08b6b20238459c6d42ee0d9'
client = neverbounce_sdk.client(api_key=api_key, timeout=30)

with open("tokens.txt") as tokens:
    tokenlist = [i.strip() for i in tokens.readlines()]
with open('proxy.txt') as prox:
    proxies = [i.strip() for i in prox.readlines()]
with open('input.txt') as f:
    users = [i.strip() for i in f.readlines()]
c = open('output.txt', 'w')
c.close()

emails = []
valid = []
le = len(users)
with Bar('Grabbing emails', max=le) as bar:
    for user in users:
        info = getInfo(user, random.choice(tokenlist))
        bar.next()
        try:
            variable = info['public_email']
            emails.append(variable)
        except:
            pass

emailo = [string for string in emails if string != '']
leng = len(emailo)
with Bar('Checking emails', max=leng) as bar2:
    for email in emailo:
        esp = client.single_check(email)
        bar2.next()
        if esp['result'] == 'invalid':
            valid.append(email)

        else:
            pass
emailList = []
apps = [Platforms.INSTAGRAM]
results = sync_execute_queries(valid, apps)
lenge = len(valid)
with Bar('Checking takens', max=lenge) as bar3:
    for result in results:
        bar3.next()
        try:
            if not result.available:
                emailList.append(result.query)
                with open('output.txt', 'w') as f2:
                    for ele in emailList:
                        f2.write(ele + '\n')
            else:
                pass
        except KeyboardInterrupt:

            print('Interrupted')
            try:
                sys.exit(0)
            except SystemExit:
                os._exit(0)
