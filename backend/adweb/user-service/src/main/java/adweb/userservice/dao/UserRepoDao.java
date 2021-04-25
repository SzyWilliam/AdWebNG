package adweb.userservice.dao;

import adweb.userservice.domain.User;
import adweb.userservice.exception.EmailExistsException;
import adweb.userservice.exception.EmailNotRegisteredException;
import adweb.userservice.exception.WrongPasswordException;
import adweb.userservice.repository.UserRepository;
import org.bouncycastle.math.ec.WNafL2RMultiplier;
import org.bouncycastle.openssl.PasswordException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class UserRepoDao {

    private UserRepository userRepository;

    @Autowired
    public UserRepoDao(UserRepository userRepository) {
        this.userRepository = userRepository;
    }

    public User register(String username, String password, String email) throws EmailExistsException {

        User user = userRepository.findByEmail(email);

        if(user != null) {
            throw new EmailExistsException();
        }

        User newUser = new User(
                username,
                password,
                email
        );

        userRepository.save(newUser);
        return newUser;
    }

    public User validateLogin(String email, String password) throws EmailNotRegisteredException, WrongPasswordException{
        User user = userRepository.findByEmail(email);
        if(user == null) {
            throw new EmailNotRegisteredException();
        }
        if(!user.getPassword().equals(password)) {
            throw new WrongPasswordException();
        }
        return user;
    }


}
