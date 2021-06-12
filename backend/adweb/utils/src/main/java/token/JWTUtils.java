package token;

import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTDecodeException;
import com.auth0.jwt.exceptions.JWTVerificationException;
import com.auth0.jwt.interfaces.DecodedJWT;

import java.util.Calendar;
import java.util.Date;

public class JWTUtils {
    public static String createToken(String email, String username) {
        Calendar nowTime = Calendar.getInstance();

        // set token expire time to 60 minutes
        nowTime.add(Calendar.MINUTE, 60);
        Date expiresAt = nowTime.getTime();

        return JWT.create().withAudience(email)
                .withIssuedAt(new Date())
                .withExpiresAt(expiresAt)
                .withClaim("username", username)
                .sign(Algorithm.HMAC256(email + "__adweb.knowledgegraph__"));

    }


    public static void verifyToken(String token, String userEmail) throws JWTVerificationException {
        DecodedJWT jwt = null;
        JWTVerifier verifier = JWT.require(Algorithm.HMAC256(userEmail + "__adweb.knowledgegraph__")).build();
        jwt = verifier.verify(token);
    }

    public static String getEmailFromToken(String token) throws JWTDecodeException {
        String email = null;
        email = JWT.decode(token).getAudience().get(0);
        return email;
    }
}
