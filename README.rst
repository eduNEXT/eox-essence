===========
eox-essence
===========

.. image:: https://circleci.com/gh/eduNEXT/eox-essence.svg?style=shield
    :target: https://circleci.com/gh/eduNEXT/eox-essence

.. image:: https://codecov.io/gh/eduNEXT/eox-essence/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/eduNEXT/eox-essence

Usage
#####

Central interface between edx-platform dependencies and any other external plugin, by default it provides the ability to use platform dependencies, however it is possible to toggle this behavior in the settings section so that each dependency can be replaced with a similar one.

Settings
********
This values can be modified in the following enviroments:

Ironwood:
++++++++
lms.env.json and cms.env.json

Juniper:
++++++++
/edx/etc/lms.yml and /edx/etc/studio.yml

Interface
#########
Reliable Open edX API(Application program interface) which provides a long term way to interact with multiple Open edX dependencies by using external tools, for the get case, this returns two kind of responses, first, an instance of the original model, which depends on the configuration and Open edX library, second, a serialized instance for the object, which is a reliable long term solution, that contains the same information through different versions in order to give a stable response to others external tools.

Application program interface
*****************************

- enrollment: Interface for course enrollment using as default model [https://github.com/edx/edx-platform/tree/master/common/djangoapps/student/models.py](CourseEnrollment)

How to use.
***********

Required configurations.
++++++++++++++++++++++++

.. code-block:: python

    EOX_ESSENCE_ENROLLMENTS = {
        'model': { # This will contain all the relate information for the enrollments model.
            'backend': 'module_path',  # [Required]Path of the model by default student.models
            'name': 'model_name',  # [Required]Model name by default CourseEnrollment
            'get': 'model_class_method',  #[Optional] if the model has a class method which returns the desired object.
            'allowed_parameters': [ #[Optional] the allowed parameter in the previous method.
                'course_key',
                'user',
            ],
        },
        'serialized': {  # This will contain all the relate information for the enrollments api.
            'backend': 'api_path', # [Required]Path of the api file.
            'name': 'api_name',  # [Required]Api name .
            'get': 'get_enrollment',  # [Required] Method name which will  return the serialized response.
            'allowed_parameters': [ #[Optional] the allowed parameter in the previous method.
                'username',
                'course_id',
            ],
        },

    }

Supported methods.
++++++++++++++++++

The following methods are supported for every interface.

- get_model
- get_serialized

Interface list.
+++++++++++++++
- Enrollments


Example:
++++++++

.. code-block:: python

  from eox_essence.interface.enrollment import EnrollmentEoxEssenceAPI

  MODEL = EnrollmentEoxEssenceAPI.get_model('staff', 'course-v1:edX+DemoX+Demo_Course')
  SERIALIZED = EnrollmentEoxEssenceAPI.get_serialized('staff', 'course-v1:edX+DemoX+Demo_Course')

Installation
############

Open edX devstack
*****************

- Clone this repo in the src folder of your devstack.
- Open a new Lms/Devstack shell.
- Install the plugin as follows: pip install -e /path/to/your/src/folder
- Restart Lms/Studio services.

Contributing
############

Add your contribution policy. (If required)