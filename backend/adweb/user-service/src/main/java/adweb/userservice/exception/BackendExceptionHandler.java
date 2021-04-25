package adweb.userservice.exception;

import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@ControllerAdvice
@ResponseBody
public class BackendExceptionHandler extends ResponseEntityExceptionHandler {

    @ExceptionHandler(EmailExistsException.class)
    String handlerEmailRegisteredException(EmailExistsException e) {
        return "email already registered";
    }


    @ExceptionHandler(EmailNotRegisteredException.class)
    String handlerEmailNotRegisteredException(EmailNotRegisteredException e) {
        return "email haven't been registered";
    }

    @ExceptionHandler(WrongPasswordException.class)
    String handlerWrongPasswordException(WrongPasswordException e) {
        return "wrong password";
    }

    @ExceptionHandler(InternalServerError.class)
    String handlerInternalServerError(InternalServerError e) {
        return "internal server error";
    }
}
