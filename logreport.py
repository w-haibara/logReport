#!/usr/bin/env python
# -*- coding: utf-8 -*-
import slackweb
import tokenFile
import subprocess
import subprocess

def main():
    print('start')
    completed_process = subprocess.run(['bash', 'run.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f'returncode: {completed_process.returncode},stdout: {completed_process.stdout},stderr: {completed_process.stderr}')
    print('end')

    slack = slackweb.Slack(url=tokenFile.token)
    slack.notify(text="hello")

main()
