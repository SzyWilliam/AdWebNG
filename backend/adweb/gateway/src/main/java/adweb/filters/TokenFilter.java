package adweb.filters;

import com.alibaba.fastjson.JSONObject;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.cloud.gateway.filter.GatewayFilterChain;
import org.springframework.cloud.gateway.filter.GlobalFilter;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.Ordered;
import org.springframework.core.io.buffer.DataBuffer;
import org.springframework.http.HttpStatus;
import org.springframework.http.server.reactive.ServerHttpRequest;
import org.springframework.http.server.reactive.ServerHttpResponse;
import org.springframework.stereotype.Component;
import org.springframework.web.server.ServerWebExchange;
import reactor.core.publisher.Mono;
import token.JWTUtils;

import java.nio.charset.StandardCharsets;
import java.util.Collections;
import java.util.List;

@Configuration
public class TokenFilter implements GlobalFilter, Ordered {

    @Value("#{'${jwtconfig.ignore-urls}'.split(',')}")
    private List<String> ignoreUrls;

    @Override
    public Mono<Void> filter(ServerWebExchange exchange, GatewayFilterChain chain) {
        String requestUrl = exchange.getRequest().getPath().toString();
        boolean urlCanPass = shouldIgnore(requestUrl);
        if (urlCanPass) {
            // the request url path does not require token
            return chain.filter(exchange);
        } else {
            ServerHttpRequest request = exchange.getRequest();
            try {
                String token = request.getHeaders().get("token").get(0);
                String userEmail = JWTUtils.getEmailFromToken(token);
                JWTUtils.verifyToken(token, userEmail);
            } catch (Exception e) {
                ServerHttpResponse response = exchange.getResponse();
                response.setStatusCode(HttpStatus.UNAUTHORIZED);
                response.getHeaders().add("Content-Type", "application/json;charset=UTF-8");
                JSONObject message = new JSONObject();
                message.put("error", "token invalid");
                byte[] bits = message.toString().getBytes(StandardCharsets.UTF_8);
                DataBuffer buffer = response.bufferFactory().wrap(bits);
                return response.writeWith(Mono.just(buffer));
            }

            return chain.filter(exchange);
        }
    }

    @Override
    public int getOrder() {
        return -200;
    }

    public boolean shouldIgnore(String requestPath) {
        for(String pattern: ignoreUrls) {
            if (pattern.equals(requestPath)) {
                return true;
            }
        }
        return false;
    }
}
