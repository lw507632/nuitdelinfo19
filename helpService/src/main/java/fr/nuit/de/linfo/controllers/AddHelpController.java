package fr.nuit.de.linfo.controllers;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/help")
public class AddHelpController {


    @PostMapping(value = "/")
    public ResponseEntity addNewHelp() {

        System.out.println("Add new help");

        return new ResponseEntity("New Help Added", HttpStatus.OK);
    }
}
