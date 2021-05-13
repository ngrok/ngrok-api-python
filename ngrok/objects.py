from __future__ import annotations
from typing import Any, Mapping, Sequence
from .iterator import PagedIterator


class Ref(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<Ref {}>".format(self.id)

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
        self._props["hostnames"] = [
            AbuseReportHostname(client, x) for x in props["hostnames"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<AbuseReport {}>".format(self.id)

    @property
    def id(self) -> str:
        """ID of the abuse report"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the abuse report API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> str:
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

    def __repr__(self):
        return "<AbuseReportHostname {}>".format(self.id)

    @property
    def hostname(self) -> str:
        """the hostname ngrok has parsed out of one of the reported URLs in this abuse report"""
        return self._props["hostname"]

    @property
    def status(self) -> str:
        """indicates what action ngrok has taken against the hostname. one of ``PENDING``, ``BANNED``, ``UNBANNED``, or ``IGNORE``"""
        return self._props["status"]


class APIKey(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<APIKey {}>".format(self.id)

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
    def created_at(self) -> str:
        """timestamp when the api key was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def token(self) -> str:
        """the bearer token that can be placed into the Authorization header to authenticate request to the ngrok API. **This value is only available one time, on the API response from key creation. Otherwise it is null.**"""
        return self._props["token"]


class APIKeyList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["keys"] = [APIKey(client, x) for x in props["keys"]]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<APIKeyList {}>".format(self.id)

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


class CertificateAuthority(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<CertificateAuthority {}>".format(self.id)

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
    def created_at(self) -> str:
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
    def not_before(self) -> str:
        """timestamp when this Certificate Authority becomes valid, RFC 3339 format"""
        return self._props["not_before"]

    @property
    def not_after(self) -> str:
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
        self._props["certificate_authorities"] = [
            CertificateAuthority(client, x) for x in props["certificate_authorities"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<CertificateAuthorityList {}>".format(self.id)

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

    def __repr__(self):
        return "<Credential {}>".format(self.id)

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
    def created_at(self) -> str:
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
        """the credential's authtoken that can be used to authenticate an ngrok client. **This value is only available one time, on the API response from credential creation, otherwise it is null.**"""
        return self._props["token"]

    @property
    def acl(self) -> Sequence[str]:
        """optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions."""
        return self._props["acl"]


class CredentialList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["credentials"] = [
            Credential(client, x) for x in props["credentials"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<CredentialList {}>".format(self.id)

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


class EventStreamList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["event_streams"] = [
            EventStream(client, x) for x in props["event_streams"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EventStreamList {}>".format(self.id)

    def __iter__(self):
        return PagedIterator(self._client, self, "event_streams")

    @property
    def event_streams(self) -> Sequence[EventStream]:
        """The list of all Event Streams on this account."""
        return self._props["event_streams"]

    @property
    def uri(self) -> str:
        """URI of the Event Stream list API resource."""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page."""
        return self._props["next_page_uri"]


class EventStream(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EventStream {}>".format(self.id)

    def delete(
        self,
    ):
        self._client.event_streams.delete(
            id=self.id,
        )

    def update(
        self,
        metadata: str = None,
        description: str = None,
        fields: Sequence[str] = None,
        destination_ids: Sequence[str] = None,
        sampling_rate: float = None,
    ):
        self._client.event_streams.update(
            id=self.id,
            metadata=metadata,
            description=description,
            fields=fields,
            destination_ids=destination_ids,
            sampling_rate=sampling_rate,
        )

    @property
    def id(self) -> str:
        """Unique identifier for this Event Stream."""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the Event Stream API resource."""
        return self._props["uri"]

    @property
    def created_at(self) -> str:
        """Timestamp when the Event Stream was created, RFC 3339 format."""
        return self._props["created_at"]

    @property
    def metadata(self) -> str:
        """Arbitrary user-defined machine-readable data of this Event Stream. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def description(self) -> str:
        """Human-readable description of the Event Stream. Optional, max 255 bytes."""
        return self._props["description"]

    @property
    def fields(self) -> Sequence[str]:
        """A list of protocol-specific fields you want to collect on each event."""
        return self._props["fields"]

    @property
    def event_type(self) -> str:
        """The protocol that determines which events will be collected. Supported values are ``tcp_connection_closed`` and ``http_request_complete``."""
        return self._props["event_type"]

    @property
    def destination_ids(self) -> Sequence[str]:
        """A list of Event Destination IDs which should be used for this Event Stream. Event Streams are required to have at least one Event Destination."""
        return self._props["destination_ids"]

    @property
    def sampling_rate(self) -> float:
        """The percentage of all events you would like to capture. Valid values range from 0.01, representing 1% of all events to 1.00, representing 100% of all events."""
        return self._props["sampling_rate"]


class EventDestination(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["target"] = EventTarget(client, props["target"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EventDestination {}>".format(self.id)

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
    def created_at(self) -> str:
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
        self._props["event_destinations"] = [
            EventDestination(client, x) for x in props["event_destinations"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EventDestinationList {}>".format(self.id)

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
        self._props["firehose"] = EventTargetFirehose(client, props["firehose"])
        self._props["kinesis"] = EventTargetKinesis(client, props["kinesis"])
        self._props["cloudwatch_logs"] = EventTargetCloudwatchLogs(
            client, props["cloudwatch_logs"]
        )

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EventTarget {}>".format(self.id)

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


class EventTargetFirehose(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["auth"] = AWSAuth(client, props["auth"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EventTargetFirehose {}>".format(self.id)

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
        self._props["auth"] = AWSAuth(client, props["auth"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EventTargetKinesis {}>".format(self.id)

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
        self._props["auth"] = AWSAuth(client, props["auth"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EventTargetCloudwatchLogs {}>".format(self.id)

    @property
    def auth(self) -> AWSAuth:
        """Configuration for how to authenticate into your AWS account. Exactly one of ``role`` or ``creds`` should be configured."""
        return self._props["auth"]

    @property
    def log_group_arn(self) -> str:
        """An Amazon Resource Name specifying the CloudWatch Logs group to deposit events into."""
        return self._props["log_group_arn"]


class AWSAuth(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["role"] = AWSRole(client, props["role"])
        self._props["creds"] = AWSCredentials(client, props["creds"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<AWSAuth {}>".format(self.id)

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

    def __repr__(self):
        return "<AWSRole {}>".format(self.id)

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

    def __repr__(self):
        return "<AWSCredentials {}>".format(self.id)

    @property
    def aws_access_key_id(self) -> str:
        """The ID portion of an AWS access key."""
        return self._props["aws_access_key_id"]

    @property
    def aws_secret_access_key(self) -> str:
        """The secret portion of an AWS access key."""
        return self._props["aws_secret_access_key"]


class IPPolicy(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<IPPolicy {}>".format(self.id)

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
    def created_at(self) -> str:
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

    @property
    def action(self) -> str:
        """the IP policy action. Supported values are ``allow`` or ``deny``"""
        return self._props["action"]


class IPPolicyList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ip_policies"] = [IPPolicy(client, x) for x in props["ip_policies"]]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<IPPolicyList {}>".format(self.id)

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
        self._props["ip_policy"] = Ref(client, props["ip_policy"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<IPPolicyRule {}>".format(self.id)

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
    def created_at(self) -> str:
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


class IPPolicyRuleList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ip_policy_rules"] = [
            IPPolicyRule(client, x) for x in props["ip_policy_rules"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<IPPolicyRuleList {}>".format(self.id)

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
        self._props["ip_policies"] = [Ref(client, x) for x in props["ip_policies"]]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<IPRestriction {}>".format(self.id)

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
    def created_at(self) -> str:
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
        """true if the IP restriction will be enforce. if false, only warnings will be issued"""
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
        self._props["ip_restrictions"] = [
            IPRestriction(client, x) for x in props["ip_restrictions"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<IPRestrictionList {}>".format(self.id)

    def __iter__(self):
        return PagedIterator(self._client, self, "ip_restrictions")

    @property
    def ip_restrictions(self) -> Sequence[IPRestriction]:
        """the list of all IP restrictions on this account"""
        return self._props["ip_restrictions"]

    @property
    def uri(self) -> str:
        """URI of the IP resrtrictions list API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class IPWhitelistEntry(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<IPWhitelistEntry {}>".format(self.id)

    def delete(
        self,
    ):
        self._client.ip_whitelist.delete(
            id=self.id,
        )

    def update(
        self,
        description: str = None,
        metadata: str = None,
    ):
        self._client.ip_whitelist.update(
            id=self.id,
            description=description,
            metadata=metadata,
        )

    @property
    def id(self) -> str:
        """unique identifier for this IP whitelist entry"""
        return self._props["id"]

    @property
    def uri(self) -> str:
        """URI of the IP whitelist entry API resource"""
        return self._props["uri"]

    @property
    def created_at(self) -> str:
        """timestamp when the IP whitelist entry was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def description(self) -> str:
        """human-readable description of the source IPs for this IP whitelist entry. optional, max 255 bytes."""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this IP whitelist entry. optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def ip_net(self) -> str:
        """an IP address or IP network range in CIDR notation (e.g. 10.1.1.1 or 10.1.0.0/16) of addresses that will be whitelisted to communicate with your tunnel endpoints"""
        return self._props["ip_net"]


class IPWhitelistEntryList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["whitelist"] = [
            IPWhitelistEntry(client, x) for x in props["whitelist"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<IPWhitelistEntryList {}>".format(self.id)

    def __iter__(self):
        return PagedIterator(self._client, self, "whitelist")

    @property
    def whitelist(self) -> Sequence[IPWhitelistEntry]:
        """the list of all IP whitelist entries on this account"""
        return self._props["whitelist"]

    @property
    def uri(self) -> str:
        """URI of the IP whitelist API resource"""
        return self._props["uri"]

    @property
    def next_page_uri(self) -> str:
        """URI of the next page, or null if there is no next page"""
        return self._props["next_page_uri"]


class EndpointConfiguration(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["circuit_breaker"] = EndpointCircuitBreaker(
            client, props["circuit_breaker"]
        )
        self._props["compression"] = EndpointCompression(client, props["compression"])
        self._props["request_headers"] = EndpointRequestHeaders(
            client, props["request_headers"]
        )
        self._props["response_headers"] = EndpointResponseHeaders(
            client, props["response_headers"]
        )
        self._props["ip_policy"] = EndpointIPPolicy(client, props["ip_policy"])
        self._props["mutual_tls"] = EndpointMutualTLS(client, props["mutual_tls"])
        self._props["tls_termination"] = EndpointTLSTermination(
            client, props["tls_termination"]
        )
        self._props["webhook_validation"] = EndpointWebhookValidation(
            client, props["webhook_validation"]
        )
        self._props["oauth"] = EndpointOAuth(client, props["oauth"])
        self._props["logging"] = EndpointLogging(client, props["logging"])
        self._props["saml"] = EndpointSAML(client, props["saml"])
        self._props["oidc"] = EndpointOIDC(client, props["oidc"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointConfiguration {}>".format(self.id)

    def delete(
        self,
    ):
        self._client.endpoint_configurations.delete(
            id=self.id,
        )

    def update(
        self,
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
    ):
        self._client.endpoint_configurations.update(
            id=self.id,
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
        )

    @property
    def id(self) -> str:
        """unique identifier of this endpoint configuration"""
        return self._props["id"]

    @property
    def type(self) -> str:
        """they type of traffic this endpoint configuration can be applied to. one of: ``http``, ``https``, ``tcp``"""
        return self._props["type"]

    @property
    def description(self) -> str:
        """human-readable description of what this endpoint configuration will be do when applied or what traffic it will be applied to. Optional, max 255 bytes"""
        return self._props["description"]

    @property
    def metadata(self) -> str:
        """arbitrary user-defined machine-readable data of this endpoint configuration. Optional, max 4096 bytes."""
        return self._props["metadata"]

    @property
    def created_at(self) -> str:
        """timestamp when the endpoint configuration was created, RFC 3339 format"""
        return self._props["created_at"]

    @property
    def uri(self) -> str:
        """URI of the endpoint configuration API resource"""
        return self._props["uri"]

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
    def ip_policy(self) -> EndpointIPPolicy:
        """ip policy module configuration or ``null``"""
        return self._props["ip_policy"]

    @property
    def mutual_tls(self) -> EndpointMutualTLS:
        """mutual TLS module configuration or ``null``"""
        return self._props["mutual_tls"]

    @property
    def tls_termination(self) -> EndpointTLSTermination:
        """TLS termination module configuration or ``null``"""
        return self._props["tls_termination"]

    @property
    def webhook_validation(self) -> EndpointWebhookValidation:
        """webhook validation module configuration or ``null``"""
        return self._props["webhook_validation"]

    @property
    def oauth(self) -> EndpointOAuth:
        """oauth module configuration or ``null``"""
        return self._props["oauth"]

    @property
    def logging(self) -> EndpointLogging:
        """logging module configuration or ``null``"""
        return self._props["logging"]

    @property
    def saml(self) -> EndpointSAML:
        """saml module configuration or ``null``"""
        return self._props["saml"]

    @property
    def oidc(self) -> EndpointOIDC:
        """oidc module configuration or ``null``"""
        return self._props["oidc"]


class EndpointConfigurationList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["endpoint_configurations"] = [
            EndpointConfiguration(client, x) for x in props["endpoint_configurations"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointConfigurationList {}>".format(self.id)

    def __iter__(self):
        return PagedIterator(self._client, self, "endpoint_configurations")

    @property
    def endpoint_configurations(self) -> Sequence[EndpointConfiguration]:
        """the list of all endpoint configurations on this account"""
        return self._props["endpoint_configurations"]

    @property
    def uri(self) -> str:
        """URI of the endpoint configurations list API resource"""
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

    def __repr__(self):
        return "<EndpointWebhookValidation {}>".format(self.id)

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def provider(self) -> str:
        """a string indicating which webhook provider will be sending webhooks to this endpoint. Value must be one of the supported providers: ``SLACK``, ``SNS``, ``STRIPE``, ``GITHUB``, ``TWILIO``, ``SHOPIFY``, ``GITLAB``, ``INTERCOM``."""
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

    def __repr__(self):
        return "<EndpointCompression {}>".format(self.id)

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]


class EndpointMutualTLS(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["certificate_authorities"] = [
            Ref(client, x) for x in props["certificate_authorities"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointMutualTLS {}>".format(self.id)

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

    def __repr__(self):
        return "<EndpointMutualTLSMutate {}>".format(self.id)

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def certificate_authority_ids(self) -> Sequence[str]:
        """list of certificate authorities that will be used to validate the TLS client certificate presnted by the initiatiator of the TLS connection"""
        return self._props["certificate_authority_ids"]


class EndpointTLSTermination(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointTLSTermination {}>".format(self.id)

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


class EndpointLogging(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["event_streams"] = [Ref(client, x) for x in props["event_streams"]]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointLogging {}>".format(self.id)

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def event_streams(self) -> Sequence[Ref]:
        """list of all EventStreams that will be used to configure and export this endpoint's logs"""
        return self._props["event_streams"]


class EndpointLoggingMutate(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointLoggingMutate {}>".format(self.id)

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def event_stream_ids(self) -> Sequence[str]:
        """list of all EventStreams that will be used to configure and export this endpoint's logs"""
        return self._props["event_stream_ids"]


class EndpointRequestHeaders(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointRequestHeaders {}>".format(self.id)

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

    def __repr__(self):
        return "<EndpointResponseHeaders {}>".format(self.id)

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
        self._props["ip_policies"] = [Ref(client, x) for x in props["ip_policies"]]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointIPPolicy {}>".format(self.id)

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def ip_policies(self) -> Sequence[Ref]:
        return self._props["ip_policies"]


class EndpointIPPolicyMutate(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointIPPolicyMutate {}>".format(self.id)

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

    def __repr__(self):
        return "<EndpointCircuitBreaker {}>".format(self.id)

    @property
    def enabled(self) -> bool:
        """``true`` if the module will be applied to traffic, ``false`` to disable. default ``true`` if unspecified"""
        return self._props["enabled"]

    @property
    def tripped_duration(self) -> int:
        """Integer number of seconds after which the circuit is tripped to wait before re-evaluating upstream health"""
        return self._props["tripped_duration"]

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
        self._props["provider"] = EndpointOAuthProvider(client, props["provider"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointOAuth {}>".format(self.id)

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
    def maximum_duration(self) -> int:
        """Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate."""
        return self._props["maximum_duration"]

    @property
    def auth_check_interval(self) -> int:
        """Integer number of seconds after which ngrok guarantees it will refresh user state from the identity provider and recheck whether the user is still authorized to access the endpoint. This is the preferred tunable to use to enforce a minimum amount of time after which a revoked user will no longer be able to access the resource."""
        return self._props["auth_check_interval"]


class EndpointOAuthProvider(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["github"] = EndpointOAuthGitHub(client, props["github"])
        self._props["facebook"] = EndpointOAuthFacebook(client, props["facebook"])
        self._props["microsoft"] = EndpointOAuthMicrosoft(client, props["microsoft"])
        self._props["google"] = EndpointOAuthGoogle(client, props["google"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointOAuthProvider {}>".format(self.id)

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


class EndpointOAuthGitHub(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointOAuthGitHub {}>".format(self.id)

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

    def __repr__(self):
        return "<EndpointOAuthFacebook {}>".format(self.id)

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

    def __repr__(self):
        return "<EndpointOAuthMicrosoft {}>".format(self.id)

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

    def __repr__(self):
        return "<EndpointOAuthGoogle {}>".format(self.id)

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


class EndpointSAML(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointSAML {}>".format(self.id)

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
    def maximum_duration(self) -> int:
        """Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate."""
        return self._props["maximum_duration"]

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


class EndpointSAMLMutate(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointSAMLMutate {}>".format(self.id)

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
    def maximum_duration(self) -> int:
        """Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate."""
        return self._props["maximum_duration"]

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


class EndpointOIDC(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<EndpointOIDC {}>".format(self.id)

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
    def maximum_duration(self) -> int:
        """Integer number of seconds of the maximum duration of an authenticated session. After this period is exceeded, a user must reauthenticate."""
        return self._props["maximum_duration"]

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


class ReservedAddr(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["endpoint_configuration"] = Ref(
            client, props["endpoint_configuration"]
        )

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<ReservedAddr {}>".format(self.id)

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
    def created_at(self) -> str:
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

    @property
    def endpoint_configuration(self) -> Ref:
        """object reference to the endpoint configuration that will be applied to traffic to this address"""
        return self._props["endpoint_configuration"]


class ReservedAddrList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["reserved_addrs"] = [
            ReservedAddr(client, x) for x in props["reserved_addrs"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<ReservedAddrList {}>".format(self.id)

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
        self._props["http_endpoint_configuration"] = Ref(
            client, props["http_endpoint_configuration"]
        )
        self._props["https_endpoint_configuration"] = Ref(
            client, props["https_endpoint_configuration"]
        )
        self._props["certificate"] = Ref(client, props["certificate"])
        self._props["certificate_management_policy"] = ReservedDomainCertPolicy(
            client, props["certificate_management_policy"]
        )
        self._props["certificate_management_status"] = ReservedDomainCertStatus(
            client, props["certificate_management_status"]
        )

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<ReservedDomain {}>".format(self.id)

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
    def created_at(self) -> str:
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
        """reserve the domain in this geographic ngrok datacenter. Optional, default is us. (au, eu, ap, us, jp, in, sa)"""
        return self._props["region"]

    @property
    def cname_target(self) -> str:
        """DNS CNAME target for a custom hostname, or null if the reserved domain is a subdomain of *.ngrok.io"""
        return self._props["cname_target"]

    @property
    def http_endpoint_configuration(self) -> Ref:
        """object referencing the endpoint configuration applied to http traffic on this domain"""
        return self._props["http_endpoint_configuration"]

    @property
    def https_endpoint_configuration(self) -> Ref:
        """object referencing the endpoint configuration applied to https traffic on this domain"""
        return self._props["https_endpoint_configuration"]

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


class ReservedDomainList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["reserved_domains"] = [
            ReservedDomain(client, x) for x in props["reserved_domains"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<ReservedDomainList {}>".format(self.id)

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

    def __repr__(self):
        return "<ReservedDomainCertPolicy {}>".format(self.id)

    @property
    def authority(self) -> str:
        """certificate authority to request certificates from. The only supported value is letsencrypt."""
        return self._props["authority"]

    @property
    def private_key_type(self) -> str:
        """type of private key to use when requesting certificates. Defaults to rsa, can be either rsa or ecdsa."""
        return self._props["private_key_type"]


class ReservedDomainCertStatus(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["provisioning_job"] = ReservedDomainCertJob(
            client, props["provisioning_job"]
        )

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<ReservedDomainCertStatus {}>".format(self.id)

    @property
    def renews_at(self) -> str:
        """timestamp when the next renewal will be requested, RFC 3339 format"""
        return self._props["renews_at"]

    @property
    def provisioning_job(self) -> ReservedDomainCertJob:
        """status of the certificate provisioning job, or null if the certificiate isn't being provisioned or renewed"""
        return self._props["provisioning_job"]


class ReservedDomainCertNSTarget(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<ReservedDomainCertNSTarget {}>".format(self.id)

    @property
    def zone(self) -> str:
        """the zone that the nameservers need to be applied to"""
        return self._props["zone"]

    @property
    def nameservers(self) -> Sequence[str]:
        """the nameservers the user must add"""
        return self._props["nameservers"]


class ReservedDomainCertJob(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ns_targets"] = [
            ReservedDomainCertNSTarget(client, x) for x in props["ns_targets"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<ReservedDomainCertJob {}>".format(self.id)

    @property
    def error_code(self) -> str:
        """if present, an error code indicating why provisioning is failing. It may be either a temporary condition (INTERNAL_ERROR), or a permanent one the user must correct (DNS_ERROR)."""
        return self._props["error_code"]

    @property
    def msg(self) -> str:
        """a message describing the current status or error"""
        return self._props["msg"]

    @property
    def started_at(self) -> str:
        """timestamp when the provisioning job started, RFC 3339 format"""
        return self._props["started_at"]

    @property
    def retries_at(self) -> str:
        """timestamp when the provisioning job will be retried"""
        return self._props["retries_at"]

    @property
    def ns_targets(self) -> Sequence[ReservedDomainCertNSTarget]:
        """if present, indicates the dns nameservers that the user must configure to complete the provisioning process of a wildcard certificate"""
        return self._props["ns_targets"]


class SSHCertificateAuthority(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<SSHCertificateAuthority {}>".format(self.id)

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
    def created_at(self) -> str:
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
        self._props["ssh_certificate_authorities"] = [
            SSHCertificateAuthority(client, x)
            for x in props["ssh_certificate_authorities"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<SSHCertificateAuthorityList {}>".format(self.id)

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

    def __repr__(self):
        return "<SSHCredential {}>".format(self.id)

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
    def created_at(self) -> str:
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
        """optional list of ACL rules. If unspecified, the credential will have no restrictions. The only allowed ACL rule at this time is the ``bind`` rule. The ``bind`` rule allows the caller to restrict what domains and addresses the token is allowed to bind. For example, to allow the token to open a tunnel on example.ngrok.io your ACL would include the rule ``bind:example.ngrok.io``. Bind rules may specify a leading wildcard to match multiple domains with a common suffix. For example, you may specify a rule of ``bind:*.example.com`` which will allow ``x.example.com``, ``y.example.com``, ``*.example.com``, etc. A rule of ``'*'`` is equivalent to no acl at all and will explicitly permit all actions."""
        return self._props["acl"]


class SSHCredentialList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["ssh_credentials"] = [
            SSHCredential(client, x) for x in props["ssh_credentials"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<SSHCredentialList {}>".format(self.id)

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

    def __repr__(self):
        return "<SSHHostCertificate {}>".format(self.id)

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
    def created_at(self) -> str:
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
    def valid_after(self) -> str:
        """the time when the ssh host certificate becomes valid, in RFC 3339 format."""
        return self._props["valid_after"]

    @property
    def valid_until(self) -> str:
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
        self._props["ssh_host_certificates"] = [
            SSHHostCertificate(client, x) for x in props["ssh_host_certificates"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<SSHHostCertificateList {}>".format(self.id)

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

    def __repr__(self):
        return "<SSHUserCertificate {}>".format(self.id)

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
    def created_at(self) -> str:
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
        """the list of principals included in the ssh user certificate. This is the list of usernames that the certificate holder may sign in as on a machine authorizinig the signing certificate authority. Dangerously, if no principals are specified, this certificate may be used to log in as any user."""
        return self._props["principals"]

    @property
    def critical_options(self) -> Mapping[str, str]:
        """A map of critical options included in the certificate. Only two critical options are currently defined by OpenSSH: ``force-command`` and ``source-address``. See `the OpenSSH certificate protocol spec` <https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys>`_ for additional details."""
        return self._props["critical_options"]

    @property
    def extensions(self) -> Mapping[str, str]:
        """A map of extensions included in the certificate. Extensions are additional metadata that can be interpreted by the SSH server for any purpose. These can be used to permit or deny the ability to open a terminal, do port forwarding, x11 forwarding, and more. If unspecified, the certificate will include limited permissions with the following extension map: ``{"permit-pty": "", "permit-user-rc": ""}`` OpenSSH understands a number of predefined extensions. See `the OpenSSH certificate protocol spec` <https://github.com/openssh/openssh-portable/blob/master/PROTOCOL.certkeys>`_ for additional details."""
        return self._props["extensions"]

    @property
    def valid_after(self) -> str:
        """the time when the ssh host certificate becomes valid, in RFC 3339 format."""
        return self._props["valid_after"]

    @property
    def valid_until(self) -> str:
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
        self._props["ssh_user_certificates"] = [
            SSHUserCertificate(client, x) for x in props["ssh_user_certificates"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<SSHUserCertificateList {}>".format(self.id)

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
        self._props["subject_alternative_names"] = TLSCertificateSANs(
            client, props["subject_alternative_names"]
        )

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<TLSCertificate {}>".format(self.id)

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
    def created_at(self) -> str:
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
        """chain of PEM-encoded certificates, leaf first. See `Certificate Bundles` <https://ngrok.com/docs/api#tls-certificates-pem>`_."""
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
    def issued_at(self) -> str:
        """timestamp (in RFC 3339 format) when this TLS certificate was issued automatically, or null if this certificate was user-uploaded"""
        return self._props["issued_at"]

    @property
    def not_before(self) -> str:
        """timestamp when this TLS certificate becomes valid, RFC 3339 format"""
        return self._props["not_before"]

    @property
    def not_after(self) -> str:
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
        self._props["tls_certificates"] = [
            TLSCertificate(client, x) for x in props["tls_certificates"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<TLSCertificateList {}>".format(self.id)

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

    def __repr__(self):
        return "<TLSCertificateSANs {}>".format(self.id)

    @property
    def dns_names(self) -> Sequence[str]:
        """set of additional domains (including wildcards) this TLS certificate is valid for"""
        return self._props["dns_names"]

    @property
    def ips(self) -> Sequence[str]:
        """set of IP addresses this TLS certificate is also valid for"""
        return self._props["ips"]


class TunnelSession(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["credential"] = Ref(client, props["credential"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<TunnelSession {}>".format(self.id)

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
    def started_at(self) -> str:
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
        self._props["tunnel_sessions"] = [
            TunnelSession(client, x) for x in props["tunnel_sessions"]
        ]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<TunnelSessionList {}>".format(self.id)

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


class Tunnel(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["tunnel_session"] = Ref(client, props["tunnel_session"])

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<Tunnel {}>".format(self.id)

    @property
    def id(self) -> str:
        """unique tunnel resource identifier"""
        return self._props["id"]

    @property
    def public_url(self) -> str:
        """URL of the tunnel's public endpoint"""
        return self._props["public_url"]

    @property
    def started_at(self) -> str:
        """timestamp when the tunnel was initiated in RFC 3339 format"""
        return self._props["started_at"]

    @property
    def metadata(self) -> str:
        """user-supplied metadata for the tunnel defined in the ngrok configuration file. See the tunnel `metadata configuration option` <https://ngrok.com/docs#tunnel-definitions-metadata>`_ In API version 0, this value was instead pulled from the top-level `metadata configuration option` <https://ngrok.com/docs#config_metadata>`_."""
        return self._props["metadata"]

    @property
    def proto(self) -> str:
        """tunnel protocol. one of ``http``, ``https``, ``tcp`` or ``tls``"""
        return self._props["proto"]

    @property
    def region(self) -> str:
        """identifier of tune region where the tunnel is running"""
        return self._props["region"]

    @property
    def tunnel_session(self) -> Ref:
        """reference object pointing to the tunnel session on which this tunnel was started"""
        return self._props["tunnel_session"]


class TunnelList(object):
    def __init__(self, client, props):
        self._client = client
        self._props = props
        self._props["tunnels"] = [Tunnel(client, x) for x in props["tunnels"]]

    def __eq__(self, other):
        return self._props == other._props

    def __repr__(self):
        return "<TunnelList {}>".format(self.id)

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
