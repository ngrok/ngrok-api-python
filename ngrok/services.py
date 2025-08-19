# Code generated for API Clients. DO NOT EDIT.


from __future__ import annotations
from collections.abc import Iterator
from typing import Any, Mapping, Sequence
from datetime import datetime, timedelta

from .http_client import HTTPClient
from .datatypes import *
from .utils import *


class AbuseReportsClient(object):
    """Abuse Reports allow you to submit take-down requests for URLs hosted by
    ngrok that violate ngrok's terms of service."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        urls: Sequence[str],
        metadata: str = "",
    ) -> AbuseReport:
        """Creates a new abuse report which will be reviewed by our system and abuse response team. This API is only available to authorized accounts. Contact abuse@ngrok.com to request access

        :param urls: a list of URLs containing suspected abusive content
        :param metadata: arbitrary user-defined data about this abuse report. Optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-abuse-reports-create
        """
        path = "/abuse_reports"
        body_arg = dict(
            urls=urls,
            metadata=metadata,
        )
        result = self._client.http_client.post(path, body_arg)
        return AbuseReport(self._client, result)

    def get(
        self,
        id: str,
    ) -> AbuseReport:
        """Get the detailed status of abuse report by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-abuse-reports-get
        """
        path = "/abuse_reports/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return AbuseReport(self._client, result)


class AgentIngressesClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        domain: str,
        description: str = "",
        metadata: str = "",
        certificate_management_policy: AgentIngressCertPolicy = None,
    ) -> AgentIngress:
        """Create a new Agent Ingress. The ngrok agent can be configured to connect to ngrok via the new set of addresses on the returned Agent Ingress.

        :param description: human-readable description of the use of this Agent Ingress. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this Agent Ingress. optional, max 4096 bytes
        :param domain: the domain that you own to be used as the base domain name to generate regional agent ingress domains.
        :param certificate_management_policy: configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled. Optional.

        https://ngrok.com/docs/api#api-agent-ingresses-create
        """
        path = "/agent_ingresses"
        body_arg = dict(
            description=description,
            metadata=metadata,
            domain=domain,
            certificate_management_policy=extract_props(certificate_management_policy),
        )
        result = self._client.http_client.post(path, body_arg)
        return AgentIngress(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an Agent Ingress by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-agent-ingresses-delete
        """
        path = "/agent_ingresses/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> AgentIngress:
        """Get the details of an Agent Ingress by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-agent-ingresses-get
        """
        path = "/agent_ingresses/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return AgentIngress(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> AgentIngressList:
        """List all Agent Ingresses owned by this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-agent-ingresses-list
        """
        path = "/agent_ingresses"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return AgentIngressList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        certificate_management_policy: AgentIngressCertPolicy = None,
    ) -> AgentIngress:
        """Update attributes of an Agent Ingress by ID.

        :param id:
        :param description: human-readable description of the use of this Agent Ingress. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this Agent Ingress. optional, max 4096 bytes
        :param certificate_management_policy: configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled. Optional.

        https://ngrok.com/docs/api#api-agent-ingresses-update
        """
        path = "/agent_ingresses/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            certificate_management_policy=extract_props(certificate_management_policy),
        )
        result = self._client.http_client.patch(path, body_arg)
        return AgentIngress(self._client, result)


class APIKeysClient(object):
    """API Keys are used to authenticate to the `ngrok
    API <https://ngrok.com/docs/api#authentication>`_. You may use the API itself
    to provision and manage API Keys but you'll need to provision your first API
    key from the `API Keys page <https://dashboard.ngrok.com/api/keys>`_ on your
    ngrok.com dashboard."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        owner_id: str = None,
    ) -> APIKey:
        """Create a new API key. The generated API key can be used to authenticate to the ngrok API.

        :param description: human-readable description of what uses the API key to authenticate. optional, max 255 bytes.
        :param metadata: arbitrary user-defined data of this API key. optional, max 4096 bytes
        :param owner_id: If supplied at credential creation, ownership will be assigned to the specified User or Bot. Only admins may specify an owner other than themselves. Defaults to the authenticated User or Bot.

        https://ngrok.com/docs/api#api-api-keys-create
        """
        path = "/api_keys"
        body_arg = dict(
            description=description,
            metadata=metadata,
            owner_id=owner_id,
        )
        result = self._client.http_client.post(path, body_arg)
        return APIKey(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an API key by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-api-keys-delete
        """
        path = "/api_keys/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> APIKey:
        """Get the details of an API key by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-api-keys-get
        """
        path = "/api_keys/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return APIKey(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> APIKeyList:
        """List all API keys owned by this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-api-keys-list
        """
        path = "/api_keys"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return APIKeyList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
    ) -> APIKey:
        """Update attributes of an API key by ID.

        :param id:
        :param description: human-readable description of what uses the API key to authenticate. optional, max 255 bytes.
        :param metadata: arbitrary user-defined data of this API key. optional, max 4096 bytes

        https://ngrok.com/docs/api#api-api-keys-update
        """
        path = "/api_keys/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.patch(path, body_arg)
        return APIKey(self._client, result)


class ApplicationSessionsClient(object):
    def __init__(self, client):
        self._client = client

    def get(
        self,
        id: str,
    ) -> ApplicationSession:
        """Get an application session by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-application-sessions-get
        """
        path = "/app/sessions/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return ApplicationSession(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an application session by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-application-sessions-delete
        """
        path = "/app/sessions/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> ApplicationSessionList:
        """List all application sessions for this account.

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-application-sessions-list
        """
        path = "/app/sessions"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return ApplicationSessionList(self._client, result)


class ApplicationUsersClient(object):
    def __init__(self, client):
        self._client = client

    def get(
        self,
        id: str,
    ) -> ApplicationUser:
        """Get an application user by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-application-users-get
        """
        path = "/app/users/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return ApplicationUser(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an application user by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-application-users-delete
        """
        path = "/app/users/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> ApplicationUserList:
        """List all application users for this account.

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-application-users-list
        """
        path = "/app/users"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return ApplicationUserList(self._client, result)


class TunnelSessionsClient(object):
    """Tunnel Sessions represent instances of ngrok agents or SSH reverse tunnel
    sessions that are running and connected to the ngrok service. Each tunnel
    session can include one or more Tunnels."""

    def __init__(self, client):
        self._client = client

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> TunnelSessionList:
        """List all online tunnel sessions running on this account.

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-tunnel-sessions-list
        """
        path = "/tunnel_sessions"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return TunnelSessionList(self._client, result)

    def get(
        self,
        id: str,
    ) -> TunnelSession:
        """Get the detailed status of a tunnel session by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tunnel-sessions-get
        """
        path = "/tunnel_sessions/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return TunnelSession(self._client, result)

    def restart(
        self,
        id: str,
    ):
        """Issues a command instructing the ngrok agent to restart. The agent restarts itself by calling exec() on platforms that support it. This operation is notably not supported on Windows. When an agent restarts, it reconnects with a new tunnel session ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tunnel-sessions-restart
        """
        path = "/tunnel_sessions/{id}/restart"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.post(path, body_arg)

    def stop(
        self,
        id: str,
    ):
        """Issues a command instructing the ngrok agent that started this tunnel session to exit.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tunnel-sessions-stop
        """
        path = "/tunnel_sessions/{id}/stop"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.post(path, body_arg)

    def update(
        self,
        id: str,
    ):
        """Issues a command instructing the ngrok agent to update itself to the latest version. After this call completes successfully, the ngrok agent will be in the update process. A caller should wait some amount of time to allow the update to complete (at least 10 seconds) before making a call to the Restart endpoint to request that the agent restart itself to start using the new code. This call will never update an ngrok agent to a new major version which could cause breaking compatibility issues. If you wish to update to a new major version, that must be done manually. Still, please be aware that updating your ngrok agent could break your integration. This call will fail in any of the following circumstances: there is no update available the ngrok agent's configuration disabled update checks the agent is currently in process of updating the agent has already successfully updated but has not yet been restarted

        :param id:

        https://ngrok.com/docs/api#api-tunnel-sessions-update
        """
        path = "/tunnel_sessions/{id}/update"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.post(path, body_arg)


class FailoverBackendsClient(object):
    """A Failover backend defines failover behavior within a list of referenced
    backends. Traffic is sent to the first backend in the list. If that backend
    is offline or no connection can be established, ngrok attempts to connect to
    the next backend in the list until one is successful."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        backends: Sequence[str] = [],
    ) -> FailoverBackend:
        """Create a new Failover backend

        :param description: human-readable description of this backend. Optional
        :param metadata: arbitrary user-defined machine-readable data of this backend. Optional
        :param backends: the ids of the child backends in order

        https://ngrok.com/docs/api#api-failover-backends-create
        """
        path = "/backends/failover"
        body_arg = dict(
            description=description,
            metadata=metadata,
            backends=backends,
        )
        result = self._client.http_client.post(path, body_arg)
        return FailoverBackend(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a Failover backend by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-failover-backends-delete
        """
        path = "/backends/failover/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> FailoverBackend:
        """Get detailed information about a Failover backend by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-failover-backends-get
        """
        path = "/backends/failover/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return FailoverBackend(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> FailoverBackendList:
        """List all Failover backends on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-failover-backends-list
        """
        path = "/backends/failover"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return FailoverBackendList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        backends: Sequence[str] = [],
    ) -> FailoverBackend:
        """Update Failover backend by ID

        :param id:
        :param description: human-readable description of this backend. Optional
        :param metadata: arbitrary user-defined machine-readable data of this backend. Optional
        :param backends: the ids of the child backends in order

        https://ngrok.com/docs/api#api-failover-backends-update
        """
        path = "/backends/failover/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            backends=backends,
        )
        result = self._client.http_client.patch(path, body_arg)
        return FailoverBackend(self._client, result)


class HTTPResponseBackendsClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        body: str = "",
        headers: Mapping[str, str] = {},
        status_code: int = None,
    ) -> HTTPResponseBackend:
        """

        :param description: human-readable description of this backend. Optional
        :param metadata: arbitrary user-defined machine-readable data of this backend. Optional
        :param body: body to return as fixed content
        :param headers: headers to return
        :param status_code: status code to return

        https://ngrok.com/docs/api#api-http-response-backends-create
        """
        path = "/backends/http_response"
        body_arg = dict(
            description=description,
            metadata=metadata,
            body=body,
            headers=headers,
            status_code=status_code,
        )
        result = self._client.http_client.post(path, body_arg)
        return HTTPResponseBackend(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-http-response-backends-delete
        """
        path = "/backends/http_response/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> HTTPResponseBackend:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-http-response-backends-get
        """
        path = "/backends/http_response/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return HTTPResponseBackend(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> HTTPResponseBackendList:
        """

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-http-response-backends-list
        """
        path = "/backends/http_response"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return HTTPResponseBackendList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        body: str = None,
        headers: Mapping[str, str] = None,
        status_code: int = None,
    ) -> HTTPResponseBackend:
        """

        :param id:
        :param description: human-readable description of this backend. Optional
        :param metadata: arbitrary user-defined machine-readable data of this backend. Optional
        :param body: body to return as fixed content
        :param headers: headers to return
        :param status_code: status code to return

        https://ngrok.com/docs/api#api-http-response-backends-update
        """
        path = "/backends/http_response/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            body=body,
            headers=headers,
            status_code=status_code,
        )
        result = self._client.http_client.patch(path, body_arg)
        return HTTPResponseBackend(self._client, result)


class StaticBackendsClient(object):
    """A static backend sends traffic to a TCP address (hostname and port) that
    is reachable on the public internet."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        address: str = "",
        tls: StaticBackendTLS = None,
    ) -> StaticBackend:
        """Create a new static backend

        :param description: human-readable description of this backend. Optional
        :param metadata: arbitrary user-defined machine-readable data of this backend. Optional
        :param address: the address to forward to
        :param tls: tls configuration to use

        https://ngrok.com/docs/api#api-static-backends-create
        """
        path = "/backends/static"
        body_arg = dict(
            description=description,
            metadata=metadata,
            address=address,
            tls=extract_props(tls),
        )
        result = self._client.http_client.post(path, body_arg)
        return StaticBackend(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a static backend by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-static-backends-delete
        """
        path = "/backends/static/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> StaticBackend:
        """Get detailed information about a static backend by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-static-backends-get
        """
        path = "/backends/static/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return StaticBackend(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> StaticBackendList:
        """List all static backends on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-static-backends-list
        """
        path = "/backends/static"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return StaticBackendList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        address: str = "",
        tls: StaticBackendTLS = None,
    ) -> StaticBackend:
        """Update static backend by ID

        :param id:
        :param description: human-readable description of this backend. Optional
        :param metadata: arbitrary user-defined machine-readable data of this backend. Optional
        :param address: the address to forward to
        :param tls: tls configuration to use

        https://ngrok.com/docs/api#api-static-backends-update
        """
        path = "/backends/static/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            address=address,
            tls=extract_props(tls),
        )
        result = self._client.http_client.patch(path, body_arg)
        return StaticBackend(self._client, result)


class TunnelGroupBackendsClient(object):
    """A Tunnel Group Backend balances traffic among all online tunnels that match
    a label selector."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        labels: Mapping[str, str] = {},
    ) -> TunnelGroupBackend:
        """Create a new TunnelGroup backend

        :param description: human-readable description of this backend. Optional
        :param metadata: arbitrary user-defined machine-readable data of this backend. Optional
        :param labels: labels to watch for tunnels on, e.g. app->foo, dc->bar

        https://ngrok.com/docs/api#api-tunnel-group-backends-create
        """
        path = "/backends/tunnel_group"
        body_arg = dict(
            description=description,
            metadata=metadata,
            labels=labels,
        )
        result = self._client.http_client.post(path, body_arg)
        return TunnelGroupBackend(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a TunnelGroup backend by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tunnel-group-backends-delete
        """
        path = "/backends/tunnel_group/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> TunnelGroupBackend:
        """Get detailed information about a TunnelGroup backend by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tunnel-group-backends-get
        """
        path = "/backends/tunnel_group/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return TunnelGroupBackend(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> TunnelGroupBackendList:
        """List all TunnelGroup backends on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-tunnel-group-backends-list
        """
        path = "/backends/tunnel_group"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return TunnelGroupBackendList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        labels: Mapping[str, str] = {},
    ) -> TunnelGroupBackend:
        """Update TunnelGroup backend by ID

        :param id:
        :param description: human-readable description of this backend. Optional
        :param metadata: arbitrary user-defined machine-readable data of this backend. Optional
        :param labels: labels to watch for tunnels on, e.g. app->foo, dc->bar

        https://ngrok.com/docs/api#api-tunnel-group-backends-update
        """
        path = "/backends/tunnel_group/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            labels=labels,
        )
        result = self._client.http_client.patch(path, body_arg)
        return TunnelGroupBackend(self._client, result)


class WeightedBackendsClient(object):
    """A Weighted Backend balances traffic among the referenced backends. Traffic
    is assigned proportionally to each based on its weight. The percentage of
    traffic is calculated by dividing a backend's weight by the sum of all
    weights."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        backends: Mapping[str, int] = {},
    ) -> WeightedBackend:
        """Create a new Weighted backend

        :param description: human-readable description of this backend. Optional
        :param metadata: arbitrary user-defined machine-readable data of this backend. Optional
        :param backends: the ids of the child backends to their weights [0-10000]

        https://ngrok.com/docs/api#api-weighted-backends-create
        """
        path = "/backends/weighted"
        body_arg = dict(
            description=description,
            metadata=metadata,
            backends=backends,
        )
        result = self._client.http_client.post(path, body_arg)
        return WeightedBackend(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a Weighted backend by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-weighted-backends-delete
        """
        path = "/backends/weighted/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> WeightedBackend:
        """Get detailed information about a Weighted backend by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-weighted-backends-get
        """
        path = "/backends/weighted/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return WeightedBackend(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> WeightedBackendList:
        """List all Weighted backends on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-weighted-backends-list
        """
        path = "/backends/weighted"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return WeightedBackendList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        backends: Mapping[str, int] = {},
    ) -> WeightedBackend:
        """Update Weighted backend by ID

        :param id:
        :param description: human-readable description of this backend. Optional
        :param metadata: arbitrary user-defined machine-readable data of this backend. Optional
        :param backends: the ids of the child backends to their weights [0-10000]

        https://ngrok.com/docs/api#api-weighted-backends-update
        """
        path = "/backends/weighted/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            backends=backends,
        )
        result = self._client.http_client.patch(path, body_arg)
        return WeightedBackend(self._client, result)


class BotUsersClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        name: str = "",
        active: bool = None,
    ) -> BotUser:
        """Create a new bot user

        :param name: human-readable name used to identify the bot
        :param active: whether or not the bot is active

        https://ngrok.com/docs/api#api-bot-users-create
        """
        path = "/bot_users"
        body_arg = dict(
            name=name,
            active=active,
        )
        result = self._client.http_client.post(path, body_arg)
        return BotUser(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a bot user by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-bot-users-delete
        """
        path = "/bot_users/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> BotUser:
        """Get the details of a Bot User by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-bot-users-get
        """
        path = "/bot_users/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return BotUser(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> BotUserList:
        """List all bot users in this account.

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-bot-users-list
        """
        path = "/bot_users"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return BotUserList(self._client, result)

    def update(
        self,
        id: str,
        name: str = None,
        active: bool = None,
    ) -> BotUser:
        """Update attributes of a bot user by ID.

        :param id:
        :param name: human-readable name used to identify the bot
        :param active: whether or not the bot is active

        https://ngrok.com/docs/api#api-bot-users-update
        """
        path = "/bot_users/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            name=name,
            active=active,
        )
        result = self._client.http_client.patch(path, body_arg)
        return BotUser(self._client, result)


class CertificateAuthoritiesClient(object):
    """Certificate Authorities are x509 certificates that are used to sign other
    x509 certificates. Attach a Certificate Authority to the Mutual TLS module
    to verify that the TLS certificate presented by a client has been signed by
    this CA. Certificate Authorities  are used only for mTLS validation only and
    thus a private key is not included in the resource."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        ca_pem: str,
        description: str = "",
        metadata: str = "",
    ) -> CertificateAuthority:
        """Upload a new Certificate Authority

        :param description: human-readable description of this Certificate Authority. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this Certificate Authority. optional, max 4096 bytes.
        :param ca_pem: raw PEM of the Certificate Authority

        https://ngrok.com/docs/api#api-certificate-authorities-create
        """
        path = "/certificate_authorities"
        body_arg = dict(
            description=description,
            metadata=metadata,
            ca_pem=ca_pem,
        )
        result = self._client.http_client.post(path, body_arg)
        return CertificateAuthority(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a Certificate Authority

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-certificate-authorities-delete
        """
        path = "/certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> CertificateAuthority:
        """Get detailed information about a certficate authority

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-certificate-authorities-get
        """
        path = "/certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return CertificateAuthority(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> CertificateAuthorityList:
        """List all Certificate Authority on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-certificate-authorities-list
        """
        path = "/certificate_authorities"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return CertificateAuthorityList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
    ) -> CertificateAuthority:
        """Update attributes of a Certificate Authority by ID

        :param id:
        :param description: human-readable description of this Certificate Authority. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this Certificate Authority. optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-certificate-authorities-update
        """
        path = "/certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.patch(path, body_arg)
        return CertificateAuthority(self._client, result)


class CredentialsClient(object):
    """Tunnel Credentials are ngrok agent authtokens. They authorize the ngrok
    agent to connect the ngrok service as your account. They are installed with
    the ``ngrok config add-authtoken`` command or by specifying it in the ``ngrok.yml``
    configuration file with the ``authtoken`` property."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        acl: Sequence[str] = [],
        owner_id: str = None,
    ) -> Credential:
        """Create a new tunnel authtoken credential. This authtoken credential can be used to start a new tunnel session. The response to this API call is the only time the generated token is available. If you need it for future use, you must save it securely yourself.

        :param description: human-readable description of who or what will use the credential to authenticate. Optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this credential. Optional, max 4096 bytes.
        :param acl: optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains, addresses, and labels the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules for domains may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. Bind rules for labels may specify a wildcard key and/or value to match multiple labels. For example, you may specify a rule of ``bind:*=example`` which will allow ``x=example``, ``y=example``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions.
        :param owner_id: If supplied at credential creation, ownership will be assigned to the specified User or Bot. Only admins may specify an owner other than themselves. Defaults to the authenticated User or Bot.

        https://ngrok.com/docs/api#api-credentials-create
        """
        path = "/credentials"
        body_arg = dict(
            description=description,
            metadata=metadata,
            acl=acl,
            owner_id=owner_id,
        )
        result = self._client.http_client.post(path, body_arg)
        return Credential(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a tunnel authtoken credential by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-credentials-delete
        """
        path = "/credentials/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> Credential:
        """Get detailed information about a tunnel authtoken credential

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-credentials-get
        """
        path = "/credentials/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return Credential(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> CredentialList:
        """List all tunnel authtoken credentials on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-credentials-list
        """
        path = "/credentials"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return CredentialList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        acl: Sequence[str] = None,
    ) -> Credential:
        """Update attributes of an tunnel authtoken credential by ID

        :param id:
        :param description: human-readable description of who or what will use the credential to authenticate. Optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this credential. Optional, max 4096 bytes.
        :param acl: optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains, addresses, and labels the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules for domains may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. Bind rules for labels may specify a wildcard key and/or value to match multiple labels. For example, you may specify a rule of ``bind:*=example`` which will allow ``x=example``, ``y=example``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions.

        https://ngrok.com/docs/api#api-credentials-update
        """
        path = "/credentials/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            acl=acl,
        )
        result = self._client.http_client.patch(path, body_arg)
        return Credential(self._client, result)


class EdgesHTTPSRoutesClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        edge_id: str,
        match_type: str,
        match: str,
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
    ) -> HTTPSEdgeRoute:
        """Create an HTTPS Edge Route

        :param edge_id: unique identifier of this edge
        :param match_type: Type of match to use for this route. Valid values are "exact_path" and "path_prefix".
        :param match: Route selector: "/blog" or "example.com" or "example.com/blog"
        :param description: human-readable description of what this edge will be used for; optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this edge. Optional, max 4096 bytes.
        :param backend: backend module configuration or ``null``
        :param ip_restriction: ip restriction module configuration or ``null``
        :param circuit_breaker: circuit breaker module configuration or ``null``
        :param compression: compression module configuration or ``null``
        :param request_headers: request headers module configuration or ``null``
        :param response_headers: response headers module configuration or ``null``
        :param webhook_verification: webhook verification module configuration or ``null``
        :param oauth: oauth module configuration or ``null``
        :param saml: saml module configuration or ``null``
        :param oidc: oidc module configuration or ``null``
        :param websocket_tcp_converter: websocket to tcp adapter configuration or ``null``
        :param user_agent_filter:
        :param traffic_policy: the traffic policy associated with this edge or null

        https://ngrok.com/docs/api#api-edges-https-routes-create
        """
        path = "/edges/https/{edge_id}/routes"
        path = path.format(
            edge_id=edge_id,
        )
        body_arg = dict(
            match_type=match_type,
            match=match,
            description=description,
            metadata=metadata,
            backend=extract_props(backend),
            ip_restriction=extract_props(ip_restriction),
            circuit_breaker=extract_props(circuit_breaker),
            compression=extract_props(compression),
            request_headers=extract_props(request_headers),
            response_headers=extract_props(response_headers),
            webhook_verification=extract_props(webhook_verification),
            oauth=extract_props(oauth),
            saml=extract_props(saml),
            oidc=extract_props(oidc),
            websocket_tcp_converter=extract_props(websocket_tcp_converter),
            user_agent_filter=extract_props(user_agent_filter),
            traffic_policy=extract_props(traffic_policy),
        )
        result = self._client.http_client.post(path, body_arg)
        return HTTPSEdgeRoute(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> HTTPSEdgeRoute:
        """Get an HTTPS Edge Route by ID

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edges-https-routes-get
        """
        path = "/edges/https/{edge_id}/routes/{id}"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return HTTPSEdgeRoute(self._client, result)

    def update(
        self,
        edge_id: str,
        id: str,
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
    ) -> HTTPSEdgeRoute:
        """Updates an HTTPS Edge Route by ID. If a module is not specified in the update, it will not be modified. However, each module configuration that is specified will completely replace the existing value. There is no way to delete an existing module via this API, instead use the delete module API.

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route
        :param match_type: Type of match to use for this route. Valid values are "exact_path" and "path_prefix".
        :param match: Route selector: "/blog" or "example.com" or "example.com/blog"
        :param description: human-readable description of what this edge will be used for; optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this edge. Optional, max 4096 bytes.
        :param backend: backend module configuration or ``null``
        :param ip_restriction: ip restriction module configuration or ``null``
        :param circuit_breaker: circuit breaker module configuration or ``null``
        :param compression: compression module configuration or ``null``
        :param request_headers: request headers module configuration or ``null``
        :param response_headers: response headers module configuration or ``null``
        :param webhook_verification: webhook verification module configuration or ``null``
        :param oauth: oauth module configuration or ``null``
        :param saml: saml module configuration or ``null``
        :param oidc: oidc module configuration or ``null``
        :param websocket_tcp_converter: websocket to tcp adapter configuration or ``null``
        :param user_agent_filter:
        :param traffic_policy: the traffic policy associated with this edge or null

        https://ngrok.com/docs/api#api-edges-https-routes-update
        """
        path = "/edges/https/{edge_id}/routes/{id}"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = dict(
            match_type=match_type,
            match=match,
            description=description,
            metadata=metadata,
            backend=extract_props(backend),
            ip_restriction=extract_props(ip_restriction),
            circuit_breaker=extract_props(circuit_breaker),
            compression=extract_props(compression),
            request_headers=extract_props(request_headers),
            response_headers=extract_props(response_headers),
            webhook_verification=extract_props(webhook_verification),
            oauth=extract_props(oauth),
            saml=extract_props(saml),
            oidc=extract_props(oidc),
            websocket_tcp_converter=extract_props(websocket_tcp_converter),
            user_agent_filter=extract_props(user_agent_filter),
            traffic_policy=extract_props(traffic_policy),
        )
        result = self._client.http_client.patch(path, body_arg)
        return HTTPSEdgeRoute(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """Delete an HTTPS Edge Route by ID

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edges-https-routes-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgesHTTPSClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        hostports: Sequence[str] = None,
        mutual_tls: EndpointMutualTLSMutate = None,
        tls_termination: EndpointTLSTerminationAtEdge = None,
    ) -> HTTPSEdge:
        """Create an HTTPS Edge

        :param description: human-readable description of what this edge will be used for; optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this edge; optional, max 4096 bytes.
        :param hostports: hostports served by this edge
        :param mutual_tls: edge modules
        :param tls_termination:

        https://ngrok.com/docs/api#api-edges-https-create
        """
        path = "/edges/https"
        body_arg = dict(
            description=description,
            metadata=metadata,
            hostports=hostports,
            mutual_tls=extract_props(mutual_tls),
            tls_termination=extract_props(tls_termination),
        )
        result = self._client.http_client.post(path, body_arg)
        return HTTPSEdge(self._client, result)

    def get(
        self,
        id: str,
    ) -> HTTPSEdge:
        """Get an HTTPS Edge by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-edges-https-get
        """
        path = "/edges/https/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return HTTPSEdge(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> HTTPSEdgeList:
        """Returns a list of all HTTPS Edges on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-edges-https-list
        """
        path = "/edges/https"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return HTTPSEdgeList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        hostports: Sequence[str] = None,
        mutual_tls: EndpointMutualTLSMutate = None,
        tls_termination: EndpointTLSTerminationAtEdge = None,
    ) -> HTTPSEdge:
        """Updates an HTTPS Edge by ID. If a module is not specified in the update, it will not be modified. However, each module configuration that is specified will completely replace the existing value. There is no way to delete an existing module via this API, instead use the delete module API.

        :param id: unique identifier of this edge
        :param description: human-readable description of what this edge will be used for; optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this edge; optional, max 4096 bytes.
        :param hostports: hostports served by this edge
        :param mutual_tls: edge modules
        :param tls_termination:

        https://ngrok.com/docs/api#api-edges-https-update
        """
        path = "/edges/https/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            hostports=hostports,
            mutual_tls=extract_props(mutual_tls),
            tls_termination=extract_props(tls_termination),
        )
        result = self._client.http_client.patch(path, body_arg)
        return HTTPSEdge(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an HTTPS Edge by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-edges-https-delete
        """
        path = "/edges/https/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class HTTPSEdgeMutualTLSModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointMutualTLSMutate = None,
    ) -> EndpointMutualTLS:
        """

        :param id:
        :param module:

        https://ngrok.com/docs/api#api-https-edge-mutual-tls-module-replace
        """
        path = "/edges/https/{id}/mutual_tls"
        path = path.format(
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointMutualTLS(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointMutualTLS:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-https-edge-mutual-tls-module-get
        """
        path = "/edges/https/{id}/mutual_tls"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointMutualTLS(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-https-edge-mutual-tls-module-delete
        """
        path = "/edges/https/{id}/mutual_tls"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class HTTPSEdgeTLSTerminationModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointTLSTerminationAtEdge = None,
    ) -> EndpointTLSTermination:
        """

        :param id:
        :param module:

        https://ngrok.com/docs/api#api-https-edge-tls-termination-module-replace
        """
        path = "/edges/https/{id}/tls_termination"
        path = path.format(
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointTLSTermination(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointTLSTermination:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-https-edge-tls-termination-module-get
        """
        path = "/edges/https/{id}/tls_termination"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointTLSTermination(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-https-edge-tls-termination-module-delete
        """
        path = "/edges/https/{id}/tls_termination"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteBackendModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointBackendMutate = None,
    ) -> EndpointBackend:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-backend-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/backend"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointBackend(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointBackend:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-backend-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/backend"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointBackend(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-backend-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/backend"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteIPRestrictionModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointIPPolicyMutate = None,
    ) -> EndpointIPPolicy:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-ip-restriction-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/ip_restriction"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointIPPolicy(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointIPPolicy:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-ip-restriction-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/ip_restriction"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointIPPolicy(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-ip-restriction-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/ip_restriction"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteRequestHeadersModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointRequestHeaders = None,
    ) -> EndpointRequestHeaders:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-request-headers-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/request_headers"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointRequestHeaders(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointRequestHeaders:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-request-headers-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/request_headers"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointRequestHeaders(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-request-headers-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/request_headers"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteResponseHeadersModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointResponseHeaders = None,
    ) -> EndpointResponseHeaders:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-response-headers-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/response_headers"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointResponseHeaders(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointResponseHeaders:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-response-headers-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/response_headers"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointResponseHeaders(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-response-headers-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/response_headers"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteCompressionModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointCompression = None,
    ) -> EndpointCompression:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-compression-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/compression"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointCompression(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointCompression:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-compression-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/compression"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointCompression(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-compression-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/compression"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteCircuitBreakerModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointCircuitBreaker = None,
    ) -> EndpointCircuitBreaker:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-circuit-breaker-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/circuit_breaker"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointCircuitBreaker(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointCircuitBreaker:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-circuit-breaker-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/circuit_breaker"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointCircuitBreaker(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-circuit-breaker-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/circuit_breaker"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteWebhookVerificationModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointWebhookValidation = None,
    ) -> EndpointWebhookValidation:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-webhook-verification-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/webhook_verification"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointWebhookValidation(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointWebhookValidation:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-webhook-verification-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/webhook_verification"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointWebhookValidation(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-webhook-verification-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/webhook_verification"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteOAuthModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointOAuth = None,
    ) -> EndpointOAuth:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-o-auth-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/oauth"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointOAuth(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointOAuth:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-o-auth-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/oauth"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointOAuth(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-o-auth-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/oauth"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteSAMLModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointSAMLMutate = None,
    ) -> EndpointSAML:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-saml-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/saml"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointSAML(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointSAML:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-saml-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/saml"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointSAML(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-saml-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/saml"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteOIDCModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointOIDC = None,
    ) -> EndpointOIDC:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-oidc-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/oidc"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointOIDC(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointOIDC:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-oidc-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/oidc"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointOIDC(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-oidc-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/oidc"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteWebsocketTCPConverterModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointWebsocketTCPConverter = None,
    ) -> EndpointWebsocketTCPConverter:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-websocket-tcp-converter-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/websocket_tcp_converter"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointWebsocketTCPConverter(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointWebsocketTCPConverter:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-websocket-tcp-converter-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/websocket_tcp_converter"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointWebsocketTCPConverter(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-websocket-tcp-converter-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/websocket_tcp_converter"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteUserAgentFilterModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointUserAgentFilter = None,
    ) -> EndpointUserAgentFilter:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-user-agent-filter-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/user_agent_filter"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointUserAgentFilter(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointUserAgentFilter:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-user-agent-filter-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/user_agent_filter"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointUserAgentFilter(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-user-agent-filter-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/user_agent_filter"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgeRouteTrafficPolicyModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        edge_id: str,
        id: str,
        module: EndpointTrafficPolicy = None,
    ) -> EndpointTrafficPolicy:
        """

        :param edge_id:
        :param id:
        :param module:

        https://ngrok.com/docs/api#api-edge-route-traffic-policy-module-replace
        """
        path = "/edges/https/{edge_id}/routes/{id}/traffic_policy"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointTrafficPolicy(self._client, result)

    def get(
        self,
        edge_id: str,
        id: str,
    ) -> EndpointTrafficPolicy:
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-traffic-policy-module-get
        """
        path = "/edges/https/{edge_id}/routes/{id}/traffic_policy"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointTrafficPolicy(self._client, result)

    def delete(
        self,
        edge_id: str,
        id: str,
    ):
        """

        :param edge_id: unique identifier of this edge
        :param id: unique identifier of this edge route

        https://ngrok.com/docs/api#api-edge-route-traffic-policy-module-delete
        """
        path = "/edges/https/{edge_id}/routes/{id}/traffic_policy"
        path = path.format(
            edge_id=edge_id,
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgesTCPClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        hostports: Sequence[str] = None,
        backend: EndpointBackendMutate = None,
        ip_restriction: EndpointIPPolicyMutate = None,
        traffic_policy: EndpointTrafficPolicy = None,
    ) -> TCPEdge:
        """Create a TCP Edge

        :param description: human-readable description of what this edge will be used for; optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this edge. Optional, max 4096 bytes.
        :param hostports: hostports served by this edge
        :param backend: edge modules
        :param ip_restriction:
        :param traffic_policy: the traffic policy associated with this edge or null

        https://ngrok.com/docs/api#api-edges-tcp-create
        """
        path = "/edges/tcp"
        body_arg = dict(
            description=description,
            metadata=metadata,
            hostports=hostports,
            backend=extract_props(backend),
            ip_restriction=extract_props(ip_restriction),
            traffic_policy=extract_props(traffic_policy),
        )
        result = self._client.http_client.post(path, body_arg)
        return TCPEdge(self._client, result)

    def get(
        self,
        id: str,
    ) -> TCPEdge:
        """Get a TCP Edge by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-edges-tcp-get
        """
        path = "/edges/tcp/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return TCPEdge(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> TCPEdgeList:
        """Returns a list of all TCP Edges on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-edges-tcp-list
        """
        path = "/edges/tcp"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return TCPEdgeList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        hostports: Sequence[str] = None,
        backend: EndpointBackendMutate = None,
        ip_restriction: EndpointIPPolicyMutate = None,
        traffic_policy: EndpointTrafficPolicy = None,
    ) -> TCPEdge:
        """Updates a TCP Edge by ID. If a module is not specified in the update, it will not be modified. However, each module configuration that is specified will completely replace the existing value. There is no way to delete an existing module via this API, instead use the delete module API.

        :param id: unique identifier of this edge
        :param description: human-readable description of what this edge will be used for; optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this edge. Optional, max 4096 bytes.
        :param hostports: hostports served by this edge
        :param backend: edge modules
        :param ip_restriction:
        :param traffic_policy: the traffic policy associated with this edge or null

        https://ngrok.com/docs/api#api-edges-tcp-update
        """
        path = "/edges/tcp/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            hostports=hostports,
            backend=extract_props(backend),
            ip_restriction=extract_props(ip_restriction),
            traffic_policy=extract_props(traffic_policy),
        )
        result = self._client.http_client.patch(path, body_arg)
        return TCPEdge(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a TCP Edge by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-edges-tcp-delete
        """
        path = "/edges/tcp/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class TCPEdgeBackendModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointBackendMutate = None,
    ) -> EndpointBackend:
        """

        :param id:
        :param module:

        https://ngrok.com/docs/api#api-tcp-edge-backend-module-replace
        """
        path = "/edges/tcp/{id}/backend"
        path = path.format(
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointBackend(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointBackend:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tcp-edge-backend-module-get
        """
        path = "/edges/tcp/{id}/backend"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointBackend(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tcp-edge-backend-module-delete
        """
        path = "/edges/tcp/{id}/backend"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class TCPEdgeIPRestrictionModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointIPPolicyMutate = None,
    ) -> EndpointIPPolicy:
        """

        :param id:
        :param module:

        https://ngrok.com/docs/api#api-tcp-edge-ip-restriction-module-replace
        """
        path = "/edges/tcp/{id}/ip_restriction"
        path = path.format(
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointIPPolicy(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointIPPolicy:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tcp-edge-ip-restriction-module-get
        """
        path = "/edges/tcp/{id}/ip_restriction"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointIPPolicy(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tcp-edge-ip-restriction-module-delete
        """
        path = "/edges/tcp/{id}/ip_restriction"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class TCPEdgeTrafficPolicyModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointTrafficPolicy = None,
    ) -> EndpointTrafficPolicy:
        """

        :param id:
        :param module:

        https://ngrok.com/docs/api#api-tcp-edge-traffic-policy-module-replace
        """
        path = "/edges/tcp/{id}/traffic_policy"
        path = path.format(
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointTrafficPolicy(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointTrafficPolicy:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tcp-edge-traffic-policy-module-get
        """
        path = "/edges/tcp/{id}/traffic_policy"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointTrafficPolicy(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tcp-edge-traffic-policy-module-delete
        """
        path = "/edges/tcp/{id}/traffic_policy"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EdgesTLSClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        hostports: Sequence[str] = None,
        backend: EndpointBackendMutate = None,
        ip_restriction: EndpointIPPolicyMutate = None,
        mutual_tls: EndpointMutualTLSMutate = None,
        tls_termination: EndpointTLSTermination = None,
        traffic_policy: EndpointTrafficPolicy = None,
    ) -> TLSEdge:
        """Create a TLS Edge

        :param description: human-readable description of what this edge will be used for; optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this edge. Optional, max 4096 bytes.
        :param hostports: hostports served by this edge
        :param backend: edge modules
        :param ip_restriction:
        :param mutual_tls:
        :param tls_termination:
        :param traffic_policy: the traffic policy associated with this edge or null

        https://ngrok.com/docs/api#api-edges-tls-create
        """
        path = "/edges/tls"
        body_arg = dict(
            description=description,
            metadata=metadata,
            hostports=hostports,
            backend=extract_props(backend),
            ip_restriction=extract_props(ip_restriction),
            mutual_tls=extract_props(mutual_tls),
            tls_termination=extract_props(tls_termination),
            traffic_policy=extract_props(traffic_policy),
        )
        result = self._client.http_client.post(path, body_arg)
        return TLSEdge(self._client, result)

    def get(
        self,
        id: str,
    ) -> TLSEdge:
        """Get a TLS Edge by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-edges-tls-get
        """
        path = "/edges/tls/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return TLSEdge(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> TLSEdgeList:
        """Returns a list of all TLS Edges on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-edges-tls-list
        """
        path = "/edges/tls"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return TLSEdgeList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        hostports: Sequence[str] = None,
        backend: EndpointBackendMutate = None,
        ip_restriction: EndpointIPPolicyMutate = None,
        mutual_tls: EndpointMutualTLSMutate = None,
        tls_termination: EndpointTLSTermination = None,
        traffic_policy: EndpointTrafficPolicy = None,
    ) -> TLSEdge:
        """Updates a TLS Edge by ID. If a module is not specified in the update, it will not be modified. However, each module configuration that is specified will completely replace the existing value. There is no way to delete an existing module via this API, instead use the delete module API.

        :param id: unique identifier of this edge
        :param description: human-readable description of what this edge will be used for; optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this edge. Optional, max 4096 bytes.
        :param hostports: hostports served by this edge
        :param backend: edge modules
        :param ip_restriction:
        :param mutual_tls:
        :param tls_termination:
        :param traffic_policy: the traffic policy associated with this edge or null

        https://ngrok.com/docs/api#api-edges-tls-update
        """
        path = "/edges/tls/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            hostports=hostports,
            backend=extract_props(backend),
            ip_restriction=extract_props(ip_restriction),
            mutual_tls=extract_props(mutual_tls),
            tls_termination=extract_props(tls_termination),
            traffic_policy=extract_props(traffic_policy),
        )
        result = self._client.http_client.patch(path, body_arg)
        return TLSEdge(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a TLS Edge by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-edges-tls-delete
        """
        path = "/edges/tls/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class TLSEdgeBackendModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointBackendMutate = None,
    ) -> EndpointBackend:
        """

        :param id:
        :param module:

        https://ngrok.com/docs/api#api-tls-edge-backend-module-replace
        """
        path = "/edges/tls/{id}/backend"
        path = path.format(
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointBackend(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointBackend:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-edge-backend-module-get
        """
        path = "/edges/tls/{id}/backend"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointBackend(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-edge-backend-module-delete
        """
        path = "/edges/tls/{id}/backend"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class TLSEdgeIPRestrictionModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointIPPolicyMutate = None,
    ) -> EndpointIPPolicy:
        """

        :param id:
        :param module:

        https://ngrok.com/docs/api#api-tls-edge-ip-restriction-module-replace
        """
        path = "/edges/tls/{id}/ip_restriction"
        path = path.format(
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointIPPolicy(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointIPPolicy:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-edge-ip-restriction-module-get
        """
        path = "/edges/tls/{id}/ip_restriction"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointIPPolicy(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-edge-ip-restriction-module-delete
        """
        path = "/edges/tls/{id}/ip_restriction"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class TLSEdgeMutualTLSModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointMutualTLSMutate = None,
    ) -> EndpointMutualTLS:
        """

        :param id:
        :param module:

        https://ngrok.com/docs/api#api-tls-edge-mutual-tls-module-replace
        """
        path = "/edges/tls/{id}/mutual_tls"
        path = path.format(
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointMutualTLS(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointMutualTLS:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-edge-mutual-tls-module-get
        """
        path = "/edges/tls/{id}/mutual_tls"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointMutualTLS(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-edge-mutual-tls-module-delete
        """
        path = "/edges/tls/{id}/mutual_tls"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class TLSEdgeTLSTerminationModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointTLSTermination = None,
    ) -> EndpointTLSTermination:
        """

        :param id:
        :param module:

        https://ngrok.com/docs/api#api-tls-edge-tls-termination-module-replace
        """
        path = "/edges/tls/{id}/tls_termination"
        path = path.format(
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointTLSTermination(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointTLSTermination:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-edge-tls-termination-module-get
        """
        path = "/edges/tls/{id}/tls_termination"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointTLSTermination(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-edge-tls-termination-module-delete
        """
        path = "/edges/tls/{id}/tls_termination"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class TLSEdgeTrafficPolicyModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointTrafficPolicy = None,
    ) -> EndpointTrafficPolicy:
        """

        :param id:
        :param module:

        https://ngrok.com/docs/api#api-tls-edge-traffic-policy-module-replace
        """
        path = "/edges/tls/{id}/traffic_policy"
        path = path.format(
            id=id,
        )
        body_arg = extract_props(module)
        result = self._client.http_client.put(path, body_arg)
        return EndpointTrafficPolicy(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointTrafficPolicy:
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-edge-traffic-policy-module-get
        """
        path = "/edges/tls/{id}/traffic_policy"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EndpointTrafficPolicy(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-edge-traffic-policy-module-delete
        """
        path = "/edges/tls/{id}/traffic_policy"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EndpointsClient(object):
    """Endpoints provides an API for querying the endpoint objects
    which define what tunnel or edge is used to serve a hostport.
    Only active endpoints associated with a tunnel or backend are returned."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        url: str,
        type: str,
        traffic_policy: str,
        description: str = None,
        metadata: str = None,
        bindings: Sequence[str] = None,
        pooling_enabled: bool = False,
    ) -> Endpoint:
        """Create an endpoint, currently available only for cloud endpoints

        :param url: the url of the endpoint
        :param type: Type of endpoint. Only 'cloud' is currently supported (represents a cloud endpoint). Defaults to 'cloud' if not specified.
        :param traffic_policy: The traffic policy attached to this endpoint
        :param description: user-supplied description of the associated tunnel
        :param metadata: user-supplied metadata of the associated tunnel or edge object
        :param bindings: the bindings associated with this endpoint
        :param pooling_enabled:

        https://ngrok.com/docs/api#api-endpoints-create
        """
        path = "/endpoints"
        body_arg = dict(
            url=url,
            type=type,
            traffic_policy=traffic_policy,
            description=description,
            metadata=metadata,
            bindings=bindings,
            pooling_enabled=pooling_enabled,
        )
        result = self._client.http_client.post(path, body_arg)
        return Endpoint(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
        id: Sequence[str] = [],
        url: Sequence[str] = [],
    ) -> EndpointList:
        """List all active endpoints on the account

        :param before_id:
        :param limit:
        :param id:
        :param url:

        https://ngrok.com/docs/api#api-endpoints-list
        """
        path = "/endpoints"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
            id=id,
            url=url,
        )
        result = self._client.http_client.get(path, body_arg)
        return EndpointList(self._client, result)

    def get(
        self,
        id: str,
    ) -> Endpoint:
        """Get the status of an endpoint by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-endpoints-get
        """
        path = "/endpoints/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return Endpoint(self._client, result)

    def update(
        self,
        id: str,
        url: str = None,
        traffic_policy: str = None,
        description: str = None,
        metadata: str = None,
        bindings: Sequence[str] = None,
        pooling_enabled: bool = False,
    ) -> Endpoint:
        """Update an Endpoint by ID, currently available only for cloud endpoints

        :param id: unique endpoint resource identifier
        :param url: the url of the endpoint
        :param traffic_policy: The traffic policy attached to this endpoint
        :param description: user-supplied description of the associated tunnel
        :param metadata: user-supplied metadata of the associated tunnel or edge object
        :param bindings: the bindings associated with this endpoint
        :param pooling_enabled:

        https://ngrok.com/docs/api#api-endpoints-update
        """
        path = "/endpoints/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            url=url,
            traffic_policy=traffic_policy,
            description=description,
            metadata=metadata,
            bindings=bindings,
            pooling_enabled=pooling_enabled,
        )
        result = self._client.http_client.patch(path, body_arg)
        return Endpoint(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an Endpoint by ID, currently available only for cloud endpoints

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-endpoints-delete
        """
        path = "/endpoints/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class EventDestinationsClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        metadata: str = "",
        description: str = "",
        format: str = "",
        target: EventTarget = None,
    ) -> EventDestination:
        """Create a new Event Destination. It will not apply to anything until it is associated with an Event Subscription.

        :param metadata: Arbitrary user-defined machine-readable data of this Event Destination. Optional, max 4096 bytes.
        :param description: Human-readable description of the Event Destination. Optional, max 255 bytes.
        :param format: The output format you would like to serialize events into when sending to their target. Currently the only accepted value is ``JSON``.
        :param target: An object that encapsulates where and how to send your events. An event destination must contain exactly one of the following objects, leaving the rest null: ``kinesis``, ``firehose``, ``cloudwatch_logs``, or ``s3``.

        https://ngrok.com/docs/api#api-event-destinations-create
        """
        path = "/event_destinations"
        body_arg = dict(
            metadata=metadata,
            description=description,
            format=format,
            target=extract_props(target),
        )
        result = self._client.http_client.post(path, body_arg)
        return EventDestination(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an Event Destination. If the Event Destination is still referenced by an Event Subscription.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-event-destinations-delete
        """
        path = "/event_destinations/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> EventDestination:
        """Get detailed information about an Event Destination by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-event-destinations-get
        """
        path = "/event_destinations/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EventDestination(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> EventDestinationList:
        """List all Event Destinations on this account.

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-event-destinations-list
        """
        path = "/event_destinations"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return EventDestinationList(self._client, result)

    def update(
        self,
        id: str,
        metadata: str = None,
        description: str = None,
        format: str = None,
        target: EventTarget = None,
    ) -> EventDestination:
        """Update attributes of an Event Destination.

        :param id: Unique identifier for this Event Destination.
        :param metadata: Arbitrary user-defined machine-readable data of this Event Destination. Optional, max 4096 bytes.
        :param description: Human-readable description of the Event Destination. Optional, max 255 bytes.
        :param format: The output format you would like to serialize events into when sending to their target. Currently the only accepted value is ``JSON``.
        :param target: An object that encapsulates where and how to send your events. An event destination must contain exactly one of the following objects, leaving the rest null: ``kinesis``, ``firehose``, ``cloudwatch_logs``, or ``s3``.

        https://ngrok.com/docs/api#api-event-destinations-update
        """
        path = "/event_destinations/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            metadata=metadata,
            description=description,
            format=format,
            target=extract_props(target),
        )
        result = self._client.http_client.patch(path, body_arg)
        return EventDestination(self._client, result)


class EventSubscriptionsClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        metadata: str = "",
        description: str = "",
        sources: Sequence[EventSourceReplace] = [],
        destination_ids: Sequence[str] = [],
    ) -> EventSubscription:
        """Create an Event Subscription.

        :param metadata: Arbitrary customer supplied information intended to be machine readable. Optional, max 4096 chars.
        :param description: Arbitrary customer supplied information intended to be human readable. Optional, max 255 chars.
        :param sources: Sources containing the types for which this event subscription will trigger
        :param destination_ids: A list of Event Destination IDs which should be used for this Event Subscription.

        https://ngrok.com/docs/api#api-event-subscriptions-create
        """
        path = "/event_subscriptions"
        body_arg = dict(
            metadata=metadata,
            description=description,
            sources=[extract_props(item) for item in sources or []],
            destination_ids=destination_ids,
        )
        result = self._client.http_client.post(path, body_arg)
        return EventSubscription(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an Event Subscription.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-event-subscriptions-delete
        """
        path = "/event_subscriptions/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> EventSubscription:
        """Get an Event Subscription by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-event-subscriptions-get
        """
        path = "/event_subscriptions/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EventSubscription(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> EventSubscriptionList:
        """List this Account's Event Subscriptions.

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-event-subscriptions-list
        """
        path = "/event_subscriptions"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return EventSubscriptionList(self._client, result)

    def update(
        self,
        id: str,
        metadata: str = None,
        description: str = None,
        sources: Sequence[EventSourceReplace] = None,
        destination_ids: Sequence[str] = None,
    ) -> EventSubscription:
        """Update an Event Subscription.

        :param id: Unique identifier for this Event Subscription.
        :param metadata: Arbitrary customer supplied information intended to be machine readable. Optional, max 4096 chars.
        :param description: Arbitrary customer supplied information intended to be human readable. Optional, max 255 chars.
        :param sources: Sources containing the types for which this event subscription will trigger
        :param destination_ids: A list of Event Destination IDs which should be used for this Event Subscription.

        https://ngrok.com/docs/api#api-event-subscriptions-update
        """
        path = "/event_subscriptions/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            metadata=metadata,
            description=description,
            sources=[extract_props(item) for item in sources or []],
            destination_ids=destination_ids,
        )
        result = self._client.http_client.patch(path, body_arg)
        return EventSubscription(self._client, result)


class EventSourcesClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        subscription_id: str,
        type: str = "",
    ) -> EventSource:
        """Add an additional type for which this event subscription will trigger

        :param subscription_id: The unique identifier for the Event Subscription that this Event Source is attached to.
        :param type: Type of event for which an event subscription will trigger

        https://ngrok.com/docs/api#api-event-sources-create
        """
        path = "/event_subscriptions/{subscription_id}/sources"
        path = path.format(
            subscription_id=subscription_id,
        )
        body_arg = dict(
            type=type,
        )
        result = self._client.http_client.post(path, body_arg)
        return EventSource(self._client, result)

    def delete(
        self,
        subscription_id: str,
        type: str,
    ):
        """Remove a type for which this event subscription will trigger

        :param subscription_id: The unique identifier for the Event Subscription that this Event Source is attached to.
        :param type: Type of event for which an event subscription will trigger

        https://ngrok.com/docs/api#api-event-sources-delete
        """
        path = "/event_subscriptions/{subscription_id}/sources/{type}"
        path = path.format(
            subscription_id=subscription_id,
            type=type,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        subscription_id: str,
        type: str,
    ) -> EventSource:
        """Get the details for a given type that triggers for the given event subscription

        :param subscription_id: The unique identifier for the Event Subscription that this Event Source is attached to.
        :param type: Type of event for which an event subscription will trigger

        https://ngrok.com/docs/api#api-event-sources-get
        """
        path = "/event_subscriptions/{subscription_id}/sources/{type}"
        path = path.format(
            subscription_id=subscription_id,
            type=type,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EventSource(self._client, result)

    def list(
        self,
        subscription_id: str,
    ) -> EventSourceList:
        """List the types for which this event subscription will trigger

        :param subscription_id: The unique identifier for the Event Subscription that this Event Source is attached to.

        https://ngrok.com/docs/api#api-event-sources-list
        """
        path = "/event_subscriptions/{subscription_id}/sources"
        path = path.format(
            subscription_id=subscription_id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return EventSourceList(self._client, result)

    def update(
        self,
        subscription_id: str,
        type: str,
    ) -> EventSource:
        """Update the type for which this event subscription will trigger

        :param subscription_id: The unique identifier for the Event Subscription that this Event Source is attached to.
        :param type: Type of event for which an event subscription will trigger

        https://ngrok.com/docs/api#api-event-sources-update
        """
        path = "/event_subscriptions/{subscription_id}/sources/{type}"
        path = path.format(
            subscription_id=subscription_id,
            type=type,
        )
        body_arg = None
        result = self._client.http_client.patch(path, body_arg)
        return EventSource(self._client, result)


class IPPoliciesClient(object):
    """IP Policies are reusable groups of CIDR ranges with an ``allow`` or ``deny``
    action. They can be attached to endpoints via the Endpoint Configuration IP
    Policy module. They can also be used with IP Restrictions to control source
    IP ranges that can start tunnel sessions and connect to the API and dashboard."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
    ) -> IPPolicy:
        """Create a new IP policy. It will not apply to any traffic until you associate to a traffic source via an endpoint configuration or IP restriction.

        :param description: human-readable description of the source IPs of this IP policy. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this IP policy. optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-ip-policies-create
        """
        path = "/ip_policies"
        body_arg = dict(
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.post(path, body_arg)
        return IPPolicy(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an IP policy. If the IP policy is referenced by another object for the purposes of traffic restriction it will be treated as if the IP policy remains but has zero rules.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ip-policies-delete
        """
        path = "/ip_policies/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> IPPolicy:
        """Get detailed information about an IP policy by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ip-policies-get
        """
        path = "/ip_policies/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return IPPolicy(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> IPPolicyList:
        """List all IP policies on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-ip-policies-list
        """
        path = "/ip_policies"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return IPPolicyList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
    ) -> IPPolicy:
        """Update attributes of an IP policy by ID

        :param id:
        :param description: human-readable description of the source IPs of this IP policy. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this IP policy. optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-ip-policies-update
        """
        path = "/ip_policies/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.patch(path, body_arg)
        return IPPolicy(self._client, result)


class IPPolicyRulesClient(object):
    """IP Policy Rules are the IPv4 or IPv6 CIDRs entries that
    make up an IP Policy."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        cidr: str,
        ip_policy_id: str,
        action: str,
        description: str = "",
        metadata: str = "",
    ) -> IPPolicyRule:
        """Create a new IP policy rule attached to an IP Policy.

        :param description: human-readable description of the source IPs of this IP rule. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this IP policy rule. optional, max 4096 bytes.
        :param cidr: an IP or IP range specified in CIDR notation. IPv4 and IPv6 are both supported.
        :param ip_policy_id: ID of the IP policy this IP policy rule will be attached to
        :param action: the action to apply to the policy rule, either ``allow`` or ``deny``

        https://ngrok.com/docs/api#api-ip-policy-rules-create
        """
        path = "/ip_policy_rules"
        body_arg = dict(
            description=description,
            metadata=metadata,
            cidr=cidr,
            ip_policy_id=ip_policy_id,
            action=action,
        )
        result = self._client.http_client.post(path, body_arg)
        return IPPolicyRule(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an IP policy rule.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ip-policy-rules-delete
        """
        path = "/ip_policy_rules/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> IPPolicyRule:
        """Get detailed information about an IP policy rule by ID.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ip-policy-rules-get
        """
        path = "/ip_policy_rules/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return IPPolicyRule(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> IPPolicyRuleList:
        """List all IP policy rules on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-ip-policy-rules-list
        """
        path = "/ip_policy_rules"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return IPPolicyRuleList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        cidr: str = None,
    ) -> IPPolicyRule:
        """Update attributes of an IP policy rule by ID

        :param id:
        :param description: human-readable description of the source IPs of this IP rule. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this IP policy rule. optional, max 4096 bytes.
        :param cidr: an IP or IP range specified in CIDR notation. IPv4 and IPv6 are both supported.

        https://ngrok.com/docs/api#api-ip-policy-rules-update
        """
        path = "/ip_policy_rules/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            cidr=cidr,
        )
        result = self._client.http_client.patch(path, body_arg)
        return IPPolicyRule(self._client, result)


class IPRestrictionsClient(object):
    """An IP restriction is a restriction placed on the CIDRs that are allowed to
    initiate traffic to a specific aspect of your ngrok account. An IP
    restriction has a type which defines the ingress it applies to. IP
    restrictions can be used to enforce the source IPs that can make API
    requests, log in to the dashboard, start ngrok agents, and connect to your
    public-facing endpoints."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        type: str,
        ip_policy_ids: Sequence[str],
        description: str = "",
        metadata: str = "",
        enforced: bool = False,
    ) -> IPRestriction:
        """Create a new IP restriction

        :param description: human-readable description of this IP restriction. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this IP restriction. optional, max 4096 bytes.
        :param enforced: true if the IP restriction will be enforced. if false, only warnings will be issued
        :param type: the type of IP restriction. this defines what traffic will be restricted with the attached policies. four values are currently supported: ``dashboard``, ``api``, ``agent``, and ``endpoints``
        :param ip_policy_ids: the set of IP policy identifiers that are used to enforce the restriction

        https://ngrok.com/docs/api#api-ip-restrictions-create
        """
        path = "/ip_restrictions"
        body_arg = dict(
            description=description,
            metadata=metadata,
            enforced=enforced,
            type=type,
            ip_policy_ids=ip_policy_ids,
        )
        result = self._client.http_client.post(path, body_arg)
        return IPRestriction(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an IP restriction

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ip-restrictions-delete
        """
        path = "/ip_restrictions/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> IPRestriction:
        """Get detailed information about an IP restriction

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ip-restrictions-get
        """
        path = "/ip_restrictions/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return IPRestriction(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> IPRestrictionList:
        """List all IP restrictions on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-ip-restrictions-list
        """
        path = "/ip_restrictions"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return IPRestrictionList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        enforced: bool = None,
        ip_policy_ids: Sequence[str] = [],
    ) -> IPRestriction:
        """Update attributes of an IP restriction by ID

        :param id:
        :param description: human-readable description of this IP restriction. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this IP restriction. optional, max 4096 bytes.
        :param enforced: true if the IP restriction will be enforced. if false, only warnings will be issued
        :param ip_policy_ids: the set of IP policy identifiers that are used to enforce the restriction

        https://ngrok.com/docs/api#api-ip-restrictions-update
        """
        path = "/ip_restrictions/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            enforced=enforced,
            ip_policy_ids=ip_policy_ids,
        )
        result = self._client.http_client.patch(path, body_arg)
        return IPRestriction(self._client, result)


class ReservedAddrsClient(object):
    """Reserved Addresses are TCP addresses that can be used to listen for traffic.
    TCP address hostnames and ports are assigned by ngrok, they cannot be
    chosen."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        region: str = "",
    ) -> ReservedAddr:
        """Create a new reserved address.

        :param description: human-readable description of what this reserved address will be used for
        :param metadata: arbitrary user-defined machine-readable data of this reserved address. Optional, max 4096 bytes.
        :param region: reserve the address in this geographic ngrok datacenter. Optional, default is us. (au, eu, ap, us, jp, in, sa)

        https://ngrok.com/docs/api#api-reserved-addrs-create
        """
        path = "/reserved_addrs"
        body_arg = dict(
            description=description,
            metadata=metadata,
            region=region,
        )
        result = self._client.http_client.post(path, body_arg)
        return ReservedAddr(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a reserved address.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-reserved-addrs-delete
        """
        path = "/reserved_addrs/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> ReservedAddr:
        """Get the details of a reserved address.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-reserved-addrs-get
        """
        path = "/reserved_addrs/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return ReservedAddr(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> ReservedAddrList:
        """List all reserved addresses on this account.

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-reserved-addrs-list
        """
        path = "/reserved_addrs"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return ReservedAddrList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
    ) -> ReservedAddr:
        """Update the attributes of a reserved address.

        :param id:
        :param description: human-readable description of what this reserved address will be used for
        :param metadata: arbitrary user-defined machine-readable data of this reserved address. Optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-reserved-addrs-update
        """
        path = "/reserved_addrs/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.patch(path, body_arg)
        return ReservedAddr(self._client, result)


class ReservedDomainsClient(object):
    """Reserved Domains are hostnames that you can listen for traffic on. Domains
    can be used to listen for http, https or tls traffic. You may use a domain
    that you own by creating a CNAME record specified in the returned resource.
    This CNAME record points traffic for that domain to ngrok's edge servers."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        domain: str = "",
        region: str = "",
        description: str = "",
        metadata: str = "",
        certificate_id: str = None,
        certificate_management_policy: ReservedDomainCertPolicy = None,
    ) -> ReservedDomain:
        """Create a new reserved domain.

        :param domain: hostname of the reserved domain
        :param region: deprecated: With the launch of the ngrok Global Network domains traffic is now handled globally. This field applied only to endpoints. Note that agents may still connect to specific regions. Optional, null by default. (au, eu, ap, us, jp, in, sa)
        :param description: human-readable description of what this reserved domain will be used for
        :param metadata: arbitrary user-defined machine-readable data of this reserved domain. Optional, max 4096 bytes.
        :param certificate_id: ID of a user-uploaded TLS certificate to use for connections to targeting this domain. Optional, mutually exclusive with ``certificate_management_policy``.
        :param certificate_management_policy: configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled. Optional, mutually exclusive with ``certificate_id``.

        https://ngrok.com/docs/api#api-reserved-domains-create
        """
        path = "/reserved_domains"
        body_arg = dict(
            domain=domain,
            region=region,
            description=description,
            metadata=metadata,
            certificate_id=certificate_id,
            certificate_management_policy=extract_props(certificate_management_policy),
        )
        result = self._client.http_client.post(path, body_arg)
        return ReservedDomain(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a reserved domain.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-reserved-domains-delete
        """
        path = "/reserved_domains/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> ReservedDomain:
        """Get the details of a reserved domain.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-reserved-domains-get
        """
        path = "/reserved_domains/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return ReservedDomain(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> ReservedDomainList:
        """List all reserved domains on this account.

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-reserved-domains-list
        """
        path = "/reserved_domains"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return ReservedDomainList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        certificate_id: str = None,
        certificate_management_policy: ReservedDomainCertPolicy = None,
    ) -> ReservedDomain:
        """Update the attributes of a reserved domain.

        :param id:
        :param description: human-readable description of what this reserved domain will be used for
        :param metadata: arbitrary user-defined machine-readable data of this reserved domain. Optional, max 4096 bytes.
        :param certificate_id: ID of a user-uploaded TLS certificate to use for connections to targeting this domain. Optional, mutually exclusive with ``certificate_management_policy``.
        :param certificate_management_policy: configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled. Optional, mutually exclusive with ``certificate_id``.

        https://ngrok.com/docs/api#api-reserved-domains-update
        """
        path = "/reserved_domains/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            certificate_id=certificate_id,
            certificate_management_policy=extract_props(certificate_management_policy),
        )
        result = self._client.http_client.patch(path, body_arg)
        return ReservedDomain(self._client, result)

    def delete_certificate_management_policy(
        self,
        id: str,
    ):
        """Detach the certificate management policy attached to a reserved domain.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-reserved-domains-delete-certificate-management-policy
        """
        path = "/reserved_domains/{id}/certificate_management_policy"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def delete_certificate(
        self,
        id: str,
    ):
        """Detach the certificate attached to a reserved domain.

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-reserved-domains-delete-certificate
        """
        path = "/reserved_domains/{id}/certificate"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)


class SecretsClient(object):
    """Secrets is an api service for securely storing and managing sensitive data such as secrets, credentials, and tokens."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        vault_id: str,
        name: str = "",
        value: str = "",
        metadata: str = "",
        description: str = "",
    ) -> Secret:
        """Create a new Secret

        :param name: Name of secret
        :param value: Value of secret
        :param metadata: Arbitrary user-defined metadata for this Secret
        :param description: description of Secret
        :param vault_id: unique identifier of the referenced vault

        https://ngrok.com/docs/api#api-secrets-create
        """
        path = "/vault_secrets"
        body_arg = dict(
            name=name,
            value=value,
            metadata=metadata,
            description=description,
            vault_id=vault_id,
        )
        result = self._client.http_client.post(path, body_arg)
        return Secret(self._client, result)

    def update(
        self,
        id: str,
        name: str = None,
        value: str = None,
        metadata: str = None,
        description: str = None,
    ) -> Secret:
        """Update an existing Secret by ID

        :param id: identifier for Secret
        :param name: Name of secret
        :param value: Value of secret
        :param metadata: Arbitrary user-defined metadata for this Secret
        :param description: description of Secret

        https://ngrok.com/docs/api#api-secrets-update
        """
        path = "/vault_secrets/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            name=name,
            value=value,
            metadata=metadata,
            description=description,
        )
        result = self._client.http_client.patch(path, body_arg)
        return Secret(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a Secret

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-secrets-delete
        """
        path = "/vault_secrets/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> Secret:
        """Get a Secret by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-secrets-get
        """
        path = "/vault_secrets/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return Secret(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> SecretList:
        """List all Secrets owned by account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-secrets-list
        """
        path = "/vault_secrets"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return SecretList(self._client, result)


class SSHCertificateAuthoritiesClient(object):
    """An SSH Certificate Authority is a pair of an SSH Certificate and its private
    key that can be used to sign other SSH host and user certificates."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        private_key_type: str = "",
        elliptic_curve: str = "",
        key_size: int = 0,
    ) -> SSHCertificateAuthority:
        """Create a new SSH Certificate Authority

        :param description: human-readable description of this SSH Certificate Authority. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this SSH Certificate Authority. optional, max 4096 bytes.
        :param private_key_type: the type of private key to generate. one of ``rsa``, ``ecdsa``, ``ed25519``
        :param elliptic_curve: the type of elliptic curve to use when creating an ECDSA key
        :param key_size: the key size to use when creating an RSA key. one of ``2048`` or ``4096``

        https://ngrok.com/docs/api#api-ssh-certificate-authorities-create
        """
        path = "/ssh_certificate_authorities"
        body_arg = dict(
            description=description,
            metadata=metadata,
            private_key_type=private_key_type,
            elliptic_curve=elliptic_curve,
            key_size=key_size,
        )
        result = self._client.http_client.post(path, body_arg)
        return SSHCertificateAuthority(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an SSH Certificate Authority

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ssh-certificate-authorities-delete
        """
        path = "/ssh_certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> SSHCertificateAuthority:
        """Get detailed information about an SSH Certficate Authority

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ssh-certificate-authorities-get
        """
        path = "/ssh_certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return SSHCertificateAuthority(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> SSHCertificateAuthorityList:
        """List all SSH Certificate Authorities on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-ssh-certificate-authorities-list
        """
        path = "/ssh_certificate_authorities"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return SSHCertificateAuthorityList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
    ) -> SSHCertificateAuthority:
        """Update an SSH Certificate Authority

        :param id:
        :param description: human-readable description of this SSH Certificate Authority. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this SSH Certificate Authority. optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-ssh-certificate-authorities-update
        """
        path = "/ssh_certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.patch(path, body_arg)
        return SSHCertificateAuthority(self._client, result)


class SSHCredentialsClient(object):
    """SSH Credentials are SSH public keys that can be used to start SSH tunnels
    via the ngrok SSH tunnel gateway."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        public_key: str,
        description: str = "",
        metadata: str = "",
        acl: Sequence[str] = [],
        owner_id: str = None,
    ) -> SSHCredential:
        """Create a new ssh_credential from an uploaded public SSH key. This ssh credential can be used to start new tunnels via ngrok's SSH gateway.

        :param description: human-readable description of who or what will use the ssh credential to authenticate. Optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this ssh credential. Optional, max 4096 bytes.
        :param acl: optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains, addresses, and labels the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules for domains may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. Bind rules for labels may specify a wildcard key and/or value to match multiple labels. For example, you may specify a rule of ``bind:*=example`` which will allow ``x=example``, ``y=example``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions.
        :param public_key: the PEM-encoded public key of the SSH keypair that will be used to authenticate
        :param owner_id: If supplied at credential creation, ownership will be assigned to the specified User or Bot. Only admins may specify an owner other than themselves. Defaults to the authenticated User or Bot.

        https://ngrok.com/docs/api#api-ssh-credentials-create
        """
        path = "/ssh_credentials"
        body_arg = dict(
            description=description,
            metadata=metadata,
            acl=acl,
            public_key=public_key,
            owner_id=owner_id,
        )
        result = self._client.http_client.post(path, body_arg)
        return SSHCredential(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an ssh_credential by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ssh-credentials-delete
        """
        path = "/ssh_credentials/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> SSHCredential:
        """Get detailed information about an ssh_credential

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ssh-credentials-get
        """
        path = "/ssh_credentials/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return SSHCredential(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> SSHCredentialList:
        """List all ssh credentials on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-ssh-credentials-list
        """
        path = "/ssh_credentials"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return SSHCredentialList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        acl: Sequence[str] = None,
    ) -> SSHCredential:
        """Update attributes of an ssh_credential by ID

        :param id:
        :param description: human-readable description of who or what will use the ssh credential to authenticate. Optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this ssh credential. Optional, max 4096 bytes.
        :param acl: optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains, addresses, and labels the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules for domains may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. Bind rules for labels may specify a wildcard key and/or value to match multiple labels. For example, you may specify a rule of ``bind:*=example`` which will allow ``x=example``, ``y=example``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions.

        https://ngrok.com/docs/api#api-ssh-credentials-update
        """
        path = "/ssh_credentials/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
            acl=acl,
        )
        result = self._client.http_client.patch(path, body_arg)
        return SSHCredential(self._client, result)


class SSHHostCertificatesClient(object):
    """SSH Host Certificates along with the corresponding private key allows an SSH
    server to assert its authenticity to connecting SSH clients who trust the
    SSH Certificate Authority that was used to sign the certificate."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        ssh_certificate_authority_id: str,
        public_key: str,
        principals: Sequence[str] = [],
        valid_after: datetime = datetime.min,
        valid_until: datetime = datetime.min,
        description: str = "",
        metadata: str = "",
    ) -> SSHHostCertificate:
        """Create a new SSH Host Certificate

        :param ssh_certificate_authority_id: the ssh certificate authority that is used to sign this ssh host certificate
        :param public_key: a public key in OpenSSH Authorized Keys format that this certificate signs
        :param principals: the list of principals included in the ssh host certificate. This is the list of hostnames and/or IP addresses that are authorized to serve SSH traffic with this certificate. Dangerously, if no principals are specified, this certificate is considered valid for all hosts.
        :param valid_after: The time when the host certificate becomes valid, in RFC 3339 format. Defaults to the current time if unspecified.
        :param valid_until: The time when this host certificate becomes invalid, in RFC 3339 format. If unspecified, a default value of one year in the future will be used. The OpenSSH certificates RFC calls this ``valid_before``.
        :param description: human-readable description of this SSH Host Certificate. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this SSH Host Certificate. optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-ssh-host-certificates-create
        """
        path = "/ssh_host_certificates"
        body_arg = dict(
            ssh_certificate_authority_id=ssh_certificate_authority_id,
            public_key=public_key,
            principals=principals,
            valid_after=valid_after,
            valid_until=valid_until,
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.post(path, body_arg)
        return SSHHostCertificate(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an SSH Host Certificate

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ssh-host-certificates-delete
        """
        path = "/ssh_host_certificates/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> SSHHostCertificate:
        """Get detailed information about an SSH Host Certficate

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ssh-host-certificates-get
        """
        path = "/ssh_host_certificates/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return SSHHostCertificate(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> SSHHostCertificateList:
        """List all SSH Host Certificates issued on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-ssh-host-certificates-list
        """
        path = "/ssh_host_certificates"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return SSHHostCertificateList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
    ) -> SSHHostCertificate:
        """Update an SSH Host Certificate

        :param id:
        :param description: human-readable description of this SSH Host Certificate. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this SSH Host Certificate. optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-ssh-host-certificates-update
        """
        path = "/ssh_host_certificates/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.patch(path, body_arg)
        return SSHHostCertificate(self._client, result)


class SSHUserCertificatesClient(object):
    """SSH User Certificates are presented by SSH clients when connecting to an SSH
    server to authenticate their connection. The SSH server must trust the SSH
    Certificate Authority used to sign the certificate."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        ssh_certificate_authority_id: str,
        public_key: str,
        principals: Sequence[str] = [],
        critical_options: Mapping[str, str] = {},
        extensions: Mapping[str, str] = {},
        valid_after: datetime = datetime.min,
        valid_until: datetime = datetime.min,
        description: str = "",
        metadata: str = "",
    ) -> SSHUserCertificate:
        """Create a new SSH User Certificate

        :param ssh_certificate_authority_id: the ssh certificate authority that is used to sign this ssh user certificate
        :param public_key: a public key in OpenSSH Authorized Keys format that this certificate signs
        :param principals: the list of principals included in the ssh user certificate. This is the list of usernames that the certificate holder may sign in as on a machine authorizing the signing certificate authority. Dangerously, if no principals are specified, this certificate may be used to log in as any user.
        :param critical_options: A map of critical options included in the certificate. Only two critical options are currently defined by OpenSSH: ``force-command`` and ``source-address``. See `the OpenSSH certificate protocol spec <https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys>`_ for additional details.
        :param extensions: A map of extensions included in the certificate. Extensions are additional metadata that can be interpreted by the SSH server for any purpose. These can be used to permit or deny the ability to open a terminal, do port forwarding, x11 forwarding, and more. If unspecified, the certificate will include limited permissions with the following extension map: ``{"permit-pty": "", "permit-user-rc": ""}`` OpenSSH understands a number of predefined extensions. See `the OpenSSH certificate protocol spec <https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys>`_ for additional details.
        :param valid_after: The time when the user certificate becomes valid, in RFC 3339 format. Defaults to the current time if unspecified.
        :param valid_until: The time when this host certificate becomes invalid, in RFC 3339 format. If unspecified, a default value of 24 hours will be used. The OpenSSH certificates RFC calls this ``valid_before``.
        :param description: human-readable description of this SSH User Certificate. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this SSH User Certificate. optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-ssh-user-certificates-create
        """
        path = "/ssh_user_certificates"
        body_arg = dict(
            ssh_certificate_authority_id=ssh_certificate_authority_id,
            public_key=public_key,
            principals=principals,
            critical_options=critical_options,
            extensions=extensions,
            valid_after=valid_after,
            valid_until=valid_until,
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.post(path, body_arg)
        return SSHUserCertificate(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an SSH User Certificate

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ssh-user-certificates-delete
        """
        path = "/ssh_user_certificates/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> SSHUserCertificate:
        """Get detailed information about an SSH User Certficate

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-ssh-user-certificates-get
        """
        path = "/ssh_user_certificates/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return SSHUserCertificate(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> SSHUserCertificateList:
        """List all SSH User Certificates issued on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-ssh-user-certificates-list
        """
        path = "/ssh_user_certificates"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return SSHUserCertificateList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
    ) -> SSHUserCertificate:
        """Update an SSH User Certificate

        :param id:
        :param description: human-readable description of this SSH User Certificate. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this SSH User Certificate. optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-ssh-user-certificates-update
        """
        path = "/ssh_user_certificates/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.patch(path, body_arg)
        return SSHUserCertificate(self._client, result)


class TLSCertificatesClient(object):
    """TLS Certificates are pairs of x509 certificates and their matching private
    key that can be used to terminate TLS traffic. TLS certificates are unused
    until they are attached to a Domain. TLS Certificates may also be
    provisioned by ngrok automatically for domains on which you have enabled
    automated certificate provisioning."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        certificate_pem: str,
        private_key_pem: str,
        description: str = "",
        metadata: str = "",
    ) -> TLSCertificate:
        """Upload a new TLS certificate

        :param description: human-readable description of this TLS certificate. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this TLS certificate. optional, max 4096 bytes.
        :param certificate_pem: chain of PEM-encoded certificates, leaf first. See `Certificate Bundles <https://ngrok.com/docs/cloud-edge/endpoints#certificate-chains>`_.
        :param private_key_pem: private key for the TLS certificate, PEM-encoded. See `Private Keys <https://ngrok.com/docs/cloud-edge/endpoints#private-keys>`_.

        https://ngrok.com/docs/api#api-tls-certificates-create
        """
        path = "/tls_certificates"
        body_arg = dict(
            description=description,
            metadata=metadata,
            certificate_pem=certificate_pem,
            private_key_pem=private_key_pem,
        )
        result = self._client.http_client.post(path, body_arg)
        return TLSCertificate(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a TLS certificate

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-certificates-delete
        """
        path = "/tls_certificates/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> TLSCertificate:
        """Get detailed information about a TLS certificate

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tls-certificates-get
        """
        path = "/tls_certificates/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return TLSCertificate(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> TLSCertificateList:
        """List all TLS certificates on this account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-tls-certificates-list
        """
        path = "/tls_certificates"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return TLSCertificateList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
    ) -> TLSCertificate:
        """Update attributes of a TLS Certificate by ID

        :param id:
        :param description: human-readable description of this TLS certificate. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this TLS certificate. optional, max 4096 bytes.

        https://ngrok.com/docs/api#api-tls-certificates-update
        """
        path = "/tls_certificates/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            description=description,
            metadata=metadata,
        )
        result = self._client.http_client.patch(path, body_arg)
        return TLSCertificate(self._client, result)


class TunnelsClient(object):
    """Tunnels provide endpoints to access services exposed by a running ngrok
    agent tunnel session or an SSH reverse tunnel session."""

    def __init__(self, client):
        self._client = client

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> TunnelList:
        """List all online tunnels currently running on the account.

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-tunnels-list
        """
        path = "/tunnels"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return TunnelList(self._client, result)

    def get(
        self,
        id: str,
    ) -> Tunnel:
        """Get the status of a tunnel by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-tunnels-get
        """
        path = "/tunnels/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return Tunnel(self._client, result)


class VaultsClient(object):
    """Vaults is an api service for securely storing and managing sensitive data such as secrets, credentials, and tokens."""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        name: str = "",
        metadata: str = "",
        description: str = "",
    ) -> Vault:
        """Create a new Vault

        :param name: Name of vault
        :param metadata: Arbitrary user-defined metadata for this Vault
        :param description: description of Vault

        https://ngrok.com/docs/api#api-vaults-create
        """
        path = "/vaults"
        body_arg = dict(
            name=name,
            metadata=metadata,
            description=description,
        )
        result = self._client.http_client.post(path, body_arg)
        return Vault(self._client, result)

    def update(
        self,
        id: str,
        name: str = None,
        metadata: str = None,
        description: str = None,
    ) -> Vault:
        """Update an existing Vault by ID

        :param id: identifier for Vault
        :param name: Name of vault
        :param metadata: Arbitrary user-defined metadata for this Vault
        :param description: description of Vault

        https://ngrok.com/docs/api#api-vaults-update
        """
        path = "/vaults/{id}"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            name=name,
            metadata=metadata,
            description=description,
        )
        result = self._client.http_client.patch(path, body_arg)
        return Vault(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a Vault

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-vaults-delete
        """
        path = "/vaults/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        self._client.http_client.delete(path, body_arg)

    def get(
        self,
        id: str,
    ) -> Vault:
        """Get a Vault by ID

        :param id: a resource identifier

        https://ngrok.com/docs/api#api-vaults-get
        """
        path = "/vaults/{id}"
        path = path.format(
            id=id,
        )
        body_arg = None
        result = self._client.http_client.get(path, body_arg)
        return Vault(self._client, result)

    def get_secrets_by_vault(
        self,
        id: str,
        before_id: str = None,
        limit: str = None,
    ) -> SecretList:
        """Get Secrets by Vault ID

        :param id: a resource identifier
        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-vaults-get-secrets-by-vault
        """
        path = "/vaults/{id}/secrets"
        path = path.format(
            id=id,
        )
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return SecretList(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> VaultList:
        """List all Vaults owned by account

        :param before_id:
        :param limit:

        https://ngrok.com/docs/api#api-vaults-list
        """
        path = "/vaults"
        body_arg = dict(
            before_id=before_id,
            limit=limit,
        )
        result = self._client.http_client.get(path, body_arg)
        return VaultList(self._client, result)
