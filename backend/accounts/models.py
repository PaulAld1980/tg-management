from django.db import models
from django.contrib.auth.models import AbstractUser

# 1. Наша собственная модель Администратора
class User(AbstractUser):
    pass # Пока используем стандартные поля (логин, пароль, email), поэтому pass

# 2. Модель для хранения ключа от Telegram Бота
class BotConfig(models.Model):
    # Привязываем бота к Администратору (при удалении админа удалится и бот)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='bot_config')
    # Токен из @BotFather
    bot_token = models.CharField(max_length=255, blank=True, null=True, verbose_name="Токен бота")
    # Куда будут приходить вопросы боту от клиентов
    manager_chat_id = models.CharField(max_length=100, blank=True, null=True, verbose_name="ID чата менеджера")

    class Meta:
        verbose_name = "Конфигурация бота"
        verbose_name_plural = "Конфигурации бота"

    def __str__(self):
        return f"Настройки бота пользователя {self.user.username}"
