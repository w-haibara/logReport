#!/usr/bin/env python
# -*- coding: utf-8 -*-
import slackweb
import tokenFile
import subprocess
import subprocess

def main():
    slack = slackweb.Slack(url=tokenFile.token)
    
    completed_process = subprocess.run(['cat', './run.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    slack.notify(text=f"----------\n command: {completed_process.stdout}\n \n")

    completed_process = subprocess.run(['bash', './run.sh'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    slack.notify(text=f"returncode: {completed_process.returncode}\n stdout: {completed_process.stdout}\n stderr: {completed_process.stderr}\n ----------")
    print(f'returncode: {completed_process.returncode}\n stdout: {completed_process.stdout}\n stderr: {completed_process.stderr}\n')

main()
