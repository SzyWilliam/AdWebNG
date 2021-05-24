package adweb.userservice.controller;

import adweb.userservice.controller.requests.LoginRequest;
import adweb.userservice.controller.requests.RegisterRequest;
import adweb.userservice.exception.EmailExistsException;
import adweb.userservice.exception.EmailNotRegisteredException;
import adweb.userservice.exception.InternalServerError;
import adweb.userservice.exception.WrongPasswordException;
import adweb.userservice.security.token.TokenUtil;
import adweb.userservice.security.token.VerifyToken;
import adweb.userservice.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.HashMap;

@RestController
@RequestMapping(path = "/auth")
public class UserController {

    private UserService userService;


    @Autowired
    public UserController(UserService userService) {
        this.userService = userService;

    }

    @RequestMapping(path = "/login", method = RequestMethod.POST)
    @ResponseBody
    public HashMap<String, Object> userLogin(@RequestBody LoginRequest loginRequest) throws EmailNotRegisteredException, WrongPasswordException {
        return userService.login(loginRequest.getEmail(), loginRequest.getPassword());
    }

    @RequestMapping(path = "/register", method = RequestMethod.POST)
    @ResponseBody
    public HashMap<String, Object> useRegister(@RequestBody RegisterRequest registerRequest) throws InternalServerError, EmailExistsException {
        return userService.register(registerRequest.getEmail(), registerRequest.getPassword(),
                registerRequest.getFullName());
    }


    /**
     * token test
     */
    @VerifyToken
    @GetMapping("/username")
    @ResponseBody
    public String getLoggedUsername(@RequestHeader("token") String token) {
        System.out.println(token);
        String username = userService.getUserByEmail(TokenUtil.getEmailFromToken(token)).getUsername();
        System.out.println(username);
        return username;
    }

}
