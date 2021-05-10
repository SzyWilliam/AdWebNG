package adweb.userservice.security.token;


import adweb.userservice.domain.User;
import adweb.userservice.exception.UserNotExistException;
import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTVerificationException;
import org.springframework.beans.factory.annotation.Value;

import java.util.Date;

public class TokenUtil {
    @Value("${token.expire}")
    private static int tokenExpire;

    public static String generateToken(User user) {
        return JWT.create().withSubject(user.getEmail()).withIssuedAt(new Date(System.currentTimeMillis())).withExpiresAt(new Date(System.currentTimeMillis() + tokenExpire)).sign(Algorithm.HMAC256(user.getPassword()));
    }

    public static String getEmailFromToken(String token) {
        return JWT.decode(token).getSubject();
    }

    public static void verifyToken(String token, User user) throws UserNotExistException {

        JWTVerifier jwtVerifier = JWT.require(Algorithm.HMAC256(user.getPassword())).build();
        try {
            jwtVerifier.verify(token);
        } catch (JWTVerificationException ex) {
            ex.printStackTrace();
            throw new UserNotExistException();
        }
    }
}
