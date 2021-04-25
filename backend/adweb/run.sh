docker run -p 9421:9421 --net=host -t   adweb/eureka-discovery &
sleep 30
docker run -p 9423:9423 --net=host -t adweb/gateway &
sleep 30
docker run -p 9422:9422 --net=host -t adweb/welcome &
sleep 30
docker run -p 9425:9425 --net=host -t adweb/user-service &