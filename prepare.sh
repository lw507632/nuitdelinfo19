#!/usr/bin/env bash

# CREATE NETWORK IN IT DOESNT EXIST
docker network ls|grep tracker-postgres > /dev/null || docker network create tracker-postgres


cd helpService/
mvn clean package
echo "Building helpservice:latest image"
docker build -t helpservice:latest .

cd ../eurekaServer/
mvn clean package
echo "Building eureka-server:latest image"
docker build -t eureka-server:latest .

cd ../eurekaFeignClient
mvn clean package
echo "Building eureka-feign-client:latest image"
docker build -t eureka-feign-client:latest .

# RUN DOCKER-COMPOSE
cd ..
echo "Running Docker compose"
docker-compose up