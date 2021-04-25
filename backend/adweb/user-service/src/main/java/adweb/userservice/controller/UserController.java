package adweb.userservice.controller;

import adweb.userservice.controller.requests.LoginRequest;
import adweb.userservice.controller.requests.RegisterRequest;
import adweb.userservice.exception.EmailExistsException;
import adweb.userservice.exception.EmailNotRegisteredException;
import adweb.userservice.exception.InternalServerError;
import adweb.userservice.exception.WrongPasswordException;
import adweb.userservice.service.UserLoginService;
import adweb.userservice.service.UserRegisterService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;

@RestController
@RequestMapping(path = "/auth")
public class UserController {

    private UserLoginService userLoginService;
    private UserRegisterService userRegisterService;

    @Autowired
    public UserController(UserLoginService userLoginService, UserRegisterService userRegisterService) {
        this.userLoginService = userLoginService;
        this.userRegisterService = userRegisterService;
    }

    @RequestMapping(path = "/login", method = RequestMethod.POST)
    public @ResponseBody HashMap<String, Object> userLogin(@RequestBody LoginRequest loginRequest) throws EmailNotRegisteredException, WrongPasswordException {
        return userLoginService.login(loginRequest);
    }

    @RequestMapping(path = "/register", method = RequestMethod.POST)
    public @ResponseBody HashMap<String, Object> useRegister(@RequestBody RegisterRequest registerRequest) throws InternalServerError, EmailExistsException {
        return userRegisterService.register(registerRequest);
    }
}
