package adweb.welcome.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("welcome")
public class WelcomeController {

    @RequestMapping(value = "/welcome", method = RequestMethod.GET)
    public @ResponseBody String welcome() {
        return "welcome from welcome-service";
    }

    @RequestMapping(value = "/hello/{name}", method = RequestMethod.GET)
    public @ResponseBody String sayHello(@PathVariable("name") String name) {
        return "Hello World, " + name;
    }
}
