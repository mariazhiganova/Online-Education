from urllib.parse import urlparse

from rest_framework import serializers


class VideoUrlValidator:
    def __call__(self, data):
        url = data.get('video_url')
        if url:
            allowed_domains = ['youtube.com', 'm.youtube.com', 'youtu.be']
            url_domain = urlparse(url).netloc.lower()
            if url_domain not in allowed_domains:
                raise serializers.ValidationError('Video url is forbidden')
