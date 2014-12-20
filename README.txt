==================
Django HTTP Status
==================

A library of useful HTTP response codes for Django.

Django includes a number of HttpResponse subclasses representing various HTTP
response codes. This library completes that list adding the missing codes as
defined in HTTP1.1.

Official Codes
--------------

The library provides a number of offical codes, except for the 1xx ones
(continue) and 402 Payment Required, which is not oficially recognized. To use
the library just import is as::

    from http_status import HttpResponse, HttpResponsePartialContent


2xx: Success
~~~~~~~~~~~~

::

    Class                                       Response Code
    -----                                       -------------
    HttpResponse                                    200
    HttpResponseCreated                             201
    HttpResponseAccepted                            202
    HttpResponseNonAuthoritativeInformation         203
    HttpResponseNoContent                           204
    HttpResponseResetContent                        205
    HttpResponsePartialContent                      206
    HttpResponseMultiStatus                         207


3xx: Redirection
~~~~~~~~~~~~~~~~

::

    Class                                       Response Code
    -----                                       -------------
    HttpResponseMultipleChoices                     300
    HttpResponsePermanentRedirect                   301
    HttpResponseRedirect                            302
    HttpResponseSeeOther                            303
    HttpResponseNotModified                         304
    HttpResponseUseProxy                            305
    HttpResponseTemporaryRedirect                   307


4xx: Client-Side Error
~~~~~~~~~~~~~~~~~~~~~~

::

    Class                                       Response Code
    -----                                       -------------
    HttpResponseBadRequest                          400
    HttpResponseUnauthorized                        401
    HttpResponseForbidden                           403
    HttpResponseNotFound                            404
    HttpResponseNotAllowed                          405
    HttpResponseNotAcceptable                       406
    HttpResponseProxyAuthenticationRequired         407
    HttpResponseRequestTimeout                      408
    HttpResponseConflict                            409
    HttpResponseGone                                410
    HttpResponseLengthRequired                      411
    HttpResponsePreconditionFailed                  412
    HttpResponseRequestEntityTooLarge               413
    HttpResponseRequestURITooLong                   414
    HttpResponseUnsupportedMediaType                415
    HttpResponseRequestedRangeNotSatisfiable        416
    HttpResponseExpectationFailed                   417


5xx: Server-Side Error
~~~~~~~~~~~~~~~~~~~~~~

::

    Class                                       Response Code
    -----                                       -------------
    HttpResponseServerError                         500
    HttpResponseNotImplemented                      501
    HttpResponseBadGateway                          502
    HttpResponseServiceUnavailable                  503
    HttpResponseGatewayTimeout                      504
    HttpResponseHttpVersionNotSupported             505


Unofficial Codes
----------------

The library also implements a number unofficial response status codes that are
not oficially a part of HTTP but were introduced by other protocols (such as
WebDAV) or simply for fun (such as 418 I'm a Teapot).

To use, import the appropriate module::

    from django-http-status.unofficial import HttpResponseTeapot


2xx: Success
~~~~~~~~~~~~

::

    Class                                       Response Code
    -----                                       -------------
    HttpResponseAlreadyReported                     208
    HttpResponseIMUsed                              226


3xx: Redirection
~~~~~~~~~~~~~~~~

::

    Class                                       Response Code
    -----                                       -------------
    HttpResponsePermanentRedirect                   308


4xx: Client-Side Error
~~~~~~~~~~~~~~~~~~~~~~

::

    Class                                       Response Code
    -----                                       -------------
    HttpResponseTeapot                              418
    HttpResponseEnhanceYourCalm                     420
    HttpResponseUnprocessableEntity                 422
    HttpResponseLocked                              423
    HttpResponseFailedDependency                    424
    HttpResponseUnorderedCollection                 425
    HttpResponseUpgradeRequired                     426
    HttpResponsePreconditionRequired                428
    HttpResponseTooManyRequests                     429
    HttpResponseRequestHeaderFieldsTooLarge         431
    HttpResponseRetryWith                           449
    HttpResponseUnavailableForLegalReasons          451


5xx: Server-Side Error
~~~~~~~~~~~~~~~~~~~~~~

::

    Class                                       Response Code
    -----                                       -------------
    HttpResponseVariantAlsoNegotiates               506
    HttpResponseInsufficientStorage                 507
    HttpResponseLoopDetected                        508
    HttpResponseBandwidthLimitExceeded              509
    HttpResponseNotExtended                         510
    HttpResponseNetworkAuthenticationRequired       511