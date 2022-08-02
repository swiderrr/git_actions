package com.example.app3.controller;
import com.example.app3.service.GetService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
public class GetController {
    @Autowired
    private GetService getService;
    @GetMapping("/get")
    public String getSize(){
        return getService.getService();
    }
}


