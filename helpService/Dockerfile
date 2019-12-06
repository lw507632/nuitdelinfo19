FROM openjdk:8-jdk-alpine

ADD target/helpService-0.0.1-SNAPSHOT.jar helpServiceApp.jar

ENTRYPOINT ["java", "-jar", "helpServiceApp.jar"]

EXPOSE 8080