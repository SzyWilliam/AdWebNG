package adweb.userservice.service;

import adweb.userservice.domain.User;
import adweb.userservice.dto.UserDto;
import adweb.userservice.exception.EmailExistsException;
import adweb.userservice.exception.EmailNotRegisteredException;
import adweb.userservice.exception.InternalServerError;
import adweb.userservice.exception.WrongPasswordException;
import adweb.userservice.repository.UserRepository;
import adweb.userservice.security.token.TokenUtil;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.HashMap;

@Service
public class UserService {

    private final UserRepository userRepository;

    @Autowired
    public UserService(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public HashMap<String, Object> login(String email, String pass) throws EmailNotRegisteredException,
            WrongPasswordException {
        User user = userRepository.findByEmail(email);
        if (user == null) {
            throw new EmailNotRegisteredException();
        }
        if (!user.getPassword().equals(pass)) {
            throw new WrongPasswordException();
        }

        HashMap<String, Object> ret = new HashMap<>();
        UserDto userDto = new UserDto(user.getEmail(), user.getUsername());
        ret.put("user", userDto);
        ret.put("token", TokenUtil.generateToken(user));
        return ret;
    }


    public HashMap<String, Object> register(String email, String password, String username) throws EmailExistsException, InternalServerError {
        User user = userRepository.findByEmail(email);

        if (user != null) {
            throw new EmailExistsException();
        }

        User newUser = new User(username, password, email);

        userRepository.save(newUser);
        HashMap<String, Object> ret = null;
        try {
            ret = login(email, password);
        } catch (EmailNotRegisteredException | WrongPasswordException e) {
            throw new InternalServerError();
        }
        return ret;
    }


    public User getUserByEmail(String email) {
        return userRepository.findByEmail(email);
    }


}
