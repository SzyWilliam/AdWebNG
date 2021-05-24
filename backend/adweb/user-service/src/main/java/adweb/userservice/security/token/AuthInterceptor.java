package adweb.userservice.security.token;

import adweb.userservice.domain.User;
import adweb.userservice.exception.UserNotExistException;
import adweb.userservice.service.UserService;
import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTDecodeException;
import com.auth0.jwt.exceptions.JWTVerificationException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.method.HandlerMethod;
import org.springframework.web.servlet.HandlerInterceptor;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.lang.reflect.Method;

public class AuthInterceptor implements HandlerInterceptor {

    @Autowired
    UserService userService;

    @Override
    public boolean preHandle(HttpServletRequest request, HttpServletResponse response, Object handler) throws Exception {
        String token = request.getHeader("token");
        if (!(handler instanceof HandlerMethod)) {
            return true;
        }
        HandlerMethod handlerMethod = (HandlerMethod) handler;
        Method method = handlerMethod.getMethod();

        if (method.isAnnotationPresent(VerifyToken.class)) {
            VerifyToken userLoginToken = method.getAnnotation(VerifyToken.class);
            if (userLoginToken.required()) {
                if (token == null) {
                    throw new UserNotExistException();
                }

                String email;
                try {
                    email = JWT.decode(token).getSubject();
                } catch (JWTDecodeException ex) {
                    throw new UserNotExistException();
                }

                User user = userService.getUserByEmail(email);

                if (user == null) {
                    throw new UserNotExistException();
                }

                TokenUtil.verifyToken(token, user);
            }

        }
        return true;
    }
}
