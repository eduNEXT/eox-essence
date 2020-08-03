from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Model
from opaque_keys import InvalidKeyError
from opaque_keys.edx.keys import CourseKey

from eox_essence.exceptions import EoxEssenceInvalidMethod, EoxEssenceInvalidModule
from eox_essence.wrappers import ModelWrapperBase
from eox_essence.wrappers.enrollments import model_settings


class EnrollmentsModelWrapper(ModelWrapperBase):
    """
    """

    backend_settings = model_settings

    @classmethod
    def get(cls, course_id, username, **kwargs):
        """
        """
        user = User.objects.get(username=username)

        try:
            course_key = CourseKey.from_string(course_id)
        except InvalidKeyError:
            return None

        kwargs.update({
            'course_key': course_key,
            'user': user,
        })

        try:
            return super().get(**kwargs)
        except EoxEssenceInvalidMethod:
            pass

        module = cls.get_module(cls.backend_settings)

        if not issubclass(module, Model):
            message = 'The module[{}] is not a subclass of django models.'.format(
                module.__name__,
            )
            raise EoxEssenceInvalidModule(message)

        try:
            return module.objects.get(course_id=course_id, user=user)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def update(cls, **kwargs):
        """
        """
        raise NotImplementedError('Update method is not supported.')

    @classmethod
    def create(cls, **kwargs):
        """
        """
        raise NotImplementedError('Create method is not supported.')

    @classmethod
    def delete(cls, **kwargs):
        """
        """
        raise NotImplementedError('Delete method is not supported.')
