from django.db import models

class CurrentHO(models.Model):
    Status_choices =(

        ('Completed','Completed'),
        ('Approved','Approved'),
        ('Blocked','Blocked'),
        ('Pending','Pending')
    )

    Issue_choices =(

        ('Incident', 'Incident'),
        ('Change', 'Change'),
        ('Mail', 'Mail')
    )
    issue_type = models.CharField(max_length=50,choices= Issue_choices)
    updated_by = models.CharField(max_length=30)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    subject = models.TextField(default='Enter the description')
    status = models.CharField(max_length=50,choices=Status_choices)

    def __str__(self):
        return self.updated_by

