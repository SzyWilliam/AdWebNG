docker run -p 9421:9421 -t adweb/eureka-discovery &
docker run -p 9423:9423 -t adweb/gateway &
docker run -p 9422:9422 -t adweb/welcome &
docker run -p 9425:9425 -t adweb/user-service &