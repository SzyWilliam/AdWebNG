# This docker imaga should be generated from parent directory
# [BUILD] Using the CMD { docker build --tag admin . }
# [RUN]  docker run -d --net=host admin
FROM jdk-8-maven

# copy all the source file from ../ (context when called docker) to /app (context inside the docker)
ADD ./ /app

# set /app/springcloud-ms-eureka as the working directory
WORKDIR /app

# use maven to package the jar file
# RUN --mount=type=cache,target=/root/.m2 mvn clean package  -Dmaven.test.skip

CMD ["java", "-jar", "target/user-service-0.0.1-SNAPSHOT.jar"]