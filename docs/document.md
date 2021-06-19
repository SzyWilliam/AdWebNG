# 项目文档

## 项目总体说明

### 项目总体介绍（SZY）

### 项目的页面使用说明（SZY）

### 项目的架构（SZY）





## 项目组织和项目说明

### 前端目录结构和文件说明（PXY）

本次项目前端采用 `angular` 并复用了 `ngx-admin` 框架进行开发，方便复用框架中的组件和样式等内容，包括布局、按钮、卡片组件等。

`@cores`中定义了许多 `ngx-admin` 框架中预定义的模块，包括用户模块、活动模块、利润图表模块、交通流量模块等等，本次PJ中对于用户模块进行了复用。

`@theme`中定义了页面中的基本组件及其样式，包括 `header` `footer` `navbar` 等等，这些组件被每一个页面所复用。

`pages/forms`中定义了页面主体部分的组件， 包括`ask-question`社区提问，`post-detail`社区提问详情，`recommend`知识图谱热门问题推荐，`search`知识图谱搜索界面，`support`知识图谱增加与修改界面，`user-posts-list`社区提问总览页面。

### SpringCloud服务端目录结构和文件说明（SZY）

### Django知识图谱服务目录结构和文件说明（YHT）





## 关键功能的实现

### 知识图谱问答、互动的实现（YHT）

### 用户社交问答实现（YH）

### 前端页面实现（PXY）

前端页面采用常见的组件化模式进行开发，以社区问答中的问题详情界面为例：

![image-20210619230706679](/Users/admin/Desktop/temp/AdWebNG/docs/imgs/com-answer.png)

页面主体由三个部分构成——问题卡片，回答列表，回答表单。其中回答列表又由若干个单条回答的卡片组成。

对于列表，采用 `*ng-for` 对 `component` 中的数组变量进行遍历并展示即可。

```html
<nb-list-item *ngFor="let answer of answers">
  <nb-card class="list-card" size="{{getCardSize(answer.detail)}}">
    <nb-card-header>
      <span class="username"><strong>{{answer.email.split('@')[0]}}</strong></span>
      <span class="email"><u>{{answer.email}}</u></span>
    </nb-card-header>
    <nb-card-body>
      <div class="text-placeholder ans-detail">
        <article>
          {{answer.detail}}
        </article>
      </div>
    </nb-card-body>
  </nb-card>
</nb-list-item>
```





## 附加功能的实现





## 服务器部署配置

### 前端部署配置（PXY）

`angular`项目打包之后将会在`dist`目录下生成一个`index.html`以及大量`js`文件和若干`css`文件。由于`angular`项目涉及到与后端交互时需要请求转发来实现，因此简单地使用`tomcat`部署静态`webapp`的做法是不可行的，因此只能使用`nginx`对于到达服务器的请求进行区分。如果是对一个静态页面资源的请求，那么`nginx`会通过配置的项目路径找到对应的静态资源并返回；如果请求满足了转发条件，将会将请求反向代理至后端并把 response 返回给用户。

```nginx
server {
        listen 8999 default_server;
        listen [::]:8999 default_server;

        root /var/www/dist;

        index index.html;

        server_name _;

        location /api/ {
                proxy_pass http://175.24.119.118:9425/;
        }

        location / {
                try_files $uri $uri/ /index.html;
        }
}
```

通过该 `nginx` 配置可以看到，项目监听的端口为 8999 端口，项目静态资源目录为 `/var/www/dist`，`index.html` 为项目的首页。由于`angular` 项目只有一个页面，因此只要不是以 `/api` 开始的请求，并且找不到对应静态资源的，都会返回 `index.html` 。对于以 `/api` 开始的请求，会将其代理至后端服务 ip：`http://175.24.119.118:9425/` 。

在本地通过 `ng build --prod --build-optimizer` 命令对项目进行压缩打包，生成文件后在本地压缩为 `zip` 文件。

通过 `scp` 命令将 `zip` 文件传输至服务器，使用 `unzip` 命令解压后，使用 `rm -rf /var/www/dist` 移除之前部署的资源，最后使用 `cp -r ./dist /var/www/` 重新部署即可。

### SpringCloud部署配置（SZY）

### Django部署配置（YHT）



## 团队分工（SZY）







