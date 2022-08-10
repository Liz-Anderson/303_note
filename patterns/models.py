from xmlrpc.client import Boolean
from django.db import models
from django.conf import settings


class Step(models.Model):
    number = models.IntegerField()
    note = models.CharField(max_length=10, blank=True, null=True)
    accent = models.BooleanField()
    slide = models.BooleanField()
    octave = models.CharField(max_length=20, blank=True, null=True)
    timing = models.CharField(max_length=10, blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.number} - {self.note}"

class Pattern(models.Model):
    title = models.CharField(max_length=200)
    notes = models.CharField(max_length=2000, blank=True, null=True)
    waveform = models.BooleanField()
    cutoff_dial = models.IntegerField()
    resonance_dial = models.IntegerField()
    envelope_dial = models.IntegerField()
    decay_dial = models.IntegerField()
    attack_dial = models.IntegerField()
    tempo_dial = models.IntegerField()
    tempo_entered = models.IntegerField()
    steps = models.ManyToManyField(Step, related_name="patterns", blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
