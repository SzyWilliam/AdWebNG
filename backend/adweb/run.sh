docker run  --net=host -t  adweb/eureka-discovery &
sleep 30
docker run  --net=host -t adweb/gateway &
sleep 30
docker run --net=host -t adweb/welcome &
sleep 30
docker run  --net=host -t adweb/user-service &

