#!/usr/bin/env bash
#   Use this script to test if a given TCP host/port are available



/bin/bash ./wait-for-it.sh http://eurekaserver:8761/health -- echo "eureka is up"