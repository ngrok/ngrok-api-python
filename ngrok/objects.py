
from __future__ import annotations
from collections.abc import Iterator
from typing import Any, Mapping

class Empty(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<Empty {}>".format(self.id)

    

class Item(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<Item {}>".format(self.id)

    
    
    @property
    def id(self):
        """ a resource identifier """
        return self._props["id"]

class Page(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<Page {}>".format(self.id)

    
    
    @property
    def before_id(self):
        """  """
        return self._props["before_id"]
    
    @property
    def limit(self):
        """  """
        return self._props["limit"]

class Error(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<Error {}>".format(self.id)

    
    
    @property
    def error_code(self):
        """  """
        return self._props["error_code"]
    
    @property
    def status_code(self):
        """  """
        return self._props["status_code"]
    
    @property
    def msg(self):
        """  """
        return self._props["msg"]
    
    @property
    def details(self):
        """  """
        return self._props["details"]

class Ref(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<Ref {}>".format(self.id)

    
    
    @property
    def id(self):
        """ a resource identifier """
        return self._props["id"]
    
    @property
    def uri(self):
        """ a uri for locating a resource """
        return self._props["uri"]

class AbuseReport(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<AbuseReport {}>".format(self.id)

    
    
    @property
    def id(self):
        """ ID of the abuse report """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the abuse report API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp that the abuse report record was created in RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def urls(self):
        """ a list of URLs containing suspected abusive content """
        return self._props["urls"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined data about this abuse report. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def status(self):
        """ Indicates whether ngrok has processed the abuse report. one of <code>PENDING</code>, <code>PROCESSED</code>, or <code>PARTIALLY_PROCESSED</code> """
        return self._props["status"]
    
    @property
    def hostnames(self):
        """ an array of hostname statuses related to the report """
        return self._props["hostnames"]

class AbuseReportHostname(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<AbuseReportHostname {}>".format(self.id)

    
    
    @property
    def hostname(self):
        """ the hostname ngrok has parsed out of one of the reported URLs in this abuse report """
        return self._props["hostname"]
    
    @property
    def status(self):
        """ indicates what action ngrok has taken against the hostname. one of <code>PENDING</code>, <code>BANNED</code>, <code>UNBANNED</code>, or <code>IGNORE</code> """
        return self._props["status"]

class AbuseReportCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<AbuseReportCreate {}>".format(self.id)

    
    
    @property
    def urls(self):
        """ a list of URLs containing suspected abusive content """
        return self._props["urls"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined data about this abuse report. Optional, max 4096 bytes. """
        return self._props["metadata"]

class APIKeyCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<APIKeyCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of what uses the API key to authenticate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined data of this API key. optional, max 4096 bytes """
        return self._props["metadata"]

class APIKeyUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<APIKeyUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of what uses the API key to authenticate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined data of this API key. optional, max 4096 bytes """
        return self._props["metadata"]

class APIKey(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<APIKey {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique API key resource identifier """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI to the API resource of this API key """
        return self._props["uri"]
    
    @property
    def description(self):
        """ human-readable description of what uses the API key to authenticate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined data of this API key. optional, max 4096 bytes """
        return self._props["metadata"]
    
    @property
    def created_at(self):
        """ timestamp when the api key was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def token(self):
        """ the bearer token that can be placed into the Authorization header to authenticate request to the ngrok API. <strong>This value is only available one time, on the API response from key creation. Otherwise it is null.</strong> """
        return self._props["token"]

class APIKeyList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<APIKeyList {}>".format(self.id)

    def __iter__(self):
        return (APIKey(o) for o in self._props["keys"])
    
    @property
    def keys(self):
        """ the list of API keys for this account """
        return self._props["keys"]
    
    @property
    def uri(self):
        """ URI of the API keys list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class PriorityBackend(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<PriorityBackend {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this Priority backend """
        return self._props["id"]
    
    @property
    def created_at(self):
        """ timestamp when the backend was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def backends(self):
        """ the ids of the child backends in order """
        return self._props["backends"]

class PriorityBackendCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<PriorityBackendCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def backends(self):
        """ the ids of the child backends in order """
        return self._props["backends"]

class PriorityBackendUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<PriorityBackendUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def backends(self):
        """ the ids of the child backends in order """
        return self._props["backends"]

class PriorityBackendList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<PriorityBackendList {}>".format(self.id)

    def __iter__(self):
        return (PriorityBackend(o) for o in self._props["backends"])
    
    @property
    def backends(self):
        """ the list of all Priority backends on this account """
        return self._props["backends"]
    
    @property
    def uri(self):
        """ URI of the Priority backends list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class StaticBackend(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<StaticBackend {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this static backend """
        return self._props["id"]
    
    @property
    def created_at(self):
        """ timestamp when the backend was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def address(self):
        """ the address to forward to """
        return self._props["address"]
    
    @property
    def tls(self):
        """ tls configuration to use """
        return self._props["tls"]

class StaticBackendTLS(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<StaticBackendTLS {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ if tls is checked """
        return self._props["enabled"]

class StaticBackendCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<StaticBackendCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def address(self):
        """ the address to forward to """
        return self._props["address"]
    
    @property
    def tls(self):
        """ tls configuration to use """
        return self._props["tls"]

class StaticBackendUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<StaticBackendUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def address(self):
        """ the address to forward to """
        return self._props["address"]
    
    @property
    def tls(self):
        """ tls configuration to use """
        return self._props["tls"]

class StaticBackendList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<StaticBackendList {}>".format(self.id)

    def __iter__(self):
        return (StaticBackend(o) for o in self._props["backends"])
    
    @property
    def backends(self):
        """ the list of all static backends on this account """
        return self._props["backends"]
    
    @property
    def uri(self):
        """ URI of the static backends list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class TunnelGroupBackend(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TunnelGroupBackend {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this TunnelGroup backend """
        return self._props["id"]
    
    @property
    def created_at(self):
        """ timestamp when the backend was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def labels(self):
        """ labels to watch for tunnels on, e.g. app->foo, dc->bar """
        return self._props["labels"]

class TunnelGroupBackendCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TunnelGroupBackendCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def labels(self):
        """ labels to watch for tunnels on, e.g. app->foo, dc->bar """
        return self._props["labels"]

class TunnelGroupBackendUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TunnelGroupBackendUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def labels(self):
        """ labels to watch for tunnels on, e.g. app->foo, dc->bar """
        return self._props["labels"]

class TunnelGroupBackendList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TunnelGroupBackendList {}>".format(self.id)

    def __iter__(self):
        return (TunnelGroupBackend(o) for o in self._props["backends"])
    
    @property
    def backends(self):
        """ the list of all TunnelGroup backends on this account """
        return self._props["backends"]
    
    @property
    def uri(self):
        """ URI of the TunnelGroup backends list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class WeightedBackend(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<WeightedBackend {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this Weighted backend """
        return self._props["id"]
    
    @property
    def created_at(self):
        """ timestamp when the backend was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def backends(self):
        """ the ids of the child backends to their weights (0-10000) """
        return self._props["backends"]

class WeightedBackendCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<WeightedBackendCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def backends(self):
        """ the ids of the child backends to their weights (0-10000) """
        return self._props["backends"]

class WeightedBackendUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<WeightedBackendUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of this backend. Optional """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this backend. Optional """
        return self._props["metadata"]
    
    @property
    def backends(self):
        """ the ids of the child backends to their weights (0-10000) """
        return self._props["backends"]

class WeightedBackendList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<WeightedBackendList {}>".format(self.id)

    def __iter__(self):
        return (WeightedBackend(o) for o in self._props["backends"])
    
    @property
    def backends(self):
        """ the list of all Weighted backends on this account """
        return self._props["backends"]
    
    @property
    def uri(self):
        """ URI of the Weighted backends list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class CertificateAuthorityCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<CertificateAuthorityCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of this Certificate Authority. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this Certificate Authority. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def ca_pem(self):
        """ raw PEM of the Certificate Authority """
        return self._props["ca_pem"]

class CertificateAuthorityUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<CertificateAuthorityUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of this Certificate Authority. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this Certificate Authority. optional, max 4096 bytes. """
        return self._props["metadata"]

class CertificateAuthority(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<CertificateAuthority {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this Certificate Authority """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the Certificate Authority API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the Certificate Authority was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of this Certificate Authority. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this Certificate Authority. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def ca_pem(self):
        """ raw PEM of the Certificate Authority """
        return self._props["ca_pem"]
    
    @property
    def subject_common_name(self):
        """ subject common name of the Certificate Authority """
        return self._props["subject_common_name"]
    
    @property
    def not_before(self):
        """ timestamp when this Certificate Authority becomes valid, RFC 3339 format """
        return self._props["not_before"]
    
    @property
    def not_after(self):
        """ timestamp when this Certificate Authority becomes invalid, RFC 3339 format """
        return self._props["not_after"]
    
    @property
    def key_usages(self):
        """ set of actions the private key of this Certificate Authority can be used for """
        return self._props["key_usages"]
    
    @property
    def extended_key_usages(self):
        """ extended set of actions the private key of this Certificate Authority can be used for """
        return self._props["extended_key_usages"]

class CertificateAuthorityList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<CertificateAuthorityList {}>".format(self.id)

    def __iter__(self):
        return (CertificateAuthority(o) for o in self._props["certificate_authorities"])
    
    @property
    def certificate_authorities(self):
        """ the list of all certificate authorities on this account """
        return self._props["certificate_authorities"]
    
    @property
    def uri(self):
        """ URI of the certificates authorities list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class CredentialCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<CredentialCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of who or what will use the credential to authenticate. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this credential. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def acl(self):
        """ optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the <code>bind</code> rule. The <code>bind</code> rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule <code>bind:example.ngrok.io</code>. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of <code>bind:*.example.com</code> which will allow <code>x.example.com</code>, <code>y.example.com</code>, <code>*.example.com</code>, etc. A rule of <code>'*'</code> is equivalent to no acl at all and will explicitly permit all actions. """
        return self._props["acl"]

class CredentialUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<CredentialUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of who or what will use the credential to authenticate. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this credential. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def acl(self):
        """ optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the <code>bind</code> rule. The <code>bind</code> rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule <code>bind:example.ngrok.io</code>. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of <code>bind:*.example.com</code> which will allow <code>x.example.com</code>, <code>y.example.com</code>, <code>*.example.com</code>, etc. A rule of <code>'*'</code> is equivalent to no acl at all and will explicitly permit all actions. """
        return self._props["acl"]

class Credential(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<Credential {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique tunnel credential resource identifier """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the tunnel credential API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the tunnel credential was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of who or what will use the credential to authenticate. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this credential. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def token(self):
        """ the credential's authtoken that can be used to authenticate an ngrok client. <strong><em>This value is only available one time, on the API response from credential creation, otherwise it is null.</em></strong> """
        return self._props["token"]
    
    @property
    def acl(self):
        """ optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the <code>bind</code> rule. The <code>bind</code> rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule <code>bind:example.ngrok.io</code>. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of <code>bind:*.example.com</code> which will allow <code>x.example.com</code>, <code>y.example.com</code>, <code>*.example.com</code>, etc. A rule of <code>'*'</code> is equivalent to no acl at all and will explicitly permit all actions. """
        return self._props["acl"]

class CredentialList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<CredentialList {}>".format(self.id)

    def __iter__(self):
        return (Credential(o) for o in self._props["credentials"])
    
    @property
    def credentials(self):
        """ the list of all tunnel credentials on this account """
        return self._props["credentials"]
    
    @property
    def uri(self):
        """ URI of the tunnel credential list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class EventStreamCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventStreamCreate {}>".format(self.id)

    
    
    @property
    def metadata(self):
        """ Arbitrary user-defined machine-readable data of this Event Stream. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def description(self):
        """ Human-readable description of the Event Stream. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def fields(self):
        """ A list of protocol-specific fields you want to collect on each event. """
        return self._props["fields"]
    
    @property
    def event_type(self):
        """ The protocol that determines which events will be collected. Supported values are <code>tcp_connection_closed</code> and <code>http_request_complete</code>. """
        return self._props["event_type"]
    
    @property
    def destination_ids(self):
        """ A list of Event Destination IDs which should be used for this Event Stream. Event Streams are required to have at least one Event Destination. """
        return self._props["destination_ids"]
    
    @property
    def sampling_rate(self):
        """ The percentage of all events you would like to capture. Valid values range from 0.01, representing 1% of all events to 1.00, representing 100% of all events. """
        return self._props["sampling_rate"]

class EventStreamUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventStreamUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """ Unique identifier for this Event Stream. """
        return self._props["id"]
    
    @property
    def metadata(self):
        """ Arbitrary user-defined machine-readable data of this Event Stream. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def description(self):
        """ Human-readable description of the Event Stream. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def fields(self):
        """ A list of protocol-specific fields you want to collect on each event. """
        return self._props["fields"]
    
    @property
    def destination_ids(self):
        """ A list of Event Destination IDs which should be used for this Event Stream. Event Streams are required to have at least one Event Destination. """
        return self._props["destination_ids"]
    
    @property
    def sampling_rate(self):
        """ The percentage of all events you would like to capture. Valid values range from 0.01, representing 1% of all events to 1.00, representing 100% of all events. """
        return self._props["sampling_rate"]

class EventStreamList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventStreamList {}>".format(self.id)

    def __iter__(self):
        return (EventStream(o) for o in self._props["event_streams"])
    
    @property
    def event_streams(self):
        """ The list of all Event Streams on this account. """
        return self._props["event_streams"]
    
    @property
    def uri(self):
        """ URI of the Event Stream list API resource. """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page. """
        return self._props["next_page_uri"]

class EventStream(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventStream {}>".format(self.id)

    
    
    @property
    def id(self):
        """ Unique identifier for this Event Stream. """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the Event Stream API resource. """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ Timestamp when the Event Stream was created, RFC 3339 format. """
        return self._props["created_at"]
    
    @property
    def metadata(self):
        """ Arbitrary user-defined machine-readable data of this Event Stream. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def description(self):
        """ Human-readable description of the Event Stream. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def fields(self):
        """ A list of protocol-specific fields you want to collect on each event. """
        return self._props["fields"]
    
    @property
    def event_type(self):
        """ The protocol that determines which events will be collected. Supported values are <code>tcp_connection_closed</code> and <code>http_request_complete</code>. """
        return self._props["event_type"]
    
    @property
    def destination_ids(self):
        """ A list of Event Destination IDs which should be used for this Event Stream. Event Streams are required to have at least one Event Destination. """
        return self._props["destination_ids"]
    
    @property
    def sampling_rate(self):
        """ The percentage of all events you would like to capture. Valid values range from 0.01, representing 1% of all events to 1.00, representing 100% of all events. """
        return self._props["sampling_rate"]

class EventDestinationCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventDestinationCreate {}>".format(self.id)

    
    
    @property
    def metadata(self):
        """ Arbitrary user-defined machine-readable data of this Event Destination. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def description(self):
        """ Human-readable description of the Event Destination. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def format(self):
        """ The output format you would like to serialize events into when sending to their target. Currently the only accepted value is <code>JSON</code>. """
        return self._props["format"]
    
    @property
    def target(self):
        """ An object that encapsulates where and how to send your events. An event destination must contain exactly one of the following objects, leaving the rest null: <code>kinesis</code>, <code>firehose</code>, <code>cloudwatch_logs</code>, or <code>s3</code>. """
        return self._props["target"]
    
    @property
    def verify_with_test_event(self):
        """  """
        return self._props["verify_with_test_event"]

class EventDestinationUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventDestinationUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """ Unique identifier for this Event Destination. """
        return self._props["id"]
    
    @property
    def metadata(self):
        """ Arbitrary user-defined machine-readable data of this Event Destination. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def description(self):
        """ Human-readable description of the Event Destination. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def format(self):
        """ The output format you would like to serialize events into when sending to their target. Currently the only accepted value is <code>JSON</code>. """
        return self._props["format"]
    
    @property
    def target(self):
        """ An object that encapsulates where and how to send your events. An event destination must contain exactly one of the following objects, leaving the rest null: <code>kinesis</code>, <code>firehose</code>, <code>cloudwatch_logs</code>, or <code>s3</code>. """
        return self._props["target"]
    
    @property
    def verify_with_test_event(self):
        """  """
        return self._props["verify_with_test_event"]

class EventDestination(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventDestination {}>".format(self.id)

    
    
    @property
    def id(self):
        """ Unique identifier for this Event Destination. """
        return self._props["id"]
    
    @property
    def metadata(self):
        """ Arbitrary user-defined machine-readable data of this Event Destination. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def created_at(self):
        """ Timestamp when the Event Destination was created, RFC 3339 format. """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ Human-readable description of the Event Destination. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def format(self):
        """ The output format you would like to serialize events into when sending to their target. Currently the only accepted value is <code>JSON</code>. """
        return self._props["format"]
    
    @property
    def target(self):
        """ An object that encapsulates where and how to send your events. An event destination must contain exactly one of the following objects, leaving the rest null: <code>kinesis</code>, <code>firehose</code>, <code>cloudwatch_logs</code>, or <code>s3</code>. """
        return self._props["target"]
    
    @property
    def uri(self):
        """ URI of the Event Destination API resource. """
        return self._props["uri"]

class EventDestinationList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventDestinationList {}>".format(self.id)

    def __iter__(self):
        return (EventDestination(o) for o in self._props["event_destinations"])
    
    @property
    def event_destinations(self):
        """ The list of all Event Destinations on this account. """
        return self._props["event_destinations"]
    
    @property
    def uri(self):
        """ URI of the Event Destinations list API resource. """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page. """
        return self._props["next_page_uri"]

class EventTarget(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventTarget {}>".format(self.id)

    
    
    @property
    def firehose(self):
        """ Configuration used to send events to Amazon Kinesis Data Firehose. """
        return self._props["firehose"]
    
    @property
    def kinesis(self):
        """ Configuration used to send events to Amazon Kinesis. """
        return self._props["kinesis"]
    
    @property
    def cloudwatch_logs(self):
        """ Configuration used to send events to Amazon CloudWatch Logs. """
        return self._props["cloudwatch_logs"]
    
    @property
    def debug(self):
        """ Configuration used for internal debugging. """
        return self._props["debug"]

class EventTargetFirehose(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventTargetFirehose {}>".format(self.id)

    
    
    @property
    def auth(self):
        """ Configuration for how to authenticate into your AWS account. Exactly one of <code>role</code> or <code>creds</code> should be configured. """
        return self._props["auth"]
    
    @property
    def delivery_stream_arn(self):
        """ An Amazon Resource Name specifying the Firehose delivery stream to deposit events into. """
        return self._props["delivery_stream_arn"]

class EventTargetKinesis(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventTargetKinesis {}>".format(self.id)

    
    
    @property
    def auth(self):
        """ Configuration for how to authenticate into your AWS account. Exactly one of <code>role</code> or <code>creds</code> should be configured. """
        return self._props["auth"]
    
    @property
    def stream_arn(self):
        """ An Amazon Resource Name specifying the Kinesis stream to deposit events into. """
        return self._props["stream_arn"]

class EventTargetCloudwatchLogs(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventTargetCloudwatchLogs {}>".format(self.id)

    
    
    @property
    def auth(self):
        """ Configuration for how to authenticate into your AWS account. Exactly one of <code>role</code> or <code>creds</code> should be configured. """
        return self._props["auth"]
    
    @property
    def log_group_arn(self):
        """ An Amazon Resource Name specifying the CloudWatch Logs group to deposit events into. """
        return self._props["log_group_arn"]

class EventTargetS3(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventTargetS3 {}>".format(self.id)

    
    
    @property
    def auth(self):
        """ Configuration for how to authenticate into your AWS account. Exactly one of <code>role</code> or <code>creds</code> should be configured. """
        return self._props["auth"]
    
    @property
    def bucket_arn(self):
        """ An Amazon Resource Name specifying the S3 bucket to deposit events into. """
        return self._props["bucket_arn"]
    
    @property
    def object_prefix(self):
        """ An optional prefix to prepend to S3 object keys. """
        return self._props["object_prefix"]
    
    @property
    def compression(self):
        """ Whether or not to compress files with gzip. """
        return self._props["compression"]
    
    @property
    def max_file_size(self):
        """ How many bytes we should accumulate into a single file before sending to S3. """
        return self._props["max_file_size"]
    
    @property
    def max_file_age(self):
        """ How many seconds we should batch up events before sending them to S3. """
        return self._props["max_file_age"]

class EventTargetDebug(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventTargetDebug {}>".format(self.id)

    
    
    @property
    def log(self):
        """ Whether or not to output to publisher service logs. """
        return self._props["log"]
    
    @property
    def callback_url(self):
        """ URL to send events to. """
        return self._props["callback_url"]

class AWSAuth(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<AWSAuth {}>".format(self.id)

    
    
    @property
    def role(self):
        """ A role for ngrok to assume on your behalf to deposit events into your AWS account. """
        return self._props["role"]
    
    @property
    def creds(self):
        """ Credentials to your AWS account if you prefer ngrok to sign in with long-term access keys. """
        return self._props["creds"]

class AWSRole(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<AWSRole {}>".format(self.id)

    
    
    @property
    def role_arn(self):
        """ An ARN that specifies the role that ngrok should use to deliver to the configured target. """
        return self._props["role_arn"]

class AWSCredentials(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<AWSCredentials {}>".format(self.id)

    
    
    @property
    def aws_access_key_id(self):
        """ The ID portion of an AWS access key. """
        return self._props["aws_access_key_id"]
    
    @property
    def aws_secret_access_key(self):
        """ The secret portion of an AWS access key. """
        return self._props["aws_secret_access_key"]

class SentEvent(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SentEvent {}>".format(self.id)

    
    
    @property
    def event_id(self):
        """  """
        return self._props["event_id"]

class EventSubscriptionCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSubscriptionCreate {}>".format(self.id)

    
    
    @property
    def metadata(self):
        """ Arbitrary customer supplied information intended to be machine readable. Optional, max 4096 chars. """
        return self._props["metadata"]
    
    @property
    def description(self):
        """ Arbitrary customer supplied information intended to be human readable. Optional, max 255 chars. """
        return self._props["description"]
    
    @property
    def sources(self):
        """ TODO """
        return self._props["sources"]
    
    @property
    def destination_ids(self):
        """ TODO """
        return self._props["destination_ids"]

class EventSubscriptionUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSubscriptionUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """ Unique identifier for this Event Subscription. """
        return self._props["id"]
    
    @property
    def metadata(self):
        """ Arbitrary customer supplied information intended to be machine readable. Optional, max 4096 chars. """
        return self._props["metadata"]
    
    @property
    def description(self):
        """ Arbitrary customer supplied information intended to be human readable. Optional, max 255 chars. """
        return self._props["description"]
    
    @property
    def sources(self):
        """ TODO """
        return self._props["sources"]
    
    @property
    def destination_ids(self):
        """ TODO """
        return self._props["destination_ids"]

class EventSubscriptionList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSubscriptionList {}>".format(self.id)

    def __iter__(self):
        return (EventSubscription(o) for o in self._props["event_subscriptions"])
    
    @property
    def event_subscriptions(self):
        """ The list of all Event Subscriptions on this account. """
        return self._props["event_subscriptions"]
    
    @property
    def uri(self):
        """ URI of the Event Subscriptions list API resource. """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of next page, or null if there is no next page. """
        return self._props["next_page_uri"]

class EventSubscription(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSubscription {}>".format(self.id)

    
    
    @property
    def id(self):
        """ Unique identifier for this Event Subscription. """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the Event Subscription API resource. """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ When the Event Subscription was created (RFC 3339 format). """
        return self._props["created_at"]
    
    @property
    def metadata(self):
        """ Arbitrary customer supplied information intended to be machine readable. Optional, max 4096 chars. """
        return self._props["metadata"]
    
    @property
    def description(self):
        """ Arbitrary customer supplied information intended to be human readable. Optional, max 255 chars. """
        return self._props["description"]
    
    @property
    def sources(self):
        """ TODO """
        return self._props["sources"]
    
    @property
    def destinations(self):
        """ TODO """
        return self._props["destinations"]

class EventSourceReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSourceReplace {}>".format(self.id)

    
    
    @property
    def type(self):
        """ TODO """
        return self._props["type"]
    
    @property
    def filter(self):
        """ TODO """
        return self._props["filter"]
    
    @property
    def fields(self):
        """ TODO """
        return self._props["fields"]

class EventSource(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSource {}>".format(self.id)

    
    
    @property
    def type(self):
        """ TODO """
        return self._props["type"]
    
    @property
    def filter(self):
        """ TODO """
        return self._props["filter"]
    
    @property
    def fields(self):
        """ TODO """
        return self._props["fields"]
    
    @property
    def uri(self):
        """ TODO """
        return self._props["uri"]

class EventSourceList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSourceList {}>".format(self.id)

    
    
    @property
    def sources(self):
        """ TODO """
        return self._props["sources"]
    
    @property
    def uri(self):
        """ TODO """
        return self._props["uri"]

class EventSourceCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSourceCreate {}>".format(self.id)

    
    
    @property
    def subscription_id(self):
        """ TODO """
        return self._props["subscription_id"]
    
    @property
    def type(self):
        """ TODO """
        return self._props["type"]
    
    @property
    def filter(self):
        """ TODO """
        return self._props["filter"]
    
    @property
    def fields(self):
        """ TODO """
        return self._props["fields"]

class EventSourceUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSourceUpdate {}>".format(self.id)

    
    
    @property
    def subscription_id(self):
        """ TODO """
        return self._props["subscription_id"]
    
    @property
    def type(self):
        """ TODO """
        return self._props["type"]
    
    @property
    def filter(self):
        """ TODO """
        return self._props["filter"]
    
    @property
    def fields(self):
        """ TODO """
        return self._props["fields"]

class EventSourceItem(object):
    """ This is needed instead of Item because the parameters are different. """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSourceItem {}>".format(self.id)

    
    
    @property
    def subscription_id(self):
        """ TODO """
        return self._props["subscription_id"]
    
    @property
    def type(self):
        """ TODO """
        return self._props["type"]

class EventSourcePage(object):
    """ This is needed instead of Page because the parameters are different. We also don't need the typical pagination params because pagination of this isn't necessary or supported. """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EventSourcePage {}>".format(self.id)

    
    
    @property
    def subscription_id(self):
        """ TODO """
        return self._props["subscription_id"]

class IPPolicyCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPPolicyCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of the source IPs of this IP policy. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP policy. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def action(self):
        """ the IP policy action. Supported values are <code>allow</code> or <code>deny</code> """
        return self._props["action"]

class IPPolicyUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPPolicyUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of the source IPs of this IP policy. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP policy. optional, max 4096 bytes. """
        return self._props["metadata"]

class IPPolicy(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPPolicy {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this IP policy """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the IP Policy API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the IP policy was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of the source IPs of this IP policy. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP policy. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def action(self):
        """ the IP policy action. Supported values are <code>allow</code> or <code>deny</code> """
        return self._props["action"]

class IPPolicyList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPPolicyList {}>".format(self.id)

    def __iter__(self):
        return (IPPolicy(o) for o in self._props["ip_policies"])
    
    @property
    def ip_policies(self):
        """ the list of all IP policies on this account """
        return self._props["ip_policies"]
    
    @property
    def uri(self):
        """ URI of the IP policy list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class IPPolicyRuleCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPPolicyRuleCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of the source IPs of this IP rule. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP policy rule. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def cidr(self):
        """ an IP or IP range specified in CIDR notation. IPv4 and IPv6 are both supported. """
        return self._props["cidr"]
    
    @property
    def ip_policy_id(self):
        """ ID of the IP policy this IP policy rule will be attached to """
        return self._props["ip_policy_id"]

class IPPolicyRuleUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPPolicyRuleUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of the source IPs of this IP rule. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP policy rule. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def cidr(self):
        """ an IP or IP range specified in CIDR notation. IPv4 and IPv6 are both supported. """
        return self._props["cidr"]

class IPPolicyRule(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPPolicyRule {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this IP policy rule """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the IP policy rule API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the IP policy rule was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of the source IPs of this IP rule. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP policy rule. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def cidr(self):
        """ an IP or IP range specified in CIDR notation. IPv4 and IPv6 are both supported. """
        return self._props["cidr"]
    
    @property
    def ip_policy(self):
        """ object describing the IP policy this IP Policy Rule belongs to """
        return self._props["ip_policy"]

class IPPolicyRuleList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPPolicyRuleList {}>".format(self.id)

    def __iter__(self):
        return (IPPolicyRule(o) for o in self._props["ip_policy_rules"])
    
    @property
    def ip_policy_rules(self):
        """ the list of all IP policy rules on this account """
        return self._props["ip_policy_rules"]
    
    @property
    def uri(self):
        """ URI of the IP policy rule list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class IPRestrictionCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPRestrictionCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of this IP restriction. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP restriction. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def enforced(self):
        """ true if the IP restriction will be enforce. if false, only warnings will be issued """
        return self._props["enforced"]
    
    @property
    def type(self):
        """ the type of IP restriction. this defines what traffic will be restricted with the attached policies. four values are currently supported: <code>dashboard</code>, <code>api</code>, <code>agent</code>, and <code>endpoints</code> """
        return self._props["type"]
    
    @property
    def ip_policy_ids(self):
        """ the set of IP policy identifiers that are used to enforce the restriction """
        return self._props["ip_policy_ids"]

class IPRestrictionUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPRestrictionUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of this IP restriction. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP restriction. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def enforced(self):
        """ true if the IP restriction will be enforce. if false, only warnings will be issued """
        return self._props["enforced"]
    
    @property
    def ip_policy_ids(self):
        """ the set of IP policy identifiers that are used to enforce the restriction """
        return self._props["ip_policy_ids"]

class IPRestriction(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPRestriction {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this IP restriction """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the IP restriction API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the IP restriction was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of this IP restriction. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP restriction. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def enforced(self):
        """ true if the IP restriction will be enforce. if false, only warnings will be issued """
        return self._props["enforced"]
    
    @property
    def type(self):
        """ the type of IP restriction. this defines what traffic will be restricted with the attached policies. four values are currently supported: <code>dashboard</code>, <code>api</code>, <code>agent</code>, and <code>endpoints</code> """
        return self._props["type"]
    
    @property
    def ip_policies(self):
        """ the set of IP policies that are used to enforce the restriction """
        return self._props["ip_policies"]

class IPRestrictionList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPRestrictionList {}>".format(self.id)

    def __iter__(self):
        return (IPRestriction(o) for o in self._props["ip_restrictions"])
    
    @property
    def ip_restrictions(self):
        """ the list of all IP restrictions on this account """
        return self._props["ip_restrictions"]
    
    @property
    def uri(self):
        """ URI of the IP resrtrictions list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class IPWhitelistEntryCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPWhitelistEntryCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of the source IPs for this IP whitelist entry. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP whitelist entry. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def ip_net(self):
        """ an IP address or IP network range in CIDR notation (e.g. 10.1.1.1 or 10.1.0.0/16) of addresses that will be whitelisted to communicate with your tunnel endpoints """
        return self._props["ip_net"]

class IPWhitelistEntryUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPWhitelistEntryUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of the source IPs for this IP whitelist entry. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP whitelist entry. optional, max 4096 bytes. """
        return self._props["metadata"]

class IPWhitelistEntry(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPWhitelistEntry {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this IP whitelist entry """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the IP whitelist entry API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the IP whitelist entry was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of the source IPs for this IP whitelist entry. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this IP whitelist entry. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def ip_net(self):
        """ an IP address or IP network range in CIDR notation (e.g. 10.1.1.1 or 10.1.0.0/16) of addresses that will be whitelisted to communicate with your tunnel endpoints """
        return self._props["ip_net"]

class IPWhitelistEntryList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<IPWhitelistEntryList {}>".format(self.id)

    def __iter__(self):
        return (IPWhitelistEntry(o) for o in self._props["whitelist"])
    
    @property
    def whitelist(self):
        """ the list of all IP whitelist entries on this account """
        return self._props["whitelist"]
    
    @property
    def uri(self):
        """ URI of the IP whitelist API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class EndpointConfiguration(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointConfiguration {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier of this endpoint configuration """
        return self._props["id"]
    
    @property
    def type(self):
        """ they type of traffic this endpoint configuration can be applied to. one of: <code>http</code>, <code>https</code>, <code>tcp</code> """
        return self._props["type"]
    
    @property
    def description(self):
        """ human-readable description of what this endpoint configuration will be do when applied or what traffic it will be applied to. Optional, max 255 bytes """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this endpoint configuration. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def created_at(self):
        """ timestamp when the endpoint configuration was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def uri(self):
        """ URI of the endpoint configuration API resource """
        return self._props["uri"]
    
    @property
    def basic_auth(self):
        """ basic auth module configuration or <code>null</code> """
        return self._props["basic_auth"]
    
    @property
    def circuit_breaker(self):
        """ circuit breaker module configuration or <code>null</code> """
        return self._props["circuit_breaker"]
    
    @property
    def compression(self):
        """ compression module configuration or <code>null</code> """
        return self._props["compression"]
    
    @property
    def request_headers(self):
        """ request headers module configuration or <code>null</code> """
        return self._props["request_headers"]
    
    @property
    def response_headers(self):
        """ response headers module configuration or <code>null</code> """
        return self._props["response_headers"]
    
    @property
    def ip_policy(self):
        """ ip policy module configuration or <code>null</code> """
        return self._props["ip_policy"]
    
    @property
    def mutual_tls(self):
        """ mutual TLS module configuration or <code>null</code> """
        return self._props["mutual_tls"]
    
    @property
    def tls_termination(self):
        """ TLS termination module configuration or <code>null</code> """
        return self._props["tls_termination"]
    
    @property
    def webhook_validation(self):
        """ webhook validation module configuration or <code>null</code> """
        return self._props["webhook_validation"]
    
    @property
    def oauth(self):
        """ oauth module configuration or <code>null</code> """
        return self._props["oauth"]
    
    @property
    def logging(self):
        """ logging module configuration or <code>null</code> """
        return self._props["logging"]
    
    @property
    def saml(self):
        """ saml module configuration or <code>null</code> """
        return self._props["saml"]
    
    @property
    def oidc(self):
        """ oidc module configuration or <code>null</code> """
        return self._props["oidc"]
    
    @property
    def backend(self):
        """ backend module configuration or <code>null</code> """
        return self._props["backend"]

class EndpointConfigurationList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointConfigurationList {}>".format(self.id)

    def __iter__(self):
        return (EndpointConfiguration(o) for o in self._props["endpoint_configurations"])
    
    @property
    def endpoint_configurations(self):
        """ the list of all endpoint configurations on this account """
        return self._props["endpoint_configurations"]
    
    @property
    def uri(self):
        """ URI of the endpoint configurations list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class EndpointConfigurationUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointConfigurationUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier of this endpoint configuration """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of what this endpoint configuration will be do when applied or what traffic it will be applied to. Optional, max 255 bytes """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this endpoint configuration. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def basic_auth(self):
        """ basic auth module configuration or <code>null</code> """
        return self._props["basic_auth"]
    
    @property
    def circuit_breaker(self):
        """ circuit breaker module configuration or <code>null</code> """
        return self._props["circuit_breaker"]
    
    @property
    def compression(self):
        """ compression module configuration or <code>null</code> """
        return self._props["compression"]
    
    @property
    def request_headers(self):
        """ request headers module configuration or <code>null</code> """
        return self._props["request_headers"]
    
    @property
    def response_headers(self):
        """ response headers module configuration or <code>null</code> """
        return self._props["response_headers"]
    
    @property
    def ip_policy(self):
        """ ip policy module configuration or <code>null</code> """
        return self._props["ip_policy"]
    
    @property
    def mutual_tls(self):
        """ mutual TLS module configuration or <code>null</code> """
        return self._props["mutual_tls"]
    
    @property
    def tls_termination(self):
        """ TLS termination module configuration or <code>null</code> """
        return self._props["tls_termination"]
    
    @property
    def webhook_validation(self):
        """ webhook validation module configuration or <code>null</code> """
        return self._props["webhook_validation"]
    
    @property
    def oauth(self):
        """ oauth module configuration or <code>null</code> """
        return self._props["oauth"]
    
    @property
    def logging(self):
        """ logging module configuration or <code>null</code> """
        return self._props["logging"]
    
    @property
    def saml(self):
        """ saml module configuration or <code>null</code> """
        return self._props["saml"]
    
    @property
    def oidc(self):
        """ oidc module configuration or <code>null</code> """
        return self._props["oidc"]
    
    @property
    def backend(self):
        """ backend module configuration or <code>null</code> """
        return self._props["backend"]

class EndpointConfigurationCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointConfigurationCreate {}>".format(self.id)

    
    
    @property
    def type(self):
        """ they type of traffic this endpoint configuration can be applied to. one of: <code>http</code>, <code>https</code>, <code>tcp</code> """
        return self._props["type"]
    
    @property
    def description(self):
        """ human-readable description of what this endpoint configuration will be do when applied or what traffic it will be applied to. Optional, max 255 bytes """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this endpoint configuration. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def basic_auth(self):
        """ basic auth module configuration or <code>null</code> """
        return self._props["basic_auth"]
    
    @property
    def circuit_breaker(self):
        """ circuit breaker module configuration or <code>null</code> """
        return self._props["circuit_breaker"]
    
    @property
    def compression(self):
        """ compression module configuration or <code>null</code> """
        return self._props["compression"]
    
    @property
    def request_headers(self):
        """ request headers module configuration or <code>null</code> """
        return self._props["request_headers"]
    
    @property
    def response_headers(self):
        """ response headers module configuration or <code>null</code> """
        return self._props["response_headers"]
    
    @property
    def ip_policy(self):
        """ ip policy module configuration or <code>null</code> """
        return self._props["ip_policy"]
    
    @property
    def mutual_tls(self):
        """ mutual TLS module configuration or <code>null</code> """
        return self._props["mutual_tls"]
    
    @property
    def tls_termination(self):
        """ TLS termination module configuration or <code>null</code> """
        return self._props["tls_termination"]
    
    @property
    def webhook_validation(self):
        """ webhook validation module configuration or <code>null</code> """
        return self._props["webhook_validation"]
    
    @property
    def oauth(self):
        """ oauth module configuration or <code>null</code> """
        return self._props["oauth"]
    
    @property
    def logging(self):
        """ logging module configuration or <code>null</code> """
        return self._props["logging"]
    
    @property
    def saml(self):
        """ saml module configuration or <code>null</code> """
        return self._props["saml"]
    
    @property
    def oidc(self):
        """ oidc module configuration or <code>null</code> """
        return self._props["oidc"]
    
    @property
    def backend(self):
        """ backend module configuration or <code>null</code> """
        return self._props["backend"]

class EndpointWebhookValidation(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointWebhookValidation {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def provider(self):
        """ a string indicating which webhook provider will be sending webhooks to this endpoint. Value must be one of the supported providers: <code>SLACK</code>, <code>SNS</code>, <code>STRIPE</code>, <code>GITHUB</code>, <code>TWILIO</code>, <code>SHOPIFY</code>, <code>GITLAB</code>, <code>INTERCOM</code>. """
        return self._props["provider"]
    
    @property
    def secret(self):
        """ a string secret used to validate requests from the given provider. All providers except AWS SNS require a secret """
        return self._props["secret"]

class EndpointCompression(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointCompression {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]

class EndpointMutualTLS(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointMutualTLS {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def certificate_authorities(self):
        """ PEM-encoded CA certificates that will be used to validate. Multiple CAs may be provided by concatenating them together. """
        return self._props["certificate_authorities"]

class EndpointMutualTLSMutate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointMutualTLSMutate {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def certificate_authority_ids(self):
        """ list of certificate authorities that will be used to validate the TLS client certificate presnted by the initiatiator of the TLS connection """
        return self._props["certificate_authority_ids"]

class EndpointTLSTermination(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointTLSTermination {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def terminate_at(self):
        """ <code>edge</code> if the ngrok edge should terminate TLS traffic, <code>upstream</code> if TLS traffic should be passed through to the upstream ngrok agent / application server for termination. if <code>upstream</code> is chosen, most other modules will be disallowed because they rely on the ngrok edge being able to access the underlying traffic. """
        return self._props["terminate_at"]
    
    @property
    def min_version(self):
        """ The minimum TLS version used for termination and advertised to the client during the TLS handshake. if unspecified, ngrok will choose an industry-safe default. This value must be null if <code>terminate_at</code> is set to <code>upstream</code>. """
        return self._props["min_version"]

class EndpointBasicAuth(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointBasicAuth {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def auth_provider_id(self):
        """ determines how the basic auth credentials are validated. Currently only the value <code>agent</code> is supported which means that credentials will be validated against the username and password specified by the ngrok agent's <code>-auth</code> flag, if any. """
        return self._props["auth_provider_id"]
    
    @property
    def realm(self):
        """ an arbitrary string to be specified in as the 'realm' value in the <code>WWW-Authenticate</code> header. default is <code>ngrok</code> """
        return self._props["realm"]
    
    @property
    def allow_options(self):
        """ true or false indicating whether to allow OPTIONS requests through without authentication which is necessary for CORS. default is <code>false</code> """
        return self._props["allow_options"]

class EndpointLogging(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointLogging {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def event_streams(self):
        """ list of all EventStreams that will be used to configure and export this endpoint's logs """
        return self._props["event_streams"]

class EndpointLoggingMutate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointLoggingMutate {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def event_stream_ids(self):
        """ list of all EventStreams that will be used to configure and export this endpoint's logs """
        return self._props["event_stream_ids"]

class EndpointRequestHeaders(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointRequestHeaders {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def add(self):
        """ a map of header key to header value that will be injected into the HTTP Request before being sent to the upstream application server """
        return self._props["add"]
    
    @property
    def remove(self):
        """ a list of header names that will be removed from the HTTP Request before being sent to the upstream application server """
        return self._props["remove"]

class EndpointResponseHeaders(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointResponseHeaders {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def add(self):
        """ a map of header key to header value that will be injected into the HTTP Response returned to the HTTP client """
        return self._props["add"]
    
    @property
    def remove(self):
        """ a list of header names that will be removed from the HTTP Response returned to the HTTP client """
        return self._props["remove"]

class EndpointIPPolicy(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointIPPolicy {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def ip_policies(self):
        """  """
        return self._props["ip_policies"]

class EndpointIPPolicyMutate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointIPPolicyMutate {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def ip_policy_ids(self):
        """ list of all IP policies that will be used to check if a source IP is allowed access to the endpoint """
        return self._props["ip_policy_ids"]

class EndpointCircuitBreaker(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointCircuitBreaker {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def tripped_duration(self):
        """ Integer number of seconds after which the circuit is tripped to wait before re-evaluating upstream health """
        return self._props["tripped_duration"]
    
    @property
    def rolling_window(self):
        """ Integer number of seconds in the statistical rolling window that metrics are retained for. """
        return self._props["rolling_window"]
    
    @property
    def num_buckets(self):
        """ Integer number of buckets into which metrics are retained. Max 128. """
        return self._props["num_buckets"]
    
    @property
    def volume_threshold(self):
        """ Integer number of requests in a rolling window that will trip the circuit. Helpful if traffic volume is low. """
        return self._props["volume_threshold"]
    
    @property
    def error_threshold_percentage(self):
        """ Error threshold percentage should be between 0 - 1.0, not 0-100.0 """
        return self._props["error_threshold_percentage"]

class EndpointOAuth(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointOAuth {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def provider(self):
        """ an object which defines the identity provider to use for authentication and configuration for who may access the endpoint """
        return self._props["provider"]
    
    @property
    def options_passthrough(self):
        """ Do not enforce authentication on HTTP OPTIONS requests. necessary if you are supporting CORS. """
        return self._props["options_passthrough"]
    
    @property
    def cookie_prefix(self):
        """ the prefix of the session cookie that ngrok sets on the http client to cache authentication. default is 'ngrok.' """
        return self._props["cookie_prefix"]
    
    @property
    def inactivity_timeout(self):
        """ Integer number of seconds of inactivity after which if the user has not accessed the endpoint, their session will time out and they will be forced to reauthenticate. """
        return self._props["inactivity_timeout"]
    
    @property
    def maximum_duration(self):
        """ Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate. """
        return self._props["maximum_duration"]
    
    @property
    def auth_check_interval(self):
        """ Integer number of seconds after which ngrok guarantees it will refresh user state from the identity provider and recheck whether the user is still authorized to access the endpoint. This is the preferred tunable to use to enforce a minimum amount of time after which a revoked user will no longer be able to access the resource. """
        return self._props["auth_check_interval"]

class EndpointOAuthProvider(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointOAuthProvider {}>".format(self.id)

    
    
    @property
    def github(self):
        """ configuration for using github as the identity provider """
        return self._props["github"]
    
    @property
    def facebook(self):
        """ configuration for using facebook as the identity provider """
        return self._props["facebook"]
    
    @property
    def microsoft(self):
        """ configuration for using microsoft as the identity provider """
        return self._props["microsoft"]
    
    @property
    def google(self):
        """ configuration for using google as the identity provider """
        return self._props["google"]

class EndpointOAuthGitHub(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointOAuthGitHub {}>".format(self.id)

    
    
    @property
    def client_id(self):
        """ the OAuth app client ID. retrieve it from the identity provider's dashboard where you created your own OAuth app. optional. if unspecified, ngrok will use its own managed oauth application which has additional restrictions. see the OAuth module docs for more details. if present, client_secret must be present as well. """
        return self._props["client_id"]
    
    @property
    def client_secret(self):
        """ the OAuth app client secret. retrieve if from the identity provider's dashboard where you created your own OAuth app. optional, see all of the caveats in the docs for <code>client_id</code>. """
        return self._props["client_secret"]
    
    @property
    def scopes(self):
        """ a list of provider-specific OAuth scopes with the permissions your OAuth app would like to ask for. these may not be set if you are using the ngrok-managed oauth app (i.e. you must pass both <code>client_id</code> and <code>client_secret</code> to set scopes) """
        return self._props["scopes"]
    
    @property
    def email_addresses(self):
        """ a list of email addresses of users authenticated by identity provider who are allowed access to the endpoint """
        return self._props["email_addresses"]
    
    @property
    def email_domains(self):
        """ a list of email domains of users authenticated by identity provider who are allowed access to the endpoint """
        return self._props["email_domains"]
    
    @property
    def teams(self):
        """ a list of github teams identifiers. users will be allowed access to the endpoint if they are a member of any of these teams. identifiers should be in the 'slug' format qualified with the org name, e.g. <code>org-name/team-name</code> """
        return self._props["teams"]
    
    @property
    def organizations(self):
        """ a list of github org identifiers. users who are members of any of the listed organizations will be allowed access. identifiers should be the organization's 'slug' """
        return self._props["organizations"]

class EndpointOAuthFacebook(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointOAuthFacebook {}>".format(self.id)

    
    
    @property
    def client_id(self):
        """ the OAuth app client ID. retrieve it from the identity provider's dashboard where you created your own OAuth app. optional. if unspecified, ngrok will use its own managed oauth application which has additional restrictions. see the OAuth module docs for more details. if present, client_secret must be present as well. """
        return self._props["client_id"]
    
    @property
    def client_secret(self):
        """ the OAuth app client secret. retrieve if from the identity provider's dashboard where you created your own OAuth app. optional, see all of the caveats in the docs for <code>client_id</code>. """
        return self._props["client_secret"]
    
    @property
    def scopes(self):
        """ a list of provider-specific OAuth scopes with the permissions your OAuth app would like to ask for. these may not be set if you are using the ngrok-managed oauth app (i.e. you must pass both <code>client_id</code> and <code>client_secret</code> to set scopes) """
        return self._props["scopes"]
    
    @property
    def email_addresses(self):
        """ a list of email addresses of users authenticated by identity provider who are allowed access to the endpoint """
        return self._props["email_addresses"]
    
    @property
    def email_domains(self):
        """ a list of email domains of users authenticated by identity provider who are allowed access to the endpoint """
        return self._props["email_domains"]

class EndpointOAuthMicrosoft(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointOAuthMicrosoft {}>".format(self.id)

    
    
    @property
    def client_id(self):
        """ the OAuth app client ID. retrieve it from the identity provider's dashboard where you created your own OAuth app. optional. if unspecified, ngrok will use its own managed oauth application which has additional restrictions. see the OAuth module docs for more details. if present, client_secret must be present as well. """
        return self._props["client_id"]
    
    @property
    def client_secret(self):
        """ the OAuth app client secret. retrieve if from the identity provider's dashboard where you created your own OAuth app. optional, see all of the caveats in the docs for <code>client_id</code>. """
        return self._props["client_secret"]
    
    @property
    def scopes(self):
        """ a list of provider-specific OAuth scopes with the permissions your OAuth app would like to ask for. these may not be set if you are using the ngrok-managed oauth app (i.e. you must pass both <code>client_id</code> and <code>client_secret</code> to set scopes) """
        return self._props["scopes"]
    
    @property
    def email_addresses(self):
        """ a list of email addresses of users authenticated by identity provider who are allowed access to the endpoint """
        return self._props["email_addresses"]
    
    @property
    def email_domains(self):
        """ a list of email domains of users authenticated by identity provider who are allowed access to the endpoint """
        return self._props["email_domains"]

class EndpointOAuthGoogle(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointOAuthGoogle {}>".format(self.id)

    
    
    @property
    def client_id(self):
        """ the OAuth app client ID. retrieve it from the identity provider's dashboard where you created your own OAuth app. optional. if unspecified, ngrok will use its own managed oauth application which has additional restrictions. see the OAuth module docs for more details. if present, client_secret must be present as well. """
        return self._props["client_id"]
    
    @property
    def client_secret(self):
        """ the OAuth app client secret. retrieve if from the identity provider's dashboard where you created your own OAuth app. optional, see all of the caveats in the docs for <code>client_id</code>. """
        return self._props["client_secret"]
    
    @property
    def scopes(self):
        """ a list of provider-specific OAuth scopes with the permissions your OAuth app would like to ask for. these may not be set if you are using the ngrok-managed oauth app (i.e. you must pass both <code>client_id</code> and <code>client_secret</code> to set scopes) """
        return self._props["scopes"]
    
    @property
    def email_addresses(self):
        """ a list of email addresses of users authenticated by identity provider who are allowed access to the endpoint """
        return self._props["email_addresses"]
    
    @property
    def email_domains(self):
        """ a list of email domains of users authenticated by identity provider who are allowed access to the endpoint """
        return self._props["email_domains"]

class EndpointSAML(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointSAML {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def options_passthrough(self):
        """ Do not enforce authentication on HTTP OPTIONS requests. necessary if you are supporting CORS. """
        return self._props["options_passthrough"]
    
    @property
    def cookie_prefix(self):
        """ the prefix of the session cookie that ngrok sets on the http client to cache authentication. default is 'ngrok.' """
        return self._props["cookie_prefix"]
    
    @property
    def inactivity_timeout(self):
        """ Integer number of seconds of inactivity after which if the user has not accessed the endpoint, their session will time out and they will be forced to reauthenticate. """
        return self._props["inactivity_timeout"]
    
    @property
    def maximum_duration(self):
        """ Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate. """
        return self._props["maximum_duration"]
    
    @property
    def idp_metadata_url(self):
        """ The IdP's metadata URL which returns the XML IdP EntityDescriptor. The IdP's metadata URL specifies how to connect to the IdP as well as its public key which is then used to validate the signature on incoming SAML assertions to the ACS endpoint. """
        return self._props["idp_metadata_url"]
    
    @property
    def idp_metadata(self):
        """ The full XML IdP EntityDescriptor. Your IdP may provide this to you as a a file to download or as a URL. """
        return self._props["idp_metadata"]
    
    @property
    def force_authn(self):
        """ If true, indicates that whenever we redirect a user to the IdP for authentication that the IdP must prompt the user for authentication credentials even if the user already has a valid session with the IdP. """
        return self._props["force_authn"]
    
    @property
    def allow_idp_initiated(self):
        """ If true, the IdP may initiate a login directly (e.g. the user does not need to visit the endpoint first and then be redirected). The IdP should set the <code>RelayState</code> parameter to the target URL of the resource they want the user to be redirected to after the SAML login assertion has been processed. """
        return self._props["allow_idp_initiated"]
    
    @property
    def authorized_groups(self):
        """ If present, only users who are a member of one of the listed groups may access the target endpoint. """
        return self._props["authorized_groups"]
    
    @property
    def entity_id(self):
        """ The SP Entity's unique ID. This always takes the form of a URL. In ngrok's implementation, this URL is the same as the metadata URL. This will need to be specified to the IdP as configuration. """
        return self._props["entity_id"]
    
    @property
    def assertion_consumer_service_url(self):
        """ The public URL of the SP's Assertion Consumer Service. This is where the IdP will redirect to during an authentication flow. This will need to be specified to the IdP as configuration. """
        return self._props["assertion_consumer_service_url"]
    
    @property
    def single_logout_url(self):
        """ The public URL of the SP's Single Logout Service. This is where the IdP will redirect to during a single logout flow. This will optionally need to be specified to the IdP as configuration. """
        return self._props["single_logout_url"]
    
    @property
    def request_signing_certificate_pem(self):
        """ PEM-encoded x.509 certificate of the key pair that is used to sign all SAML requests that the ngrok SP makes to the IdP. Many IdPs do not support request signing verification, but we highly recommend specifying this in the IdP's configuration if it is supported. """
        return self._props["request_signing_certificate_pem"]
    
    @property
    def metadata_url(self):
        """ A public URL where the SP's metadata is hosted. If an IdP supports dynamic configuration, this is the URL it can use to retrieve the SP metadata. """
        return self._props["metadata_url"]

class EndpointSAMLMutate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointSAMLMutate {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def options_passthrough(self):
        """ Do not enforce authentication on HTTP OPTIONS requests. necessary if you are supporting CORS. """
        return self._props["options_passthrough"]
    
    @property
    def cookie_prefix(self):
        """ the prefix of the session cookie that ngrok sets on the http client to cache authentication. default is 'ngrok.' """
        return self._props["cookie_prefix"]
    
    @property
    def inactivity_timeout(self):
        """ Integer number of seconds of inactivity after which if the user has not accessed the endpoint, their session will time out and they will be forced to reauthenticate. """
        return self._props["inactivity_timeout"]
    
    @property
    def maximum_duration(self):
        """ Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate. """
        return self._props["maximum_duration"]
    
    @property
    def idp_metadata_url(self):
        """ The IdP's metadata URL which returns the XML IdP EntityDescriptor. The IdP's metadata URL specifies how to connect to the IdP as well as its public key which is then used to validate the signature on incoming SAML assertions to the ACS endpoint. """
        return self._props["idp_metadata_url"]
    
    @property
    def idp_metadata(self):
        """ The full XML IdP EntityDescriptor. Your IdP may provide this to you as a a file to download or as a URL. """
        return self._props["idp_metadata"]
    
    @property
    def force_authn(self):
        """ If true, indicates that whenever we redirect a user to the IdP for authentication that the IdP must prompt the user for authentication credentials even if the user already has a valid session with the IdP. """
        return self._props["force_authn"]
    
    @property
    def allow_idp_initiated(self):
        """ If true, the IdP may initiate a login directly (e.g. the user does not need to visit the endpoint first and then be redirected). The IdP should set the <code>RelayState</code> parameter to the target URL of the resource they want the user to be redirected to after the SAML login assertion has been processed. """
        return self._props["allow_idp_initiated"]
    
    @property
    def authorized_groups(self):
        """ If present, only users who are a member of one of the listed groups may access the target endpoint. """
        return self._props["authorized_groups"]

class EndpointOIDC(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointOIDC {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def options_passthrough(self):
        """ Do not enforce authentication on HTTP OPTIONS requests. necessary if you are supporting CORS. """
        return self._props["options_passthrough"]
    
    @property
    def cookie_prefix(self):
        """ the prefix of the session cookie that ngrok sets on the http client to cache authentication. default is 'ngrok.' """
        return self._props["cookie_prefix"]
    
    @property
    def inactivity_timeout(self):
        """ Integer number of seconds of inactivity after which if the user has not accessed the endpoint, their session will time out and they will be forced to reauthenticate. """
        return self._props["inactivity_timeout"]
    
    @property
    def maximum_duration(self):
        """ Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate. """
        return self._props["maximum_duration"]
    
    @property
    def issuer(self):
        """ URL of the OIDC "OpenID provider". This is the base URL used for discovery. """
        return self._props["issuer"]
    
    @property
    def client_id(self):
        """ The OIDC app's client ID and OIDC audience. """
        return self._props["client_id"]
    
    @property
    def client_secret(self):
        """ The OIDC app's client secret. """
        return self._props["client_secret"]
    
    @property
    def scopes(self):
        """ The set of scopes to request from the OIDC identity provider. """
        return self._props["scopes"]

class EndpointBackend(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointBackend {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def backend(self):
        """ backend to be used to back this endpoint """
        return self._props["backend"]

class EndpointBackendMutate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointBackendMutate {}>".format(self.id)

    
    
    @property
    def enabled(self):
        """ <code>true</code> if the module will be applied to traffic, <code>false</code> to disable. default <code>true</code> if unspecified """
        return self._props["enabled"]
    
    @property
    def backend_id(self):
        """ backend to be used to back this endpoint """
        return self._props["backend_id"]

class EndpointLoggingReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointLoggingReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointBasicAuthReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointBasicAuthReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointCircuitBreakerReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointCircuitBreakerReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointCompressionReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointCompressionReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointTLSTerminationReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointTLSTerminationReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointIPPolicyReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointIPPolicyReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointMutualTLSReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointMutualTLSReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointRequestHeadersReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointRequestHeadersReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointResponseHeadersReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointResponseHeadersReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointOAuthReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointOAuthReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointWebhookValidationReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointWebhookValidationReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointSAMLReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointSAMLReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointOIDCReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointOIDCReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class EndpointBackendReplace(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<EndpointBackendReplace {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def module(self):
        """  """
        return self._props["module"]

class ReservedAddrCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedAddrCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of what this reserved address will be used for """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this reserved address. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def region(self):
        """ reserve the address in this geographic ngrok datacenter. Optional, default is us. (au, eu, ap, us, jp, in, sa) """
        return self._props["region"]
    
    @property
    def endpoint_configuration_id(self):
        """ ID of an endpoint configuration of type tcp that will be used to handle inbound traffic to this address """
        return self._props["endpoint_configuration_id"]

class ReservedAddrUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedAddrUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of what this reserved address will be used for """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this reserved address. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def endpoint_configuration_id(self):
        """ ID of an endpoint configuration of type tcp that will be used to handle inbound traffic to this address """
        return self._props["endpoint_configuration_id"]

class ReservedAddr(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedAddr {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique reserved address resource identifier """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the reserved address API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the reserved address was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of what this reserved address will be used for """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this reserved address. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def addr(self):
        """ hostname:port of the reserved address that was assigned at creation time """
        return self._props["addr"]
    
    @property
    def region(self):
        """ reserve the address in this geographic ngrok datacenter. Optional, default is us. (au, eu, ap, us, jp, in, sa) """
        return self._props["region"]
    
    @property
    def endpoint_configuration(self):
        """ object reference to the endpoint configuration that will be applied to traffic to this address """
        return self._props["endpoint_configuration"]

class ReservedAddrList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedAddrList {}>".format(self.id)

    def __iter__(self):
        return (ReservedAddr(o) for o in self._props["reserved_addrs"])
    
    @property
    def reserved_addrs(self):
        """ the list of all reserved addresses on this account """
        return self._props["reserved_addrs"]
    
    @property
    def uri(self):
        """ URI of the reserved address list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class ReservedDomainCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedDomainCreate {}>".format(self.id)

    
    
    @property
    def name(self):
        """ the domain name to reserve. It may be a full domain name like app.example.com. If the name does not contain a '.' it will reserve that subdomain on ngrok.io. """
        return self._props["name"]
    
    @property
    def region(self):
        """ reserve the domain in this geographic ngrok datacenter. Optional, default is us. (au, eu, ap, us, jp, in, sa) """
        return self._props["region"]
    
    @property
    def description(self):
        """ human-readable description of what this reserved domain will be used for """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this reserved domain. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def http_endpoint_configuration_id(self):
        """ ID of an endpoint configuration of type http that will be used to handle inbound http traffic to this domain """
        return self._props["http_endpoint_configuration_id"]
    
    @property
    def https_endpoint_configuration_id(self):
        """ ID of an endpoint configuration of type https that will be used to handle inbound https traffic to this domain """
        return self._props["https_endpoint_configuration_id"]
    
    @property
    def certificate_id(self):
        """ ID of a user-uploaded TLS certificate to use for connections to targeting this domain. Optional, mutually exclusive with `certificate_management_policy`. """
        return self._props["certificate_id"]
    
    @property
    def certificate_management_policy(self):
        """ configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled. Optional, mutually exclusive with `certificate_id`. """
        return self._props["certificate_management_policy"]

class ReservedDomainUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedDomainUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of what this reserved domain will be used for """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this reserved domain. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def http_endpoint_configuration_id(self):
        """ ID of an endpoint configuration of type http that will be used to handle inbound http traffic to this domain """
        return self._props["http_endpoint_configuration_id"]
    
    @property
    def https_endpoint_configuration_id(self):
        """ ID of an endpoint configuration of type https that will be used to handle inbound https traffic to this domain """
        return self._props["https_endpoint_configuration_id"]
    
    @property
    def certificate_id(self):
        """ ID of a user-uploaded TLS certificate to use for connections to targeting this domain. Optional, mutually exclusive with `certificate_management_policy`. """
        return self._props["certificate_id"]
    
    @property
    def certificate_management_policy(self):
        """ configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled. Optional, mutually exclusive with `certificate_id`. """
        return self._props["certificate_management_policy"]

class ReservedDomain(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedDomain {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique reserved domain resource identifier """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the reserved domain API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the reserved domain was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of what this reserved domain will be used for """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this reserved domain. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def domain(self):
        """ hostname of the reserved domain """
        return self._props["domain"]
    
    @property
    def region(self):
        """ reserve the domain in this geographic ngrok datacenter. Optional, default is us. (au, eu, ap, us, jp, in, sa) """
        return self._props["region"]
    
    @property
    def cname_target(self):
        """ DNS CNAME target for a custom hostname, or null if the reserved domain is a subdomain of *.ngrok.io """
        return self._props["cname_target"]
    
    @property
    def http_endpoint_configuration(self):
        """ object referencing the endpoint configuration applied to http traffic on this domain """
        return self._props["http_endpoint_configuration"]
    
    @property
    def https_endpoint_configuration(self):
        """ object referencing the endpoint configuration applied to https traffic on this domain """
        return self._props["https_endpoint_configuration"]
    
    @property
    def certificate(self):
        """ object referencing the TLS certificate used for connections to this domain. This can be either a user-uploaded certificate, the most recently issued automatic one, or null otherwise. """
        return self._props["certificate"]
    
    @property
    def certificate_management_policy(self):
        """ configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled """
        return self._props["certificate_management_policy"]
    
    @property
    def certificate_management_status(self):
        """ status of the automatic certificate management for this domain, or null if automatic management is disabled """
        return self._props["certificate_management_status"]

class ReservedDomainList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedDomainList {}>".format(self.id)

    def __iter__(self):
        return (ReservedDomain(o) for o in self._props["reserved_domains"])
    
    @property
    def reserved_domains(self):
        """ the list of all reserved domains on this account """
        return self._props["reserved_domains"]
    
    @property
    def uri(self):
        """ URI of the reserved domain list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class ReservedDomainCertPolicy(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedDomainCertPolicy {}>".format(self.id)

    
    
    @property
    def authority(self):
        """ certificate authority to request certificates from. The only supported value is letsencrypt. """
        return self._props["authority"]
    
    @property
    def private_key_type(self):
        """ type of private key to use when requesting certificates. Defaults to rsa, can be either rsa or ecdsa. """
        return self._props["private_key_type"]

class ReservedDomainCertStatus(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedDomainCertStatus {}>".format(self.id)

    
    
    @property
    def renews_at(self):
        """ timestamp when the next renewal will be requested, RFC 3339 format """
        return self._props["renews_at"]
    
    @property
    def provisioning_job(self):
        """ status of the certificate provisioning job, or null if the certificiate isn't being provisioned or renewed """
        return self._props["provisioning_job"]

class ReservedDomainCertNSTarget(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedDomainCertNSTarget {}>".format(self.id)

    
    
    @property
    def zone(self):
        """ the zone that the nameservers need to be applied to """
        return self._props["zone"]
    
    @property
    def nameservers(self):
        """ the nameservers the user must add """
        return self._props["nameservers"]

class ReservedDomainCertJob(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<ReservedDomainCertJob {}>".format(self.id)

    
    
    @property
    def error_code(self):
        """ if present, an error code indicating why provisioning is failing. It may be either a temporary condition (INTERNAL_ERROR), or a permanent one the user must correct (DNS_ERROR). """
        return self._props["error_code"]
    
    @property
    def msg(self):
        """ a message describing the current status or error """
        return self._props["msg"]
    
    @property
    def started_at(self):
        """ timestamp when the provisioning job started, RFC 3339 format """
        return self._props["started_at"]
    
    @property
    def retries_at(self):
        """ timestamp when the provisioning job will be retried """
        return self._props["retries_at"]
    
    @property
    def ns_targets(self):
        """ if present, indicates the dns nameservers that the user must configure to complete the provisioning process of a wildcard certificate """
        return self._props["ns_targets"]

class RootResponse(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<RootResponse {}>".format(self.id)

    
    
    @property
    def uri(self):
        """  """
        return self._props["uri"]
    
    @property
    def subresource_uris(self):
        """  """
        return self._props["subresource_uris"]

class SSHCertificateAuthorityCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHCertificateAuthorityCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of this SSH Certificate Authority. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this SSH Certificate Authority. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def private_key_type(self):
        """ the type of private key to generate. one of <code>rsa</code>, <code>ecdsa</code>, <code>ed25519</code> """
        return self._props["private_key_type"]
    
    @property
    def elliptic_curve(self):
        """ the type of elliptic curve to use when creating an ECDSA key """
        return self._props["elliptic_curve"]
    
    @property
    def key_size(self):
        """ the key size to use when creating an RSA key. one of <code>2048</code> or <code>4096</code> """
        return self._props["key_size"]

class SSHCertificateAuthorityUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHCertificateAuthorityUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of this SSH Certificate Authority. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this SSH Certificate Authority. optional, max 4096 bytes. """
        return self._props["metadata"]

class SSHCertificateAuthority(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHCertificateAuthority {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this SSH Certificate Authority """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the SSH Certificate Authority API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the SSH Certificate Authority API resource was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of this SSH Certificate Authority. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this SSH Certificate Authority. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def public_key(self):
        """ raw public key for this SSH Certificate Authority """
        return self._props["public_key"]
    
    @property
    def key_type(self):
        """ the type of private key for this SSH Certificate Authority """
        return self._props["key_type"]

class SSHCertificateAuthorityList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHCertificateAuthorityList {}>".format(self.id)

    def __iter__(self):
        return (SSHCertificateAuthority(o) for o in self._props["ssh_certificate_authorities"])
    
    @property
    def ssh_certificate_authorities(self):
        """ the list of all certificate authorities on this account """
        return self._props["ssh_certificate_authorities"]
    
    @property
    def uri(self):
        """ URI of the certificates authorities list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class SSHCredentialCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHCredentialCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of who or what will use the ssh credential to authenticate. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this ssh credential. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def acl(self):
        """ optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the <code>bind</code> rule. The <code>bind</code> rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule <code>bind:example.ngrok.io</code>. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of <code>bind:*.example.com</code> which will allow <code>x.example.com</code>, <code>y.example.com</code>, <code>*.example.com</code>, etc. A rule of <code>'*'</code> is equivalent to no acl at all and will explicitly permit all actions. """
        return self._props["acl"]
    
    @property
    def public_key(self):
        """ the PEM-encoded public key of the SSH keypair that will be used to authenticate """
        return self._props["public_key"]

class SSHCredentialUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHCredentialUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of who or what will use the ssh credential to authenticate. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this ssh credential. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def acl(self):
        """ optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the <code>bind</code> rule. The <code>bind</code> rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule <code>bind:example.ngrok.io</code>. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of <code>bind:*.example.com</code> which will allow <code>x.example.com</code>, <code>y.example.com</code>, <code>*.example.com</code>, etc. A rule of <code>'*'</code> is equivalent to no acl at all and will explicitly permit all actions. """
        return self._props["acl"]

class SSHCredential(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHCredential {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique ssh credential resource identifier """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the ssh credential API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the ssh credential was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of who or what will use the ssh credential to authenticate. Optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this ssh credential. Optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def public_key(self):
        """ the PEM-encoded public key of the SSH keypair that will be used to authenticate """
        return self._props["public_key"]
    
    @property
    def acl(self):
        """ optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the <code>bind</code> rule. The <code>bind</code> rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule <code>bind:example.ngrok.io</code>. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of <code>bind:*.example.com</code> which will allow <code>x.example.com</code>, <code>y.example.com</code>, <code>*.example.com</code>, etc. A rule of <code>'*'</code> is equivalent to no acl at all and will explicitly permit all actions. """
        return self._props["acl"]

class SSHCredentialList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHCredentialList {}>".format(self.id)

    def __iter__(self):
        return (SSHCredential(o) for o in self._props["ssh_credentials"])
    
    @property
    def ssh_credentials(self):
        """ the list of all ssh credentials on this account """
        return self._props["ssh_credentials"]
    
    @property
    def uri(self):
        """ URI of the ssh credential list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class SSHHostCertificateCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHHostCertificateCreate {}>".format(self.id)

    
    
    @property
    def ssh_certificate_authority_id(self):
        """ the ssh certificate authority that is used to sign this ssh host certificate """
        return self._props["ssh_certificate_authority_id"]
    
    @property
    def public_key(self):
        """ a public key in OpenSSH Authorized Keys format that this certificate signs """
        return self._props["public_key"]
    
    @property
    def principals(self):
        """ the list of principals included in the ssh host certificate. This is the list of hostnames and/or IP addresses that are authorized to serve SSH traffic with this certificate. Dangerously, if no principals are specified, this certificate is considered valid for all hosts. """
        return self._props["principals"]
    
    @property
    def valid_after(self):
        """ The time when the host certificate becomes valid, in RFC 3339 format. Defaults to the current time if unspecified. """
        return self._props["valid_after"]
    
    @property
    def valid_until(self):
        """ The time when this host certificate becomes invalid, in RFC 3339 format. If unspecified, a default value of one year in the future will be used. The OpenSSH certificates RFC calls this <code>valid_before</code>. """
        return self._props["valid_until"]
    
    @property
    def description(self):
        """ human-readable description of this SSH Host Certificate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this SSH Host Certificate. optional, max 4096 bytes. """
        return self._props["metadata"]

class SSHHostCertificateUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHHostCertificateUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of this SSH Host Certificate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this SSH Host Certificate. optional, max 4096 bytes. """
        return self._props["metadata"]

class SSHHostCertificate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHHostCertificate {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this SSH Host Certificate """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the SSH Host Certificate API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the SSH Host Certificate API resource was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of this SSH Host Certificate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this SSH Host Certificate. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def public_key(self):
        """ a public key in OpenSSH Authorized Keys format that this certificate signs """
        return self._props["public_key"]
    
    @property
    def key_type(self):
        """ the key type of the <code>public_key</code>, one of <code>rsa</code>, <code>ecdsa</code> or <code>ed25519</code> """
        return self._props["key_type"]
    
    @property
    def ssh_certificate_authority_id(self):
        """ the ssh certificate authority that is used to sign this ssh host certificate """
        return self._props["ssh_certificate_authority_id"]
    
    @property
    def principals(self):
        """ the list of principals included in the ssh host certificate. This is the list of hostnames and/or IP addresses that are authorized to serve SSH traffic with this certificate. Dangerously, if no principals are specified, this certificate is considered valid for all hosts. """
        return self._props["principals"]
    
    @property
    def valid_after(self):
        """ the time when the ssh host certificate becomes valid, in RFC 3339 format. """
        return self._props["valid_after"]
    
    @property
    def valid_until(self):
        """ the time after which the ssh host certificate becomes invalid, in RFC 3339 format. the OpenSSH certificates RFC calls this <code>valid_before</code>. """
        return self._props["valid_until"]
    
    @property
    def certificate(self):
        """ the signed SSH certificate in OpenSSH Authorized Keys format. this value should be placed in a <code>-cert.pub</code> certificate file on disk that should be referenced in your <code>sshd_config</code> configuration file with a <code>HostCertificate</code> directive """
        return self._props["certificate"]

class SSHHostCertificateList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHHostCertificateList {}>".format(self.id)

    def __iter__(self):
        return (SSHHostCertificate(o) for o in self._props["ssh_host_certificates"])
    
    @property
    def ssh_host_certificates(self):
        """ the list of all ssh host certificates on this account """
        return self._props["ssh_host_certificates"]
    
    @property
    def uri(self):
        """ URI of the ssh host certificates list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class SSHUserCertificateCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHUserCertificateCreate {}>".format(self.id)

    
    
    @property
    def ssh_certificate_authority_id(self):
        """ the ssh certificate authority that is used to sign this ssh user certificate """
        return self._props["ssh_certificate_authority_id"]
    
    @property
    def public_key(self):
        """ a public key in OpenSSH Authorized Keys format that this certificate signs """
        return self._props["public_key"]
    
    @property
    def principals(self):
        """ the list of principals included in the ssh user certificate. This is the list of usernames that the certificate holder may sign in as on a machine authorizinig the signing certificate authority. Dangerously, if no principals are specified, this certificate may be used to log in as any user. """
        return self._props["principals"]
    
    @property
    def critical_options(self):
        """ A map of critical options included in the certificate. Only two critical options are currently defined by OpenSSH: <code>force-command</code> and <code>source-address</code>. See <a href="https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys">the OpenSSH certificate protocol spec</a> for additional details. """
        return self._props["critical_options"]
    
    @property
    def extensions(self):
        """ A map of extensions included in the certificate. Extensions are additional metadata that can be interpreted by the SSH server for any purpose. These can be used to permit or deny the ability to open a terminal, do port forwarding, x11 forwarding, and more. If unspecified, the certificate will include limited permissions with the following extension map: <code>{"permit-pty": "", "permit-user-rc": ""}</code> OpenSSH understands a number of predefined extensions. See <a href="https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys">the OpenSSH certificate protocol spec</a> for additional details. """
        return self._props["extensions"]
    
    @property
    def valid_after(self):
        """ The time when the user certificate becomes valid, in RFC 3339 format. Defaults to the current time if unspecified. """
        return self._props["valid_after"]
    
    @property
    def valid_until(self):
        """ The time when this host certificate becomes invalid, in RFC 3339 format. If unspecified, a default value of 24 hours will be used. The OpenSSH certificates RFC calls this <code>valid_before</code>. """
        return self._props["valid_until"]
    
    @property
    def description(self):
        """ human-readable description of this SSH User Certificate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this SSH User Certificate. optional, max 4096 bytes. """
        return self._props["metadata"]

class SSHUserCertificateUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHUserCertificateUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of this SSH User Certificate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this SSH User Certificate. optional, max 4096 bytes. """
        return self._props["metadata"]

class SSHUserCertificate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHUserCertificate {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this SSH User Certificate """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the SSH User Certificate API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the SSH User Certificate API resource was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of this SSH User Certificate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this SSH User Certificate. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def public_key(self):
        """ a public key in OpenSSH Authorized Keys format that this certificate signs """
        return self._props["public_key"]
    
    @property
    def key_type(self):
        """ the key type of the <code>public_key</code>, one of <code>rsa</code>, <code>ecdsa</code> or <code>ed25519</code> """
        return self._props["key_type"]
    
    @property
    def ssh_certificate_authority_id(self):
        """ the ssh certificate authority that is used to sign this ssh user certificate """
        return self._props["ssh_certificate_authority_id"]
    
    @property
    def principals(self):
        """ the list of principals included in the ssh user certificate. This is the list of usernames that the certificate holder may sign in as on a machine authorizinig the signing certificate authority. Dangerously, if no principals are specified, this certificate may be used to log in as any user. """
        return self._props["principals"]
    
    @property
    def critical_options(self):
        """ A map of critical options included in the certificate. Only two critical options are currently defined by OpenSSH: <code>force-command</code> and <code>source-address</code>. See <a href="https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys">the OpenSSH certificate protocol spec</a> for additional details. """
        return self._props["critical_options"]
    
    @property
    def extensions(self):
        """ A map of extensions included in the certificate. Extensions are additional metadata that can be interpreted by the SSH server for any purpose. These can be used to permit or deny the ability to open a terminal, do port forwarding, x11 forwarding, and more. If unspecified, the certificate will include limited permissions with the following extension map: <code>{"permit-pty": "", "permit-user-rc": ""}</code> OpenSSH understands a number of predefined extensions. See <a href="https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys">the OpenSSH certificate protocol spec</a> for additional details. """
        return self._props["extensions"]
    
    @property
    def valid_after(self):
        """ the time when the ssh host certificate becomes valid, in RFC 3339 format. """
        return self._props["valid_after"]
    
    @property
    def valid_until(self):
        """ the time after which the ssh host certificate becomes invalid, in RFC 3339 format. the OpenSSH certificates RFC calls this <code>valid_before</code>. """
        return self._props["valid_until"]
    
    @property
    def certificate(self):
        """ the signed SSH certificate in OpenSSH Authorized Keys Format. this value should be placed in a <code>-cert.pub</code> certificate file on disk that should be referenced in your <code>sshd_config</code> configuration file with a <code>HostCertificate</code> directive """
        return self._props["certificate"]

class SSHUserCertificateList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<SSHUserCertificateList {}>".format(self.id)

    def __iter__(self):
        return (SSHUserCertificate(o) for o in self._props["ssh_user_certificates"])
    
    @property
    def ssh_user_certificates(self):
        """ the list of all ssh user certificates on this account """
        return self._props["ssh_user_certificates"]
    
    @property
    def uri(self):
        """ URI of the ssh user certificates list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class TLSCertificateCreate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TLSCertificateCreate {}>".format(self.id)

    
    
    @property
    def description(self):
        """ human-readable description of this TLS certificate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this TLS certificate. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def certificate_pem(self):
        """ chain of PEM-encoded certificates, leaf first. See <a href="#tls-certificates-pem">Certificate Bundles</a>. """
        return self._props["certificate_pem"]
    
    @property
    def private_key_pem(self):
        """ private key for the TLS certificate, PEM-encoded. See <a href="#tls-certificates-key">Private Keys</a>. """
        return self._props["private_key_pem"]

class TLSCertificateUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TLSCertificateUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def description(self):
        """ human-readable description of this TLS certificate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this TLS certificate. optional, max 4096 bytes. """
        return self._props["metadata"]

class TLSCertificate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TLSCertificate {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique identifier for this TLS certificate """
        return self._props["id"]
    
    @property
    def uri(self):
        """ URI of the TLS certificate API resource """
        return self._props["uri"]
    
    @property
    def created_at(self):
        """ timestamp when the TLS certificate was created, RFC 3339 format """
        return self._props["created_at"]
    
    @property
    def description(self):
        """ human-readable description of this TLS certificate. optional, max 255 bytes. """
        return self._props["description"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined machine-readable data of this TLS certificate. optional, max 4096 bytes. """
        return self._props["metadata"]
    
    @property
    def certificate_pem(self):
        """ chain of PEM-encoded certificates, leaf first. See <a href="#tls-certificates-pem">Certificate Bundles</a>. """
        return self._props["certificate_pem"]
    
    @property
    def subject_common_name(self):
        """ subject common name from the leaf of this TLS certificate """
        return self._props["subject_common_name"]
    
    @property
    def subject_alternative_names(self):
        """ subject alternative names (SANs) from the leaf of this TLS certificate """
        return self._props["subject_alternative_names"]
    
    @property
    def issued_at(self):
        """ timestamp (in RFC 3339 format) when this TLS certificate was issued automatically, or null if this certificate was user-uploaded """
        return self._props["issued_at"]
    
    @property
    def not_before(self):
        """ timestamp when this TLS certificate becomes valid, RFC 3339 format """
        return self._props["not_before"]
    
    @property
    def not_after(self):
        """ timestamp when this TLS certificate becomes invalid, RFC 3339 format """
        return self._props["not_after"]
    
    @property
    def key_usages(self):
        """ set of actions the private key of this TLS certificate can be used for """
        return self._props["key_usages"]
    
    @property
    def extended_key_usages(self):
        """ extended set of actions the private key of this TLS certificate can be used for """
        return self._props["extended_key_usages"]
    
    @property
    def private_key_type(self):
        """ type of the private key of this TLS certificate. One of rsa, ecdsa, or ed25519. """
        return self._props["private_key_type"]
    
    @property
    def issuer_common_name(self):
        """ issuer common name from the leaf of this TLS certificate """
        return self._props["issuer_common_name"]
    
    @property
    def serial_number(self):
        """ serial number of the leaf of this TLS certificate """
        return self._props["serial_number"]
    
    @property
    def subject_organization(self):
        """ subject organization from the leaf of this TLS certificate """
        return self._props["subject_organization"]
    
    @property
    def subject_organizational_unit(self):
        """ subject organizational unit from the leaf of this TLS certificate """
        return self._props["subject_organizational_unit"]
    
    @property
    def subject_locality(self):
        """ subject locality from the leaf of this TLS certificate """
        return self._props["subject_locality"]
    
    @property
    def subject_province(self):
        """ subject province from the leaf of this TLS certificate """
        return self._props["subject_province"]
    
    @property
    def subject_country(self):
        """ subject country from the leaf of this TLS certificate """
        return self._props["subject_country"]

class TLSCertificateList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TLSCertificateList {}>".format(self.id)

    def __iter__(self):
        return (TLSCertificate(o) for o in self._props["tls_certificates"])
    
    @property
    def tls_certificates(self):
        """ the list of all TLS certificates on this account """
        return self._props["tls_certificates"]
    
    @property
    def uri(self):
        """ URI of the TLS certificates list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class TLSCertificateSANs(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TLSCertificateSANs {}>".format(self.id)

    
    
    @property
    def dns_names(self):
        """ set of additional domains (including wildcards) this TLS certificate is valid for """
        return self._props["dns_names"]
    
    @property
    def ips(self):
        """ set of IP addresses this TLS certificate is also valid for """
        return self._props["ips"]

class TunnelSession(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TunnelSession {}>".format(self.id)

    
    
    @property
    def agent_version(self):
        """ version of the ngrok agent that started this ngrok tunnel session """
        return self._props["agent_version"]
    
    @property
    def credential(self):
        """ reference to the tunnel credential or ssh credential used by the ngrok agent to start this tunnel session """
        return self._props["credential"]
    
    @property
    def id(self):
        """ unique tunnel session resource identifier """
        return self._props["id"]
    
    @property
    def ip(self):
        """ source ip address of the tunnel session """
        return self._props["ip"]
    
    @property
    def metadata(self):
        """ arbitrary user-defined data specified in the metadata property in the ngrok configuration file. See the metadata configuration option """
        return self._props["metadata"]
    
    @property
    def os(self):
        """ operating system of the host the ngrok agent is running on """
        return self._props["os"]
    
    @property
    def region(self):
        """ the ngrok region identifier in which this tunnel session was started """
        return self._props["region"]
    
    @property
    def started_at(self):
        """ time when the tunnel session first connected to the ngrok servers """
        return self._props["started_at"]
    
    @property
    def transport(self):
        """ the transport protocol used to start the tunnel session. Either <code>ngrok/v2</code> or <code>ssh</code> """
        return self._props["transport"]
    
    @property
    def uri(self):
        """ URI to the API resource of the tunnel session """
        return self._props["uri"]

class TunnelSessionList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TunnelSessionList {}>".format(self.id)

    def __iter__(self):
        return (TunnelSession(o) for o in self._props["tunnel_sessions"])
    
    @property
    def tunnel_sessions(self):
        """ list of all tunnel sessions on this account """
        return self._props["tunnel_sessions"]
    
    @property
    def uri(self):
        """ URI to the API resource of the tunnel session list """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]

class TunnelSessionsUpdate(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TunnelSessionsUpdate {}>".format(self.id)

    
    
    @property
    def id(self):
        """  """
        return self._props["id"]
    
    @property
    def version(self):
        """ request that the ngrok agent update to this specific version instead of the latest available version """
        return self._props["version"]

class Tunnel(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<Tunnel {}>".format(self.id)

    
    
    @property
    def id(self):
        """ unique tunnel resource identifier """
        return self._props["id"]
    
    @property
    def public_url(self):
        """ URL of the tunnel's public endpoint """
        return self._props["public_url"]
    
    @property
    def started_at(self):
        """ timestamp when the tunnel was initiated in RFC 3339 format """
        return self._props["started_at"]
    
    @property
    def metadata(self):
        """ user-supplied metadata for the tunnel defined in the ngrok configuration file. See the tunnel <a href="https://ngrok.com/docs#tunnel-definitions-metadata">metadata configuration option</a> In API version 0, this value was instead pulled from the top-level <a href="https://ngrok.com/docs#config_metadata">metadata configuration option</a>. """
        return self._props["metadata"]
    
    @property
    def proto(self):
        """ tunnel protocol. one of <code>http</code>, <code>https</code>, <code>tcp</code> or <code>tls</code> """
        return self._props["proto"]
    
    @property
    def region(self):
        """ identifier of tune region where the tunnel is running """
        return self._props["region"]
    
    @property
    def tunnel_session(self):
        """ reference object pointing to the tunnel session on which this tunnel was started """
        return self._props["tunnel_session"]

class TunnelList(object):
    """  """
    def __init__(self, props):
       self._props = props

    def __eq__(self, other):
       return self._props == other._props

    def __repr__(self):
       return "<TunnelList {}>".format(self.id)

    def __iter__(self):
        return (Tunnel(o) for o in self._props["tunnels"])
    
    @property
    def tunnels(self):
        """ the list of all online tunnels on this account """
        return self._props["tunnels"]
    
    @property
    def uri(self):
        """ URI of the tunnels list API resource """
        return self._props["uri"]
    
    @property
    def next_page_uri(self):
        """ URI of the next page, or null if there is no next page """
        return self._props["next_page_uri"]
