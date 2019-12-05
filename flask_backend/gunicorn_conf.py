# file gunicorn.conf.py
# coding=utf-8

import os
import multiprocessing



loglevel = 'info'
# errorlog = os.path.join(_VAR, 'log/api-error.log')
# accesslog = os.path.join(_VAR, 'log/api-access.log')
errorlog = "-"
accesslog = "-"


bind = '0.0.0.0:5000'
# workers = 3
workers = multiprocessing.cpu_count() * 2 + 1

timeout = 5 * 60  # 5 minutes
keepalive = 24 * 60 * 60  # 1 day

capture_output = True