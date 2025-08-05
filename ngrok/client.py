# Code generated for API Clients. DO NOT EDIT.


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
        API <https://ngrok.com/docs/api#authentication>`_. You may use the API itself
        to provision and manage API Keys but you'll need to provision your first API
        key from the `API Keys page <https://dashboard.ngrok.com/api/keys>`_ on your
        ngrok.com dashboard."""
        return APIKeysClient(self)

    @property
    def application_sessions(self) -> ApplicationSessionsClient:
        return ApplicationSessionsClient(self)

    @property
    def application_users(self) -> ApplicationUsersClient:
        return ApplicationUsersClient(self)

    @property
    def tunnel_sessions(self) -> TunnelSessionsClient:
        """Tunnel Sessions represent instances of ngrok agents or SSH reverse tunnel
        sessions that are running and connected to the ngrok service. Each tunnel
        session can include one or more Tunnels."""
        return TunnelSessionsClient(self)

    @property
    def bot_users(self) -> BotUsersClient:
        return BotUsersClient(self)

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
        the ``ngrok config add-authtoken`` command or by specifying it in the ``ngrok.yml``
        configuration file with the ``authtoken`` property."""
        return CredentialsClient(self)

    @property
    def endpoints(self) -> EndpointsClient:
        """Endpoints provides an API for querying the endpoint objects
        which define what tunnel or edge is used to serve a hostport.
        Only active endpoints associated with a tunnel or backend are returned."""
        return EndpointsClient(self)

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
    def secrets(self) -> SecretsClient:
        """Secrets is an api service for securely storing and managing sensitive data such as secrets, credentials, and tokens."""
        return SecretsClient(self)

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
    def tunnels(self) -> TunnelsClient:
        """Tunnels provide endpoints to access services exposed by a running ngrok
        agent tunnel session or an SSH reverse tunnel session."""
        return TunnelsClient(self)

    @property
    def vaults(self) -> VaultsClient:
        """Vaults is an api service for securely storing and managing sensitive data such as secrets, credentials, and tokens."""
        return VaultsClient(self)

    @property
    def backends(self):
        ns = collections.namedtuple(
            "Namespace",
            [
                "failover",
                "http_response",
                "static_address",
                "tunnel_group",
                "weighted",
            ],
        )
        return ns(
            failover=FailoverBackendsClient(self),
            http_response=HTTPResponseBackendsClient(self),
            static_address=StaticBackendsClient(self),
            tunnel_group=TunnelGroupBackendsClient(self),
            weighted=WeightedBackendsClient(self),
        )

    @property
    def edges(self):
        ns = collections.namedtuple(
            "Namespace",
            [
                "https_routes",
                "https",
                "tcp",
                "tls",
            ],
        )
        return ns(
            https_routes=EdgesHTTPSRoutesClient(self),
            https=EdgesHTTPSClient(self),
            tcp=EdgesTCPClient(self),
            tls=EdgesTLSClient(self),
        )

    @property
    def edge_modules(self):
        ns = collections.namedtuple(
            "Namespace",
            [
                "https_edge_mutual_tls",
                "https_edge_tls_termination",
                "https_edge_route_backend",
                "https_edge_route_ip_restriction",
                "https_edge_route_request_headers",
                "https_edge_route_response_headers",
                "https_edge_route_compression",
                "https_edge_route_circuit_breaker",
                "https_edge_route_webhook_verification",
                "https_edge_route_oauth",
                "https_edge_route_saml",
                "https_edge_route_oidc",
                "https_edge_route_websocket_tcp_converter",
                "https_edge_route_user_agent_filter",
                "https_edge_route_traffic_policy",
                "tcp_edge_backend",
                "tcp_edge_ip_restriction",
                "tcp_edge_traffic_policy",
                "tls_edge_backend",
                "tls_edge_ip_restriction",
                "tls_edge_mutual_tls",
                "tls_edge_tls_termination",
                "tls_edge_traffic_policy",
            ],
        )
        return ns(
            https_edge_mutual_tls=HTTPSEdgeMutualTLSModuleClient(self),
            https_edge_tls_termination=HTTPSEdgeTLSTerminationModuleClient(self),
            https_edge_route_backend=EdgeRouteBackendModuleClient(self),
            https_edge_route_ip_restriction=EdgeRouteIPRestrictionModuleClient(self),
            https_edge_route_request_headers=EdgeRouteRequestHeadersModuleClient(self),
            https_edge_route_response_headers=EdgeRouteResponseHeadersModuleClient(
                self
            ),
            https_edge_route_compression=EdgeRouteCompressionModuleClient(self),
            https_edge_route_circuit_breaker=EdgeRouteCircuitBreakerModuleClient(self),
            https_edge_route_webhook_verification=EdgeRouteWebhookVerificationModuleClient(
                self
            ),
            https_edge_route_oauth=EdgeRouteOAuthModuleClient(self),
            https_edge_route_saml=EdgeRouteSAMLModuleClient(self),
            https_edge_route_oidc=EdgeRouteOIDCModuleClient(self),
            https_edge_route_websocket_tcp_converter=EdgeRouteWebsocketTCPConverterModuleClient(
                self
            ),
            https_edge_route_user_agent_filter=EdgeRouteUserAgentFilterModuleClient(
                self
            ),
            https_edge_route_traffic_policy=EdgeRouteTrafficPolicyModuleClient(self),
            tcp_edge_backend=TCPEdgeBackendModuleClient(self),
            tcp_edge_ip_restriction=TCPEdgeIPRestrictionModuleClient(self),
            tcp_edge_traffic_policy=TCPEdgeTrafficPolicyModuleClient(self),
            tls_edge_backend=TLSEdgeBackendModuleClient(self),
            tls_edge_ip_restriction=TLSEdgeIPRestrictionModuleClient(self),
            tls_edge_mutual_tls=TLSEdgeMutualTLSModuleClient(self),
            tls_edge_tls_termination=TLSEdgeTLSTerminationModuleClient(self),
            tls_edge_traffic_policy=TLSEdgeTrafficPolicyModuleClient(self),
        )
