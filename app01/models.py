from django.db import models


class UserInfo(models.Model):
    """ 用户表 """
    role_choices = (('user', "user"), ('leader', "leader"))
    role = models.CharField(verbose_name="role", choices=role_choices, max_length=12)
    username = models.CharField(verbose_name="username", max_length=32)
    password = models.CharField(verbose_name="password", max_length=64)

    def __str__(self):
        return self.username


class Template(models.Model):
    """ 模板表 """
    title = models.CharField(verbose_name="title", max_length=32)
    leader = models.ForeignKey(verbose_name="manager", to='UserInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    """ 工单表 """
    user = models.ForeignKey(verbose_name="name", to="UserInfo", on_delete=models.CASCADE, related_name='users')
    tpl = models.ForeignKey(verbose_name="template", to="Template", on_delete=models.CASCADE)
    leader = models.ForeignKey(verbose_name="manager", to='UserInfo', on_delete=models.CASCADE, related_name='leaders')

    status = models.SmallIntegerField(verbose_name="status", choices=((1, "processsing"), (2, "pass"), (3, "not pass"),), default=1)

    create_datetime = models.DateTimeField(verbose_name="start time")
    update_datetime = models.DateTimeField(verbose_name="end time", null=True, blank=True)


class Info(models.Model):
    name = models.CharField(verbose_name="name", max_length=32)
    avatar = models.FileField(verbose_name="image", upload_to='xxxx/')
