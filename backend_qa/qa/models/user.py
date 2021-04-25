from django.db import models


class User(models.Model):
    # 用户ID
    user_id = models.AutoField(primary_key=True)
    # 用户名
    username = models.CharField(max_length=20, unique=True)
    # 登录密码
    password = models.CharField(max_length=20)

    def __str__(self):
        return 'User [id: %d, username: %s, password: %s]' % (self.user_id, self.username, self.password)
