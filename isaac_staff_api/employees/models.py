from django.db import models

# Superuser login:
# Username: iruonagbeisaac
# Email: isaac@gmail.com
# Password: isaacpassword123


class StaffBase(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)

    class Meta:
        abstract = True

    def get_role(self):
        return "Staff"


class Manager(StaffBase):
    department = models.CharField(max_length=100)
    has_company_card = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Manager"

    def get_role(self):
        return "Manager"


class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE, related_name='interns')
    internship_end = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Intern"

    def get_role(self):
        return "Intern"
class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"
