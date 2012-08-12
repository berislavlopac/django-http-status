HTTPResponseCodes
=================

A library of useful HTTP response codes for Django.

Django includes a number of HttpResponse subclasses representing various HTTP response codes. This library completes that list adding the missing codes as defined in HTTP1.1.


2xx Codes: Success
------------------

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


3xx Codes: Redirection
----------------------

    Class                                       Response Code
    -----                                       -------------
    HttpResponseMultipleChoices                     300
    HttpResponsePermanentRedirect                   301
    HttpResponseRedirect                            302
    HttpResponseSeeOther                            303
    HttpResponseNotModified                         304
    HttpResponseUseProxy                            305
    HttpResponseTemporaryRedirect                   307


4xx Codes: Client-Side Error
----------------------------

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


5xx Codes: Server-Side Error
----------------------------

    Class                                       Response Code
    -----                                       -------------
    HttpResponseServerError                         500
    HttpResponseNotImplemented                      501
    HttpResponseBadGateway                          502
    HttpResponseServiceUnavailable                  503
    HttpResponseGatewayTimeout                      504
    HttpResponseHttpVersionNotSupported             505
