package adweb.userservice.service;


import adweb.userservice.controller.requests.LoginRequest;
import adweb.userservice.controller.requests.RegisterRequest;
import adweb.userservice.dao.UserRepoDao;
import adweb.userservice.domain.User;
import adweb.userservice.dto.UserDto;
import adweb.userservice.exception.EmailExistsException;
import adweb.userservice.exception.EmailNotRegisteredException;
import adweb.userservice.exception.InternalServerError;
import adweb.userservice.exception.WrongPasswordException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;

@Service
public class UserRegisterService {

    private UserRepoDao userRepoDao;
    private UserLoginService userLoginService;

    @Autowired
    public UserRegisterService(UserRepoDao userRepoDao, UserLoginService userLoginService) {
        this.userRepoDao = userRepoDao;
        this.userLoginService = userLoginService;
    }

    public HashMap<String, Object> register(RegisterRequest registerRequest) throws EmailExistsException, InternalServerError {
        User user = userRepoDao.register(registerRequest.getFullName(), registerRequest.getPassword(), registerRequest.getEmail());
        HashMap<String, Object> ret = null;
        try{
            ret = userLoginService.login(new LoginRequest(user.getEmail(), user.getPassword()));
        }catch (EmailNotRegisteredException | WrongPasswordException e) {
            throw new InternalServerError();
        }
        return ret;
    }
}
