from azure.storage.common._constants import (
    SERVICE_HOST_BASE
)


class Credentials(object):
    def __init__(self, account_name, account_key,
                 access_token, cloud_endpoint_suffix):
        self.account_name = account_name
        self.account_key = account_key
        self.access_token = access_token

        # Support to select the specific Azure Cloud
        #  (i.e. AzureCloud, AzureChinaCloud, AzureGermanCloud, ...)
        # by passing the corresponding endpoint suffix.
        # Azure Cloud to endpoint suffix mappings could be found here:
        # https://docs.microsoft.com/en-gb/azure/storage/common/
        #         storage-powershell-independent-clouds#endpoint-suffix
        # Fallback is the default cloud as defined in the Azure SDK
        if cloud_endpoint_suffix:
            self.cloud_endpoint_suffix = cloud_endpoint_suffix
        else:
            self.cloud_endpoint_suffix = SERVICE_HOST_BASE
