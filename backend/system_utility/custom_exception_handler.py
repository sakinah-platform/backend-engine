import logging

import requests
from drf_standardized_errors.handler import ExceptionHandler
from rest_framework.exceptions import APIException
import traceback

from backend.system_utility.system_constant import SYSTEM_CONSTANT, SERVICE_UNAVAILABLE_STRCODE, SYSTEM_UNKNOWN_ERR_STRCODE

logger = logging.getLogger('CustomExceptionHandler')

class ServiceUnavailableException(APIException):

    status_code = 503
    default_detail = SYSTEM_CONSTANT.get(SERVICE_UNAVAILABLE_STRCODE)
    default_code =  SERVICE_UNAVAILABLE_STRCODE


class AndieniSpecialException(APIException):

    default_status_code = 503
    default_detail = SYSTEM_CONSTANT.get(SYSTEM_UNKNOWN_ERR_STRCODE)
    default_code = SYSTEM_UNKNOWN_ERR_STRCODE

    def __init__(self, detail=default_detail, code=default_code, status_code=default_status_code):

        AndieniSpecialException.status_code = status_code
        AndieniSpecialException.detail = detail
        AndieniSpecialException.code = code


class ExceptionHandlerWithLogging(ExceptionHandler):

    def convert_known_exceptions(self, exc: Exception) -> Exception:

        logger.error(traceback.format_exc())

        if isinstance(exc, requests.Timeout):

            return ServiceUnavailableException()

        else:

            return super().convert_known_exceptions(exc)
