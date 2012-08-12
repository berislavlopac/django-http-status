"""
Defines classes for the "important" HTTP Response codes.
The status codes chosen were based off of "RESTful Web Services" by Richardson and Ruby
Codes not implemented:
    100: continue
    101: switching protocols
    401: payment required
"""

# 2XX Codes: Success
from django.http import HttpResponse # 200
class HttpResponseCreated(HttpResponse):
    status_code = 201
class HttpResponseAccepted(HttpResponse):
    status_code = 202
class HttpResponseNonAuthoritativeInformation(HttpResponse):
    status_code = 203
class HttpResponseNoContent(HttpResponse):
    status_code = 204
class HttpResponseResetContent(HttpResponse):
    status_code = 205
class HttpResponsePartialContent(HttpResponse):
    status_code = 206
class HttpResponseMultiStatus(HttpResponse):
    status_code = 207

# 3xx Codes: Redirection
class HttpResponseMultipleChoices(HttpResponse):
    status_code = 300
from django.http import HttpResponsePermanentRedirect # 301
from django.http import HttpResponseRedirect # 302
class HttpResponseSeeOther(HttpResponse):
    status_code = 303
from django.http import HttpResponseNotModified # 304
class HttpResponseUseProxy(HttpResponse):
    status_code = 305
class HttpResponseTemporaryRedirect(HttpResponse):
    status_code = 307

# 4xx Codes: Client-Side Error
from django.http import HttpResponseBadRequest # 400
class HttpResponseUnauthorized(HttpResponse):
    status_code = 401
from django.http import HttpResponseForbidden # 403
from django.http import HttpResponseNotFound # 404
from django.http import HttpResponseNotAllowed # 405
class HttpResponseNotAcceptable(HttpResponse):
    status_code = 406
class HttpResponseProxyAuthenticationRequired(HttpResponse):
    status_code = 407
class HttpResponseRequestTimeout(HttpResponse):
    status_code = 408
class HttpResponseConflict(HttpResponse):
    status_code = 409
from django.http import HttpResponseGone # 410
class HttpResponseLengthRequired(HttpResponse):
    status_code = 411
class HttpResponsePreconditionFailed(HttpResponse):
    status_code = 412
class HttpResponseRequestEntityTooLarge(HttpResponse):
    status_code = 413
class HttpResponseRequestURITooLong(HttpResponse):
    status_code = 414
class HttpResponseUnsupportedMediaType(HttpResponse):
    status_code = 415
class HttpResponseRequestedRangeNotSatisfiable(HttpResponse):
    status_code = 416
class HttpResponseExpectationFailed(HttpResponse):
    status_code = 417

# 5xx Codes: Server-Side Error
from django.http import HttpResponseServerError # 500
class HttpResponseNotImplemented(HttpResponse):
    status_code = 501
class HttpResponseBadGateway(HttpResponse):
    status_code = 502
class HttpResponseServiceUnavailable(HttpResponse):
    status_code = 503
class HttpResponseGatewayTimeout(HttpResponse):
    status_code = 504
class HttpResponseHttpVersionNotSupported(HttpResponse):
    status_code = 505
