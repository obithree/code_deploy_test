#!/bin/bash
cd /var/test
nohup python3 web_app.py >out.log 2>err.log &
