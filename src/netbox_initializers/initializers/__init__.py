# ruff: noqa: F401
# All initializers must be imported here, to be registered
from .aggregates import AggregateInitializer
from .asns import ASNInitializer
from .cables import CableInitializer
from .circuit_types import CircuitTypeInitializer
from .circuits import CircuitInitializer
from .cluster_groups import ClusterGroupInitializer
from .cluster_types import ClusterTypesInitializer
from .clusters import ClusterInitializer
from .config_contexts import ConfigContextInitializer
from .config_templates import ConfigTemplateInitializer
from .contact_groups import ContactGroupInitializer
from .contact_roles import ContactRoleInitializer
from .contacts import ContactInitializer
from .custom_fields import CustomFieldInitializer
from .custom_links import CustomLinkInitializer
from .device_roles import DeviceRoleInitializer
from .device_types import DeviceTypeInitializer
from .devices import DeviceInitializer
from .groups import GroupInitializer
from .interfaces import InterfaceInitializer
from .ip_addresses import IPAddressInitializer
from .locations import LocationInitializer
from .macs import MACAddressInitializer
from .manufacturers import ManufacturerInitializer
from .object_permissions import ObjectPermissionInitializer
from .platforms import PlatformInitializer
from .power_feeds import PowerFeedInitializer
from .power_panels import PowerPanelInitializer
from .prefix_vlan_roles import RoleInitializer
from .prefixes import PrefixInitializer
from .primary_ips import PrimaryIPInitializer
from .providers import ProviderInitializer
from .rack_roles import RackRoleInitializer
from .rack_types import RackTypeInitializer
from .racks import RackInitializer
from .regions import RegionInitializer
from .rirs import RIRInitializer
from .route_targets import RouteTargetInitializer
from .service_templates import ServiceTemplateInitializer
from .services import ServiceInitializer
from .site_groups import SiteGroupInitializer
from .sites import SiteInitializer
from .tags import TagInitializer
from .tenant_groups import TenantGroupInitializer
from .tenants import TenantInitializer
from .users import UserInitializer
from .virtual_machines import VirtualMachineInitializer
from .virtualization_interfaces import VMInterfaceInitializer
from .vlan_groups import VLANGroupInitializer
from .vlans import VLANInitializer
from .vrfs import VRFInitializer
from .webhooks import WebhookInitializer
