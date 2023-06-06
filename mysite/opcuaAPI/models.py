from django.db import models

# Create your models here.
class MainCylinderStateModel(models.Model):
    x1 = models.IntegerField()
    x_1 = models.BooleanField()
    x_n1 = models.BooleanField()
    y1 = models.BooleanField()
    yn1 = models.BooleanField()


    def __str__(self):
        return f'x1: {self.x1} | y1: {self.y1} | yn1: {self.yn1}'


class AuxiliaryCylinderStateModel(models.Model):
    x2 = models.BooleanField()
    xn2 = models.BooleanField()
    y2 = models.BooleanField()


    def __str__(self):
        return f'x2: {self.x2} | xn2: {self.xn2}, | y2: {self.y2}'

class SystemStateModel(models.Model):
    xauto = models.BooleanField()
    xnext = models.BooleanField()
    xpause = models.BooleanField()
    xreset = models.BooleanField()
    xrun = models.BooleanField()
    xstep = models.BooleanField()


    def __str__(self):
        return f'xrun: {self.xrun}'

class DesiredStateModel(models.Model):
    '''
    Клас для опису команд, які задаються користувачем з серверу.
    '''
    xpause_desired = models.BooleanField()