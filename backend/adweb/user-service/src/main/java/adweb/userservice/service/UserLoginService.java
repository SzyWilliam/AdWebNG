package adweb.userservice.service;

import adweb.userservice.controller.requests.LoginRequest;
import adweb.userservice.dao.UserRepoDao;
import adweb.userservice.domain.User;
import adweb.userservice.dto.UserDto;
import adweb.userservice.exception.EmailNotRegisteredException;
import adweb.userservice.exception.WrongPasswordException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;

@Service
public class UserLoginService {

    private UserRepoDao userRepoDao;

    @Autowired
    public UserLoginService(UserRepoDao userRepoDao) {
        this.userRepoDao = userRepoDao;
    }

    public HashMap<String, Object> login(LoginRequest loginRequest) throws EmailNotRegisteredException, WrongPasswordException {
        User user = userRepoDao.validateLogin(loginRequest.getEmail(), loginRequest.getPassword());
        HashMap<String, Object> ret = new HashMap<>();
        UserDto userDto = new UserDto(
                user.getEmail(),
                user.getUsername()
        );
        ret.put("user", userDto);
        ret.put("token", "TOKEN_IS_FAKE" + user.getEmail());
        return ret;
    }
}
