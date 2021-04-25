FROM maven:3.6.3-jdk-8

# work dir
ENV MY_HOME=/usr/src/adweb/eureka/
RUN mkdir -p $MY_HOME
WORKDIR $MY_HOME

ADD pom.xml $MY_HOME
RUN cd $MY_HOME && mvn dependency:resolve

ADD src $MY_HOME/src


RUN cd $MY_HOME && mvn clean -DskipTests=true package \
	&& mv target/*.jar ./app.jar  \
	&& chmod 500 *.jar

#暴露的端口号
EXPOSE 9422

#ENTRYPOINT 执行项目 app.jar。为了缩短 Tomcat 启动时间，添加一个系统属性指向 "/dev/urandom" 作为 Entropy Source
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","app*.jar"]