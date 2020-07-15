from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    class Meta:
        db_table = 'tbl_posts'
    message = models.TextField(blank=True,null=True)
    post_id = models.CharField(max_length=250,blank=True,null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now=True,auto_now_add=False)
    created_by = models.ForeignKey(User,null=True,related_name='guardian_created_by_user',on_delete=models.CASCADE)
    modified_date = models.DateField(null=True)
    modified_by = models.ForeignKey(User,null=True,related_name='guardian_modified_by_user',on_delete=models.CASCADE)
    is_deleted = models.BooleanField(null=True)
    deleted_date = models.DateField(null=True)
    deleted_by = models.ForeignKey(User,null=True,related_name='guardian_deleted_by_user',on_delete=models.CASCADE)

    def __str__(self):
        return ('%s' % (self.post_id))

class PostFiles(models.Model):
    class Meta:
        db_table = 'tbl_post_files'
    file = models.FileField(upload_to='post/file',blank=True)
    post = models.OneToOneField("Post", on_delete=models.CASCADE)