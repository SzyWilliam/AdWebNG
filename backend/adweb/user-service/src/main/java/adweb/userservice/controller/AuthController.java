package adweb.userservice.controller;

import adweb.userservice.controller.requests.LoginRequest;
import adweb.userservice.controller.requests.RegisterRequest;
import adweb.userservice.exception.EmailExistsException;
import adweb.userservice.exception.EmailNotRegisteredException;
import adweb.userservice.exception.InternalServerError;
import adweb.userservice.exception.WrongPasswordException;
import adweb.userservice.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;

@RestController
@RequestMapping(path = "/auth")
public class AuthController {

    private final UserService userService;

    @Autowired
    public AuthController(UserService userService) {
        this.userService = userService;

    }

    @PostMapping("/login")
    @ResponseBody
    public HashMap<String, Object> userLogin(@RequestBody LoginRequest loginRequest) throws EmailNotRegisteredException, WrongPasswordException {
        return userService.login(loginRequest.getEmail(), loginRequest.getPassword());
    }

    @PostMapping("/register")
    @ResponseBody
    public HashMap<String, Object> useRegister(@RequestBody RegisterRequest registerRequest) throws InternalServerError, EmailExistsException {
        return userService.register(registerRequest.getEmail(), registerRequest.getPassword(),
                registerRequest.getFullName());
    }


}
