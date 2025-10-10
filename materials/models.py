from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название курса', help_text='Укажите название курса')
    description = models.TextField(max_length=500, verbose_name='Описание курса', help_text='Опишите курс')
    preview = models.ImageField(upload_to='materials/course_previews', null=True, blank=True,
                                verbose_name='Превью курса', help_text='Загрузите фото для превью курса')

    def __str__(self):
        return f'Курс {self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название урока', help_text='Укажите название урока')
    description = models.TextField(max_length=500, verbose_name='Описание урока', help_text='Опишите урок')
    preview = models.ImageField(upload_to='materials/lessons_previews', null=True, blank=True,
                                verbose_name='Превью урока', help_text='Загрузите фото для превью урока')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс', help_text='Выберите курс')

    def __str__(self):
        return f'Урок {self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
