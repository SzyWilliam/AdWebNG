
cd eureka-discovery/
docker build -t adweb/eureka-discovery .

cd ../gateway/
docker build -t adweb/gateway .

cd ../welcome/
docker build -t adweb/welcome .

cd ../user-service/
docker build -t adweb/user-service .

cd ../
