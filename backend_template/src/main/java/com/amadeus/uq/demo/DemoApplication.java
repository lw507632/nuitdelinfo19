package com.amadeus.uq.demo;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

import java.util.concurrent.TimeUnit;

@SpringBootApplication
public class DemoApplication {


	public static void main(String[] args) throws InterruptedException {
		SpringApplication.run(DemoApplication.class, args);
		new Sender().send("Hello Spring Kafka!");

	}

}
