from django.db import models

# Create your models here.
class EmpdataModel(models.Model):
    empid = models.IntegerField()
    empname = models.CharField(max_length=100)
    empsal = models.FloatField()
    empaddress = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.empname
    class Meta:
        db_table = "Empdata"