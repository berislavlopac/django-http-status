"""
Defines classes for the unofficial HTTP Response codes, usually defined by
other RFCs or as proprietary extenxions.

Based on (and the docstrings taken from) the list at
http://en.wikipedia.org/wiki/List_of_HTTP_status_codes

Nginx internal codes, as well as a few others, were not included.
"""

from django.http import HttpResponse # 200


# 2XX Codes: Success
class HttpResponseAlreadyReported(HttpResponse):
    """
    208 Already Reported (WebDAV; RFC 5842)
    The members of a DAV binding have already been enumerated in a previous
    reply to this request, and are not being included again.
    """
    status_code = 208


class HttpResponseIMUsed(HttpResponse):
    """
    226 IM Used (RFC 3229)
    The server has fulfilled a GET request for the resource, and the response
    is a representation of the result of one or more instance-manipulations
    applied to the current instance.
    """
    status_code = 226


# 3xx Codes: Redirection
class HttpResponsePermanentRedirect(HttpResponse):
    """
    308 Permanent Redirect (approved as experimental RFC])
    The request, and all future requests should be repeated using another URI.
    307 and 308 (as proposed) parallel the behaviours of 302 and 301, but do
    not allow the HTTP method to change. So, for example, submitting a form to
    a permanently redirected resource may continue smoothly.
    """
    status_code = 308


# 4xx Codes: Client-Side Error
class HttpResponseTeapot(HttpResponse):
    """
    418 I'm a teapot (RFC 2324)
    This code was defined in 1998 as one of the traditional IETF April Fools'
    jokes, in RFC 2324, Hyper Text Coffee Pot Control Protocol, and is not
    expected to be implemented by actual HTTP servers. However, known
    implementations do exist.
    """
    status_code = 418


class HttpResponseEnhanceYourCalm(HttpResponse):
    """
    420 Enhance Your Calm (Twitter)
    Not part of the HTTP standard, but returned by the Twitter Search and
    Trends API when the client is being rate limited.[13] Other services may
    wish to implement the 429 Too Many Requests response code instead.
    """
    status_code = 420


class HttpResponseUnprocessableEntity(HttpResponse):
    """
    422 Unprocessable Entity (WebDAV; RFC 4918)
    The request was well-formed but was unable to be followed due to semantic
    errors.
    """
    status_code = 422


class HttpResponseLocked(HttpResponse):
    """
    423 Locked (WebDAV; RFC 4918)
    The resource that is being accessed is locked.
    """
    status_code = 423


class HttpResponseFailedDependency(HttpResponse):
    """
    424 Failed Dependency (WebDAV; RFC 4918)
    The request failed due to failure of a previous request (e.g. a PROPPATCH).
    """
    status_code = 424


class HttpResponseUnorderedCollection(HttpResponse):
    """
    425 Unordered Collection (Internet draft)
    Defined in drafts of "WebDAV Advanced Collections Protocol", but not
    present in "Web Distributed Authoring and Versioning (WebDAV) Ordered
    Collections Protocol".
    """
    status_code = 425


class HttpResponseUpgradeRequired(HttpResponse):
    """
    426 Upgrade Required (RFC 2817)
    The client should switch to a different protocol such as TLS/1.0.
    """
    status_code = 426


class HttpResponsePreconditionRequired(HttpResponse):
    """
    428 Precondition Required (RFC 6585)
    The origin server requires the request to be conditional. Intended to
    prevent "the 'lost update' problem, where a client GETs a resource's state,
    modifies it, and PUTs it back to the server, when meanwhile a third party
    has modified the state on the server, leading to a conflict."
    """
    status_code = 428


class HttpResponseTooManyRequests(HttpResponse):
    """
    429 Too Many Requests (RFC 6585)
    The user has sent too many requests in a given amount of time. Intended for
    use with rate limiting schemes.
    """
    status_code = 429


class HttpResponseRequestHeaderFieldsTooLarge(HttpResponse):
    """
    431 Request Header Fields Too Large (RFC 6585)
    The server is unwilling to process the request because either an individual
    header field, or all the header fields collectively, are too large.
    """
    status_code = 431


class HttpResponseRetryWith(HttpResponse):
    """
    449 Retry With (Microsoft)
    A Microsoft extension. The request should be retried after performing the
    appropriate action.
    Often search-engines or custom applications will ignore required
    parameters. Where no default action is appropriate, the Aviongoo website
    sends a "HTTP/1.1 449 Retry with valid parameters: param1, param2, . . ."
    response. The applications may choose to learn, or not.
    """
    status_code = 449


class HttpResponseUnavailableForLegalReasons(HttpResponse):
    """
    451 Unavailable For Legal Reasons (Internet draft)
    Defined in the internet draft "A New HTTP Status Code for
    Legally-restricted Resources". Intended to be used when resource access is
    denied for legal reasons, e.g. censorship or government-mandated blocked
    access. Likely a reference to the 1953 dystopian novel Fahrenheit 451,
    where books are outlawed.
    """
    status_code = 451


# 5xx Codes: Server-Side Error
class HttpResponseVariantAlsoNegotiates(HttpResponse):
    """
    506 Variant Also Negotiates (RFC 2295)
    Transparent content negotiation for the request results in a circular
    reference.
    """
    status_code = 506


class HttpResponseInsufficientStorage(HttpResponse):
    """
    507 Insufficient Storage (WebDAV; RFC 4918)
    The server is unable to store the representation needed to complete the
    request.
    """
    status_code = 507


class HttpResponseLoopDetected(HttpResponse):
    """
    508 Loop Detected (WebDAV; RFC 5842)
    The server detected an infinite loop while processing the request (sent in
    lieu of 208).
    """
    status_code = 508


class HttpResponseBandwidthLimitExceeded(HttpResponse):
    """
    509 Bandwidth Limit Exceeded (Apache bw/limited extension)
    This status code, while used by many servers, is not specified in any RFCs.
    """
    status_code = 509


class HttpResponseNotExtended(HttpResponse):
    """
    510 Not Extended (RFC 2774)
    Further extensions to the request are required for the server to fulfill it.
    """
    status_code = 510


class HttpResponseNetworkAuthenticationRequired(HttpResponse):
    """
    511 Network Authentication Required (RFC 6585)
    The client needs to authenticate to gain network access. Intended for use
    by intercepting proxies used to control access to the network (e.g.
    "captive portals" used to require agreement to Terms of Service before
    granting full Internet access via a Wi-Fi hotspot).
    """
    status_code = 511
