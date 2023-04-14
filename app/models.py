from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=20,null=False)
    loc=models.CharField(max_length=20,null=False)

    def __str__(self):
        return self.dname
    

class Emp(models.Model):
    empno=models.IntegerField(null=False)
    ename=models.CharField(max_length=25)
    job=models.CharField(max_length=25,null=False)
    mgr=models.IntegerField(null=True,blank=True)
    hiredate=models.DateField()
    sal=models.IntegerField(null=False)
    comm=models.IntegerField(null=True,blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    
    def __str__(self):
        return self.ename

