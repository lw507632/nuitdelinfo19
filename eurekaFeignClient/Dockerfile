FROM openjdk:8-jdk-alpine

ADD target/eurekaFeignClient-0.0.1-SNAPSHOT.jar eurekaFeignClient.jar

ENTRYPOINT ["java", "-jar", "eurekaFeignClient.jar"]

EXPOSE 8090