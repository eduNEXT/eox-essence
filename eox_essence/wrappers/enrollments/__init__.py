from django.conf import settings

enrollment_settings = getattr(settings, 'EOX_ESSENCE_ENROLLMENTS', {})
model_settings = enrollment_settings.get('model', {})
serialized_settings = enrollment_settings.get('serialized', {})
