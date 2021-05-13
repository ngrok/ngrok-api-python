from __future__ import annotations
from collections.abc import Iterator
from typing import Any, Mapping, Sequence

from .api_client import APIClient
from .objects import *


class AbuseReportsClient(object):
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
        """
        path = "/abuse_reports"
        result = self._client.api_client.post(
            path,
            dict(
                urls=urls,
                metadata=metadata,
            ),
        )
        return AbuseReport(self._client, result)

    def get(
        self,
        id: str,
    ) -> AbuseReport:
        """Get the detailed status of abuse report by ID.

        :param id: a resource identifier
        """
        path = "/abuse_reports/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return AbuseReport(self._client, result)


class APIKeysClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
    ) -> APIKey:
        """Create a new API key. The generated API key can be used to authenticate to the ngrok API.

        :param description: human-readable description of what uses the API key to authenticate. optional, max 255 bytes.
        :param metadata: arbitrary user-defined data of this API key. optional, max 4096 bytes
        """
        path = "/api_keys"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
            ),
        )
        return APIKey(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an API key by ID

        :param id: a resource identifier
        """
        path = "/api_keys/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> APIKey:
        """Get the details of an API key by ID.

        :param id: a resource identifier
        """
        path = "/api_keys/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return APIKey(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> APIKeyList:
        """List all API keys owned by this account

        :param before_id:
        :param limit:
        """
        path = "/api_keys"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        """
        path = "/api_keys/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
            ),
        )
        return APIKey(self._client, result)


class CertificateAuthoritiesClient(object):
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
        """
        path = "/certificate_authorities"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
                ca_pem=ca_pem,
            ),
        )
        return CertificateAuthority(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a Certificate Authority

        :param id: a resource identifier
        """
        path = "/certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> CertificateAuthority:
        """Get detailed information about a certficate authority

        :param id: a resource identifier
        """
        path = "/certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return CertificateAuthority(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> CertificateAuthorityList:
        """List all Certificate Authority on this account

        :param before_id:
        :param limit:
        """
        path = "/certificate_authorities"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        """
        path = "/certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
            ),
        )
        return CertificateAuthority(self._client, result)


class CredentialsClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        acl: Sequence[str] = [],
    ) -> Credential:
        """Create a new tunnel authtoken credential. This authtoken credential can be used to start a new tunnel session. The response to this API call is the only time the generated token is available. If you need it for future use, you must save it securely yourself.

        :param description: human-readable description of who or what will use the credential to authenticate. Optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this credential. Optional, max 4096 bytes.
        :param acl: optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions.
        """
        path = "/credentials"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
                acl=acl,
            ),
        )
        return Credential(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a tunnel authtoken credential by ID

        :param id: a resource identifier
        """
        path = "/credentials/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> Credential:
        """Get detailed information about a tunnel authtoken credential

        :param id: a resource identifier
        """
        path = "/credentials/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return Credential(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> CredentialList:
        """List all tunnel authtoken credentials on this account

        :param before_id:
        :param limit:
        """
        path = "/credentials"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        :param acl: optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions.
        """
        path = "/credentials/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
                acl=acl,
            ),
        )
        return Credential(self._client, result)


class EventStreamsClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        metadata: str = "",
        description: str = "",
        fields: Sequence[str] = [],
        event_type: str = "",
        destination_ids: Sequence[str] = [],
        sampling_rate: float = 0,
    ) -> EventStream:
        """Create a new Event Stream. It will not apply to anything until you associate it with one or more Endpoint Configs.

        :param metadata: Arbitrary user-defined machine-readable data of this Event Stream. Optional, max 4096 bytes.
        :param description: Human-readable description of the Event Stream. Optional, max 255 bytes.
        :param fields: A list of protocol-specific fields you want to collect on each event.
        :param event_type: The protocol that determines which events will be collected. Supported values are ``tcp_connection_closed`` and ``http_request_complete``.
        :param destination_ids: A list of Event Destination IDs which should be used for this Event Stream. Event Streams are required to have at least one Event Destination.
        :param sampling_rate: The percentage of all events you would like to capture. Valid values range from 0.01, representing 1% of all events to 1.00, representing 100% of all events.
        """
        path = "/event_streams"
        result = self._client.api_client.post(
            path,
            dict(
                metadata=metadata,
                description=description,
                fields=fields,
                event_type=event_type,
                destination_ids=destination_ids,
                sampling_rate=sampling_rate,
            ),
        )
        return EventStream(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an Event Stream. Associated Event Destinations will be preserved.

        :param id: a resource identifier
        """
        path = "/event_streams/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> EventStream:
        """Get detailed information about an Event Stream by ID.

        :param id: a resource identifier
        """
        path = "/event_streams/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EventStream(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> EventStreamList:
        """List all Event Streams available on this account.

        :param before_id:
        :param limit:
        """
        path = "/event_streams"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
        return EventStreamList(self._client, result)

    def update(
        self,
        id: str,
        metadata: str = None,
        description: str = None,
        fields: Sequence[str] = None,
        destination_ids: Sequence[str] = None,
        sampling_rate: float = None,
    ) -> EventStream:
        """Update attributes of an Event Stream by ID.

        :param id: Unique identifier for this Event Stream.
        :param metadata: Arbitrary user-defined machine-readable data of this Event Stream. Optional, max 4096 bytes.
        :param description: Human-readable description of the Event Stream. Optional, max 255 bytes.
        :param fields: A list of protocol-specific fields you want to collect on each event.
        :param destination_ids: A list of Event Destination IDs which should be used for this Event Stream. Event Streams are required to have at least one Event Destination.
        :param sampling_rate: The percentage of all events you would like to capture. Valid values range from 0.01, representing 1% of all events to 1.00, representing 100% of all events.
        """
        path = "/event_streams/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                metadata=metadata,
                description=description,
                fields=fields,
                destination_ids=destination_ids,
                sampling_rate=sampling_rate,
            ),
        )
        return EventStream(self._client, result)


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
        """Create a new Event Destination. It will not apply to anything until it is associated with an Event Stream, and that Event Stream is associated with an Endpoint Config.

        :param metadata: Arbitrary user-defined machine-readable data of this Event Destination. Optional, max 4096 bytes.
        :param description: Human-readable description of the Event Destination. Optional, max 255 bytes.
        :param format: The output format you would like to serialize events into when sending to their target. Currently the only accepted value is ``JSON``.
        :param target: An object that encapsulates where and how to send your events. An event destination must contain exactly one of the following objects, leaving the rest null: ``kinesis``, ``firehose``, ``cloudwatch_logs``, or ``s3``.
        """
        path = "/event_destinations"
        result = self._client.api_client.post(
            path,
            dict(
                metadata=metadata,
                description=description,
                format=format,
                target=target,
            ),
        )
        return EventDestination(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an Event Destination. If the Event Destination is still referenced by an Event Stream, this will throw an error until that Event Stream has removed that reference.

        :param id: a resource identifier
        """
        path = "/event_destinations/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> EventDestination:
        """Get detailed information about an Event Destination by ID.

        :param id: a resource identifier
        """
        path = "/event_destinations/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EventDestination(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> EventDestinationList:
        """List all Event Destinations on this account.

        :param before_id:
        :param limit:
        """
        path = "/event_destinations"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        """
        path = "/event_destinations/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                metadata=metadata,
                description=description,
                format=format,
                target=target,
            ),
        )
        return EventDestination(self._client, result)


class IPPoliciesClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        action: str,
        description: str = "",
        metadata: str = "",
    ) -> IPPolicy:
        """Create a new IP policy. It will not apply to any traffic until you associate to a traffic source via an endpoint configuration or IP restriction.

        :param description: human-readable description of the source IPs of this IP policy. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this IP policy. optional, max 4096 bytes.
        :param action: the IP policy action. Supported values are ``allow`` or ``deny``
        """
        path = "/ip_policies"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
                action=action,
            ),
        )
        return IPPolicy(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an IP policy. If the IP policy is referenced by another object for the purposes of traffic restriction it will be treated as if the IP policy remains but has zero rules.

        :param id: a resource identifier
        """
        path = "/ip_policies/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> IPPolicy:
        """Get detailed information about an IP policy by ID.

        :param id: a resource identifier
        """
        path = "/ip_policies/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return IPPolicy(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> IPPolicyList:
        """List all IP policies on this account

        :param before_id:
        :param limit:
        """
        path = "/ip_policies"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        """
        path = "/ip_policies/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
            ),
        )
        return IPPolicy(self._client, result)


class IPPolicyRulesClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        cidr: str,
        ip_policy_id: str,
        description: str = "",
        metadata: str = "",
    ) -> IPPolicyRule:
        """Create a new IP policy rule attached to an IP Policy.

        :param description: human-readable description of the source IPs of this IP rule. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this IP policy rule. optional, max 4096 bytes.
        :param cidr: an IP or IP range specified in CIDR notation. IPv4 and IPv6 are both supported.
        :param ip_policy_id: ID of the IP policy this IP policy rule will be attached to
        """
        path = "/ip_policy_rules"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
                cidr=cidr,
                ip_policy_id=ip_policy_id,
            ),
        )
        return IPPolicyRule(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an IP policy rule.

        :param id: a resource identifier
        """
        path = "/ip_policy_rules/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> IPPolicyRule:
        """Get detailed information about an IP policy rule by ID.

        :param id: a resource identifier
        """
        path = "/ip_policy_rules/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return IPPolicyRule(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> IPPolicyRuleList:
        """List all IP policy rules on this account

        :param before_id:
        :param limit:
        """
        path = "/ip_policy_rules"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        """
        path = "/ip_policy_rules/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
                cidr=cidr,
            ),
        )
        return IPPolicyRule(self._client, result)


class IPRestrictionsClient(object):
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
        :param enforced: true if the IP restriction will be enforce. if false, only warnings will be issued
        :param type: the type of IP restriction. this defines what traffic will be restricted with the attached policies. four values are currently supported: ``dashboard``, ``api``, ``agent``, and ``endpoints``
        :param ip_policy_ids: the set of IP policy identifiers that are used to enforce the restriction
        """
        path = "/ip_restrictions"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
                enforced=enforced,
                type=type,
                ip_policy_ids=ip_policy_ids,
            ),
        )
        return IPRestriction(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an IP restriction

        :param id: a resource identifier
        """
        path = "/ip_restrictions/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> IPRestriction:
        """Get detailed information about an IP restriction

        :param id: a resource identifier
        """
        path = "/ip_restrictions/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return IPRestriction(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> IPRestrictionList:
        """List all IP restrictions on this account

        :param before_id:
        :param limit:
        """
        path = "/ip_restrictions"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        :param enforced: true if the IP restriction will be enforce. if false, only warnings will be issued
        :param ip_policy_ids: the set of IP policy identifiers that are used to enforce the restriction
        """
        path = "/ip_restrictions/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
                enforced=enforced,
                ip_policy_ids=ip_policy_ids,
            ),
        )
        return IPRestriction(self._client, result)


class IPWhitelistClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        ip_net: str = "",
    ) -> IPWhitelistEntry:
        """Create a new IP whitelist entry that will restrict traffic to all tunnel endpoints on the account.

        :param description: human-readable description of the source IPs for this IP whitelist entry. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this IP whitelist entry. optional, max 4096 bytes.
        :param ip_net: an IP address or IP network range in CIDR notation (e.g. 10.1.1.1 or 10.1.0.0/16) of addresses that will be whitelisted to communicate with your tunnel endpoints
        """
        path = "/ip_whitelist"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
                ip_net=ip_net,
            ),
        )
        return IPWhitelistEntry(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an IP whitelist entry.

        :param id: a resource identifier
        """
        path = "/ip_whitelist/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> IPWhitelistEntry:
        """Get detailed information about an IP whitelist entry by ID.

        :param id: a resource identifier
        """
        path = "/ip_whitelist/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return IPWhitelistEntry(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> IPWhitelistEntryList:
        """List all IP whitelist entries on this account

        :param before_id:
        :param limit:
        """
        path = "/ip_whitelist"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
        return IPWhitelistEntryList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
    ) -> IPWhitelistEntry:
        """Update attributes of an IP whitelist entry by ID

        :param id:
        :param description: human-readable description of the source IPs for this IP whitelist entry. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this IP whitelist entry. optional, max 4096 bytes.
        """
        path = "/ip_whitelist/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
            ),
        )
        return IPWhitelistEntry(self._client, result)


class EndpointConfigurationsClient(object):
    """Endpoint Configuration managementAn `Endpoint Configuration` <https://ngrok.com/docs/ngrok-link#api-endpoint-configurations>`_ describes
    a ngrok network endpoint instance.*Endpoints are your gateway to ngrok features!*"""

    def __init__(self, client):
        self._client = client

    def create(
        self,
        type: str = "",
        description: str = "",
        metadata: str = "",
        circuit_breaker: EndpointCircuitBreaker = None,
        compression: EndpointCompression = None,
        request_headers: EndpointRequestHeaders = None,
        response_headers: EndpointResponseHeaders = None,
        ip_policy: EndpointIPPolicyMutate = None,
        mutual_tls: EndpointMutualTLSMutate = None,
        tls_termination: EndpointTLSTermination = None,
        webhook_validation: EndpointWebhookValidation = None,
        oauth: EndpointOAuth = None,
        logging: EndpointLoggingMutate = None,
        saml: EndpointSAMLMutate = None,
        oidc: EndpointOIDC = None,
    ) -> EndpointConfiguration:
        """Create a new endpoint configuration

        :param type: they type of traffic this endpoint configuration can be applied to. one of: ``http``, ``https``, ``tcp``
        :param description: human-readable description of what this endpoint configuration will be do when applied or what traffic it will be applied to. Optional, max 255 bytes
        :param metadata: arbitrary user-defined machine-readable data of this endpoint configuration. Optional, max 4096 bytes.
        :param circuit_breaker: circuit breaker module configuration or ``null``
        :param compression: compression module configuration or ``null``
        :param request_headers: request headers module configuration or ``null``
        :param response_headers: response headers module configuration or ``null``
        :param ip_policy: ip policy module configuration or ``null``
        :param mutual_tls: mutual TLS module configuration or ``null``
        :param tls_termination: TLS termination module configuration or ``null``
        :param webhook_validation: webhook validation module configuration or ``null``
        :param oauth: oauth module configuration or ``null``
        :param logging: logging module configuration or ``null``
        :param saml: saml module configuration or ``null``
        :param oidc: oidc module configuration or ``null``
        """
        path = "/endpoint_configurations"
        result = self._client.api_client.post(
            path,
            dict(
                type=type,
                description=description,
                metadata=metadata,
                circuit_breaker=circuit_breaker,
                compression=compression,
                request_headers=request_headers,
                response_headers=response_headers,
                ip_policy=ip_policy,
                mutual_tls=mutual_tls,
                tls_termination=tls_termination,
                webhook_validation=webhook_validation,
                oauth=oauth,
                logging=logging,
                saml=saml,
                oidc=oidc,
            ),
        )
        return EndpointConfiguration(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an endpoint configuration. This operation will fail if the endpoint configuration is still referenced by any reserved domain or reserved address.

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> EndpointConfiguration:
        """Returns detailed information about an endpoint configuration

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointConfiguration(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> EndpointConfigurationList:
        """Returns a list of all endpoint configurations on this account

        :param before_id:
        :param limit:
        """
        path = "/endpoint_configurations"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
        return EndpointConfigurationList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        circuit_breaker: EndpointCircuitBreaker = None,
        compression: EndpointCompression = None,
        request_headers: EndpointRequestHeaders = None,
        response_headers: EndpointResponseHeaders = None,
        ip_policy: EndpointIPPolicyMutate = None,
        mutual_tls: EndpointMutualTLSMutate = None,
        tls_termination: EndpointTLSTermination = None,
        webhook_validation: EndpointWebhookValidation = None,
        oauth: EndpointOAuth = None,
        logging: EndpointLoggingMutate = None,
        saml: EndpointSAMLMutate = None,
        oidc: EndpointOIDC = None,
    ) -> EndpointConfiguration:
        """Updates an endpoint configuration. If a module is not specified in the update, it will not be modified. However, each module configuration that is specified will completely replace the existing value. There is no way to delete an existing module via this API, instead use the delete module API.

        :param id: unique identifier of this endpoint configuration
        :param description: human-readable description of what this endpoint configuration will be do when applied or what traffic it will be applied to. Optional, max 255 bytes
        :param metadata: arbitrary user-defined machine-readable data of this endpoint configuration. Optional, max 4096 bytes.
        :param circuit_breaker: circuit breaker module configuration or ``null``
        :param compression: compression module configuration or ``null``
        :param request_headers: request headers module configuration or ``null``
        :param response_headers: response headers module configuration or ``null``
        :param ip_policy: ip policy module configuration or ``null``
        :param mutual_tls: mutual TLS module configuration or ``null``
        :param tls_termination: TLS termination module configuration or ``null``
        :param webhook_validation: webhook validation module configuration or ``null``
        :param oauth: oauth module configuration or ``null``
        :param logging: logging module configuration or ``null``
        :param saml: saml module configuration or ``null``
        :param oidc: oidc module configuration or ``null``
        """
        path = "/endpoint_configurations/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
                circuit_breaker=circuit_breaker,
                compression=compression,
                request_headers=request_headers,
                response_headers=response_headers,
                ip_policy=ip_policy,
                mutual_tls=mutual_tls,
                tls_termination=tls_termination,
                webhook_validation=webhook_validation,
                oauth=oauth,
                logging=logging,
                saml=saml,
                oidc=oidc,
            ),
        )
        return EndpointConfiguration(self._client, result)


class EndpointLoggingModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointLoggingMutate = None,
    ) -> EndpointLogging:
        """

        :param id:
        :param module:
        """
        path = "/endpoint_configurations/{id}/logging"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointLogging(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointLogging:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/logging"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointLogging(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/logging"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointCircuitBreakerModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointCircuitBreaker = None,
    ) -> EndpointCircuitBreaker:
        """

        :param id:
        :param module:
        """
        path = "/endpoint_configurations/{id}/circuit_breaker"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointCircuitBreaker(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointCircuitBreaker:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/circuit_breaker"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointCircuitBreaker(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/circuit_breaker"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointCompressionModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointCompression = None,
    ) -> EndpointCompression:
        """

        :param id:
        :param module:
        """
        path = "/endpoint_configurations/{id}/compression"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointCompression(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointCompression:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/compression"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointCompression(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/compression"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointTLSTerminationModuleClient(object):
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
        """
        path = "/endpoint_configurations/{id}/tls_termination"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointTLSTermination(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointTLSTermination:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/tls_termination"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointTLSTermination(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/tls_termination"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointIPPolicyModuleClient(object):
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
        """
        path = "/endpoint_configurations/{id}/ip_policy"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointIPPolicy(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointIPPolicy:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/ip_policy"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointIPPolicy(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/ip_policy"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointMutualTLSModuleClient(object):
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
        """
        path = "/endpoint_configurations/{id}/mutual_tls"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointMutualTLS(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointMutualTLS:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/mutual_tls"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointMutualTLS(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/mutual_tls"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointRequestHeadersModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointRequestHeaders = None,
    ) -> EndpointRequestHeaders:
        """

        :param id:
        :param module:
        """
        path = "/endpoint_configurations/{id}/request_headers"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointRequestHeaders(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointRequestHeaders:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/request_headers"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointRequestHeaders(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/request_headers"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointResponseHeadersModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointResponseHeaders = None,
    ) -> EndpointResponseHeaders:
        """

        :param id:
        :param module:
        """
        path = "/endpoint_configurations/{id}/response_headers"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointResponseHeaders(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointResponseHeaders:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/response_headers"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointResponseHeaders(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/response_headers"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointOAuthModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointOAuth = None,
    ) -> EndpointOAuth:
        """

        :param id:
        :param module:
        """
        path = "/endpoint_configurations/{id}/oauth"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointOAuth(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointOAuth:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/oauth"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointOAuth(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/oauth"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointWebhookValidationModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointWebhookValidation = None,
    ) -> EndpointWebhookValidation:
        """

        :param id:
        :param module:
        """
        path = "/endpoint_configurations/{id}/webhook_validation"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointWebhookValidation(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointWebhookValidation:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/webhook_validation"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointWebhookValidation(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/webhook_validation"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointSAMLModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointSAMLMutate = None,
    ) -> EndpointSAML:
        """

        :param id:
        :param module:
        """
        path = "/endpoint_configurations/{id}/saml"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointSAML(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointSAML:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/saml"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointSAML(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/saml"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class EndpointOIDCModuleClient(object):
    def __init__(self, client):
        self._client = client

    def replace(
        self,
        id: str,
        module: EndpointOIDC = None,
    ) -> EndpointOIDC:
        """

        :param id:
        :param module:
        """
        path = "/endpoint_configurations/{id}/oidc"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.put(
            path,
            dict(
                module=module,
            ),
        )
        return EndpointOIDC(self._client, result)

    def get(
        self,
        id: str,
    ) -> EndpointOIDC:
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/oidc"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return EndpointOIDC(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """

        :param id: a resource identifier
        """
        path = "/endpoint_configurations/{id}/oidc"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class ReservedAddrsClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        description: str = "",
        metadata: str = "",
        region: str = "",
        endpoint_configuration_id: str = "",
    ) -> ReservedAddr:
        """Create a new reserved address.

        :param description: human-readable description of what this reserved address will be used for
        :param metadata: arbitrary user-defined machine-readable data of this reserved address. Optional, max 4096 bytes.
        :param region: reserve the address in this geographic ngrok datacenter. Optional, default is us. (au, eu, ap, us, jp, in, sa)
        :param endpoint_configuration_id: ID of an endpoint configuration of type tcp that will be used to handle inbound traffic to this address
        """
        path = "/reserved_addrs"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
                region=region,
                endpoint_configuration_id=endpoint_configuration_id,
            ),
        )
        return ReservedAddr(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a reserved address.

        :param id: a resource identifier
        """
        path = "/reserved_addrs/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> ReservedAddr:
        """Get the details of a reserved address.

        :param id: a resource identifier
        """
        path = "/reserved_addrs/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return ReservedAddr(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> ReservedAddrList:
        """List all reserved addresses on this account.

        :param before_id:
        :param limit:
        """
        path = "/reserved_addrs"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
        return ReservedAddrList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        endpoint_configuration_id: str = None,
    ) -> ReservedAddr:
        """Update the attributes of a reserved address.

        :param id:
        :param description: human-readable description of what this reserved address will be used for
        :param metadata: arbitrary user-defined machine-readable data of this reserved address. Optional, max 4096 bytes.
        :param endpoint_configuration_id: ID of an endpoint configuration of type tcp that will be used to handle inbound traffic to this address
        """
        path = "/reserved_addrs/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
                endpoint_configuration_id=endpoint_configuration_id,
            ),
        )
        return ReservedAddr(self._client, result)

    def delete_endpoint_config(
        self,
        id: str,
    ):
        """Detach the endpoint configuration attached to a reserved address.

        :param id: a resource identifier
        """
        path = "/reserved_addrs/{id}/endpoint_configuration"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class ReservedDomainsClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        name: str,
        region: str = "",
        description: str = "",
        metadata: str = "",
        http_endpoint_configuration_id: str = "",
        https_endpoint_configuration_id: str = "",
        certificate_id: str = None,
        certificate_management_policy: ReservedDomainCertPolicy = None,
    ) -> ReservedDomain:
        """Create a new reserved domain.

        :param name: the domain name to reserve. It may be a full domain name like app.example.com. If the name does not contain a '.' it will reserve that subdomain on ngrok.io.
        :param region: reserve the domain in this geographic ngrok datacenter. Optional, default is us. (au, eu, ap, us, jp, in, sa)
        :param description: human-readable description of what this reserved domain will be used for
        :param metadata: arbitrary user-defined machine-readable data of this reserved domain. Optional, max 4096 bytes.
        :param http_endpoint_configuration_id: ID of an endpoint configuration of type http that will be used to handle inbound http traffic to this domain
        :param https_endpoint_configuration_id: ID of an endpoint configuration of type https that will be used to handle inbound https traffic to this domain
        :param certificate_id: ID of a user-uploaded TLS certificate to use for connections to targeting this domain. Optional, mutually exclusive with ``certificate_management_policy``.
        :param certificate_management_policy: configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled. Optional, mutually exclusive with ``certificate_id``.
        """
        path = "/reserved_domains"
        result = self._client.api_client.post(
            path,
            dict(
                name=name,
                region=region,
                description=description,
                metadata=metadata,
                http_endpoint_configuration_id=http_endpoint_configuration_id,
                https_endpoint_configuration_id=https_endpoint_configuration_id,
                certificate_id=certificate_id,
                certificate_management_policy=certificate_management_policy,
            ),
        )
        return ReservedDomain(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a reserved domain.

        :param id: a resource identifier
        """
        path = "/reserved_domains/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> ReservedDomain:
        """Get the details of a reserved domain.

        :param id: a resource identifier
        """
        path = "/reserved_domains/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return ReservedDomain(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> ReservedDomainList:
        """List all reserved domains on this account.

        :param before_id:
        :param limit:
        """
        path = "/reserved_domains"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
        return ReservedDomainList(self._client, result)

    def update(
        self,
        id: str,
        description: str = None,
        metadata: str = None,
        http_endpoint_configuration_id: str = None,
        https_endpoint_configuration_id: str = None,
        certificate_id: str = None,
        certificate_management_policy: ReservedDomainCertPolicy = None,
    ) -> ReservedDomain:
        """Update the attributes of a reserved domain.

        :param id:
        :param description: human-readable description of what this reserved domain will be used for
        :param metadata: arbitrary user-defined machine-readable data of this reserved domain. Optional, max 4096 bytes.
        :param http_endpoint_configuration_id: ID of an endpoint configuration of type http that will be used to handle inbound http traffic to this domain
        :param https_endpoint_configuration_id: ID of an endpoint configuration of type https that will be used to handle inbound https traffic to this domain
        :param certificate_id: ID of a user-uploaded TLS certificate to use for connections to targeting this domain. Optional, mutually exclusive with ``certificate_management_policy``.
        :param certificate_management_policy: configuration for automatic management of TLS certificates for this domain, or null if automatic management is disabled. Optional, mutually exclusive with ``certificate_id``.
        """
        path = "/reserved_domains/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
                http_endpoint_configuration_id=http_endpoint_configuration_id,
                https_endpoint_configuration_id=https_endpoint_configuration_id,
                certificate_id=certificate_id,
                certificate_management_policy=certificate_management_policy,
            ),
        )
        return ReservedDomain(self._client, result)

    def delete_certificate_management_policy(
        self,
        id: str,
    ):
        """Detach the certificate management policy attached to a reserved domain.

        :param id: a resource identifier
        """
        path = "/reserved_domains/{id}/certificate_management_policy"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def delete_certificate(
        self,
        id: str,
    ):
        """Detach the certificate attached to a reserved domain.

        :param id: a resource identifier
        """
        path = "/reserved_domains/{id}/certificate"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def delete_http_endpoint_config(
        self,
        id: str,
    ):
        """Detach the http endpoint configuration attached to a reserved domain.

        :param id: a resource identifier
        """
        path = "/reserved_domains/{id}/http_endpoint_configuration"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def delete_https_endpoint_config(
        self,
        id: str,
    ):
        """Detach the https endpoint configuration attached to a reserved domain.

        :param id: a resource identifier
        """
        path = "/reserved_domains/{id}/https_endpoint_configuration"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())


class SSHCertificateAuthoritiesClient(object):
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
        """
        path = "/ssh_certificate_authorities"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
                private_key_type=private_key_type,
                elliptic_curve=elliptic_curve,
                key_size=key_size,
            ),
        )
        return SSHCertificateAuthority(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an SSH Certificate Authority

        :param id: a resource identifier
        """
        path = "/ssh_certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> SSHCertificateAuthority:
        """Get detailed information about an SSH Certficate Authority

        :param id: a resource identifier
        """
        path = "/ssh_certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return SSHCertificateAuthority(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> SSHCertificateAuthorityList:
        """List all SSH Certificate Authorities on this account

        :param before_id:
        :param limit:
        """
        path = "/ssh_certificate_authorities"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        """
        path = "/ssh_certificate_authorities/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
            ),
        )
        return SSHCertificateAuthority(self._client, result)


class SSHCredentialsClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        public_key: str,
        description: str = "",
        metadata: str = "",
        acl: Sequence[str] = [],
    ) -> SSHCredential:
        """Create a new ssh_credential from an uploaded public SSH key. This ssh credential can be used to start new tunnels via ngrok's SSH gateway.

        :param description: human-readable description of who or what will use the ssh credential to authenticate. Optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this ssh credential. Optional, max 4096 bytes.
        :param acl: optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions.
        :param public_key: the PEM-encoded public key of the SSH keypair that will be used to authenticate
        """
        path = "/ssh_credentials"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
                acl=acl,
                public_key=public_key,
            ),
        )
        return SSHCredential(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an ssh_credential by ID

        :param id: a resource identifier
        """
        path = "/ssh_credentials/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> SSHCredential:
        """Get detailed information about an ssh_credential

        :param id: a resource identifier
        """
        path = "/ssh_credentials/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return SSHCredential(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> SSHCredentialList:
        """List all ssh credentials on this account

        :param before_id:
        :param limit:
        """
        path = "/ssh_credentials"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        :param acl: optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions.
        """
        path = "/ssh_credentials/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
                acl=acl,
            ),
        )
        return SSHCredential(self._client, result)


class SSHHostCertificatesClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        ssh_certificate_authority_id: str,
        public_key: str,
        principals: Sequence[str] = [],
        valid_after: str = "",
        valid_until: str = "",
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
        """
        path = "/ssh_host_certificates"
        result = self._client.api_client.post(
            path,
            dict(
                ssh_certificate_authority_id=ssh_certificate_authority_id,
                public_key=public_key,
                principals=principals,
                valid_after=valid_after,
                valid_until=valid_until,
                description=description,
                metadata=metadata,
            ),
        )
        return SSHHostCertificate(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an SSH Host Certificate

        :param id: a resource identifier
        """
        path = "/ssh_host_certificates/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> SSHHostCertificate:
        """Get detailed information about an SSH Host Certficate

        :param id: a resource identifier
        """
        path = "/ssh_host_certificates/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return SSHHostCertificate(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> SSHHostCertificateList:
        """List all SSH Host Certificates issued on this account

        :param before_id:
        :param limit:
        """
        path = "/ssh_host_certificates"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        """
        path = "/ssh_host_certificates/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
            ),
        )
        return SSHHostCertificate(self._client, result)


class SSHUserCertificatesClient(object):
    def __init__(self, client):
        self._client = client

    def create(
        self,
        ssh_certificate_authority_id: str,
        public_key: str,
        principals: Sequence[str] = [],
        critical_options: Mapping[str, str] = {},
        extensions: Mapping[str, str] = {},
        valid_after: str = "",
        valid_until: str = "",
        description: str = "",
        metadata: str = "",
    ) -> SSHUserCertificate:
        """Create a new SSH User Certificate

        :param ssh_certificate_authority_id: the ssh certificate authority that is used to sign this ssh user certificate
        :param public_key: a public key in OpenSSH Authorized Keys format that this certificate signs
        :param principals: the list of principals included in the ssh user certificate. This is the list of usernames that the certificate holder may sign in as on a machine authorizinig the signing certificate authority. Dangerously, if no principals are specified, this certificate may be used to log in as any user.
        :param critical_options: A map of critical options included in the certificate. Only two critical options are currently defined by OpenSSH: ``force-command`` and ``source-address``. See `the OpenSSH certificate protocol spec` <https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys>`_ for additional details.
        :param extensions: A map of extensions included in the certificate. Extensions are additional metadata that can be interpreted by the SSH server for any purpose. These can be used to permit or deny the ability to open a terminal, do port forwarding, x11 forwarding, and more. If unspecified, the certificate will include limited permissions with the following extension map: ``{"permit-pty": "", "permit-user-rc": ""}`` OpenSSH understands a number of predefined extensions. See `the OpenSSH certificate protocol spec` <https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys>`_ for additional details.
        :param valid_after: The time when the user certificate becomes valid, in RFC 3339 format. Defaults to the current time if unspecified.
        :param valid_until: The time when this host certificate becomes invalid, in RFC 3339 format. If unspecified, a default value of 24 hours will be used. The OpenSSH certificates RFC calls this ``valid_before``.
        :param description: human-readable description of this SSH User Certificate. optional, max 255 bytes.
        :param metadata: arbitrary user-defined machine-readable data of this SSH User Certificate. optional, max 4096 bytes.
        """
        path = "/ssh_user_certificates"
        result = self._client.api_client.post(
            path,
            dict(
                ssh_certificate_authority_id=ssh_certificate_authority_id,
                public_key=public_key,
                principals=principals,
                critical_options=critical_options,
                extensions=extensions,
                valid_after=valid_after,
                valid_until=valid_until,
                description=description,
                metadata=metadata,
            ),
        )
        return SSHUserCertificate(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete an SSH User Certificate

        :param id: a resource identifier
        """
        path = "/ssh_user_certificates/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> SSHUserCertificate:
        """Get detailed information about an SSH User Certficate

        :param id: a resource identifier
        """
        path = "/ssh_user_certificates/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return SSHUserCertificate(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> SSHUserCertificateList:
        """List all SSH User Certificates issued on this account

        :param before_id:
        :param limit:
        """
        path = "/ssh_user_certificates"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        """
        path = "/ssh_user_certificates/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
            ),
        )
        return SSHUserCertificate(self._client, result)


class TLSCertificatesClient(object):
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
        :param certificate_pem: chain of PEM-encoded certificates, leaf first. See `Certificate Bundles` <https://ngrok.com/docs/api#tls-certificates-pem>`_.
        :param private_key_pem: private key for the TLS certificate, PEM-encoded. See `Private Keys` <https://ngrok.com/docs/ngrok-link#tls-certificates-key>`_.
        """
        path = "/tls_certificates"
        result = self._client.api_client.post(
            path,
            dict(
                description=description,
                metadata=metadata,
                certificate_pem=certificate_pem,
                private_key_pem=private_key_pem,
            ),
        )
        return TLSCertificate(self._client, result)

    def delete(
        self,
        id: str,
    ):
        """Delete a TLS certificate

        :param id: a resource identifier
        """
        path = "/tls_certificates/{id}"
        path = path.format(
            id=id,
        )
        self._client.api_client.delete(path, dict())

    def get(
        self,
        id: str,
    ) -> TLSCertificate:
        """Get detailed information about a TLS certificate

        :param id: a resource identifier
        """
        path = "/tls_certificates/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return TLSCertificate(self._client, result)

    def list(
        self,
        before_id: str = None,
        limit: str = None,
    ) -> TLSCertificateList:
        """List all TLS certificates on this account

        :param before_id:
        :param limit:
        """
        path = "/tls_certificates"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
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
        """
        path = "/tls_certificates/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.patch(
            path,
            dict(
                description=description,
                metadata=metadata,
            ),
        )
        return TLSCertificate(self._client, result)


class TunnelSessionsClient(object):
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
        """
        path = "/tunnel_sessions"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
        return TunnelSessionList(self._client, result)

    def get(
        self,
        id: str,
    ) -> TunnelSession:
        """Get the detailed status of a tunnel session by ID

        :param id: a resource identifier
        """
        path = "/tunnel_sessions/{id}"
        path = path.format(
            id=id,
        )
        result = self._client.api_client.get(path, dict())
        return TunnelSession(self._client, result)

    def restart(
        self,
        id: str,
    ):
        """Issues a command instructing the ngrok agent to restart. The agent restarts itself by calling exec() on platforms that support it. This operation is notably not supported on Windows. When an agent restarts, it reconnects with a new tunnel session ID.

        :param id: a resource identifier
        """
        path = "/tunnel_sessions/{id}/restart"
        path = path.format(
            id=id,
        )
        self._client.api_client.post(path, dict())

    def stop(
        self,
        id: str,
    ):
        """Issues a command instructing the ngrok agent that started this tunnel session to exit.

        :param id: a resource identifier
        """
        path = "/tunnel_sessions/{id}/stop"
        path = path.format(
            id=id,
        )
        self._client.api_client.post(path, dict())

    def update(
        self,
        id: str,
    ):
        """Issues a command instructing the ngrok agent to update itself to the latest version. After this call completes successfully, the ngrok agent will be in the update process. A caller should wait some amount of time to allow the update to complete (at least 10 seconds) before making a call to the Restart endpoint to request that the agent restart itself to start using the new code. This call will never update an ngrok agent to a new major version which could cause breaking compatibility issues. If you wish to update to a new major version, that must be done manually. Still, please be aware that updating your ngrok agent could break your integration. This call will fail in any of the following circumstances: there is no update available the ngrok agent's configuration disabled update checks the agent is currently in process of updating the agent has already successfully updated but has not yet been restarted

        :param id:
        """
        path = "/tunnel_sessions/{id}/update"
        path = path.format(
            id=id,
        )
        self._client.api_client.post(path, dict())


class TunnelsClient(object):
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
        """
        path = "/tunnels"
        result = self._client.api_client.get(
            path,
            dict(
                before_id=before_id,
                limit=limit,
            ),
        )
        return TunnelList(self._client, result)
