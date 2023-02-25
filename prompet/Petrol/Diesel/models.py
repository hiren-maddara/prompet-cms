from django.db import models


class Diese(models.Model):
    Customername = models.CharField(max_length=200)
    Telephonecontact = models.CharField(max_length=200)
    Date = models.DateField()
    EmployeeName = models.CharField(max_length=200)
    EmployeeAddress = models.CharField(max_length=200)
    Fueltype = models.CharField(max_length=200)
    AmountinLitres = models.CharField(max_length=200)
    UnitPrice = models.CharField(max_length=200)
    TotalPrice = models.CharField(max_length=200)


class Employee(models.Model):
    EmployeeName = models.CharField(max_length=200)
    BranchName = models.CharField(max_length=200)
    EmployeeCOntact = models.CharField(max_length=200)
