from django.db import models


class DeviceOwnerBase(models.Model):
    pass


class HealthPlace(models.Model):
    owner_pk = models.OneToOneField(DeviceOwnerBase, on_delete=models.CASCADE, primary_key=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="HealthPlace")
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


class Role(models.Model):
    name = models.CharField(max_length=100)
    workplace = models.ForeignKey(HealthPlace, on_delete=models.CASCADE)
    person = models.ForeignKey("Person", on_delete=models.CASCADE)


class Person(models.Model):
    owner_pk = models.OneToOneField(DeviceOwnerBase, on_delete=models.CASCADE, primary_key=True)
    fullname = models.CharField(max_length=100)
    sex = models.CharField(max_length=1)
    assigned_to = models.ManyToManyField("Person", through="DoctorAssignemt")
    profession = models.ManyToManyField(HealthPlace, through=Role)


class Device(models.Model):
    type = models.CharField(max_length=30)
    owned_by = models.ForeignKey(DeviceOwnerBase, on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(Person, on_delete=models.CASCADE)


class DoctorAssignemt(models.Model):
    doctor = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="doctor")
    patient = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="patient")
    expiry_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)


class Vital(models.Model):
    name = models.CharField(max_length=30)
    min_threshold = models.FloatField()
    max_threshold = models.FloatField()
    patient = models.ForeignKey(Person, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [models.Index(fields=["name"])]


class VitalMeasurement(models.Model):
    patient = models.ForeignKey(Person, on_delete=models.CASCADE)
    vital_id = models.ForeignKey(Vital, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
