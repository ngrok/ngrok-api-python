# Code generated for API Clients. DO NOT EDIT.


from __future__ import annotations
from typing import Any, Mapping, Sequence
from datetime import datetime, timedelta
from .iterator import PagedIterator


class Ref(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<Ref {} {}>".format(self.id, repr(self._props))
        else:
            return "<Ref {}>".format(repr(self._props))

    @property
    def id(self) -> str:
        """a resource identifier"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """a uri for locating a resource"""
        return self._props["uri"]


class AbuseReport(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["hostnames"] = (
            [AbuseReportHostname(client, x) for x in props["hostnames"]]
            if props.get("hostnames") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<AbuseReport {} {}>".format(self.id, repr(self._props))
        else:
            return "<AbuseReport {}>".format(repr(self._props))

    @property
    def id(self) -> str:
        """ID of the abuse report"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the abuse report API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp that the abuse report record was created in RFC 3339 format"""
        return self._props["created_at"]

    @property
    def urls(self) -> Sequence[str]:
        """a list of URLs containing suspected abusive content"""
        return self._props["urls"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined data about this abuse report. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def status(self) -> str:
        """Indicates whether ngrok has processed the abuse report. one of ``PENDING``, ``PROCESSED``, or ``PARTIALLY_PROCESSED``"""
        return self._props["status"]

    @property
    def hostnames(self) -> Sequence[AbuseReportHostname]:
        """an array of hostname statuses related to the report"""
        return self._props["hostnames"]


class AbuseReportHostname(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<AbuseReportHostname {} {}>".format(self.id, repr(self._props))
        else:
            return "<AbuseReportHostname {}>".format(repr(self._props))

    @property
    def hostname(self) -> str:
        """the hostname ngrok has parsed out of one of the reported URLs in this abuse report"""
        return self._props["hostname"]

    @property
    def status(self) -> str:
        """indicates what action ngrok has taken against the hostname. one of ``PENDING``, ``BANNED``, ``UNBANNED``, or ``IGNORE``"""
        return self._props["status"]


class AgentIngress(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["certificate_management_policy"] = (
            AgentIngressCertPolicy(client, props["certificate_management_policy"])
            if props.get("certificate_management_policy") is not None
            else None
        )
        self._props["certificate_management_status"] = (
            AgentIngressCertStatus(client, props["certificate_management_status"])
            if props.get("certificate_management_status") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<AgentIngress {} {}>".format(self.id, repr(self._props))
        else:
            return "<AgentIngress {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.agent_ingresses.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
        certificate_management_policy: AgentIngressCertPolicy = None,
    ):
        self._client.agent_ingresses.update(
            id=self.id,
            description=description,
            metadata=metadata,
            certificate_management_policy=certificate_management_policy,
        )

    @property
    def id(self) -> str:
        """unique Agent Ingress resource identifier"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI to the API resource of this Agent ingress"""
        return self._props["uri"]

    @property
    def description(self) -> str:
        """human-readable description of the use of this Agent Ingress. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this Agent Ingress. optional, max 4096 bytes"""
        return self._props["metadata"]

    @property
    def domain(self) -> str:
        """the domain that you own to be used as the base domain name to generate regional agent ingress domains."""
        return self._props["domain"]

    @property
    def ns_targets(self) -> Sequence[str]:
        """a list of target values to use as the values of NS records for the domain property these values will delegate control over the domain to ngrok"""
        return self._props["ns_targets"]

    @property
    def region_domains(self) -> Sequence[str]:
        """a list of regional agent ingress domains that are subdomains of the value of domain this value may increase over time as ngrok adds more regions"""
        return self._props["region_domains"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the Agent Ingress was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def certificate_management_policy(self) -> AgentIngressCertPolicy:
        """configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled"""
        return self._props["certificate_management_policy"]

    @property
    def certificate_management_status(self) -> AgentIngressCertStatus:
        """status of the automatic certificate management for this domain, or null if automatic management is disabled"""
        return self._props["certificate_management_status"]


class AgentIngressList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ingresses"] = (
            [AgentIngress(client, x) for x in props["ingresses"]]
            if props.get("ingresses") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<AgentIngressList {} {}>".format(self.id, repr(self._props))
        else:
            return "<AgentIngressList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "ingresses")

    @property
    def ingresses(self) -> Sequence[AgentIngress]:
        """the list of Agent Ingresses owned by this account"""
        return self._props["ingresses"]

    @property
    def uri(self) -> str:
        """URI of the Agent Ingress list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class AgentIngressCertPolicy(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<AgentIngressCertPolicy {} {}>".format(self.id, repr(self._props))
        else:
            return "<AgentIngressCertPolicy {}>".format(repr(self._props))

    @property
    def authority(self) -> str:
        """certificate authority to request certificates from. The only supported value is letsencrypt."""
        return self._props["authority"]

    @property
    def private_key_type(self) -> str:
        """type of private key to use when requesting certificates. Defaults to rsa, can be either rsa or ecdsa."""
        return self._props["private_key_type"]


class AgentIngressCertStatus(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["provisioning_job"] = (
            AgentIngressCertJob(client, props["provisioning_job"])
            if props.get("provisioning_job") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<AgentIngressCertStatus {} {}>".format(self.id, repr(self._props))
        else:
            return "<AgentIngressCertStatus {}>".format(repr(self._props))

    @property
    def renews_at(self) -> datetime:
        """timestamp when the next renewal will be requested, RFC 3339 format"""
        return self._props["renews_at"]

    @property
    def provisioning_job(self) -> AgentIngressCertJob:
        """status of the certificate provisioning job, or null if the certificiate isn't being provisioned or renewed"""
        return self._props["provisioning_job"]


class AgentIngressCertJob(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<AgentIngressCertJob {} {}>".format(self.id, repr(self._props))
        else:
            return "<AgentIngressCertJob {}>".format(repr(self._props))

    @property
    def error_code(self) -> str:
        """if present, an error code indicating why provisioning is failing. It may be either a temporary condition (INTERNAL_ERROR), or a permanent one the user must correct (DNS_ERROR)."""
        return self._props["error_code"]

    @property
    def msg(self) -> str:
        """a message describing the current status or error"""
        return self._props["msg"]

    @property
    def started_at(self) -> datetime:
        """timestamp when the provisioning job started, RFC 3339 format"""
        return self._props["started_at"]

    @property
    def retries_at(self) -> datetime:
        """timestamp when the provisioning job will be retried"""
        return self._props["retries_at"]


class APIKey(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<APIKey {} {}>".format(self.id, repr(self._props))
        else:
            return "<APIKey {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.api_keys.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
    ):
        self._client.api_keys.update(
            id=self.id,
            description=description,
            metadata=metadata,
        )

    @property
    def id(self) -> str:
        """unique API key resource identifier"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI to the API resource of this API key"""
        return self._props["uri"]

    @property
    def description(self) -> str:
        """human-readable description of what uses the API key to authenticate. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined data of this API key. optional, max 4096 bytes"""
        return self._props["metadata"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the api key was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def token(self) -> str:
        """the bearer token that can be placed into the Authorization header to authenticate request to the ngrok API. **This value is only available one time, on the API response from key creation. Otherwise it is null.**"""
        return self._props["token"]

    @property
    def owner_id(self) -> str:
        """If supplied at credential creation, ownership will be assigned to the specified User or Bot. Only admins may specify an owner other than themselves. Defaults to the authenticated User or Bot."""
        return self._props["owner_id"]


class APIKeyList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["keys"] = (
            [APIKey(client, x) for x in props["keys"]]
            if props.get("keys") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<APIKeyList {} {}>".format(self.id, repr(self._props))
        else:
            return "<APIKeyList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "keys")

    @property
    def keys(self) -> Sequence[APIKey]:
        """the list of API keys for this account"""
        return self._props["keys"]

    @property
    def uri(self) -> str:
        """URI of the API keys list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class ApplicationSession(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["browser_session"] = (
            BrowserSession(client, props["browser_session"])
            if props.get("browser_session") is not None
            else None
        )
        self._props["application_user"] = (
            Ref(client, props["application_user"])
            if props.get("application_user") is not None
            else None
        )
        self._props["endpoint"] = (
            Ref(client, props["endpoint"])
            if props.get("endpoint") is not None
            else None
        )
        self._props["edge"] = (
            Ref(client, props["edge"]) if props.get("edge") is not None else None
        )
        self._props["route"] = (
            Ref(client, props["route"]) if props.get("route") is not None else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ApplicationSession {} {}>".format(self.id, repr(self._props))
        else:
            return "<ApplicationSession {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.application_sessions.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """unique application session resource identifier"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the application session API resource"""
        return self._props["uri"]

    @property
    def public_url(self) -> str:
        """URL of the hostport served by this endpoint"""
        return self._props["public_url"]

    @property
    def browser_session(self) -> BrowserSession:
        """browser session details of the application session"""
        return self._props["browser_session"]

    @property
    def application_user(self) -> Ref:
        """application user this session is associated with"""
        return self._props["application_user"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the user was created in RFC 3339 format"""
        return self._props["created_at"]

    @property
    def last_active(self) -> datetime:
        """timestamp when the user was last active in RFC 3339 format"""
        return self._props["last_active"]

    @property
    def expires_at(self) -> datetime:
        """timestamp when session expires in RFC 3339 format"""
        return self._props["expires_at"]

    @property
    def endpoint(self) -> Ref:
        """ephemeral endpoint this session is associated with"""
        return self._props["endpoint"]

    @property
    def edge(self) -> Ref:
        """edge this session is associated with, null if the endpoint is agent-initiated"""
        return self._props["edge"]

    @property
    def route(self) -> Ref:
        """route this session is associated with, null if the endpoint is agent-initiated"""
        return self._props["route"]


class ApplicationSessionList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["application_sessions"] = (
            [ApplicationSession(client, x) for x in props["application_sessions"]]
            if props.get("application_sessions") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ApplicationSessionList {} {}>".format(self.id, repr(self._props))
        else:
            return "<ApplicationSessionList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "application_sessions")

    @property
    def application_sessions(self) -> Sequence[ApplicationSession]:
        """list of all application sessions on this account"""
        return self._props["application_sessions"]

    @property
    def uri(self) -> str:
        """URI of the application session list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class BrowserSession(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["user_agent"] = (
            UserAgent(client, props["user_agent"])
            if props.get("user_agent") is not None
            else None
        )
        self._props["location"] = (
            Location(client, props["location"])
            if props.get("location") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<BrowserSession {} {}>".format(self.id, repr(self._props))
        else:
            return "<BrowserSession {}>".format(repr(self._props))

    @property
    def user_agent(self) -> UserAgent:
        """HTTP User-Agent data"""
        return self._props["user_agent"]

    @property
    def ip_address(self) -> str:
        """IP address"""
        return self._props["ip_address"]

    @property
    def location(self) -> Location:
        """IP geolocation data"""
        return self._props["location"]


class UserAgent(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<UserAgent {} {}>".format(self.id, repr(self._props))
        else:
            return "<UserAgent {}>".format(repr(self._props))

    @property
    def raw(self) -> str:
        """raw User-Agent request header"""
        return self._props["raw"]

    @property
    def browser_name(self) -> str:
        """browser name (e.g. Chrome)"""
        return self._props["browser_name"]

    @property
    def browser_version(self) -> str:
        """browser version (e.g. 102)"""
        return self._props["browser_version"]

    @property
    def device_type(self) -> str:
        """type of device (e.g. Desktop)"""
        return self._props["device_type"]

    @property
    def os_name(self) -> str:
        """operating system name (e.g. MacOS)"""
        return self._props["os_name"]

    @property
    def os_version(self) -> str:
        """operating system version (e.g. 10.15.7)"""
        return self._props["os_version"]


class Location(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<Location {} {}>".format(self.id, repr(self._props))
        else:
            return "<Location {}>".format(repr(self._props))

    @property
    def country_code(self) -> str:
        """ISO country code"""
        return self._props["country_code"]

    @property
    def latitude(self) -> float:
        """geographical latitude"""
        return self._props["latitude"]

    @property
    def longitude(self) -> float:
        """geographical longitude"""
        return self._props["longitude"]

    @property
    def lat_long_radius_km(self) -> int:
        """accuracy radius of the geographical coordinates"""
        return self._props["lat_long_radius_km"]


class ApplicationUser(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["identity_provider"] = (
            IdentityProvider(client, props["identity_provider"])
            if props.get("identity_provider") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ApplicationUser {} {}>".format(self.id, repr(self._props))
        else:
            return "<ApplicationUser {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.application_users.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """unique application user resource identifier"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the application user API resource"""
        return self._props["uri"]

    @property
    def identity_provider(self) -> IdentityProvider:
        """identity provider that the user authenticated with"""
        return self._props["identity_provider"]

    @property
    def provider_user_id(self) -> str:
        """unique user identifier"""
        return self._props["provider_user_id"]

    @property
    def username(self) -> str:
        """user username"""
        return self._props["username"]

    @property
    def email(self) -> str:
        """user email"""
        return self._props["email"]

    @property
    def name(self) -> str:
        """user common name"""
        return self._props["name"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the user was created in RFC 3339 format"""
        return self._props["created_at"]

    @property
    def last_active(self) -> datetime:
        """timestamp when the user was last active in RFC 3339 format"""
        return self._props["last_active"]

    @property
    def last_login(self) -> datetime:
        """timestamp when the user last signed-in in RFC 3339 format"""
        return self._props["last_login"]


class ApplicationUserList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["application_users"] = (
            [ApplicationUser(client, x) for x in props["application_users"]]
            if props.get("application_users") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ApplicationUserList {} {}>".format(self.id, repr(self._props))
        else:
            return "<ApplicationUserList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "application_users")

    @property
    def application_users(self) -> Sequence[ApplicationUser]:
        """list of all application users on this account"""
        return self._props["application_users"]

    @property
    def uri(self) -> str:
        """URI of the application user list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class IdentityProvider(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<IdentityProvider {} {}>".format(self.id, repr(self._props))
        else:
            return "<IdentityProvider {}>".format(repr(self._props))

    @property
    def name(self) -> str:
        """name of the identity provider (e.g. Google)"""
        return self._props["name"]

    @property
    def url(self) -> str:
        """URL of the identity provider (e.g. `https://accounts.google.com <https://accounts.google.com>`_)"""
        return self._props["url"]


class TunnelSession(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["credential"] = (
            Ref(client, props["credential"])
            if props.get("credential") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TunnelSession {} {}>".format(self.id, repr(self._props))
        else:
            return "<TunnelSession {}>".format(repr(self._props))

    @property
    def agent_version(self) -> str:
        """version of the ngrok agent that started this ngrok tunnel session"""
        return self._props["agent_version"]

    @property
    def credential(self) -> Ref:
        """reference to the tunnel credential or ssh credential used by the ngrok agent to start this tunnel session"""
        return self._props["credential"]

    @property
    def id(self) -> str:
        """unique tunnel session resource identifier"""
        return self._props["id"]

    @property
    def ip(self) -> str:
        """source ip address of the tunnel session"""
        return self._props["ip"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined data specified in the metadata property in the ngrok configuration file. See the metadata configuration option"""
        return self._props["metadata"]

    @property
    def os(self) -> str:
        """operating system of the host the ngrok agent is running on"""
        return self._props["os"]

    @property
    def region(self) -> str:
        """the ngrok region identifier in which this tunnel session was started"""
        return self._props["region"]

    @property
    def started_at(self) -> datetime:
        """time when the tunnel session first connected to the ngrok servers"""
        return self._props["started_at"]

    @property
    def transport(self) -> str:
        """the transport protocol used to start the tunnel session. Either ``ngrok/v2`` or ``ssh``"""
        return self._props["transport"]

    @property
    def uri(self) -> str:
        """URI to the API resource of the tunnel session"""
        return self._props["uri"]


class TunnelSessionList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["tunnel_sessions"] = (
            [TunnelSession(client, x) for x in props["tunnel_sessions"]]
            if props.get("tunnel_sessions") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TunnelSessionList {} {}>".format(self.id, repr(self._props))
        else:
            return "<TunnelSessionList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "tunnel_sessions")

    @property
    def tunnel_sessions(self) -> Sequence[TunnelSession]:
        """list of all tunnel sessions on this account"""
        return self._props["tunnel_sessions"]

    @property
    def uri(self) -> str:
        """URI to the API resource of the tunnel session list"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class FailoverBackend(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<FailoverBackend {} {}>".format(self.id, repr(self._props))
        else:
            return "<FailoverBackend {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.backends.failover.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
        backends: Sequence[str] = [],
    ):
        self._client.backends.failover.update(
            id=self.id,
            description=description,
            metadata=metadata,
            backends=backends,
        )

    @property
    def id(self) -> str:
        """unique identifier for this Failover backend"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the FailoverBackend API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the backend was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this backend. Optional"""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this backend. Optional"""
        return self._props["metadata"]

    @property
    def backends(self) -> Sequence[str]:
        """the ids of the child backends in order"""
        return self._props["backends"]


class FailoverBackendList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["backends"] = (
            [FailoverBackend(client, x) for x in props["backends"]]
            if props.get("backends") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<FailoverBackendList {} {}>".format(self.id, repr(self._props))
        else:
            return "<FailoverBackendList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "backends")

    @property
    def backends(self) -> Sequence[FailoverBackend]:
        """the list of all Failover backends on this account"""
        return self._props["backends"]

    @property
    def uri(self) -> str:
        """URI of the Failover backends list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class HTTPResponseBackend(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<HTTPResponseBackend {} {}>".format(self.id, repr(self._props))
        else:
            return "<HTTPResponseBackend {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.backends.http_response.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
        body: str = None,
        headers: Mapping[str, str] = None,
        status_code: int = None,
    ):
        self._client.backends.http_response.update(
            id=self.id,
            description=description,
            metadata=metadata,
            body=body,
            headers=headers,
            status_code=status_code,
        )

    @property
    def id(self) -> str:
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the HTTPResponseBackend API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the backend was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this backend. Optional"""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this backend. Optional"""
        return self._props["metadata"]

    @property
    def body(self) -> str:
        """body to return as fixed content"""
        return self._props["body"]

    @property
    def headers(self) -> Mapping[str, str]:
        """headers to return"""
        return self._props["headers"]

    @property
    def status_code(self) -> int:
        """status code to return"""
        return self._props["status_code"]


class HTTPResponseBackendList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["backends"] = (
            [HTTPResponseBackend(client, x) for x in props["backends"]]
            if props.get("backends") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<HTTPResponseBackendList {} {}>".format(self.id, repr(self._props))
        else:
            return "<HTTPResponseBackendList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "backends")

    @property
    def backends(self) -> Sequence[HTTPResponseBackend]:
        return self._props["backends"]

    @property
    def uri(self) -> str:
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        return self._props["next_page_uri"]


class StaticBackend(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["tls"] = (
            StaticBackendTLS(client, props["tls"])
            if props.get("tls") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<StaticBackend {} {}>".format(self.id, repr(self._props))
        else:
            return "<StaticBackend {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.backends.static_address.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
        address: str = "",
        tls: StaticBackendTLS = None,
    ):
        self._client.backends.static_address.update(
            id=self.id,
            description=description,
            metadata=metadata,
            address=address,
            tls=tls,
        )

    @property
    def id(self) -> str:
        """unique identifier for this static backend"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the StaticBackend API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the backend was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this backend. Optional"""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this backend. Optional"""
        return self._props["metadata"]

    @property
    def address(self) -> str:
        """the address to forward to"""
        return self._props["address"]

    @property
    def tls(self) -> StaticBackendTLS:
        """tls configuration to use"""
        return self._props["tls"]


class StaticBackendTLS(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<StaticBackendTLS {} {}>".format(self.id, repr(self._props))
        else:
            return "<StaticBackendTLS {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """if TLS is checked"""
        return self._props["enabled"]


class StaticBackendList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["backends"] = (
            [StaticBackend(client, x) for x in props["backends"]]
            if props.get("backends") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<StaticBackendList {} {}>".format(self.id, repr(self._props))
        else:
            return "<StaticBackendList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "backends")

    @property
    def backends(self) -> Sequence[StaticBackend]:
        """the list of all static backends on this account"""
        return self._props["backends"]

    @property
    def uri(self) -> str:
        """URI of the static backends list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class TunnelGroupBackend(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["tunnels"] = (
            [Ref(client, x) for x in props["tunnels"]]
            if props.get("tunnels") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TunnelGroupBackend {} {}>".format(self.id, repr(self._props))
        else:
            return "<TunnelGroupBackend {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.backends.tunnel_group.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
        labels: Mapping[str, str] = {},
    ):
        self._client.backends.tunnel_group.update(
            id=self.id,
            description=description,
            metadata=metadata,
            labels=labels,
        )

    @property
    def id(self) -> str:
        """unique identifier for this TunnelGroup backend"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the TunnelGroupBackend API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the backend was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this backend. Optional"""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this backend. Optional"""
        return self._props["metadata"]

    @property
    def labels(self) -> Mapping[str, str]:
        """labels to watch for tunnels on, e.g. app->foo, dc->bar"""
        return self._props["labels"]

    @property
    def tunnels(self) -> Sequence[Ref]:
        """tunnels matching this backend"""
        return self._props["tunnels"]


class TunnelGroupBackendList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["backends"] = (
            [TunnelGroupBackend(client, x) for x in props["backends"]]
            if props.get("backends") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TunnelGroupBackendList {} {}>".format(self.id, repr(self._props))
        else:
            return "<TunnelGroupBackendList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "backends")

    @property
    def backends(self) -> Sequence[TunnelGroupBackend]:
        """the list of all TunnelGroup backends on this account"""
        return self._props["backends"]

    @property
    def uri(self) -> str:
        """URI of the TunnelGroup backends list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class WeightedBackend(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<WeightedBackend {} {}>".format(self.id, repr(self._props))
        else:
            return "<WeightedBackend {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.backends.weighted.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
        backends: Mapping[str, int] = {},
    ):
        self._client.backends.weighted.update(
            id=self.id,
            description=description,
            metadata=metadata,
            backends=backends,
        )

    @property
    def id(self) -> str:
        """unique identifier for this Weighted backend"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the WeightedBackend API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the backend was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this backend. Optional"""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this backend. Optional"""
        return self._props["metadata"]

    @property
    def backends(self) -> Mapping[str, int]:
        """the ids of the child backends to their weights [0-10000]"""
        return self._props["backends"]


class WeightedBackendList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["backends"] = (
            [WeightedBackend(client, x) for x in props["backends"]]
            if props.get("backends") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<WeightedBackendList {} {}>".format(self.id, repr(self._props))
        else:
            return "<WeightedBackendList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "backends")

    @property
    def backends(self) -> Sequence[WeightedBackend]:
        """the list of all Weighted backends on this account"""
        return self._props["backends"]

    @property
    def uri(self) -> str:
        """URI of the Weighted backends list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class BotUser(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<BotUser {} {}>".format(self.id, repr(self._props))
        else:
            return "<BotUser {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.bot_users.delete(
            id=self.id,
        )

    def update(
        self,
        name: str = None,
        active: bool = None,
    ):
        self._client.bot_users.update(
            id=self.id,
            name=name,
            active=active,
        )

    @property
    def id(self) -> str:
        """unique API key resource identifier"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI to the API resource of this bot user"""
        return self._props["uri"]

    @property
    def name(self) -> str:
        """human-readable name used to identify the bot"""
        return self._props["name"]

    @property
    def active(self) -> bool:
        """whether or not the bot is active"""
        return self._props["active"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the api key was created, RFC 3339 format"""
        return self._props["created_at"]


class BotUserList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["bot_users"] = (
            [BotUser(client, x) for x in props["bot_users"]]
            if props.get("bot_users") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<BotUserList {} {}>".format(self.id, repr(self._props))
        else:
            return "<BotUserList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "bot_users")

    @property
    def bot_users(self) -> Sequence[BotUser]:
        """the list of all bot users on this account"""
        return self._props["bot_users"]

    @property
    def uri(self) -> str:
        """URI of the bot users list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class CertificateAuthority(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<CertificateAuthority {} {}>".format(self.id, repr(self._props))
        else:
            return "<CertificateAuthority {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.certificate_authorities.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
    ):
        self._client.certificate_authorities.update(
            id=self.id,
            description=description,
            metadata=metadata,
        )

    @property
    def id(self) -> str:
        """unique identifier for this Certificate Authority"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the Certificate Authority API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the Certificate Authority was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this Certificate Authority. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this Certificate Authority. optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def ca_pem(self) -> str:
        """raw PEM of the Certificate Authority"""
        return self._props["ca_pem"]

    @property
    def subject_common_name(self) -> str:
        """subject common name of the Certificate Authority"""
        return self._props["subject_common_name"]

    @property
    def not_before(self) -> datetime:
        """timestamp when this Certificate Authority becomes valid, RFC 3339 format"""
        return self._props["not_before"]

    @property
    def not_after(self) -> datetime:
        """timestamp when this Certificate Authority becomes invalid, RFC 3339 format"""
        return self._props["not_after"]

    @property
    def key_usages(self) -> Sequence[str]:
        """set of actions the private key of this Certificate Authority can be used for"""
        return self._props["key_usages"]

    @property
    def extended_key_usages(self) -> Sequence[str]:
        """extended set of actions the private key of this Certificate Authority can be used for"""
        return self._props["extended_key_usages"]


class CertificateAuthorityList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["certificate_authorities"] = (
            [CertificateAuthority(client, x) for x in props["certificate_authorities"]]
            if props.get("certificate_authorities") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<CertificateAuthorityList {} {}>".format(self.id, repr(self._props))
        else:
            return "<CertificateAuthorityList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "certificate_authorities")

    @property
    def certificate_authorities(self) -> Sequence[CertificateAuthority]:
        """the list of all certificate authorities on this account"""
        return self._props["certificate_authorities"]

    @property
    def uri(self) -> str:
        """URI of the certificates authorities list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class Credential(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<Credential {} {}>".format(self.id, repr(self._props))
        else:
            return "<Credential {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.credentials.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
        acl: Sequence[str] = None,
    ):
        self._client.credentials.update(
            id=self.id,
            description=description,
            metadata=metadata,
            acl=acl,
        )

    @property
    def id(self) -> str:
        """unique tunnel credential resource identifier"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the tunnel credential API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the tunnel credential was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of who or what will use the credential to authenticate. Optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this credential. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def token(self) -> str:
        """the credential's authtoken that can be used to authenticate an ngrok agent. **This value is only available one time, on the API response from credential creation, otherwise it is null.**"""
        return self._props["token"]

    @property
    def acl(self) -> Sequence[str]:
        """optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains, addresses, and labels the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules for domains may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. Bind rules for labels may specify a wildcard key and/or value to match multiple labels. For example, you may specify a rule of ``bind:*=example`` which will allow ``x=example``, ``y=example``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions."""
        return self._props["acl"]

    @property
    def owner_id(self) -> str:
        """If supplied at credential creation, ownership will be assigned to the specified User or Bot. Only admins may specify an owner other than themselves. Defaults to the authenticated User or Bot."""
        return self._props["owner_id"]


class CredentialList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["credentials"] = (
            [Credential(client, x) for x in props["credentials"]]
            if props.get("credentials") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<CredentialList {} {}>".format(self.id, repr(self._props))
        else:
            return "<CredentialList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "credentials")

    @property
    def credentials(self) -> Sequence[Credential]:
        """the list of all tunnel credentials on this account"""
        return self._props["credentials"]

    @property
    def uri(self) -> str:
        """URI of the tunnel credential list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class EndpointWebhookValidation(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointWebhookValidation {} {}>".format(
                self.id, repr(self._props)
            )
        else:
            return "<EndpointWebhookValidation {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def provider(self) -> str:
        """a string indicating which webhook provider will be sending webhooks to this endpoint. Value must be one of the supported providers defined at `https://ngrok.com/docs/cloud-edge/modules/webhook-verification <https://ngrok.com/docs/cloud-edge/modules/webhook-verification>`_"""
        return self._props["provider"]

    @property
    def secret(self) -> str:
        """a string secret used to validate requests from the given provider. All providers except AWS SNS require a secret"""
        return self._props["secret"]


class EndpointCompression(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointCompression {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointCompression {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]


class EndpointMutualTLS(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["certificate_authorities"] = (
            [Ref(client, x) for x in props["certificate_authorities"]]
            if props.get("certificate_authorities") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointMutualTLS {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointMutualTLS {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def certificate_authorities(self) -> Sequence[Ref]:
        """PEM-encoded CA certificates that will be used to validate. Multiple CAs may be provided by concatenating them together."""
        return self._props["certificate_authorities"]


class EndpointMutualTLSMutate(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointMutualTLSMutate {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointMutualTLSMutate {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def certificate_authority_ids(self) -> Sequence[str]:
        """list of certificate authorities that will be used to validate the TLS client certificate presented by the initiator of the TLS connection"""
        return self._props["certificate_authority_ids"]


class EndpointTLSTermination(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointTLSTermination {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointTLSTermination {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def terminate_at(self) -> str:
        """``edge`` if the ngrok edge should terminate TLS traffic, ``upstream`` if TLS traffic should be passed through to the upstream ngrok agent / application server for termination. if ``upstream`` is chosen, most other modules will be disallowed because they rely on the ngrok edge being able to access the underlying traffic."""
        return self._props["terminate_at"]

    @property
    def min_version(self) -> str:
        """The minimum TLS version used for termination and advertised to the client during the TLS handshake. if unspecified, ngrok will choose an industry-safe default. This value must be null if ``terminate_at`` is set to ``upstream``."""
        return self._props["min_version"]


class EndpointTLSTerminationAtEdge(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointTLSTerminationAtEdge {} {}>".format(
                self.id, repr(self._props)
            )
        else:
            return "<EndpointTLSTerminationAtEdge {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def min_version(self) -> str:
        """The minimum TLS version used for termination and advertised to the client during the TLS handshake. if unspecified, ngrok will choose an industry-safe default. This value must be null if ``terminate_at`` is set to ``upstream``."""
        return self._props["min_version"]


class EndpointRequestHeaders(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointRequestHeaders {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointRequestHeaders {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def add(self) -> Mapping[str, str]:
        """a map of header key to header value that will be injected into the HTTP Request before being sent to the upstream application server"""
        return self._props["add"]

    @property
    def remove(self) -> Sequence[str]:
        """a list of header names that will be removed from the HTTP Request before being sent to the upstream application server"""
        return self._props["remove"]


class EndpointResponseHeaders(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointResponseHeaders {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointResponseHeaders {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def add(self) -> Mapping[str, str]:
        """a map of header key to header value that will be injected into the HTTP Response returned to the HTTP client"""
        return self._props["add"]

    @property
    def remove(self) -> Sequence[str]:
        """a list of header names that will be removed from the HTTP Response returned to the HTTP client"""
        return self._props["remove"]


class EndpointIPPolicy(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ip_policies"] = (
            [Ref(client, x) for x in props["ip_policies"]]
            if props.get("ip_policies") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointIPPolicy {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointIPPolicy {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def ip_policies(self) -> Sequence[Ref]:
        """list of all IP policies that will be used to check if a source IP is allowed access to the endpoint"""
        return self._props["ip_policies"]


class EndpointIPPolicyMutate(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointIPPolicyMutate {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointIPPolicyMutate {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def ip_policy_ids(self) -> Sequence[str]:
        """list of all IP policies that will be used to check if a source IP is allowed access to the endpoint"""
        return self._props["ip_policy_ids"]


class EndpointCircuitBreaker(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointCircuitBreaker {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointCircuitBreaker {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def tripped_duration(self) -> timedelta:
        """Integer number of seconds after which the circuit is tripped to wait before re-evaluating upstream health"""
        return timedelta(seconds=self._props["tripped_duration"])

    @property
    def rolling_window(self) -> int:
        """Integer number of seconds in the statistical rolling window that metrics are retained for."""
        return self._props["rolling_window"]

    @property
    def num_buckets(self) -> int:
        """Integer number of buckets into which metrics are retained. Max 128."""
        return self._props["num_buckets"]

    @property
    def volume_threshold(self) -> int:
        """Integer number of requests in a rolling window that will trip the circuit. Helpful if traffic volume is low."""
        return self._props["volume_threshold"]

    @property
    def error_threshold_percentage(self) -> float:
        """Error threshold percentage should be between 0 - 1.0, not 0-100.0"""
        return self._props["error_threshold_percentage"]


class EndpointOAuth(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["provider"] = (
            EndpointOAuthProvider(client, props["provider"])
            if props.get("provider") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOAuth {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOAuth {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def provider(self) -> EndpointOAuthProvider:
        """an object which defines the identity provider to use for authentication and configuration for who may access the endpoint"""
        return self._props["provider"]

    @property
    def options_passthrough(self) -> bool:
        """Do not enforce authentication on HTTP OPTIONS requests. necessary if you are supporting CORS."""
        return self._props["options_passthrough"]

    @property
    def cookie_prefix(self) -> str:
        """the prefix of the session cookie that ngrok sets on the http client to cache authentication. default is 'ngrok.'"""
        return self._props["cookie_prefix"]

    @property
    def inactivity_timeout(self) -> int:
        """Integer number of seconds of inactivity after which if the user has not accessed the endpoint, their session will time out and they will be forced to reauthenticate."""
        return self._props["inactivity_timeout"]

    @property
    def maximum_duration(self) -> timedelta:
        """Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate."""
        return timedelta(seconds=self._props["maximum_duration"])

    @property
    def auth_check_interval(self) -> int:
        """Integer number of seconds after which ngrok guarantees it will refresh user state from the identity provider and recheck whether the user is still authorized to access the endpoint. This is the preferred tunable to use to enforce a minimum amount of time after which a revoked user will no longer be able to access the resource."""
        return self._props["auth_check_interval"]


class EndpointOAuthProvider(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["github"] = (
            EndpointOAuthGitHub(client, props["github"])
            if props.get("github") is not None
            else None
        )
        self._props["facebook"] = (
            EndpointOAuthFacebook(client, props["facebook"])
            if props.get("facebook") is not None
            else None
        )
        self._props["microsoft"] = (
            EndpointOAuthMicrosoft(client, props["microsoft"])
            if props.get("microsoft") is not None
            else None
        )
        self._props["google"] = (
            EndpointOAuthGoogle(client, props["google"])
            if props.get("google") is not None
            else None
        )
        self._props["linkedin"] = (
            EndpointOAuthLinkedIn(client, props["linkedin"])
            if props.get("linkedin") is not None
            else None
        )
        self._props["gitlab"] = (
            EndpointOAuthGitLab(client, props["gitlab"])
            if props.get("gitlab") is not None
            else None
        )
        self._props["twitch"] = (
            EndpointOAuthTwitch(client, props["twitch"])
            if props.get("twitch") is not None
            else None
        )
        self._props["amazon"] = (
            EndpointOAuthAmazon(client, props["amazon"])
            if props.get("amazon") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOAuthProvider {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOAuthProvider {}>".format(repr(self._props))

    @property
    def github(self) -> EndpointOAuthGitHub:
        """configuration for using github as the identity provider"""
        return self._props["github"]

    @property
    def facebook(self) -> EndpointOAuthFacebook:
        """configuration for using facebook as the identity provider"""
        return self._props["facebook"]

    @property
    def microsoft(self) -> EndpointOAuthMicrosoft:
        """configuration for using microsoft as the identity provider"""
        return self._props["microsoft"]

    @property
    def google(self) -> EndpointOAuthGoogle:
        """configuration for using google as the identity provider"""
        return self._props["google"]

    @property
    def linkedin(self) -> EndpointOAuthLinkedIn:
        """configuration for using linkedin as the identity provider"""
        return self._props["linkedin"]

    @property
    def gitlab(self) -> EndpointOAuthGitLab:
        """configuration for using gitlab as the identity provider"""
        return self._props["gitlab"]

    @property
    def twitch(self) -> EndpointOAuthTwitch:
        """configuration for using twitch as the identity provider"""
        return self._props["twitch"]

    @property
    def amazon(self) -> EndpointOAuthAmazon:
        """configuration for using amazon as the identity provider"""
        return self._props["amazon"]


class EndpointOAuthGitHub(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOAuthGitHub {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOAuthGitHub {}>".format(repr(self._props))

    @property
    def client_id(self) -> str:
        """the OAuth app client ID. retrieve it from the identity provider's dashboard where you created your own OAuth app. optional. if unspecified, ngrok will use its own managed oauth application which has additional restrictions. see the OAuth module docs for more details. if present, client_secret must be present as well."""
        return self._props["client_id"]

    @property
    def client_secret(self) -> str:
        """the OAuth app client secret. retrieve if from the identity provider's dashboard where you created your own OAuth app. optional, see all of the caveats in the docs for ``client_id``."""
        return self._props["client_secret"]

    @property
    def scopes(self) -> Sequence[str]:
        """a list of provider-specific OAuth scopes with the permissions your OAuth app would like to ask for. these may not be set if you are using the ngrok-managed oauth app (i.e. you must pass both ``client_id`` and ``client_secret`` to set scopes)"""
        return self._props["scopes"]

    @property
    def email_addresses(self) -> Sequence[str]:
        """a list of email addresses of users authenticated by identity provider who are allowed access to the endpoint"""
        return self._props["email_addresses"]

    @property
    def email_domains(self) -> Sequence[str]:
        """a list of email domains of users authenticated by identity provider who are allowed access to the endpoint"""
        return self._props["email_domains"]

    @property
    def teams(self) -> Sequence[str]:
        """a list of github teams identifiers. users will be allowed access to the endpoint if they are a member of any of these teams. identifiers should be in the 'slug' format qualified with the org name, e.g. ``org-name/team-name``"""
        return self._props["teams"]

    @property
    def organizations(self) -> Sequence[str]:
        """a list of github org identifiers. users who are members of any of the listed organizations will be allowed access. identifiers should be the organization's 'slug'"""
        return self._props["organizations"]


class EndpointOAuthFacebook(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOAuthFacebook {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOAuthFacebook {}>".format(repr(self._props))

    @property
    def client_id(self) -> str:
        """the OAuth app client ID. retrieve it from the identity provider's dashboard where you created your own OAuth app. optional. if unspecified, ngrok will use its own managed oauth application which has additional restrictions. see the OAuth module docs for more details. if present, client_secret must be present as well."""
        return self._props["client_id"]

    @property
    def client_secret(self) -> str:
        """the OAuth app client secret. retrieve if from the identity provider's dashboard where you created your own OAuth app. optional, see all of the caveats in the docs for ``client_id``."""
        return self._props["client_secret"]

    @property
    def scopes(self) -> Sequence[str]:
        """a list of provider-specific OAuth scopes with the permissions your OAuth app would like to ask for. these may not be set if you are using the ngrok-managed oauth app (i.e. you must pass both ``client_id`` and ``client_secret`` to set scopes)"""
        return self._props["scopes"]

    @property
    def email_addresses(self) -> Sequence[str]:
        """a list of email addresses of users authenticated by identity provider who are allowed access to the endpoint"""
        return self._props["email_addresses"]

    @property
    def email_domains(self) -> Sequence[str]:
        """a list of email domains of users authenticated by identity provider who are allowed access to the endpoint"""
        return self._props["email_domains"]


class EndpointOAuthMicrosoft(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOAuthMicrosoft {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOAuthMicrosoft {}>".format(repr(self._props))

    @property
    def client_id(self) -> str:
        """the OAuth app client ID. retrieve it from the identity provider's dashboard where you created your own OAuth app. optional. if unspecified, ngrok will use its own managed oauth application which has additional restrictions. see the OAuth module docs for more details. if present, client_secret must be present as well."""
        return self._props["client_id"]

    @property
    def client_secret(self) -> str:
        """the OAuth app client secret. retrieve if from the identity provider's dashboard where you created your own OAuth app. optional, see all of the caveats in the docs for ``client_id``."""
        return self._props["client_secret"]

    @property
    def scopes(self) -> Sequence[str]:
        """a list of provider-specific OAuth scopes with the permissions your OAuth app would like to ask for. these may not be set if you are using the ngrok-managed oauth app (i.e. you must pass both ``client_id`` and ``client_secret`` to set scopes)"""
        return self._props["scopes"]

    @property
    def email_addresses(self) -> Sequence[str]:
        """a list of email addresses of users authenticated by identity provider who are allowed access to the endpoint"""
        return self._props["email_addresses"]

    @property
    def email_domains(self) -> Sequence[str]:
        """a list of email domains of users authenticated by identity provider who are allowed access to the endpoint"""
        return self._props["email_domains"]


class EndpointOAuthGoogle(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOAuthGoogle {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOAuthGoogle {}>".format(repr(self._props))

    @property
    def client_id(self) -> str:
        """the OAuth app client ID. retrieve it from the identity provider's dashboard where you created your own OAuth app. optional. if unspecified, ngrok will use its own managed oauth application which has additional restrictions. see the OAuth module docs for more details. if present, client_secret must be present as well."""
        return self._props["client_id"]

    @property
    def client_secret(self) -> str:
        """the OAuth app client secret. retrieve if from the identity provider's dashboard where you created your own OAuth app. optional, see all of the caveats in the docs for ``client_id``."""
        return self._props["client_secret"]

    @property
    def scopes(self) -> Sequence[str]:
        """a list of provider-specific OAuth scopes with the permissions your OAuth app would like to ask for. these may not be set if you are using the ngrok-managed oauth app (i.e. you must pass both ``client_id`` and ``client_secret`` to set scopes)"""
        return self._props["scopes"]

    @property
    def email_addresses(self) -> Sequence[str]:
        """a list of email addresses of users authenticated by identity provider who are allowed access to the endpoint"""
        return self._props["email_addresses"]

    @property
    def email_domains(self) -> Sequence[str]:
        """a list of email domains of users authenticated by identity provider who are allowed access to the endpoint"""
        return self._props["email_domains"]


class EndpointOAuthLinkedIn(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOAuthLinkedIn {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOAuthLinkedIn {}>".format(repr(self._props))

    @property
    def client_id(self) -> str:
        return self._props["client_id"]

    @property
    def client_secret(self) -> str:
        return self._props["client_secret"]

    @property
    def scopes(self) -> Sequence[str]:
        return self._props["scopes"]

    @property
    def email_addresses(self) -> Sequence[str]:
        return self._props["email_addresses"]

    @property
    def email_domains(self) -> Sequence[str]:
        return self._props["email_domains"]


class EndpointOAuthGitLab(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOAuthGitLab {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOAuthGitLab {}>".format(repr(self._props))

    @property
    def client_id(self) -> str:
        return self._props["client_id"]

    @property
    def client_secret(self) -> str:
        return self._props["client_secret"]

    @property
    def scopes(self) -> Sequence[str]:
        return self._props["scopes"]

    @property
    def email_addresses(self) -> Sequence[str]:
        return self._props["email_addresses"]

    @property
    def email_domains(self) -> Sequence[str]:
        return self._props["email_domains"]


class EndpointOAuthTwitch(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOAuthTwitch {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOAuthTwitch {}>".format(repr(self._props))

    @property
    def client_id(self) -> str:
        return self._props["client_id"]

    @property
    def client_secret(self) -> str:
        return self._props["client_secret"]

    @property
    def scopes(self) -> Sequence[str]:
        return self._props["scopes"]

    @property
    def email_addresses(self) -> Sequence[str]:
        return self._props["email_addresses"]

    @property
    def email_domains(self) -> Sequence[str]:
        return self._props["email_domains"]


class EndpointOAuthAmazon(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOAuthAmazon {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOAuthAmazon {}>".format(repr(self._props))

    @property
    def client_id(self) -> str:
        return self._props["client_id"]

    @property
    def client_secret(self) -> str:
        return self._props["client_secret"]

    @property
    def scopes(self) -> Sequence[str]:
        return self._props["scopes"]

    @property
    def email_addresses(self) -> Sequence[str]:
        return self._props["email_addresses"]

    @property
    def email_domains(self) -> Sequence[str]:
        return self._props["email_domains"]


class EndpointSAML(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointSAML {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointSAML {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def options_passthrough(self) -> bool:
        """Do not enforce authentication on HTTP OPTIONS requests. necessary if you are supporting CORS."""
        return self._props["options_passthrough"]

    @property
    def cookie_prefix(self) -> str:
        """the prefix of the session cookie that ngrok sets on the http client to cache authentication. default is 'ngrok.'"""
        return self._props["cookie_prefix"]

    @property
    def inactivity_timeout(self) -> int:
        """Integer number of seconds of inactivity after which if the user has not accessed the endpoint, their session will time out and they will be forced to reauthenticate."""
        return self._props["inactivity_timeout"]

    @property
    def maximum_duration(self) -> timedelta:
        """Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate."""
        return timedelta(seconds=self._props["maximum_duration"])

    @property
    def idp_metadata(self) -> str:
        """The full XML IdP EntityDescriptor. Your IdP may provide this to you as a a file to download or as a URL."""
        return self._props["idp_metadata"]

    @property
    def force_authn(self) -> bool:
        """If true, indicates that whenever we redirect a user to the IdP for authentication that the IdP must prompt the user for authentication credentials even if the user already has a valid session with the IdP."""
        return self._props["force_authn"]

    @property
    def allow_idp_initiated(self) -> bool:
        """If true, the IdP may initiate a login directly (e.g. the user does not need to visit the endpoint first and then be redirected). The IdP should set the ``RelayState`` parameter to the target URL of the resource they want the user to be redirected to after the SAML login assertion has been processed."""
        return self._props["allow_idp_initiated"]

    @property
    def authorized_groups(self) -> Sequence[str]:
        """If present, only users who are a member of one of the listed groups may access the target endpoint."""
        return self._props["authorized_groups"]

    @property
    def entity_id(self) -> str:
        """The SP Entity's unique ID. This always takes the form of a URL. In ngrok's implementation, this URL is the same as the metadata URL. This will need to be specified to the IdP as configuration."""
        return self._props["entity_id"]

    @property
    def assertion_consumer_service_url(self) -> str:
        """The public URL of the SP's Assertion Consumer Service. This is where the IdP will redirect to during an authentication flow. This will need to be specified to the IdP as configuration."""
        return self._props["assertion_consumer_service_url"]

    @property
    def single_logout_url(self) -> str:
        """The public URL of the SP's Single Logout Service. This is where the IdP will redirect to during a single logout flow. This will optionally need to be specified to the IdP as configuration."""
        return self._props["single_logout_url"]

    @property
    def request_signing_certificate_pem(self) -> str:
        """PEM-encoded x.509 certificate of the key pair that is used to sign all SAML requests that the ngrok SP makes to the IdP. Many IdPs do not support request signing verification, but we highly recommend specifying this in the IdP's configuration if it is supported."""
        return self._props["request_signing_certificate_pem"]

    @property
    def metadata_url(self) -> str:
        """A public URL where the SP's metadata is hosted. If an IdP supports dynamic configuration, this is the URL it can use to retrieve the SP metadata."""
        return self._props["metadata_url"]

    @property
    def nameid_format(self) -> str:
        """Defines the name identifier format the SP expects the IdP to use in its assertions to identify subjects. If unspecified, a default value of ``urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`` will be used. A subset of the allowed values enumerated by the SAML specification are supported."""
        return self._props["nameid_format"]


class EndpointSAMLMutate(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointSAMLMutate {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointSAMLMutate {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def options_passthrough(self) -> bool:
        """Do not enforce authentication on HTTP OPTIONS requests. necessary if you are supporting CORS."""
        return self._props["options_passthrough"]

    @property
    def cookie_prefix(self) -> str:
        """the prefix of the session cookie that ngrok sets on the http client to cache authentication. default is 'ngrok.'"""
        return self._props["cookie_prefix"]

    @property
    def inactivity_timeout(self) -> int:
        """Integer number of seconds of inactivity after which if the user has not accessed the endpoint, their session will time out and they will be forced to reauthenticate."""
        return self._props["inactivity_timeout"]

    @property
    def maximum_duration(self) -> timedelta:
        """Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate."""
        return timedelta(seconds=self._props["maximum_duration"])

    @property
    def idp_metadata(self) -> str:
        """The full XML IdP EntityDescriptor. Your IdP may provide this to you as a a file to download or as a URL."""
        return self._props["idp_metadata"]

    @property
    def force_authn(self) -> bool:
        """If true, indicates that whenever we redirect a user to the IdP for authentication that the IdP must prompt the user for authentication credentials even if the user already has a valid session with the IdP."""
        return self._props["force_authn"]

    @property
    def allow_idp_initiated(self) -> bool:
        """If true, the IdP may initiate a login directly (e.g. the user does not need to visit the endpoint first and then be redirected). The IdP should set the ``RelayState`` parameter to the target URL of the resource they want the user to be redirected to after the SAML login assertion has been processed."""
        return self._props["allow_idp_initiated"]

    @property
    def authorized_groups(self) -> Sequence[str]:
        """If present, only users who are a member of one of the listed groups may access the target endpoint."""
        return self._props["authorized_groups"]

    @property
    def nameid_format(self) -> str:
        """Defines the name identifier format the SP expects the IdP to use in its assertions to identify subjects. If unspecified, a default value of ``urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`` will be used. A subset of the allowed values enumerated by the SAML specification are supported."""
        return self._props["nameid_format"]


class EndpointOIDC(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointOIDC {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointOIDC {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def options_passthrough(self) -> bool:
        """Do not enforce authentication on HTTP OPTIONS requests. necessary if you are supporting CORS."""
        return self._props["options_passthrough"]

    @property
    def cookie_prefix(self) -> str:
        """the prefix of the session cookie that ngrok sets on the http client to cache authentication. default is 'ngrok.'"""
        return self._props["cookie_prefix"]

    @property
    def inactivity_timeout(self) -> int:
        """Integer number of seconds of inactivity after which if the user has not accessed the endpoint, their session will time out and they will be forced to reauthenticate."""
        return self._props["inactivity_timeout"]

    @property
    def maximum_duration(self) -> timedelta:
        """Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate."""
        return timedelta(seconds=self._props["maximum_duration"])

    @property
    def issuer(self) -> str:
        """URL of the OIDC "OpenID provider". This is the base URL used for discovery."""
        return self._props["issuer"]

    @property
    def client_id(self) -> str:
        """The OIDC app's client ID and OIDC audience."""
        return self._props["client_id"]

    @property
    def client_secret(self) -> str:
        """The OIDC app's client secret."""
        return self._props["client_secret"]

    @property
    def scopes(self) -> Sequence[str]:
        """The set of scopes to request from the OIDC identity provider."""
        return self._props["scopes"]


class EndpointBackend(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["backend"] = (
            Ref(client, props["backend"]) if props.get("backend") is not None else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointBackend {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointBackend {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def backend(self) -> Ref:
        """backend to be used to back this endpoint"""
        return self._props["backend"]


class EndpointBackendMutate(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointBackendMutate {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointBackendMutate {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def backend_id(self) -> str:
        """backend to be used to back this endpoint"""
        return self._props["backend_id"]


class EndpointWebsocketTCPConverter(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointWebsocketTCPConverter {} {}>".format(
                self.id, repr(self._props)
            )
        else:
            return "<EndpointWebsocketTCPConverter {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]


class EndpointUserAgentFilter(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointUserAgentFilter {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointUserAgentFilter {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        return self._props["enabled"]

    @property
    def allow(self) -> Sequence[str]:
        return self._props["allow"]

    @property
    def deny(self) -> Sequence[str]:
        return self._props["deny"]


class EndpointTrafficPolicy(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointTrafficPolicy {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointTrafficPolicy {}>".format(repr(self._props))

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def value(self) -> str:
        """the traffic policy that should be applied to the traffic on your endpoint."""
        return self._props["value"]


class HTTPSEdgeRoute(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["backend"] = (
            EndpointBackend(client, props["backend"])
            if props.get("backend") is not None
            else None
        )
        self._props["ip_restriction"] = (
            EndpointIPPolicy(client, props["ip_restriction"])
            if props.get("ip_restriction") is not None
            else None
        )
        self._props["circuit_breaker"] = (
            EndpointCircuitBreaker(client, props["circuit_breaker"])
            if props.get("circuit_breaker") is not None
            else None
        )
        self._props["compression"] = (
            EndpointCompression(client, props["compression"])
            if props.get("compression") is not None
            else None
        )
        self._props["request_headers"] = (
            EndpointRequestHeaders(client, props["request_headers"])
            if props.get("request_headers") is not None
            else None
        )
        self._props["response_headers"] = (
            EndpointResponseHeaders(client, props["response_headers"])
            if props.get("response_headers") is not None
            else None
        )
        self._props["webhook_verification"] = (
            EndpointWebhookValidation(client, props["webhook_verification"])
            if props.get("webhook_verification") is not None
            else None
        )
        self._props["oauth"] = (
            EndpointOAuth(client, props["oauth"])
            if props.get("oauth") is not None
            else None
        )
        self._props["saml"] = (
            EndpointSAML(client, props["saml"])
            if props.get("saml") is not None
            else None
        )
        self._props["oidc"] = (
            EndpointOIDC(client, props["oidc"])
            if props.get("oidc") is not None
            else None
        )
        self._props["websocket_tcp_converter"] = (
            EndpointWebsocketTCPConverter(client, props["websocket_tcp_converter"])
            if props.get("websocket_tcp_converter") is not None
            else None
        )
        self._props["user_agent_filter"] = (
            EndpointUserAgentFilter(client, props["user_agent_filter"])
            if props.get("user_agent_filter") is not None
            else None
        )
        self._props["traffic_policy"] = (
            EndpointTrafficPolicy(client, props["traffic_policy"])
            if props.get("traffic_policy") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<HTTPSEdgeRoute {} {}>".format(self.id, repr(self._props))
        else:
            return "<HTTPSEdgeRoute {}>".format(repr(self._props))

    def update(
        self,
        match_type: str = "",
        match: str = "",
        description: str = "",
        metadata: str = "",
        backend: EndpointBackendMutate = None,
        ip_restriction: EndpointIPPolicyMutate = None,
        circuit_breaker: EndpointCircuitBreaker = None,
        compression: EndpointCompression = None,
        request_headers: EndpointRequestHeaders = None,
        response_headers: EndpointResponseHeaders = None,
        webhook_verification: EndpointWebhookValidation = None,
        oauth: EndpointOAuth = None,
        saml: EndpointSAMLMutate = None,
        oidc: EndpointOIDC = None,
        websocket_tcp_converter: EndpointWebsocketTCPConverter = None,
        user_agent_filter: EndpointUserAgentFilter = None,
        traffic_policy: EndpointTrafficPolicy = None,
    ):
        self._client.edges.https_routes.update(
            edge_id=self.edge_id,
            id=self.id,
            match_type=match_type,
            match=match,
            description=description,
            metadata=metadata,
            backend=backend,
            ip_restriction=ip_restriction,
            circuit_breaker=circuit_breaker,
            compression=compression,
            request_headers=request_headers,
            response_headers=response_headers,
            webhook_verification=webhook_verification,
            oauth=oauth,
            saml=saml,
            oidc=oidc,
            websocket_tcp_converter=websocket_tcp_converter,
            user_agent_filter=user_agent_filter,
            traffic_policy=traffic_policy,
        )

    def delete(
        self,
    ):
        self._client.edges.https_routes.delete(
            edge_id=self.edge_id,
            id=self.id,
        )

    @property
    def edge_id(self) -> str:
        """unique identifier of this edge"""
        return self._props["edge_id"]

    @property
    def id(self) -> str:
        """unique identifier of this edge route"""
        return self._props["id"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the edge configuration was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def match_type(self) -> str:
        """Type of match to use for this route. Valid values are "exact_path" and "path_prefix"."""
        return self._props["match_type"]

    @property
    def match(self) -> str:
        """Route selector: "/blog" or "example.com" or "example.com/blog" """
        return self._props["match"]

    @property
    def uri(self) -> str:
        """URI of the edge API resource"""
        return self._props["uri"]

    @property
    def description(self) -> str:
        """human-readable description of what this edge will be used for; optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this edge. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def backend(self) -> EndpointBackend:
        """backend module configuration or ``null``"""
        return self._props["backend"]

    @property
    def ip_restriction(self) -> EndpointIPPolicy:
        """ip restriction module configuration or ``null``"""
        return self._props["ip_restriction"]

    @property
    def circuit_breaker(self) -> EndpointCircuitBreaker:
        """circuit breaker module configuration or ``null``"""
        return self._props["circuit_breaker"]

    @property
    def compression(self) -> EndpointCompression:
        """compression module configuration or ``null``"""
        return self._props["compression"]

    @property
    def request_headers(self) -> EndpointRequestHeaders:
        """request headers module configuration or ``null``"""
        return self._props["request_headers"]

    @property
    def response_headers(self) -> EndpointResponseHeaders:
        """response headers module configuration or ``null``"""
        return self._props["response_headers"]

    @property
    def webhook_verification(self) -> EndpointWebhookValidation:
        """webhook verification module configuration or ``null``"""
        return self._props["webhook_verification"]

    @property
    def oauth(self) -> EndpointOAuth:
        """oauth module configuration or ``null``"""
        return self._props["oauth"]

    @property
    def saml(self) -> EndpointSAML:
        """saml module configuration or ``null``"""
        return self._props["saml"]

    @property
    def oidc(self) -> EndpointOIDC:
        """oidc module configuration or ``null``"""
        return self._props["oidc"]

    @property
    def websocket_tcp_converter(self) -> EndpointWebsocketTCPConverter:
        """websocket to tcp adapter configuration or ``null``"""
        return self._props["websocket_tcp_converter"]

    @property
    def user_agent_filter(self) -> EndpointUserAgentFilter:
        return self._props["user_agent_filter"]

    @property
    def traffic_policy(self) -> EndpointTrafficPolicy:
        """the traffic policy associated with this edge or null"""
        return self._props["traffic_policy"]


class HTTPSEdgeList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["https_edges"] = (
            [HTTPSEdge(client, x) for x in props["https_edges"]]
            if props.get("https_edges") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<HTTPSEdgeList {} {}>".format(self.id, repr(self._props))
        else:
            return "<HTTPSEdgeList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "https_edges")

    @property
    def https_edges(self) -> Sequence[HTTPSEdge]:
        """the list of all HTTPS Edges on this account"""
        return self._props["https_edges"]

    @property
    def uri(self) -> str:
        """URI of the HTTPS Edge list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class HTTPSEdge(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["mutual_tls"] = (
            EndpointMutualTLS(client, props["mutual_tls"])
            if props.get("mutual_tls") is not None
            else None
        )
        self._props["tls_termination"] = (
            EndpointTLSTermination(client, props["tls_termination"])
            if props.get("tls_termination") is not None
            else None
        )
        self._props["routes"] = (
            [HTTPSEdgeRoute(client, x) for x in props["routes"]]
            if props.get("routes") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<HTTPSEdge {} {}>".format(self.id, repr(self._props))
        else:
            return "<HTTPSEdge {}>".format(repr(self._props))

    def update(
        self,
        description: str = None,
        metadata: str = None,
        hostports: Sequence[str] = None,
        mutual_tls: EndpointMutualTLSMutate = None,
        tls_termination: EndpointTLSTerminationAtEdge = None,
    ):
        self._client.edges.https.update(
            id=self.id,
            description=description,
            metadata=metadata,
            hostports=hostports,
            mutual_tls=mutual_tls,
            tls_termination=tls_termination,
        )

    def delete(
        self,
    ):
        self._client.edges.https.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """unique identifier of this edge"""
        return self._props["id"]

    @property
    def description(self) -> str:
        """human-readable description of what this edge will be used for; optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this edge; optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the edge configuration was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def uri(self) -> str:
        """URI of the edge API resource"""
        return self._props["uri"]

    @property
    def hostports(self) -> Sequence[str]:
        """hostports served by this edge"""
        return self._props["hostports"]

    @property
    def mutual_tls(self) -> EndpointMutualTLS:
        """edge modules"""
        return self._props["mutual_tls"]

    @property
    def tls_termination(self) -> EndpointTLSTermination:
        return self._props["tls_termination"]

    @property
    def routes(self) -> Sequence[HTTPSEdgeRoute]:
        """routes"""
        return self._props["routes"]


class TCPEdgeList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["tcp_edges"] = (
            [TCPEdge(client, x) for x in props["tcp_edges"]]
            if props.get("tcp_edges") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TCPEdgeList {} {}>".format(self.id, repr(self._props))
        else:
            return "<TCPEdgeList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "tcp_edges")

    @property
    def tcp_edges(self) -> Sequence[TCPEdge]:
        """the list of all TCP Edges on this account"""
        return self._props["tcp_edges"]

    @property
    def uri(self) -> str:
        """URI of the TCP Edge list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class TCPEdge(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["backend"] = (
            EndpointBackend(client, props["backend"])
            if props.get("backend") is not None
            else None
        )
        self._props["ip_restriction"] = (
            EndpointIPPolicy(client, props["ip_restriction"])
            if props.get("ip_restriction") is not None
            else None
        )
        self._props["traffic_policy"] = (
            EndpointTrafficPolicy(client, props["traffic_policy"])
            if props.get("traffic_policy") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TCPEdge {} {}>".format(self.id, repr(self._props))
        else:
            return "<TCPEdge {}>".format(repr(self._props))

    def update(
        self,
        description: str = None,
        metadata: str = None,
        hostports: Sequence[str] = None,
        backend: EndpointBackendMutate = None,
        ip_restriction: EndpointIPPolicyMutate = None,
        traffic_policy: EndpointTrafficPolicy = None,
    ):
        self._client.edges.tcp.update(
            id=self.id,
            description=description,
            metadata=metadata,
            hostports=hostports,
            backend=backend,
            ip_restriction=ip_restriction,
            traffic_policy=traffic_policy,
        )

    def delete(
        self,
    ):
        self._client.edges.tcp.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """unique identifier of this edge"""
        return self._props["id"]

    @property
    def description(self) -> str:
        """human-readable description of what this edge will be used for; optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this edge. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the edge was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def uri(self) -> str:
        """URI of the edge API resource"""
        return self._props["uri"]

    @property
    def hostports(self) -> Sequence[str]:
        """hostports served by this edge"""
        return self._props["hostports"]

    @property
    def backend(self) -> EndpointBackend:
        """edge modules"""
        return self._props["backend"]

    @property
    def ip_restriction(self) -> EndpointIPPolicy:
        return self._props["ip_restriction"]

    @property
    def traffic_policy(self) -> EndpointTrafficPolicy:
        """the traffic policy associated with this edge or null"""
        return self._props["traffic_policy"]


class TLSEdgeList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["tls_edges"] = (
            [TLSEdge(client, x) for x in props["tls_edges"]]
            if props.get("tls_edges") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TLSEdgeList {} {}>".format(self.id, repr(self._props))
        else:
            return "<TLSEdgeList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "tls_edges")

    @property
    def tls_edges(self) -> Sequence[TLSEdge]:
        """the list of all TLS Edges on this account"""
        return self._props["tls_edges"]

    @property
    def uri(self) -> str:
        """URI of the TLS Edge list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class TLSEdge(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["backend"] = (
            EndpointBackend(client, props["backend"])
            if props.get("backend") is not None
            else None
        )
        self._props["ip_restriction"] = (
            EndpointIPPolicy(client, props["ip_restriction"])
            if props.get("ip_restriction") is not None
            else None
        )
        self._props["mutual_tls"] = (
            EndpointMutualTLS(client, props["mutual_tls"])
            if props.get("mutual_tls") is not None
            else None
        )
        self._props["tls_termination"] = (
            EndpointTLSTermination(client, props["tls_termination"])
            if props.get("tls_termination") is not None
            else None
        )
        self._props["traffic_policy"] = (
            EndpointTrafficPolicy(client, props["traffic_policy"])
            if props.get("traffic_policy") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TLSEdge {} {}>".format(self.id, repr(self._props))
        else:
            return "<TLSEdge {}>".format(repr(self._props))

    def update(
        self,
        description: str = None,
        metadata: str = None,
        hostports: Sequence[str] = None,
        backend: EndpointBackendMutate = None,
        ip_restriction: EndpointIPPolicyMutate = None,
        mutual_tls: EndpointMutualTLSMutate = None,
        tls_termination: EndpointTLSTermination = None,
        traffic_policy: EndpointTrafficPolicy = None,
    ):
        self._client.edges.tls.update(
            id=self.id,
            description=description,
            metadata=metadata,
            hostports=hostports,
            backend=backend,
            ip_restriction=ip_restriction,
            mutual_tls=mutual_tls,
            tls_termination=tls_termination,
            traffic_policy=traffic_policy,
        )

    def delete(
        self,
    ):
        self._client.edges.tls.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """unique identifier of this edge"""
        return self._props["id"]

    @property
    def description(self) -> str:
        """human-readable description of what this edge will be used for; optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this edge. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the edge configuration was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def uri(self) -> str:
        """URI of the edge API resource"""
        return self._props["uri"]

    @property
    def hostports(self) -> Sequence[str]:
        """hostports served by this edge"""
        return self._props["hostports"]

    @property
    def backend(self) -> EndpointBackend:
        """edge modules"""
        return self._props["backend"]

    @property
    def ip_restriction(self) -> EndpointIPPolicy:
        return self._props["ip_restriction"]

    @property
    def mutual_tls(self) -> EndpointMutualTLS:
        return self._props["mutual_tls"]

    @property
    def tls_termination(self) -> EndpointTLSTermination:
        return self._props["tls_termination"]

    @property
    def traffic_policy(self) -> EndpointTrafficPolicy:
        """the traffic policy associated with this edge or null"""
        return self._props["traffic_policy"]


class Endpoint(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["domain"] = (
            Ref(client, props["domain"]) if props.get("domain") is not None else None
        )
        self._props["tcp_addr"] = (
            Ref(client, props["tcp_addr"])
            if props.get("tcp_addr") is not None
            else None
        )
        self._props["tunnel"] = (
            Ref(client, props["tunnel"]) if props.get("tunnel") is not None else None
        )
        self._props["edge"] = (
            Ref(client, props["edge"]) if props.get("edge") is not None else None
        )
        self._props["principal"] = (
            Ref(client, props["principal"])
            if props.get("principal") is not None
            else None
        )
        self._props["tunnel_session"] = (
            Ref(client, props["tunnel_session"])
            if props.get("tunnel_session") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<Endpoint {} {}>".format(self.id, repr(self._props))
        else:
            return "<Endpoint {}>".format(repr(self._props))

    def update(
        self,
        url: str = None,
        traffic_policy: str = None,
        description: str = None,
        metadata: str = None,
        bindings: Sequence[str] = None,
        pooling_enabled: bool = False,
    ):
        self._client.endpoints.update(
            id=self.id,
            url=url,
            traffic_policy=traffic_policy,
            description=description,
            metadata=metadata,
            bindings=bindings,
            pooling_enabled=pooling_enabled,
        )

    def delete(
        self,
    ):
        self._client.endpoints.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """unique endpoint resource identifier"""
        return self._props["id"]

    @property
    def region(self) -> str:
        """identifier of the region this endpoint belongs to"""
        return self._props["region"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the endpoint was created in RFC 3339 format"""
        return self._props["created_at"]

    @property
    def updated_at(self) -> datetime:
        """timestamp when the endpoint was updated in RFC 3339 format"""
        return self._props["updated_at"]

    @property
    def public_url(self) -> str:
        """URL of the hostport served by this endpoint"""
        return self._props["public_url"]

    @property
    def proto(self) -> str:
        """protocol served by this endpoint. one of ``http``, ``https``, ``tcp``, or ``tls``"""
        return self._props["proto"]

    @property
    def scheme(self) -> str:
        return self._props["scheme"]

    @property
    def hostport(self) -> str:
        """hostport served by this endpoint (hostname:port) -> soon to be deprecated"""
        return self._props["hostport"]

    @property
    def host(self) -> str:
        return self._props["host"]

    @property
    def port(self) -> int:
        return self._props["port"]

    @property
    def type(self) -> str:
        """whether the endpoint is ``ephemeral`` (served directly by an agent-initiated tunnel) or ``edge`` (served by an edge) or ``cloud (represents a cloud endpoint)``"""
        return self._props["type"]

    @property
    def metadata(self) -> str:
        """user-supplied metadata of the associated tunnel or edge object"""
        return self._props["metadata"]

    @property
    def description(self) -> str:
        """user-supplied description of the associated tunnel"""
        return self._props["description"]

    @property
    def domain(self) -> Ref:
        """the domain reserved for this endpoint"""
        return self._props["domain"]

    @property
    def tcp_addr(self) -> Ref:
        """the address reserved for this endpoint"""
        return self._props["tcp_addr"]

    @property
    def tunnel(self) -> Ref:
        """the tunnel serving requests to this endpoint, if this is an ephemeral endpoint"""
        return self._props["tunnel"]

    @property
    def edge(self) -> Ref:
        """the edge serving requests to this endpoint, if this is an edge endpoint"""
        return self._props["edge"]

    @property
    def upstream_url(self) -> str:
        """the local address the tunnel forwards to"""
        return self._props["upstream_url"]

    @property
    def upstream_protocol(self) -> str:
        """the protocol the agent uses to forward with"""
        return self._props["upstream_protocol"]

    @property
    def url(self) -> str:
        """the url of the endpoint"""
        return self._props["url"]

    @property
    def principal(self) -> Ref:
        """The ID of the owner (bot or user) that owns this endpoint"""
        return self._props["principal"]

    @property
    def traffic_policy(self) -> str:
        """The traffic policy attached to this endpoint"""
        return self._props["traffic_policy"]

    @property
    def bindings(self) -> Sequence[str]:
        """the bindings associated with this endpoint"""
        return self._props["bindings"]

    @property
    def tunnel_session(self) -> Ref:
        """The tunnel session of the agent for this endpoint"""
        return self._props["tunnel_session"]

    @property
    def uri(self) -> str:
        """URI of the Cloud Endpoint API resource"""
        return self._props["uri"]

    @property
    def name(self) -> str:
        """user supplied name for the endpoint"""
        return self._props["name"]

    @property
    def pooling_enabled(self) -> bool:
        """whether the endpoint allows pooling"""
        return self._props["pooling_enabled"]


class EndpointList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["endpoints"] = (
            [Endpoint(client, x) for x in props["endpoints"]]
            if props.get("endpoints") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EndpointList {} {}>".format(self.id, repr(self._props))
        else:
            return "<EndpointList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "endpoints")

    @property
    def endpoints(self) -> Sequence[Endpoint]:
        """the list of all active endpoints on this account"""
        return self._props["endpoints"]

    @property
    def uri(self) -> str:
        """URI of the endpoints list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class EventDestination(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["target"] = (
            EventTarget(client, props["target"])
            if props.get("target") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventDestination {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventDestination {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.event_destinations.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """Unique identifier for this Event Destination."""
        return self._props["id"]

    @property
    def metadata(self) -> str:
        """Arbitrary user-defined machine-readable data of this Event Destination. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def created_at(self) -> datetime:
        """Timestamp when the Event Destination was created, RFC 3339 format."""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """Human-readable description of the Event Destination. Optional, max 255 bytes."""
        return self._props["description"]

    @property
    def format(self) -> str:
        """The output format you would like to serialize events into when sending to their target. Currently the only accepted value is ``JSON``."""
        return self._props["format"]

    @property
    def target(self) -> EventTarget:
        """An object that encapsulates where and how to send your events. An event destination must contain exactly one of the following objects, leaving the rest null: ``kinesis``, ``firehose``, ``cloudwatch_logs``, or ``s3``."""
        return self._props["target"]

    @property
    def uri(self) -> str:
        """URI of the Event Destination API resource."""
        return self._props["uri"]


class EventDestinationList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["event_destinations"] = (
            [EventDestination(client, x) for x in props["event_destinations"]]
            if props.get("event_destinations") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventDestinationList {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventDestinationList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "event_destinations")

    @property
    def event_destinations(self) -> Sequence[EventDestination]:
        """The list of all Event Destinations on this account."""
        return self._props["event_destinations"]

    @property
    def uri(self) -> str:
        """URI of the Event Destinations list API resource."""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page."""
        return self._props["next_page_uri"]


class EventTarget(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["firehose"] = (
            EventTargetFirehose(client, props["firehose"])
            if props.get("firehose") is not None
            else None
        )
        self._props["kinesis"] = (
            EventTargetKinesis(client, props["kinesis"])
            if props.get("kinesis") is not None
            else None
        )
        self._props["cloudwatch_logs"] = (
            EventTargetCloudwatchLogs(client, props["cloudwatch_logs"])
            if props.get("cloudwatch_logs") is not None
            else None
        )
        self._props["datadog"] = (
            EventTargetDatadog(client, props["datadog"])
            if props.get("datadog") is not None
            else None
        )
        self._props["azure_logs_ingestion"] = (
            EventTargetAzureLogsIngestion(client, props["azure_logs_ingestion"])
            if props.get("azure_logs_ingestion") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventTarget {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventTarget {}>".format(repr(self._props))

    @property
    def firehose(self) -> EventTargetFirehose:
        """Configuration used to send events to Amazon Kinesis Data Firehose."""
        return self._props["firehose"]

    @property
    def kinesis(self) -> EventTargetKinesis:
        """Configuration used to send events to Amazon Kinesis."""
        return self._props["kinesis"]

    @property
    def cloudwatch_logs(self) -> EventTargetCloudwatchLogs:
        """Configuration used to send events to Amazon CloudWatch Logs."""
        return self._props["cloudwatch_logs"]

    @property
    def datadog(self) -> EventTargetDatadog:
        """Configuration used to send events to Datadog."""
        return self._props["datadog"]

    @property
    def azure_logs_ingestion(self) -> EventTargetAzureLogsIngestion:
        return self._props["azure_logs_ingestion"]


class EventTargetFirehose(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["auth"] = (
            AWSAuth(client, props["auth"]) if props.get("auth") is not None else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventTargetFirehose {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventTargetFirehose {}>".format(repr(self._props))

    @property
    def auth(self) -> AWSAuth:
        """Configuration for how to authenticate into your AWS account. Exactly one of ``role`` or ``creds`` should be configured."""
        return self._props["auth"]

    @property
    def delivery_stream_arn(self) -> str:
        """An Amazon Resource Name specifying the Firehose delivery stream to deposit events into."""
        return self._props["delivery_stream_arn"]


class EventTargetKinesis(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["auth"] = (
            AWSAuth(client, props["auth"]) if props.get("auth") is not None else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventTargetKinesis {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventTargetKinesis {}>".format(repr(self._props))

    @property
    def auth(self) -> AWSAuth:
        """Configuration for how to authenticate into your AWS account. Exactly one of ``role`` or ``creds`` should be configured."""
        return self._props["auth"]

    @property
    def stream_arn(self) -> str:
        """An Amazon Resource Name specifying the Kinesis stream to deposit events into."""
        return self._props["stream_arn"]


class EventTargetCloudwatchLogs(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["auth"] = (
            AWSAuth(client, props["auth"]) if props.get("auth") is not None else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventTargetCloudwatchLogs {} {}>".format(
                self.id, repr(self._props)
            )
        else:
            return "<EventTargetCloudwatchLogs {}>".format(repr(self._props))

    @property
    def auth(self) -> AWSAuth:
        """Configuration for how to authenticate into your AWS account. Exactly one of ``role`` or ``creds`` should be configured."""
        return self._props["auth"]

    @property
    def log_group_arn(self) -> str:
        """An Amazon Resource Name specifying the CloudWatch Logs group to deposit events into."""
        return self._props["log_group_arn"]


class EventTargetDatadog(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventTargetDatadog {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventTargetDatadog {}>".format(repr(self._props))

    @property
    def api_key(self) -> str:
        """Datadog API key to use."""
        return self._props["api_key"]

    @property
    def ddtags(self) -> str:
        """Tags to send with the event."""
        return self._props["ddtags"]

    @property
    def service(self) -> str:
        """Service name to send with the event."""
        return self._props["service"]

    @property
    def ddsite(self) -> str:
        """Datadog site to send event to."""
        return self._props["ddsite"]


class EventTargetAzureLogsIngestion(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventTargetAzureLogsIngestion {} {}>".format(
                self.id, repr(self._props)
            )
        else:
            return "<EventTargetAzureLogsIngestion {}>".format(repr(self._props))

    @property
    def tenant_id(self) -> str:
        """Tenant ID for the Azure account"""
        return self._props["tenant_id"]

    @property
    def client_id(self) -> str:
        """Client ID for the application client"""
        return self._props["client_id"]

    @property
    def client_secret(self) -> str:
        """Client Secret for the application client"""
        return self._props["client_secret"]

    @property
    def logs_ingestion_uri(self) -> str:
        """Data collection endpoint logs ingestion URI"""
        return self._props["logs_ingestion_uri"]

    @property
    def data_collection_rule_id(self) -> str:
        """Data collection rule immutable ID"""
        return self._props["data_collection_rule_id"]

    @property
    def data_collection_stream_name(self) -> str:
        """Data collection stream name to use as destination, located inside the DCR"""
        return self._props["data_collection_stream_name"]


class AWSAuth(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["role"] = (
            AWSRole(client, props["role"]) if props.get("role") is not None else None
        )
        self._props["creds"] = (
            AWSCredentials(client, props["creds"])
            if props.get("creds") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<AWSAuth {} {}>".format(self.id, repr(self._props))
        else:
            return "<AWSAuth {}>".format(repr(self._props))

    @property
    def role(self) -> AWSRole:
        """A role for ngrok to assume on your behalf to deposit events into your AWS account."""
        return self._props["role"]

    @property
    def creds(self) -> AWSCredentials:
        """Credentials to your AWS account if you prefer ngrok to sign in with long-term access keys."""
        return self._props["creds"]


class AWSRole(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<AWSRole {} {}>".format(self.id, repr(self._props))
        else:
            return "<AWSRole {}>".format(repr(self._props))

    @property
    def role_arn(self) -> str:
        """An ARN that specifies the role that ngrok should use to deliver to the configured target."""
        return self._props["role_arn"]


class AWSCredentials(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<AWSCredentials {} {}>".format(self.id, repr(self._props))
        else:
            return "<AWSCredentials {}>".format(repr(self._props))

    @property
    def aws_access_key_id(self) -> str:
        """The ID portion of an AWS access key."""
        return self._props["aws_access_key_id"]

    @property
    def aws_secret_access_key(self) -> str:
        """The secret portion of an AWS access key."""
        return self._props["aws_secret_access_key"]


class EventSubscriptionList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["event_subscriptions"] = (
            [EventSubscription(client, x) for x in props["event_subscriptions"]]
            if props.get("event_subscriptions") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventSubscriptionList {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventSubscriptionList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "event_subscriptions")

    @property
    def event_subscriptions(self) -> Sequence[EventSubscription]:
        """The list of all Event Subscriptions on this account."""
        return self._props["event_subscriptions"]

    @property
    def uri(self) -> str:
        """URI of the Event Subscriptions list API resource."""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of next page, or null if there is no next page."""
        return self._props["next_page_uri"]


class EventSubscription(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["sources"] = (
            [EventSource(client, x) for x in props["sources"]]
            if props.get("sources") is not None
            else []
        )
        self._props["destinations"] = (
            [Ref(client, x) for x in props["destinations"]]
            if props.get("destinations") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventSubscription {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventSubscription {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.event_subscriptions.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """Unique identifier for this Event Subscription."""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the Event Subscription API resource."""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """When the Event Subscription was created (RFC 3339 format)."""
        return self._props["created_at"]

    @property
    def metadata(self) -> str:
        """Arbitrary customer supplied information intended to be machine readable. Optional, max 4096 chars."""
        return self._props["metadata"]

    @property
    def description(self) -> str:
        """Arbitrary customer supplied information intended to be human readable. Optional, max 255 chars."""
        return self._props["description"]

    @property
    def sources(self) -> Sequence[EventSource]:
        """Sources containing the types for which this event subscription will trigger"""
        return self._props["sources"]

    @property
    def destinations(self) -> Sequence[Ref]:
        """Destinations to which these events will be sent"""
        return self._props["destinations"]


class EventSourceReplace(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventSourceReplace {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventSourceReplace {}>".format(repr(self._props))

    @property
    def type(self) -> str:
        """Type of event for which an event subscription will trigger"""
        return self._props["type"]


class EventSource(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventSource {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventSource {}>".format(repr(self._props))

    @property
    def type(self) -> str:
        """Type of event for which an event subscription will trigger"""
        return self._props["type"]

    @property
    def uri(self) -> str:
        """URI of the Event Source API resource."""
        return self._props["uri"]


class EventSourceList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["sources"] = (
            [EventSource(client, x) for x in props["sources"]]
            if props.get("sources") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<EventSourceList {} {}>".format(self.id, repr(self._props))
        else:
            return "<EventSourceList {}>".format(repr(self._props))

    @property
    def sources(self) -> Sequence[EventSource]:
        """The list of all Event Sources for an Event Subscription"""
        return self._props["sources"]

    @property
    def uri(self) -> str:
        """URI of the next page, or null if there is no next page."""
        return self._props["uri"]


class IPPolicy(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<IPPolicy {} {}>".format(self.id, repr(self._props))
        else:
            return "<IPPolicy {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.ip_policies.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
    ):
        self._client.ip_policies.update(
            id=self.id,
            description=description,
            metadata=metadata,
        )

    @property
    def id(self) -> str:
        """unique identifier for this IP policy"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the IP Policy API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the IP policy was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of the source IPs of this IP policy. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this IP policy. optional, max 4096 bytes."""
        return self._props["metadata"]


class IPPolicyList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ip_policies"] = (
            [IPPolicy(client, x) for x in props["ip_policies"]]
            if props.get("ip_policies") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<IPPolicyList {} {}>".format(self.id, repr(self._props))
        else:
            return "<IPPolicyList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "ip_policies")

    @property
    def ip_policies(self) -> Sequence[IPPolicy]:
        """the list of all IP policies on this account"""
        return self._props["ip_policies"]

    @property
    def uri(self) -> str:
        """URI of the IP policy list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class IPPolicyRule(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ip_policy"] = (
            Ref(client, props["ip_policy"])
            if props.get("ip_policy") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<IPPolicyRule {} {}>".format(self.id, repr(self._props))
        else:
            return "<IPPolicyRule {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.ip_policy_rules.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
        cidr: str = None,
    ):
        self._client.ip_policy_rules.update(
            id=self.id,
            description=description,
            metadata=metadata,
            cidr=cidr,
        )

    @property
    def id(self) -> str:
        """unique identifier for this IP policy rule"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the IP policy rule API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the IP policy rule was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of the source IPs of this IP rule. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this IP policy rule. optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def cidr(self) -> str:
        """an IP or IP range specified in CIDR notation. IPv4 and IPv6 are both supported."""
        return self._props["cidr"]

    @property
    def ip_policy(self) -> Ref:
        """object describing the IP policy this IP Policy Rule belongs to"""
        return self._props["ip_policy"]

    @property
    def action(self) -> str:
        """the action to apply to the policy rule, either ``allow`` or ``deny``"""
        return self._props["action"]


class IPPolicyRuleList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ip_policy_rules"] = (
            [IPPolicyRule(client, x) for x in props["ip_policy_rules"]]
            if props.get("ip_policy_rules") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<IPPolicyRuleList {} {}>".format(self.id, repr(self._props))
        else:
            return "<IPPolicyRuleList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "ip_policy_rules")

    @property
    def ip_policy_rules(self) -> Sequence[IPPolicyRule]:
        """the list of all IP policy rules on this account"""
        return self._props["ip_policy_rules"]

    @property
    def uri(self) -> str:
        """URI of the IP policy rule list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class IPRestriction(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ip_policies"] = (
            [Ref(client, x) for x in props["ip_policies"]]
            if props.get("ip_policies") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<IPRestriction {} {}>".format(self.id, repr(self._props))
        else:
            return "<IPRestriction {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.ip_restrictions.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """unique identifier for this IP restriction"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the IP restriction API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the IP restriction was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this IP restriction. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this IP restriction. optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def enforced(self) -> bool:
        """true if the IP restriction will be enforced. if false, only warnings will be issued"""
        return self._props["enforced"]

    @property
    def type(self) -> str:
        """the type of IP restriction. this defines what traffic will be restricted with the attached policies. four values are currently supported: ``dashboard``, ``api``, ``agent``, and ``endpoints``"""
        return self._props["type"]

    @property
    def ip_policies(self) -> Sequence[Ref]:
        """the set of IP policies that are used to enforce the restriction"""
        return self._props["ip_policies"]


class IPRestrictionList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ip_restrictions"] = (
            [IPRestriction(client, x) for x in props["ip_restrictions"]]
            if props.get("ip_restrictions") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<IPRestrictionList {} {}>".format(self.id, repr(self._props))
        else:
            return "<IPRestrictionList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "ip_restrictions")

    @property
    def ip_restrictions(self) -> Sequence[IPRestriction]:
        """the list of all IP restrictions on this account"""
        return self._props["ip_restrictions"]

    @property
    def uri(self) -> str:
        """URI of the IP restrictions list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class ReservedAddr(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ReservedAddr {} {}>".format(self.id, repr(self._props))
        else:
            return "<ReservedAddr {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.reserved_addrs.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """unique reserved address resource identifier"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the reserved address API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the reserved address was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of what this reserved address will be used for"""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this reserved address. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def addr(self) -> str:
        """hostname:port of the reserved address that was assigned at creation time"""
        return self._props["addr"]

    @property
    def region(self) -> str:
        """reserve the address in this geographic ngrok datacenter. Optional, default is us. (au, eu, ap, us, jp, in, sa)"""
        return self._props["region"]


class ReservedAddrList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["reserved_addrs"] = (
            [ReservedAddr(client, x) for x in props["reserved_addrs"]]
            if props.get("reserved_addrs") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ReservedAddrList {} {}>".format(self.id, repr(self._props))
        else:
            return "<ReservedAddrList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "reserved_addrs")

    @property
    def reserved_addrs(self) -> Sequence[ReservedAddr]:
        """the list of all reserved addresses on this account"""
        return self._props["reserved_addrs"]

    @property
    def uri(self) -> str:
        """URI of the reserved address list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class ReservedDomain(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["certificate"] = (
            Ref(client, props["certificate"])
            if props.get("certificate") is not None
            else None
        )
        self._props["certificate_management_policy"] = (
            ReservedDomainCertPolicy(client, props["certificate_management_policy"])
            if props.get("certificate_management_policy") is not None
            else None
        )
        self._props["certificate_management_status"] = (
            ReservedDomainCertStatus(client, props["certificate_management_status"])
            if props.get("certificate_management_status") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ReservedDomain {} {}>".format(self.id, repr(self._props))
        else:
            return "<ReservedDomain {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.reserved_domains.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """unique reserved domain resource identifier"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the reserved domain API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the reserved domain was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of what this reserved domain will be used for"""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this reserved domain. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def domain(self) -> str:
        """hostname of the reserved domain"""
        return self._props["domain"]

    @property
    def region(self) -> str:
        """deprecated: With the launch of the ngrok Global Network domains traffic is now handled globally. This field applied only to endpoints. Note that agents may still connect to specific regions. Optional, null by default. (au, eu, ap, us, jp, in, sa)"""
        return self._props["region"]

    @property
    def cname_target(self) -> str:
        """DNS CNAME target for a custom hostname, or null if the reserved domain is a subdomain of an ngrok owned domain (e.g. *.ngrok.app)"""
        return self._props["cname_target"]

    @property
    def certificate(self) -> Ref:
        """object referencing the TLS certificate used for connections to this domain. This can be either a user-uploaded certificate, the most recently issued automatic one, or null otherwise."""
        return self._props["certificate"]

    @property
    def certificate_management_policy(self) -> ReservedDomainCertPolicy:
        """configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled"""
        return self._props["certificate_management_policy"]

    @property
    def certificate_management_status(self) -> ReservedDomainCertStatus:
        """status of the automatic certificate management for this domain, or null if automatic management is disabled"""
        return self._props["certificate_management_status"]

    @property
    def acme_challenge_cname_target(self) -> str:
        """DNS CNAME target for the host _acme-challenge.example.com, where example.com is your reserved domain name. This is required to issue certificates for wildcard, non-ngrok reserved domains. Must be null for non-wildcard domains and ngrok subdomains."""
        return self._props["acme_challenge_cname_target"]


class ReservedDomainList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["reserved_domains"] = (
            [ReservedDomain(client, x) for x in props["reserved_domains"]]
            if props.get("reserved_domains") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ReservedDomainList {} {}>".format(self.id, repr(self._props))
        else:
            return "<ReservedDomainList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "reserved_domains")

    @property
    def reserved_domains(self) -> Sequence[ReservedDomain]:
        """the list of all reserved domains on this account"""
        return self._props["reserved_domains"]

    @property
    def uri(self) -> str:
        """URI of the reserved domain list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class ReservedDomainCertPolicy(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ReservedDomainCertPolicy {} {}>".format(self.id, repr(self._props))
        else:
            return "<ReservedDomainCertPolicy {}>".format(repr(self._props))

    @property
    def authority(self) -> str:
        """certificate authority to request certificates from. The only supported value is letsencrypt."""
        return self._props["authority"]

    @property
    def private_key_type(self) -> str:
        """type of private key to use when requesting certificates. Defaults to ecdsa, can be either rsa or ecdsa."""
        return self._props["private_key_type"]


class ReservedDomainCertStatus(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["provisioning_job"] = (
            ReservedDomainCertJob(client, props["provisioning_job"])
            if props.get("provisioning_job") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ReservedDomainCertStatus {} {}>".format(self.id, repr(self._props))
        else:
            return "<ReservedDomainCertStatus {}>".format(repr(self._props))

    @property
    def renews_at(self) -> datetime:
        """timestamp when the next renewal will be requested, RFC 3339 format"""
        return self._props["renews_at"]

    @property
    def provisioning_job(self) -> ReservedDomainCertJob:
        """status of the certificate provisioning job, or null if the certificiate isn't being provisioned or renewed"""
        return self._props["provisioning_job"]


class ReservedDomainCertJob(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<ReservedDomainCertJob {} {}>".format(self.id, repr(self._props))
        else:
            return "<ReservedDomainCertJob {}>".format(repr(self._props))

    @property
    def error_code(self) -> str:
        """if present, an error code indicating why provisioning is failing. It may be either a temporary condition (INTERNAL_ERROR), or a permanent one the user must correct (DNS_ERROR)."""
        return self._props["error_code"]

    @property
    def msg(self) -> str:
        """a message describing the current status or error"""
        return self._props["msg"]

    @property
    def started_at(self) -> datetime:
        """timestamp when the provisioning job started, RFC 3339 format"""
        return self._props["started_at"]

    @property
    def retries_at(self) -> datetime:
        """timestamp when the provisioning job will be retried"""
        return self._props["retries_at"]


class Secret(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["created_by"] = (
            Ref(client, props["created_by"])
            if props.get("created_by") is not None
            else None
        )
        self._props["last_updated_by"] = (
            Ref(client, props["last_updated_by"])
            if props.get("last_updated_by") is not None
            else None
        )
        self._props["vault"] = (
            Ref(client, props["vault"]) if props.get("vault") is not None else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<Secret {} {}>".format(self.id, repr(self._props))
        else:
            return "<Secret {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.secrets.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """identifier for Secret"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of this Secret API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """Timestamp when the Secret was created (RFC 3339 format)"""
        return self._props["created_at"]

    @property
    def updated_at(self) -> datetime:
        """Timestamp when the Secret was last updated (RFC 3339 format)"""
        return self._props["updated_at"]

    @property
    def name(self) -> str:
        """Name of secret"""
        return self._props["name"]

    @property
    def description(self) -> str:
        """description of Secret"""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """Arbitrary user-defined metadata for this Secret"""
        return self._props["metadata"]

    @property
    def created_by(self) -> Ref:
        """Reference to who created this Secret"""
        return self._props["created_by"]

    @property
    def last_updated_by(self) -> Ref:
        """Reference to who created this Secret"""
        return self._props["last_updated_by"]

    @property
    def vault(self) -> Ref:
        """Reference to the vault the secret is stored in"""
        return self._props["vault"]


class SecretList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["secrets"] = (
            [Secret(client, x) for x in props["secrets"]]
            if props.get("secrets") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<SecretList {} {}>".format(self.id, repr(self._props))
        else:
            return "<SecretList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "secrets")

    @property
    def secrets(self) -> Sequence[Secret]:
        """The list of Secrets for this account"""
        return self._props["secrets"]

    @property
    def uri(self) -> str:
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page of results, or null if there is no next page"""
        return self._props["next_page_uri"]


class SSHCertificateAuthority(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<SSHCertificateAuthority {} {}>".format(self.id, repr(self._props))
        else:
            return "<SSHCertificateAuthority {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.ssh_certificate_authorities.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
    ):
        self._client.ssh_certificate_authorities.update(
            id=self.id,
            description=description,
            metadata=metadata,
        )

    @property
    def id(self) -> str:
        """unique identifier for this SSH Certificate Authority"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the SSH Certificate Authority API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the SSH Certificate Authority API resource was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this SSH Certificate Authority. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this SSH Certificate Authority. optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def public_key(self) -> str:
        """raw public key for this SSH Certificate Authority"""
        return self._props["public_key"]

    @property
    def key_type(self) -> str:
        """the type of private key for this SSH Certificate Authority"""
        return self._props["key_type"]


class SSHCertificateAuthorityList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ssh_certificate_authorities"] = (
            [
                SSHCertificateAuthority(client, x)
                for x in props["ssh_certificate_authorities"]
            ]
            if props.get("ssh_certificate_authorities") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<SSHCertificateAuthorityList {} {}>".format(
                self.id, repr(self._props)
            )
        else:
            return "<SSHCertificateAuthorityList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "ssh_certificate_authorities")

    @property
    def ssh_certificate_authorities(self) -> Sequence[SSHCertificateAuthority]:
        """the list of all certificate authorities on this account"""
        return self._props["ssh_certificate_authorities"]

    @property
    def uri(self) -> str:
        """URI of the certificates authorities list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class SSHCredential(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<SSHCredential {} {}>".format(self.id, repr(self._props))
        else:
            return "<SSHCredential {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.ssh_credentials.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
        acl: Sequence[str] = None,
    ):
        self._client.ssh_credentials.update(
            id=self.id,
            description=description,
            metadata=metadata,
            acl=acl,
        )

    @property
    def id(self) -> str:
        """unique ssh credential resource identifier"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the ssh credential API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the ssh credential was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of who or what will use the ssh credential to authenticate. Optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this ssh credential. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def public_key(self) -> str:
        """the PEM-encoded public key of the SSH keypair that will be used to authenticate"""
        return self._props["public_key"]

    @property
    def acl(self) -> Sequence[str]:
        """optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains, addresses, and labels the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules for domains may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. Bind rules for labels may specify a wildcard key and/or value to match multiple labels. For example, you may specify a rule of ``bind:*=example`` which will allow ``x=example``, ``y=example``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions."""
        return self._props["acl"]

    @property
    def owner_id(self) -> str:
        """If supplied at credential creation, ownership will be assigned to the specified User or Bot. Only admins may specify an owner other than themselves. Defaults to the authenticated User or Bot."""
        return self._props["owner_id"]


class SSHCredentialList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ssh_credentials"] = (
            [SSHCredential(client, x) for x in props["ssh_credentials"]]
            if props.get("ssh_credentials") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<SSHCredentialList {} {}>".format(self.id, repr(self._props))
        else:
            return "<SSHCredentialList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "ssh_credentials")

    @property
    def ssh_credentials(self) -> Sequence[SSHCredential]:
        """the list of all ssh credentials on this account"""
        return self._props["ssh_credentials"]

    @property
    def uri(self) -> str:
        """URI of the ssh credential list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class SSHHostCertificate(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<SSHHostCertificate {} {}>".format(self.id, repr(self._props))
        else:
            return "<SSHHostCertificate {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.ssh_host_certificates.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
    ):
        self._client.ssh_host_certificates.update(
            id=self.id,
            description=description,
            metadata=metadata,
        )

    @property
    def id(self) -> str:
        """unique identifier for this SSH Host Certificate"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the SSH Host Certificate API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the SSH Host Certificate API resource was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this SSH Host Certificate. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this SSH Host Certificate. optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def public_key(self) -> str:
        """a public key in OpenSSH Authorized Keys format that this certificate signs"""
        return self._props["public_key"]

    @property
    def key_type(self) -> str:
        """the key type of the ``public_key``, one of ``rsa``, ``ecdsa`` or ``ed25519``"""
        return self._props["key_type"]

    @property
    def ssh_certificate_authority_id(self) -> str:
        """the ssh certificate authority that is used to sign this ssh host certificate"""
        return self._props["ssh_certificate_authority_id"]

    @property
    def principals(self) -> Sequence[str]:
        """the list of principals included in the ssh host certificate. This is the list of hostnames and/or IP addresses that are authorized to serve SSH traffic with this certificate. Dangerously, if no principals are specified, this certificate is considered valid for all hosts."""
        return self._props["principals"]

    @property
    def valid_after(self) -> datetime:
        """the time when the ssh host certificate becomes valid, in RFC 3339 format."""
        return self._props["valid_after"]

    @property
    def valid_until(self) -> datetime:
        """the time after which the ssh host certificate becomes invalid, in RFC 3339 format. the OpenSSH certificates RFC calls this ``valid_before``."""
        return self._props["valid_until"]

    @property
    def certificate(self) -> str:
        """the signed SSH certificate in OpenSSH Authorized Keys format. this value should be placed in a ``-cert.pub`` certificate file on disk that should be referenced in your ``sshd_config`` configuration file with a ``HostCertificate`` directive"""
        return self._props["certificate"]


class SSHHostCertificateList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ssh_host_certificates"] = (
            [SSHHostCertificate(client, x) for x in props["ssh_host_certificates"]]
            if props.get("ssh_host_certificates") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<SSHHostCertificateList {} {}>".format(self.id, repr(self._props))
        else:
            return "<SSHHostCertificateList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "ssh_host_certificates")

    @property
    def ssh_host_certificates(self) -> Sequence[SSHHostCertificate]:
        """the list of all ssh host certificates on this account"""
        return self._props["ssh_host_certificates"]

    @property
    def uri(self) -> str:
        """URI of the ssh host certificates list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class SSHUserCertificate(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<SSHUserCertificate {} {}>".format(self.id, repr(self._props))
        else:
            return "<SSHUserCertificate {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.ssh_user_certificates.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
    ):
        self._client.ssh_user_certificates.update(
            id=self.id,
            description=description,
            metadata=metadata,
        )

    @property
    def id(self) -> str:
        """unique identifier for this SSH User Certificate"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the SSH User Certificate API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the SSH User Certificate API resource was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this SSH User Certificate. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this SSH User Certificate. optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def public_key(self) -> str:
        """a public key in OpenSSH Authorized Keys format that this certificate signs"""
        return self._props["public_key"]

    @property
    def key_type(self) -> str:
        """the key type of the ``public_key``, one of ``rsa``, ``ecdsa`` or ``ed25519``"""
        return self._props["key_type"]

    @property
    def ssh_certificate_authority_id(self) -> str:
        """the ssh certificate authority that is used to sign this ssh user certificate"""
        return self._props["ssh_certificate_authority_id"]

    @property
    def principals(self) -> Sequence[str]:
        """the list of principals included in the ssh user certificate. This is the list of usernames that the certificate holder may sign in as on a machine authorizing the signing certificate authority. Dangerously, if no principals are specified, this certificate may be used to log in as any user."""
        return self._props["principals"]

    @property
    def critical_options(self) -> Mapping[str, str]:
        """A map of critical options included in the certificate. Only two critical options are currently defined by OpenSSH: ``force-command`` and ``source-address``. See `the OpenSSH certificate protocol spec <https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys>`_ for additional details."""
        return self._props["critical_options"]

    @property
    def extensions(self) -> Mapping[str, str]:
        """A map of extensions included in the certificate. Extensions are additional metadata that can be interpreted by the SSH server for any purpose. These can be used to permit or deny the ability to open a terminal, do port forwarding, x11 forwarding, and more. If unspecified, the certificate will include limited permissions with the following extension map: ``{"permit-pty": "", "permit-user-rc": ""}`` OpenSSH understands a number of predefined extensions. See `the OpenSSH certificate protocol spec <https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys>`_ for additional details."""
        return self._props["extensions"]

    @property
    def valid_after(self) -> datetime:
        """the time when the ssh host certificate becomes valid, in RFC 3339 format."""
        return self._props["valid_after"]

    @property
    def valid_until(self) -> datetime:
        """the time after which the ssh host certificate becomes invalid, in RFC 3339 format. the OpenSSH certificates RFC calls this ``valid_before``."""
        return self._props["valid_until"]

    @property
    def certificate(self) -> str:
        """the signed SSH certificate in OpenSSH Authorized Keys Format. this value should be placed in a ``-cert.pub`` certificate file on disk that should be referenced in your ``sshd_config`` configuration file with a ``HostCertificate`` directive"""
        return self._props["certificate"]


class SSHUserCertificateList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ssh_user_certificates"] = (
            [SSHUserCertificate(client, x) for x in props["ssh_user_certificates"]]
            if props.get("ssh_user_certificates") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<SSHUserCertificateList {} {}>".format(self.id, repr(self._props))
        else:
            return "<SSHUserCertificateList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "ssh_user_certificates")

    @property
    def ssh_user_certificates(self) -> Sequence[SSHUserCertificate]:
        """the list of all ssh user certificates on this account"""
        return self._props["ssh_user_certificates"]

    @property
    def uri(self) -> str:
        """URI of the ssh user certificates list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class TLSCertificate(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["subject_alternative_names"] = (
            TLSCertificateSANs(client, props["subject_alternative_names"])
            if props.get("subject_alternative_names") is not None
            else None
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TLSCertificate {} {}>".format(self.id, repr(self._props))
        else:
            return "<TLSCertificate {}>".format(repr(self._props))

    def delete(
        self,
    ):
        self._client.tls_certificates.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
    ):
        self._client.tls_certificates.update(
            id=self.id,
            description=description,
            metadata=metadata,
        )

    @property
    def id(self) -> str:
        """unique identifier for this TLS certificate"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the TLS certificate API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """timestamp when the TLS certificate was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of this TLS certificate. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this TLS certificate. optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def certificate_pem(self) -> str:
        """chain of PEM-encoded certificates, leaf first. See `Certificate Bundles <https://ngrok.com/docs/cloud-edge/endpoints#certificate-chains>`_."""
        return self._props["certificate_pem"]

    @property
    def subject_common_name(self) -> str:
        """subject common name from the leaf of this TLS certificate"""
        return self._props["subject_common_name"]

    @property
    def subject_alternative_names(self) -> TLSCertificateSANs:
        """subject alternative names (SANs) from the leaf of this TLS certificate"""
        return self._props["subject_alternative_names"]

    @property
    def issued_at(self) -> datetime:
        """timestamp (in RFC 3339 format) when this TLS certificate was issued automatically, or null if this certificate was user-uploaded"""
        return self._props["issued_at"]

    @property
    def not_before(self) -> datetime:
        """timestamp when this TLS certificate becomes valid, RFC 3339 format"""
        return self._props["not_before"]

    @property
    def not_after(self) -> datetime:
        """timestamp when this TLS certificate becomes invalid, RFC 3339 format"""
        return self._props["not_after"]

    @property
    def key_usages(self) -> Sequence[str]:
        """set of actions the private key of this TLS certificate can be used for"""
        return self._props["key_usages"]

    @property
    def extended_key_usages(self) -> Sequence[str]:
        """extended set of actions the private key of this TLS certificate can be used for"""
        return self._props["extended_key_usages"]

    @property
    def private_key_type(self) -> str:
        """type of the private key of this TLS certificate. One of rsa, ecdsa, or ed25519."""
        return self._props["private_key_type"]

    @property
    def issuer_common_name(self) -> str:
        """issuer common name from the leaf of this TLS certificate"""
        return self._props["issuer_common_name"]

    @property
    def serial_number(self) -> str:
        """serial number of the leaf of this TLS certificate"""
        return self._props["serial_number"]

    @property
    def subject_organization(self) -> str:
        """subject organization from the leaf of this TLS certificate"""
        return self._props["subject_organization"]

    @property
    def subject_organizational_unit(self) -> str:
        """subject organizational unit from the leaf of this TLS certificate"""
        return self._props["subject_organizational_unit"]

    @property
    def subject_locality(self) -> str:
        """subject locality from the leaf of this TLS certificate"""
        return self._props["subject_locality"]

    @property
    def subject_province(self) -> str:
        """subject province from the leaf of this TLS certificate"""
        return self._props["subject_province"]

    @property
    def subject_country(self) -> str:
        """subject country from the leaf of this TLS certificate"""
        return self._props["subject_country"]


class TLSCertificateList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["tls_certificates"] = (
            [TLSCertificate(client, x) for x in props["tls_certificates"]]
            if props.get("tls_certificates") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TLSCertificateList {} {}>".format(self.id, repr(self._props))
        else:
            return "<TLSCertificateList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "tls_certificates")

    @property
    def tls_certificates(self) -> Sequence[TLSCertificate]:
        """the list of all TLS certificates on this account"""
        return self._props["tls_certificates"]

    @property
    def uri(self) -> str:
        """URI of the TLS certificates list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class TLSCertificateSANs(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TLSCertificateSANs {} {}>".format(self.id, repr(self._props))
        else:
            return "<TLSCertificateSANs {}>".format(repr(self._props))

    @property
    def dns_names(self) -> Sequence[str]:
        """set of additional domains (including wildcards) this TLS certificate is valid for"""
        return self._props["dns_names"]

    @property
    def ips(self) -> Sequence[str]:
        """set of IP addresses this TLS certificate is also valid for"""
        return self._props["ips"]


class Tunnel(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["tunnel_session"] = (
            Ref(client, props["tunnel_session"])
            if props.get("tunnel_session") is not None
            else None
        )
        self._props["endpoint"] = (
            Ref(client, props["endpoint"])
            if props.get("endpoint") is not None
            else None
        )
        self._props["backends"] = (
            [Ref(client, x) for x in props["backends"]]
            if props.get("backends") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<Tunnel {} {}>".format(self.id, repr(self._props))
        else:
            return "<Tunnel {}>".format(repr(self._props))

    @property
    def id(self) -> str:
        """unique tunnel resource identifier"""
        return self._props["id"]

    @property
    def public_url(self) -> str:
        """URL of the ephemeral tunnel's public endpoint"""
        return self._props["public_url"]

    @property
    def started_at(self) -> datetime:
        """timestamp when the tunnel was initiated in RFC 3339 format"""
        return self._props["started_at"]

    @property
    def metadata(self) -> str:
        """user-supplied metadata for the tunnel defined in the ngrok configuration file. See the tunnel `metadata configuration option <https://ngrok.com/docs/secure-tunnels/ngrok-agent/reference/config#common-tunnel-configuration-properties>`_ In API version 0, this value was instead pulled from the top-level `metadata configuration option <https://ngrok.com/docs/secure-tunnels/ngrok-agent/reference/config#metadata>`_."""
        return self._props["metadata"]

    @property
    def proto(self) -> str:
        """tunnel protocol for ephemeral tunnels. one of ``http``, ``https``, ``tcp`` or ``tls``"""
        return self._props["proto"]

    @property
    def region(self) -> str:
        """identifier of tune region where the tunnel is running"""
        return self._props["region"]

    @property
    def tunnel_session(self) -> Ref:
        """reference object pointing to the tunnel session on which this tunnel was started"""
        return self._props["tunnel_session"]

    @property
    def endpoint(self) -> Ref:
        """the ephemeral endpoint this tunnel is associated with, if this is an agent-initiated tunnel"""
        return self._props["endpoint"]

    @property
    def labels(self) -> Mapping[str, str]:
        """the labels the tunnel group backends will match against, if this is a backend tunnel"""
        return self._props["labels"]

    @property
    def backends(self) -> Sequence[Ref]:
        """tunnel group backends served by this backend tunnel"""
        return self._props["backends"]

    @property
    def forwards_to(self) -> str:
        """upstream address the ngrok agent forwards traffic over this tunnel to. this may be expressed as a URL or a network address."""
        return self._props["forwards_to"]


class TunnelList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["tunnels"] = (
            [Tunnel(client, x) for x in props["tunnels"]]
            if props.get("tunnels") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<TunnelList {} {}>".format(self.id, repr(self._props))
        else:
            return "<TunnelList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "tunnels")

    @property
    def tunnels(self) -> Sequence[Tunnel]:
        """the list of all online tunnels on this account"""
        return self._props["tunnels"]

    @property
    def uri(self) -> str:
        """URI of the tunnels list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class Vault(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<Vault {} {}>".format(self.id, repr(self._props))
        else:
            return "<Vault {}>".format(repr(self._props))

    def update(
        self,
        name: str = None,
        metadata: str = None,
        description: str = None,
    ):
        self._client.vaults.update(
            id=self.id,
            name=name,
            metadata=metadata,
            description=description,
        )

    def delete(
        self,
    ):
        self._client.vaults.delete(
            id=self.id,
        )

    @property
    def id(self) -> str:
        """identifier for Vault"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of this Vault API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> datetime:
        """Timestamp when the Vault was created (RFC 3339 format)"""
        return self._props["created_at"]

    @property
    def updated_at(self) -> datetime:
        """Timestamp when the Vault was last updated (RFC 3339 format)"""
        return self._props["updated_at"]

    @property
    def name(self) -> str:
        """Name of vault"""
        return self._props["name"]

    @property
    def description(self) -> str:
        """description of Vault"""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """Arbitrary user-defined metadata for this Vault"""
        return self._props["metadata"]

    @property
    def created_by(self) -> str:
        """Reference to who created this Vault"""
        return self._props["created_by"]

    @property
    def last_updated_by(self) -> str:
        """Reference to who created this Vault"""
        return self._props["last_updated_by"]


class VaultList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["vaults"] = (
            [Vault(client, x) for x in props["vaults"]]
            if props.get("vaults") is not None
            else []
        )

    def __eq__(self, other):
        return self._props == other._props

    def __str__(self):
        if "id" in self._props:
            return "<VaultList {} {}>".format(self.id, repr(self._props))
        else:
            return "<VaultList {}>".format(repr(self._props))

    def __iter__(self):
        return PagedIterator(self._client, self, "vaults")

    @property
    def vaults(self) -> Sequence[Vault]:
        """The list of Vaults for this account"""
        return self._props["vaults"]

    @property
    def uri(self) -> str:
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page of results, or null if there is no next page"""
        return self._props["next_page_uri"]
