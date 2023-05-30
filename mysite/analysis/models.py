from django.db import models

# Історія стану першого циліндра.
class MainStateHistory(models.Model):
    x_1_h = models.BooleanField()
    x_n1_h = models.BooleanField()
    y1_h = models.BooleanField()
    yn1_h = models.BooleanField()

    x_1_count = models.IntegerField(default=0)
    x_n1_count = models.IntegerField(default=0)
    y1_count = models.IntegerField(default=0)
    yn1_count = models.IntegerField(default=0)

    x_1_last_true = models.DateTimeField(null=True, blank=True)
    x_1_last_false = models.DateTimeField(null=True, blank=True)
    x_n1_last_true = models.DateTimeField(null=True, blank=True)
    x_n1_last_false = models.DateTimeField(null=True, blank=True)
    y1_last_true = models.DateTimeField(null=True, blank=True)
    y1_last_false = models.DateTimeField(null=True, blank=True)
    yn1_last_true = models.DateTimeField(null=True, blank=True)
    yn1_last_false = models.DateTimeField(null=True, blank=True)

    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Логіка підрахунку кількості перемикань та засікання часу

        # Перевірка x_1_h
        if self.x_1_h:
            if not self.x_1_last_true:
                self.x_1_count += 1
            self.x_1_last_true = self.time
            self.x_1_last_false = None
        else:
            self.x_1_last_false = self.time

        # Перевірка x_n1_h
        if self.x_n1_h:
            if not self.x_n1_last_true:
                self.x_n1_count += 1
            self.x_n1_last_true = self.time
            self.x_n1_last_false = None
        else:
            self.x_n1_last_false = self.time

        # Перевірка y1_h
        if self.y1_h:
            if not self.y1_last_true:
                self.y1_count += 1
            self.y1_last_true = self.time
            self.y1_last_false = None
        else:
            self.y1_last_false = self.time

        # Перевірка yn1_h
        if self.yn1_h:
            if not self.yn1_last_true:
                self.yn1_count += 1
            self.yn1_last_true = self.time
            self.yn1_last_false = None
        else:
            self.yn1_last_false = self.time

        super().save(*args, **kwargs)

# Історія стану другого циліндра.
class AuxiliaryStateHistory(models.Model):
    x2_h = models.BooleanField()
    xn2_h = models.BooleanField()
    y2_h = models.BooleanField()

    x2_count = models.IntegerField(default=0)
    xn2_count = models.IntegerField(default=0)
    y2_count = models.IntegerField(default=0)

    x2_last_true = models.DateTimeField(null=True, blank=True)
    x2_last_false = models.DateTimeField(null=True, blank=True)
    xn2_last_true = models.DateTimeField(null=True, blank=True)
    xn2_last_false = models.DateTimeField(null=True, blank=True)
    y2_last_true = models.DateTimeField(null=True, blank=True)
    y2_last_false = models.DateTimeField(null=True, blank=True)

    time = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Логіка підрахунку кількості перемикань та засікання часу

        # Перевірка x2_h
        if self.x2_h:
            if not self.x2_last_true:
                self.x2_count += 1
            self.x2_last_true = self.time
            self.x2_last_false = None
        else:
            self.x2_last_false = self.time

        # Перевірка xn2_h
        if self.xn2_h:
            if not self.xn2_last_true:
                self.xn2_count += 1
            self.xn2_last_true = self.time
            self.xn2_last_false = None
        else:
            self.xn2_last_false = self.time

        # Перевірка y2_h
        if self.y2_h:
            if not self.y2_last_true:
                self.y2_count += 1
            self.y2_last_true = self.time
            self.y2_last_false = None
        else:
            self.y2_last_false = self.time

        super().save(*args, **kwargs)
