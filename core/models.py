from django.db import models


class Project(models.Model):
    project_title = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField("date published")
    location = models.CharField(max_length=200)
    target_amount = models.DecimalField(max_digits=10, decimal_places=2)
    amount_raised = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    deadline = models.DateTimeField()
    project_owner = models.CharField(max_length=200)

    def __str__(self):
        return self.project_title


class Investor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15)
    joined_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Investment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    investment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.investor} invested {self.amount} in {self.project}"


class Update(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    update_title = models.CharField(max_length=200)
    update_description = models.TextField()
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.project}: {self.update_title}"


class Payment(models.Model):
    investment = models.ForeignKey(Investment, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment of {self.payment_amount} for {self.investment}"
