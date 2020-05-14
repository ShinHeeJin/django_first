from django.db import models

# Create your models here.

# One to Many
class Board(models.Model):
    title = models.CharField(max_length=128, verbose_name="제목")
    contents = models.TextField(max_length=128, verbose_name="내용") # 길이제한 없음
    writer = models.ForeignKey('fcuser.Fcuser',
            on_delete=models.CASCADE, # 사용자 정보가 삭제될 경우 제목이 삭제되게 된다.
            verbose_name="작성자") # DB 연결\

    tags = models.ManyToManyField('tag.Tag', verbose_name="태그")
    registered_dttm = models.DateTimeField(
        auto_now_add=True, verbose_name="등록시간")

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'fastcampus_board'
        verbose_name = '패스트캠퍼스 게시글'
        verbose_name_plural = "패스트캠퍼스 게시글"
