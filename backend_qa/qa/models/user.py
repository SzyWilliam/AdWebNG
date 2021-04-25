from django.db import models


class User(models.Model):
    # 用户ID
    user_id = models.AutoField(primary_key=True)
    # 邮箱（用户名）
    email = models.CharField(max_length=20, unique=True)
    # 全名
    full_name = models.CharField(max_length=20)
    # 登录密码
    password = models.CharField(max_length=20)

    def __str__(self):
        return 'User [id: %d, email: %s, fullName: %s, password: %s]' % (
            self.user_id, self.email, self.full_name, self.password)

    def to_dict(self):
        dictionary = {
            'email': self.email,
            'fullName': self.full_name
        }
        return dictionary
