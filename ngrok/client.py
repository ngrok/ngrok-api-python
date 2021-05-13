from __future__ import annotations
import collections
import os
from .services import *


class Client(object):
    def __init__(self, api_key: str = "", base_url: str = "https://api.ngrok.com"):
        self.api_key = api_key or os.getenv("NGROK_API_KEY")
        self.api_client = APIClient(api_key, base_url)

    @property
    def abuse_reports(self) -> AbuseReportsClient:
        return AbuseReportsClient(self)

    @property
    def api_keys(self) -> APIKeysClient:
        return APIKeysClient(self)

    @property
    def certificate_authorities(self) -> CertificateAuthoritiesClient:
        return CertificateAuthoritiesClient(self)

    @property
    def credentials(self) -> CredentialsClient:
        return CredentialsClient(self)

    @property
    def event_streams(self) -> EventStreamsClient:
        return EventStreamsClient(self)

    @property
    def event_destinations(self) -> EventDestinationsClient:
        return EventDestinationsClient(self)

    @property
    def ip_policies(self) -> IPPoliciesClient:
        return IPPoliciesClient(self)

    @property
    def ip_policy_rules(self) -> IPPolicyRulesClient:
        return IPPolicyRulesClient(self)

    @property
    def ip_restrictions(self) -> IPRestrictionsClient:
        return IPRestrictionsClient(self)

    @property
    def ip_whitelist(self) -> IPWhitelistClient:
        return IPWhitelistClient(self)

    @property
    def endpoint_configurations(self) -> EndpointConfigurationsClient:
        """Endpoint Configuration managementAn `Endpoint Configuration` <https://ngrok.com/docs/ngrok-link#api-endpoint-configurations>`_ describes
        a ngrok network endpoint instance.*Endpoints are your gateway to ngrok features!*"""
        return EndpointConfigurationsClient(self)

    @property
    def reserved_addrs(self) -> ReservedAddrsClient:
        return ReservedAddrsClient(self)

    @property
    def reserved_domains(self) -> ReservedDomainsClient:
        return ReservedDomainsClient(self)

    @property
    def ssh_certificate_authorities(self) -> SSHCertificateAuthoritiesClient:
        return SSHCertificateAuthoritiesClient(self)

    @property
    def ssh_credentials(self) -> SSHCredentialsClient:
        return SSHCredentialsClient(self)

    @property
    def ssh_host_certificates(self) -> SSHHostCertificatesClient:
        return SSHHostCertificatesClient(self)

    @property
    def ssh_user_certificates(self) -> SSHUserCertificatesClient:
        return SSHUserCertificatesClient(self)

    @property
    def tls_certificates(self) -> TLSCertificatesClient:
        return TLSCertificatesClient(self)

    @property
    def tunnel_sessions(self) -> TunnelSessionsClient:
        return TunnelSessionsClient(self)

    @property
    def tunnels(self) -> TunnelsClient:
        return TunnelsClient(self)

    @property
    def pointcfg_module(self):
        ns = collections.namedtuple(
            "Namespace",
            "logging",
            "circuit_breaker",
            "compression",
            "tls_termination",
            "ip_policy",
            "mutual_tls",
            "request_headers",
            "response_headers",
            "oauth",
            "webhook_validation",
            "saml",
            "oidc",
        )
        return ns(
            logging=EndpointLoggingModuleClient(self),
            circuit_breaker=EndpointCircuitBreakerModuleClient(self),
            compression=EndpointCompressionModuleClient(self),
            tls_termination=EndpointTLSTerminationModuleClient(self),
            ip_policy=EndpointIPPolicyModuleClient(self),
            mutual_tls=EndpointMutualTLSModuleClient(self),
            request_headers=EndpointRequestHeadersModuleClient(self),
            response_headers=EndpointResponseHeadersModuleClient(self),
            oauth=EndpointOAuthModuleClient(self),
            webhook_validation=EndpointWebhookValidationModuleClient(self),
            saml=EndpointSAMLModuleClient(self),
            oidc=EndpointOIDCModuleClient(self),
        )
