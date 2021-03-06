from django.db import models


class StreamType(models.Model):
    stream_type = models.CharField(max_length=5)

    def __unicode__(self):
        return self.stream_type


class Station(models.Model):
    streamType = models.ForeignKey(StreamType)
    name = models.CharField(max_length=45)
    url_text = models.CharField(max_length=1000)
    encoding = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name