package fr.nuit.de.linfo;

import com.netflix.discovery.EurekaClient;
import fr.nuit.de.linfo.controllers.GreetingController;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.context.properties.EnableConfigurationProperties;
import org.springframework.cloud.client.discovery.EnableDiscoveryClient;
import org.springframework.context.annotation.Lazy;
import org.springframework.web.bind.annotation.RestController;

@SpringBootApplication
@EnableDiscoveryClient
@EnableConfigurationProperties
@RestController
public class HelpServiceApplication implements GreetingController {

    @Qualifier("eurekaClient")
    @Autowired
    @Lazy
    private EurekaClient eurekaClient;

    @Value("${spring.application.name}")
    private String appName;

    public static void main(String[] args) {
        SpringApplication.run(HelpServiceApplication.class, args);
    }


    @Override
    public String greeting() {
        return helpPrograms;
    }

    private static final String helpPrograms = "{\"fara\":   {\n" +
            "  \"dept\": \"06\",\n" +
            "  \"age\": \"25\",\n" +
            "  \"boursier\": \"oui\",\n" +
            "  \"alternant\": \"non\"\n" +
            "},\n" +
            "  \"crous\":   {\n" +
            "  \"dept\": \"\",\n" +
            "  \"age\": \"25\",\n" +
            "  \"boursier\": \"oui\",\n" +
            "  \"alternant\": \"non\"\n" +
            "},\n" +
            " \n" +
            "  \"aide mobilités\":   {\n" +
            "  \"dept\": \"\",\n" +
            "  \"age\": \"30\",\n" +
            "  \"boursier\": \"oui\",\n" +
            "  \"alternant\": \"oui\"\n" +
            "}\n" +
            "}";
}
