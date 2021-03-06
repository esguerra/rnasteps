from django.db import models

class Forces(models.Model):
    parameter = models.CharField(max_length=30, blank=True)
    step_id = models.CharField(max_length=24, blank=True)
    shift = models.FloatField(null=True, blank=True)
    slide = models.FloatField(null=True, blank=True)
    rise = models.FloatField(null=True, blank=True)
    tilt = models.FloatField(null=True, blank=True)
    roll = models.FloatField(null=True, blank=True)
    twist = models.FloatField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'forces'

class Steps(models.Model):
    stack_type = models.CharField(max_length=18, blank=True)
    step_id = models.CharField(max_length=24, blank=True)
    count = models.IntegerField(null=True, blank=True)
    shift = models.FloatField(null=True, blank=True)
    shift_std = models.FloatField(null=True, blank=True)
    slide = models.FloatField(null=True, blank=True)
    slide_std = models.FloatField(null=True, blank=True)
    rise = models.FloatField(null=True, blank=True)
    rise_std = models.FloatField(null=True, blank=True)
    tilt = models.FloatField(null=True, blank=True)
    tilt_std = models.FloatField(null=True, blank=True)
    roll = models.FloatField(null=True, blank=True)
    roll_std = models.FloatField(null=True, blank=True)
    twist = models.FloatField(null=True, blank=True)
    twist_std = models.FloatField(null=True, blank=True)
    volume = models.FloatField(null=True, blank=True)
    rmsd = models.FloatField(null=True, blank=True)
    rmsd_std = models.FloatField(null=True, blank=True)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'steps'

class StepIds(models.Model):
    ndb_id = models.CharField(max_length=30)
    pdb_id = models.CharField(max_length=30)
    edge3 = models.CharField(max_length=15)
    edge4 = models.CharField(max_length=15)
    gly_orie2 = models.CharField(max_length=15)
    step_id = models.CharField(max_length=45)
    residue1 = models.CharField(max_length=150)
    residue2 = models.CharField(max_length=150)
    residue3 = models.CharField(max_length=150)
    residue4 = models.CharField(max_length=150)
    edge1 = models.CharField(max_length=15)
    edge2 = models.CharField(max_length=15)
    gly_orie1 = models.CharField(max_length=15)
    id = models.IntegerField(primary_key=True)
    class Meta:
        db_table = u'step_ids'
