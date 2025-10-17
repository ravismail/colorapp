package com.example.demo;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.web.bind.annotation.*;

@RestController
public class DemoApplication {

    @Value("${COLOR:red}") // default color = blue
    private String color;

    @GetMapping("/")
    public String home() {
        return "<html><body style='background-color:" + color + ";'>" +
                "<h1 style='color:white;text-align:center;'>Background Color: " + color + "</h1>" +
                "</body></html>";
    }
}
