
from __future__ import annotations
import os
from .services import *

class Client(object):
    def __init__(self, api_key: str = os.getenv("NGROK_API_KEY", ""), base_url: str = "https://api.ngrok.com"):
        self.api_client = APIClient(api_key, base_url)
    @property
    def abuse_reports(self) -> AbuseReportsClient:
    	return AbuseReportsClient(self.api_client)
    @property
    def api_keys(self) -> APIKeysClient:
    	return APIKeysClient(self.api_client)
    @property
    def certificate_authorities(self) -> CertificateAuthoritiesClient:
    	return CertificateAuthoritiesClient(self.api_client)
    @property
    def credentials(self) -> CredentialsClient:
    	return CredentialsClient(self.api_client)
    @property
    def event_streams(self) -> EventStreamsClient:
    	return EventStreamsClient(self.api_client)
    @property
    def event_destinations(self) -> EventDestinationsClient:
    	return EventDestinationsClient(self.api_client)
    @property
    def ip_policies(self) -> IPPoliciesClient:
    	return IPPoliciesClient(self.api_client)
    @property
    def ip_policy_rules(self) -> IPPolicyRulesClient:
    	return IPPolicyRulesClient(self.api_client)
    @property
    def ip_restrictions(self) -> IPRestrictionsClient:
    	return IPRestrictionsClient(self.api_client)
    @property
    def ip_whitelist(self) -> IPWhitelistClient:
    	return IPWhitelistClient(self.api_client)
    @property
    def endpoint_configurations(self) -> EndpointConfigurationsClient:
    	return EndpointConfigurationsClient(self.api_client)
    @property
    def endpoint_logging_module(self) -> EndpointLoggingModuleClient:
    	return EndpointLoggingModuleClient(self.api_client)
    @property
    def endpoint_circuit_breaker_module(self) -> EndpointCircuitBreakerModuleClient:
    	return EndpointCircuitBreakerModuleClient(self.api_client)
    @property
    def endpoint_compression_module(self) -> EndpointCompressionModuleClient:
    	return EndpointCompressionModuleClient(self.api_client)
    @property
    def endpoint_tls_termination_module(self) -> EndpointTLSTerminationModuleClient:
    	return EndpointTLSTerminationModuleClient(self.api_client)
    @property
    def endpoint_ip_policy_module(self) -> EndpointIPPolicyModuleClient:
    	return EndpointIPPolicyModuleClient(self.api_client)
    @property
    def endpoint_mutual_tls_module(self) -> EndpointMutualTLSModuleClient:
    	return EndpointMutualTLSModuleClient(self.api_client)
    @property
    def endpoint_request_headers_module(self) -> EndpointRequestHeadersModuleClient:
    	return EndpointRequestHeadersModuleClient(self.api_client)
    @property
    def endpoint_response_headers_module(self) -> EndpointResponseHeadersModuleClient:
    	return EndpointResponseHeadersModuleClient(self.api_client)
    @property
    def endpoint_o_auth_module(self) -> EndpointOAuthModuleClient:
    	return EndpointOAuthModuleClient(self.api_client)
    @property
    def endpoint_webhook_validation_module(self) -> EndpointWebhookValidationModuleClient:
    	return EndpointWebhookValidationModuleClient(self.api_client)
    @property
    def endpoint_saml_module(self) -> EndpointSAMLModuleClient:
    	return EndpointSAMLModuleClient(self.api_client)
    @property
    def endpoint_oidc_module(self) -> EndpointOIDCModuleClient:
    	return EndpointOIDCModuleClient(self.api_client)
    @property
    def reserved_addrs(self) -> ReservedAddrsClient:
    	return ReservedAddrsClient(self.api_client)
    @property
    def reserved_domains(self) -> ReservedDomainsClient:
    	return ReservedDomainsClient(self.api_client)
    @property
    def ssh_certificate_authorities(self) -> SSHCertificateAuthoritiesClient:
    	return SSHCertificateAuthoritiesClient(self.api_client)
    @property
    def ssh_credentials(self) -> SSHCredentialsClient:
    	return SSHCredentialsClient(self.api_client)
    @property
    def ssh_host_certificates(self) -> SSHHostCertificatesClient:
    	return SSHHostCertificatesClient(self.api_client)
    @property
    def ssh_user_certificates(self) -> SSHUserCertificatesClient:
    	return SSHUserCertificatesClient(self.api_client)
    @property
    def tls_certificates(self) -> TLSCertificatesClient:
    	return TLSCertificatesClient(self.api_client)
    @property
    def tunnel_sessions(self) -> TunnelSessionsClient:
    	return TunnelSessionsClient(self.api_client)
    @property
    def tunnels(self) -> TunnelsClient:
    	return TunnelsClient(self.api_client)
