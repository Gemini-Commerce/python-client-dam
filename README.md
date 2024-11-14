# dam_client
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.3.0
- Generator version: 7.9.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/Gemini-Commerce/python-client-dam.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/Gemini-Commerce/python-client-dam.git`)

Then import the package:
```python
import dam
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import dam
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import dam
from dam.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dam.api.gogemini.io
# See configuration.py for a list of all supported configuration parameters.
configuration = dam.Configuration(
    host = "https://dam.api.gogemini.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.


# Enter a context with an instance of the API client
with dam.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dam.BasicOperationsApi(api_client)
    body = dam.DamBatchUploadAssetsRequest() # DamBatchUploadAssetsRequest | 

    try:
        # Batch Upload Assets
        api_response = api_instance.batch_upload_assets(body)
        print("The response of BasicOperationsApi->batch_upload_assets:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling BasicOperationsApi->batch_upload_assets: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://dam.api.gogemini.io*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*BasicOperationsApi* | [**batch_upload_assets**](docs/BasicOperationsApi.md#batch_upload_assets) | **POST** /dam.Dam/BatchUploadAssets | Batch Upload Assets
*BasicOperationsApi* | [**batch_upload_assets_0**](docs/BasicOperationsApi.md#batch_upload_assets_0) | **POST** /dam/batch_upload_assets | Batch Upload Assets
*BasicOperationsApi* | [**create_asset**](docs/BasicOperationsApi.md#create_asset) | **POST** /dam.Dam/CreateAsset | Create Asset
*BasicOperationsApi* | [**create_asset_0**](docs/BasicOperationsApi.md#create_asset_0) | **POST** /dam/create_asset | Create Asset
*BasicOperationsApi* | [**get_asset_by_code**](docs/BasicOperationsApi.md#get_asset_by_code) | **POST** /dam.Dam/GetAssetByCode | Get Asset By Code
*BasicOperationsApi* | [**get_asset_by_code_0**](docs/BasicOperationsApi.md#get_asset_by_code_0) | **POST** /dam/get_asset_by_code | Get Asset By Code
*BasicOperationsApi* | [**list_assets**](docs/BasicOperationsApi.md#list_assets) | **POST** /dam.Dam/ListAssets | List Assets
*BasicOperationsApi* | [**list_assets_0**](docs/BasicOperationsApi.md#list_assets_0) | **POST** /dam/list_assets | List Assets
*BasicOperationsApi* | [**list_assets_by_codes**](docs/BasicOperationsApi.md#list_assets_by_codes) | **POST** /dam.Dam/ListAssetsByCodes | List Assets By Codes
*BasicOperationsApi* | [**list_assets_by_codes_0**](docs/BasicOperationsApi.md#list_assets_by_codes_0) | **POST** /dam/list_assets_by_codes | List Assets By Codes
*BasicOperationsApi* | [**list_assets_by_ids**](docs/BasicOperationsApi.md#list_assets_by_ids) | **POST** /dam.Dam/ListAssetsByIds | List Assets By Ids
*BasicOperationsApi* | [**list_assets_by_ids_0**](docs/BasicOperationsApi.md#list_assets_by_ids_0) | **POST** /dam/list_assets_by_ids | List Assets By Ids
*BasicOperationsApi* | [**update_asset**](docs/BasicOperationsApi.md#update_asset) | **POST** /dam.Dam/UpdateAsset | Update Asset
*BasicOperationsApi* | [**update_asset_0**](docs/BasicOperationsApi.md#update_asset_0) | **POST** /dam/update_asset | Update Asset


## Documentation For Models

 - [AssetMetadata](docs/AssetMetadata.md)
 - [AssetOriginTypes](docs/AssetOriginTypes.md)
 - [BatchUploadAssetsRequestFiles](docs/BatchUploadAssetsRequestFiles.md)
 - [DamAsset](docs/DamAsset.md)
 - [DamAssetOrigin](docs/DamAssetOrigin.md)
 - [DamAssetType](docs/DamAssetType.md)
 - [DamBatchUploadAssetsRequest](docs/DamBatchUploadAssetsRequest.md)
 - [DamBatchUploadAssetsResponse](docs/DamBatchUploadAssetsResponse.md)
 - [DamCreateAssetRequest](docs/DamCreateAssetRequest.md)
 - [DamGetAssetByCodeRequest](docs/DamGetAssetByCodeRequest.md)
 - [DamListAssetsByCodesRequest](docs/DamListAssetsByCodesRequest.md)
 - [DamListAssetsByCodesResponse](docs/DamListAssetsByCodesResponse.md)
 - [DamListAssetsByIdsRequest](docs/DamListAssetsByIdsRequest.md)
 - [DamListAssetsByIdsResponse](docs/DamListAssetsByIdsResponse.md)
 - [DamListAssetsRequest](docs/DamListAssetsRequest.md)
 - [DamListAssetsResponse](docs/DamListAssetsResponse.md)
 - [DamUpdateAssetRequest](docs/DamUpdateAssetRequest.md)
 - [ProtobufAny](docs/ProtobufAny.md)
 - [RpcStatus](docs/RpcStatus.md)
 - [UpdateAssetRequestPayload](docs/UpdateAssetRequestPayload.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author

info@gemini-commerce.com


