from __future__ import annotations
import collections
import os
from .services import *


class Client(object):
    def __init__(self, api_key: str, base_url: str = "https://api.ngrok.com"):
        self.http_client = HTTPClient(api_key, base_url)

    @property
    def abuse_reports(self) -> AbuseReportsClient:
        """Abuse Reports allow you to submit take-down requests for URLs hosted by
        ngrok that violate ngrok's terms of service."""
        return AbuseReportsClient(self)

    @property
    def agent_ingresses(self) -> AgentIngressesClient:
        return AgentIngressesClient(self)

    @property
    def api_keys(self) -> APIKeysClient:
        """API Keys are used to authenticate to the `ngrok
        API` <https://ngrok.com/docs/api#authentication>`_. You may use the API itself
        to provision and manage API Keys but you'll need to provision your first API
        key from the `API Keys page` <https://dashboard.ngrok.com/api/keys>`_ on your
        ngrok.com dashboard."""
        return APIKeysClient(self)

    @property
    def certificate_authorities(self) -> CertificateAuthoritiesClient:
        """Certificate Authorities are x509 certificates that are used to sign other
        x509 certificates. Attach a Certificate Authority to the Mutual TLS module
        to verify that the TLS certificate presented by a client has been signed by
        this CA. Certificate Authorities  are used only for mTLS validation only and
        thus a private key is not included in the resource."""
        return CertificateAuthoritiesClient(self)

    @property
    def credentials(self) -> CredentialsClient:
        """Tunnel Credentials are ngrok agent authtokens. They authorize the ngrok
        agent to connect the ngrok service as your account. They are installed with
        the ``ngrok authtoken`` command or by specifying it in the ``ngrok.yml``
        configuration file with the ``authtoken`` property."""
        return CredentialsClient(self)

    @property
    def endpoint_configurations(self) -> EndpointConfigurationsClient:
        """Endpoint Configurations are a reusable group of modules that encapsulate how
        traffic to a domain or address is handled. Endpoint configurations are only
        applied to Domains and TCP Addresses they have been attached to."""
        return EndpointConfigurationsClient(self)

    @property
    def event_streams(self) -> EventStreamsClient:
        return EventStreamsClient(self)

    @property
    def event_destinations(self) -> EventDestinationsClient:
        return EventDestinationsClient(self)

    @property
    def event_subscriptions(self) -> EventSubscriptionsClient:
        return EventSubscriptionsClient(self)

    @property
    def event_sources(self) -> EventSourcesClient:
        return EventSourcesClient(self)

    @property
    def ip_policies(self) -> IPPoliciesClient:
        """IP Policies are reusable groups of CIDR ranges with an ``allow`` or ``deny``
        action. They can be attached to endpoints via the Endpoint Configuration IP
        Policy module. They can also be used with IP Restrictions to control source
        IP ranges that can start tunnel sessions and connect to the API and dashboard."""
        return IPPoliciesClient(self)

    @property
    def ip_policy_rules(self) -> IPPolicyRulesClient:
        """IP Policy Rules are the IPv4 or IPv6 CIDRs entries that
        make up an IP Policy."""
        return IPPolicyRulesClient(self)

    @property
    def ip_restrictions(self) -> IPRestrictionsClient:
        """An IP restriction is a restriction placed on the CIDRs that are allowed to
        initiate traffic to a specific aspect of your ngrok account. An IP
        restriction has a type which defines the ingress it applies to. IP
        restrictions can be used to enforce the source IPs that can make API
        requests, log in to the dashboard, start ngrok agents, and connect to your
        public-facing endpoints."""
        return IPRestrictionsClient(self)

    @property
    def reserved_addrs(self) -> ReservedAddrsClient:
        """Reserved Addresses are TCP addresses that can be used to listen for traffic.
        TCP address hostnames and ports are assigned by ngrok, they cannot be
        chosen."""
        return ReservedAddrsClient(self)

    @property
    def reserved_domains(self) -> ReservedDomainsClient:
        """Reserved Domains are hostnames that you can listen for traffic on. Domains
        can be used to listen for http, https or tls traffic. You may use a domain
        that you own by creating a CNAME record specified in the returned resource.
        This CNAME record points traffic for that domain to ngrok's edge servers."""
        return ReservedDomainsClient(self)

    @property
    def ssh_certificate_authorities(self) -> SSHCertificateAuthoritiesClient:
        """An SSH Certificate Authority is a pair of an SSH Certificate and its private
        key that can be used to sign other SSH host and user certificates."""
        return SSHCertificateAuthoritiesClient(self)

    @property
    def ssh_credentials(self) -> SSHCredentialsClient:
        """SSH Credentials are SSH public keys that can be used to start SSH tunnels
        via the ngrok SSH tunnel gateway."""
        return SSHCredentialsClient(self)

    @property
    def ssh_host_certificates(self) -> SSHHostCertificatesClient:
        """SSH Host Certificates along with the corresponding private key allows an SSH
        server to assert its authenticity to connecting SSH clients who trust the
        SSH Certificate Authority that was used to sign the certificate."""
        return SSHHostCertificatesClient(self)

    @property
    def ssh_user_certificates(self) -> SSHUserCertificatesClient:
        """SSH User Certificates are presented by SSH clients when connecting to an SSH
        server to authenticate their connection. The SSH server must trust the SSH
        Certificate Authority used to sign the certificate."""
        return SSHUserCertificatesClient(self)

    @property
    def tls_certificates(self) -> TLSCertificatesClient:
        """TLS Certificates are pairs of x509 certificates and their matching private
        key that can be used to terminate TLS traffic. TLS certificates are unused
        until they are attached to a Domain. TLS Certificates may also be
        provisioned by ngrok automatically for domains on which you have enabled
        automated certificate provisioning."""
        return TLSCertificatesClient(self)

    @property
    def tunnel_sessions(self) -> TunnelSessionsClient:
        """Tunnel Sessions represent instances of ngrok agents or SSH reverse tunnel
        sessions that are running and connected to the ngrok service. Each tunnel
        session can include one or more Tunnels."""
        return TunnelSessionsClient(self)

    @property
    def tunnels(self) -> TunnelsClient:
        """Tunnels provide endpoints to access services exposed by a running ngrok
        agent tunnel session or an SSH reverse tunnel session."""
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
