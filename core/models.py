from django.db import models


# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mno = models.BigIntegerField()
    hire_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    manager = models.ForeignKey(
        "self", on_delete=models.SET_NULL, null=True, blank=True, related_name="employee_manager"
    )
    salary = models.IntegerField()
    job_title = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.first_name + self.last_name


class Project(models.Model):
    name = models.CharField(max_length=50)
    budget = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    members = models.ManyToManyField(Employee, through="ProjectAssignment")

    def __str__(self):
        return self.name


class ProjectAssignment(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    assigned_date = models.DateField(auto_now=False, auto_now_add=True)
    role = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.employee} → {self.project} ({self.role})"


class Task(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    status = models.CharField(
        max_length=4, choices=[("TD", "todo"), ("IP", "in-progress"), ("DONE", "done")]
    )
    assign_to = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    due_date = models.DateTimeField(auto_now=False, auto_now_add=False)
    complated_date = models.DateTimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title


class LeaveRequest(models.Model):
    emolpyee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_employee')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    approved_by = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_employee'
    )
    status = models.CharField(
        max_length=50,
        choices=[
            ("APPROVED", "approved"),
            ("PENDING", "pending"),
            ("REJECTED", "rejected"),
        ],
    )

    def __str__(self):
        return self.emolpyee


class Appraisal(models.Model):
    emolpyee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='appraisal')
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviewer')
    review_date = models.DateField()
    score = models.IntegerField()
    comments = models.TextField()

    def __str__(self):
        return self.employee


class Asset(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.IntegerField()
    purchase_date = models.DateField()
    assigned_to = models.ForeignKey(
        Employee, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.name
    
class Payroll(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    month = models.DateField()
    base_salary = models.IntegerField()
    bonus = models.IntegerField()
    deductions = models.IntegerField()
    net_salary = models.IntegerField()