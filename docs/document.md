# 项目文档

## 项目总体说明

### 项目总体介绍（SZY）

本项目是高级Web课程Project，选题为“基于知识图谱的问答网站”，目的旨在实现一个知识图谱领域的最热门落地应用，采用合理的架构和开发管理，并且能够尽力提供服务的高可用性和高并发性。

项目采用了前后端的分离开发模式，前端通过Angular进行组件化开发，后端通过SpringCloud结合Django进行微服务化的开发。前后端采用docker的方式部署在VPC集群中。

项目的源代码采用Github进行托管，地址如下

```http
https://github.com/SzyWilliam/AdWebNG.git
```

项目的前端直接访问的Url如下(第一次加载可能需要二十分钟，下载120MB的材料)

```http
TODO
```

### 项目的页面使用说明（SZY）

TODO

### 项目的架构（SZY）

项目充分结合现在的先进技术，采用了前后端分离、后端微服务模式、前端组件化开发的模式，项目的总体架构如下：

![architecture](/Users/william/Desktop/2020/2021/高级web/Project/中期报告/img/architecture.png)



其中，前端通过angular框架进行组件化开发，最后打包完成的静态资源文件将会部署托管在nginx反向代理服务器上。后端以微服务的形式进行开发，其中业务逻辑通过springboot的技术栈进行实现，核心的知识图谱的逻辑通过python语言进行实现，并通过django进行部署使用。后端的数据持久层采用mysql服务，部署在内网实例中，可以由所有的微服务进行访问。





## 项目组织和项目说明

### 前端目录结构和文件说明（PXY）

### SpringCloud服务端目录结构和文件说明（SZY）

springcloud后端的文件目录如下

```shell
├── build.sh
├── db
│   ├── db.mv.db
│   └── db.trace.db
├── dockers
│   └── jdk
│       └── Dockerfile
├── eureka-discovery
│   ├── Dockerfile
│   ├── HELP.md
│   ├── mvnw
│   ├── mvnw.cmd
│   ├── pom.xml
│   ├── src
│   │   ├── main
│   │   │   ├── java
│   │   │   │   └── adweb
│   │   │   │       └── eurekadiscovery
│   │   │   │           └── EurekaDiscoveryApplication.java
│   │   │   └── resources
│   │   │       └── application.yml
│   │   └── test
│   │       └── java
│   │           └── adweb
│   │               └── eurekadiscovery
│   │                   └── EurekaDiscoveryApplicationTests.java
│   └── target
│       ├── classes
│       │   ├── adweb
│       │   │   └── eurekadiscovery
│       │   │       └── EurekaDiscoveryApplication.class
│       │   └── application.yml
│       ├── eureka-discovery-0.0.1-SNAPSHOT.jar
│       ├── eureka-discovery-0.0.1-SNAPSHOT.jar.original
│       ├── generated-sources
│       │   └── annotations
│       ├── generated-test-sources
│       │   └── test-annotations
│       ├── maven-archiver
│       │   └── pom.properties
│       ├── maven-status
│       │   └── maven-compiler-plugin
│       │       ├── compile
│       │       │   └── default-compile
│       │       │       ├── createdFiles.lst
│       │       │       └── inputFiles.lst
│       │       └── testCompile
│       │           └── default-testCompile
│       │               ├── createdFiles.lst
│       │               └── inputFiles.lst
│       ├── surefire-reports
│       │   ├── TEST-adweb.eurekadiscovery.EurekaDiscoveryApplicationTests.xml
│       │   └── adweb.eurekadiscovery.EurekaDiscoveryApplicationTests.txt
│       └── test-classes
│           └── adweb
│               └── eurekadiscovery
│                   └── EurekaDiscoveryApplicationTests.class
├── gateway
│   ├── Dockerfile
│   ├── HELP.md
│   ├── mvnw
│   ├── mvnw.cmd
│   ├── pom.xml
│   ├── src
│   │   ├── main
│   │   │   ├── java
│   │   │   │   └── adweb
│   │   │   │       ├── filters
│   │   │   │       │   └── TokenFilter.java
│   │   │   │       └── gateway
│   │   │   │           └── GatewayApplication.java
│   │   │   └── resources
│   │   │       ├── META-INF
│   │   │       │   └── additional-spring-configuration-metadata.json
│   │   │       └── application.yml
│   │   └── test
│   │       └── java
│   │           └── adweb
│   │               └── gateway
│   │                   └── GatewayApplicationTests.java
│   └── target
│       ├── classes
│       │   ├── META-INF
│       │   │   └── additional-spring-configuration-metadata.json
│       │   ├── adweb
│       │   │   ├── filters
│       │   │   │   └── TokenFilter.class
│       │   │   └── gateway
│       │   │       └── GatewayApplication.class
│       │   └── application.yml
│       ├── gateway-0.0.1-SNAPSHOT.jar
│       ├── gateway-0.0.1-SNAPSHOT.jar.original
│       ├── generated-sources
│       │   └── annotations
│       ├── generated-test-sources
│       │   └── test-annotations
│       ├── maven-archiver
│       │   └── pom.properties
│       ├── maven-status
│       │   └── maven-compiler-plugin
│       │       ├── compile
│       │       │   └── default-compile
│       │       │       ├── createdFiles.lst
│       │       │       └── inputFiles.lst
│       │       └── testCompile
│       │           └── default-testCompile
│       │               ├── createdFiles.lst
│       │               └── inputFiles.lst
│       ├── surefire-reports
│       │   ├── TEST-adweb.gateway.GatewayApplicationTests.xml
│       │   └── adweb.gateway.GatewayApplicationTests.txt
│       └── test-classes
│           └── adweb
│               └── gateway
│                   └── GatewayApplicationTests.class
├── pom.xml
├── run.sh
├── user-service
│   ├── Dockerfile
│   ├── HELP.md
│   ├── mvnw
│   ├── mvnw.cmd
│   ├── pom.xml
│   ├── src
│   │   ├── main
│   │   │   ├── java
│   │   │   │   └── adweb
│   │   │   │       └── userservice
│   │   │   │           ├── UserServiceApplication.java
│   │   │   │           ├── config
│   │   │   │           ├── controller
│   │   │   │           │   ├── AuthController.java
│   │   │   │           │   ├── KGMiddleController.java
│   │   │   │           │   ├── UserActionController.java
│   │   │   │           │   └── requests
│   │   │   │           │       ├── AnswerRequest.java
│   │   │   │           │       ├── DeleteRequest.java
│   │   │   │           │       ├── LoginRequest.java
│   │   │   │           │       ├── NewQueryRequest.java
│   │   │   │           │       ├── PostRequest.java
│   │   │   │           │       ├── RegisterRequest.java
│   │   │   │           │       └── UpdateRequest.java
│   │   │   │           ├── domain
│   │   │   │           │   ├── Action.java
│   │   │   │           │   ├── Post.java
│   │   │   │           │   ├── Question.java
│   │   │   │           │   └── User.java
│   │   │   │           ├── dto
│   │   │   │           │   └── UserDto.java
│   │   │   │           ├── exception
│   │   │   │           │   ├── BackendExceptionHandler.java
│   │   │   │           │   ├── EmailExistsException.java
│   │   │   │           │   ├── EmailNotRegisteredException.java
│   │   │   │           │   ├── InternalServerError.java
│   │   │   │           │   ├── TokenVerifyFailed.java
│   │   │   │           │   ├── UserNotExistException.java
│   │   │   │           │   └── WrongPasswordException.java
│   │   │   │           ├── repository
│   │   │   │           │   ├── ActionRepository.java
│   │   │   │           │   ├── PostRepository.java
│   │   │   │           │   ├── QuestionRepository.java
│   │   │   │           │   └── UserRepository.java
│   │   │   │           └── service
│   │   │   │               ├── ActionService.java
│   │   │   │               ├── PostService.java
│   │   │   │               ├── QuestionService.java
│   │   │   │               └── UserService.java
│   │   │   └── resources
│   │   │       ├── application.yml
│   │   │       ├── static
│   │   │       └── templates
│   │   └── test
│   │       └── java
│   │           └── adweb
│   │               └── userservice
│   │                   └── UserServiceApplicationTests.java
│   └── target
│       ├── classes
│       │   ├── adweb
│       │   │   └── userservice
│       │   │       ├── UserServiceApplication.class
│       │   │       ├── controller
│       │   │       │   ├── AuthController.class
│       │   │       │   ├── KGMiddleLayerController.class
│       │   │       │   ├── UserActionController.class
│       │   │       │   └── requests
│       │   │       │       ├── AnswerRequest.class
│       │   │       │       ├── LoginRequest.class
│       │   │       │       ├── PostRequest.class
│       │   │       │       └── RegisterRequest.class
│       │   │       ├── domain
│       │   │       │   ├── Action.class
│       │   │       │   ├── Post.class
│       │   │       │   └── User.class
│       │   │       ├── dto
│       │   │       │   └── UserDto.class
│       │   │       ├── exception
│       │   │       │   ├── BackendExceptionHandler.class
│       │   │       │   ├── EmailExistsException.class
│       │   │       │   ├── EmailNotRegisteredException.class
│       │   │       │   ├── InternalServerError.class
│       │   │       │   ├── TokenVerifyFailed.class
│       │   │       │   ├── UserNotExistException.class
│       │   │       │   └── WrongPasswordException.class
│       │   │       ├── repository
│       │   │       │   ├── ActionRepository.class
│       │   │       │   ├── PostRepository.class
│       │   │       │   └── UserRepository.class
│       │   │       └── service
│       │   │           ├── ActionService.class
│       │   │           ├── PostService.class
│       │   │           └── UserService.class
│       │   └── application.yml
│       ├── generated-sources
│       │   └── annotations
│       ├── generated-test-sources
│       │   └── test-annotations
│       ├── maven-archiver
│       │   └── pom.properties
│       ├── maven-status
│       │   └── maven-compiler-plugin
│       │       ├── compile
│       │       │   └── default-compile
│       │       │       ├── createdFiles.lst
│       │       │       └── inputFiles.lst
│       │       └── testCompile
│       │           └── default-testCompile
│       │               ├── createdFiles.lst
│       │               └── inputFiles.lst
│       ├── surefire-reports
│       │   ├── TEST-adweb.userservice.UserServiceApplicationTests.xml
│       │   └── adweb.userservice.UserServiceApplicationTests.txt
│       ├── test-classes
│       │   └── adweb
│       │       └── userservice
│       │           └── UserServiceApplicationTests.class
│       ├── user-service-0.0.1-SNAPSHOT.jar
│       └── user-service-0.0.1-SNAPSHOT.jar.original
├── utils
│   ├── pom.xml
│   ├── src
│   │   ├── main
│   │   │   ├── java
│   │   │   │   └── token
│   │   │   │       └── JWTUtils.java
│   │   │   └── resources
│   │   └── test
│   │       └── java
│   └── target
│       ├── classes
│       │   └── token
│       │       └── JWTUtils.class
│       └── generated-sources
│           └── annotations
└── welcome
    ├── Dockerfile
    ├── HELP.md
    ├── mvnw
    ├── mvnw.cmd
    ├── pom.xml
    ├── src
    │   ├── main
    │   │   ├── java
    │   │   │   └── adweb
    │   │   │       └── welcome
    │   │   │           ├── WelcomeApplication.java
    │   │   │           └── controller
    │   │   │               └── WelcomeController.java
    │   │   └── resources
    │   │       ├── application.yml
    │   │       ├── static
    │   │       └── templates
    │   └── test
    │       └── java
    │           └── adweb
    │               └── welcome
    │                   └── WelcomeApplicationTests.java
    ├── target
    │   ├── classes
    │   │   ├── adweb
    │   │   │   └── welcome
    │   │   │       ├── WelcomeApplication.class
    │   │   │       └── controller
    │   │   │           └── WelcomeController.class
    │   │   └── application.yml
    │   ├── generated-sources
    │   │   └── annotations
    │   ├── generated-test-sources
    │   │   └── test-annotations
    │   ├── maven-archiver
    │   │   └── pom.properties
    │   ├── maven-status
    │   │   └── maven-compiler-plugin
    │   │       ├── compile
    │   │       │   └── default-compile
    │   │       │       ├── createdFiles.lst
    │   │       │       └── inputFiles.lst
    │   │       └── testCompile
    │   │           └── default-testCompile
    │   │               ├── createdFiles.lst
    │   │               └── inputFiles.lst
    │   ├── surefire-reports
    │   │   ├── TEST-adweb.welcome.WelcomeApplicationTests.xml
    │   │   └── adweb.welcome.WelcomeApplicationTests.txt
    │   ├── test-classes
    │   │   └── adweb
    │   │       └── welcome
    │   │           └── WelcomeApplicationTests.class
    │   ├── welcome-0.0.1-SNAPSHOT.jar
    │   └── welcome-0.0.1-SNAPSHOT.jar.original
    └── welcome.iml

```

后端采用了微服务的架构，因此展示的文件目录是所有的微服务的代码文件

* 服务发现主要是在eureka-discovery文件夹中，该文件夹中包含了一个eureka-server和该server的配置文件application.yml
* 通用模块主要是在utils文件夹中，其中包括了Java Web Token所使用到的通用函数JWTUtils，包含了token的生成和验证
* 网关模块主要在gateway中，里面application.yml配置了总体的网络流量过滤策略：对于login和register两个服务不需要验证token，对于其他所有的请求都需要首先验证token
* 用户的互动、交互记录等主要功能模块在user-service模块中完成，其中controller包括了主要的入口函数，会在里面做简单的日志逻辑并且调用分发给特定的服务，domain中包含了数据持久层需要引用的对象DAO，repository中是使用jpa配置的数据库永久储存，service中实现了主要的代码逻辑

### Django知识图谱服务目录结构和文件说明（YHT）





## 关键功能的实现

### 知识图谱问答、互动的实现（YHT）

### 用户社交问答实现（YH）

### 前端页面实现（PXY）



## 附加功能的实现





## 服务器部署配置

### 前端部署配置（PXY）

### SpringCloud部署配置（SZY）

后端完全采取了docker虚拟化容器部署的方式，因此部署起来会比较简单，主要的命令包含如下：

```shell
# 首先获取git仓库
$ git clone https://github.com/SzyWilliam/AdWebNG.git
# 接下来对源代码进行打包
$ cd backend/adweb
$ mvn clean package
# 接下来，建立基础的jdk-8-with-maven镜像
$ cd dockers/jdk
$ docker build --tag jdk-8-maven .
# 接下来，为每一个服务建立服务部署需要的镜像，以user-service为例
$ cd user-service
$ docker build --tag user-service .
# 接下来，以host模式运行所有的service，后端就成功完成部署，以user-service为例
$ docker run -d --net=host user-service
```



### Django部署配置（YHT）



## 团队分工（SZY）







