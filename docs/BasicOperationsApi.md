# dam.BasicOperationsApi

All URIs are relative to *https://dam.api.gogemini.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**batch_upload_assets**](BasicOperationsApi.md#batch_upload_assets) | **POST** /dam.Dam/BatchUploadAssets | Batch Upload Assets
[**batch_upload_assets_0**](BasicOperationsApi.md#batch_upload_assets_0) | **POST** /dam/batch_upload_assets | Batch Upload Assets
[**create_asset**](BasicOperationsApi.md#create_asset) | **POST** /dam.Dam/CreateAsset | Create Asset
[**create_asset_0**](BasicOperationsApi.md#create_asset_0) | **POST** /dam/create_asset | Create Asset
[**get_asset_by_code**](BasicOperationsApi.md#get_asset_by_code) | **POST** /dam.Dam/GetAssetByCode | Get Asset By Code
[**get_asset_by_code_0**](BasicOperationsApi.md#get_asset_by_code_0) | **POST** /dam/get_asset_by_code | Get Asset By Code
[**list_assets**](BasicOperationsApi.md#list_assets) | **POST** /dam.Dam/ListAssets | List Assets
[**list_assets_0**](BasicOperationsApi.md#list_assets_0) | **POST** /dam/list_assets | List Assets
[**list_assets_by_codes**](BasicOperationsApi.md#list_assets_by_codes) | **POST** /dam.Dam/ListAssetsByCodes | List Assets By Codes
[**list_assets_by_codes_0**](BasicOperationsApi.md#list_assets_by_codes_0) | **POST** /dam/list_assets_by_codes | List Assets By Codes
[**list_assets_by_ids**](BasicOperationsApi.md#list_assets_by_ids) | **POST** /dam.Dam/ListAssetsByIds | List Assets By Ids
[**list_assets_by_ids_0**](BasicOperationsApi.md#list_assets_by_ids_0) | **POST** /dam/list_assets_by_ids | List Assets By Ids
[**update_asset**](BasicOperationsApi.md#update_asset) | **POST** /dam.Dam/UpdateAsset | Update Asset
[**update_asset_0**](BasicOperationsApi.md#update_asset_0) | **POST** /dam/update_asset | Update Asset


# **batch_upload_assets**
> DamBatchUploadAssetsResponse batch_upload_assets(body)

Batch Upload Assets

### Example


```python
import time
import os
import dam
from dam.models.dam_batch_upload_assets_request import DamBatchUploadAssetsRequest
from dam.models.dam_batch_upload_assets_response import DamBatchUploadAssetsResponse
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
    except Exception as e:
        print("Exception when calling BasicOperationsApi->batch_upload_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamBatchUploadAssetsRequest**](DamBatchUploadAssetsRequest.md)|  | 

### Return type

[**DamBatchUploadAssetsResponse**](DamBatchUploadAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_upload_assets_0**
> DamBatchUploadAssetsResponse batch_upload_assets_0(body)

Batch Upload Assets

### Example


```python
import time
import os
import dam
from dam.models.dam_batch_upload_assets_request import DamBatchUploadAssetsRequest
from dam.models.dam_batch_upload_assets_response import DamBatchUploadAssetsResponse
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
        api_response = api_instance.batch_upload_assets_0(body)
        print("The response of BasicOperationsApi->batch_upload_assets_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->batch_upload_assets_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamBatchUploadAssetsRequest**](DamBatchUploadAssetsRequest.md)|  | 

### Return type

[**DamBatchUploadAssetsResponse**](DamBatchUploadAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset**
> DamAsset create_asset(body)

Create Asset

### Example


```python
import time
import os
import dam
from dam.models.dam_asset import DamAsset
from dam.models.dam_create_asset_request import DamCreateAssetRequest
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
    body = dam.DamCreateAssetRequest() # DamCreateAssetRequest | 

    try:
        # Create Asset
        api_response = api_instance.create_asset(body)
        print("The response of BasicOperationsApi->create_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->create_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamCreateAssetRequest**](DamCreateAssetRequest.md)|  | 

### Return type

[**DamAsset**](DamAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_asset_0**
> DamAsset create_asset_0(body)

Create Asset

### Example


```python
import time
import os
import dam
from dam.models.dam_asset import DamAsset
from dam.models.dam_create_asset_request import DamCreateAssetRequest
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
    body = dam.DamCreateAssetRequest() # DamCreateAssetRequest | 

    try:
        # Create Asset
        api_response = api_instance.create_asset_0(body)
        print("The response of BasicOperationsApi->create_asset_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->create_asset_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamCreateAssetRequest**](DamCreateAssetRequest.md)|  | 

### Return type

[**DamAsset**](DamAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_code**
> DamAsset get_asset_by_code(body)

Get Asset By Code

### Example


```python
import time
import os
import dam
from dam.models.dam_asset import DamAsset
from dam.models.dam_get_asset_by_code_request import DamGetAssetByCodeRequest
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
    body = dam.DamGetAssetByCodeRequest() # DamGetAssetByCodeRequest | 

    try:
        # Get Asset By Code
        api_response = api_instance.get_asset_by_code(body)
        print("The response of BasicOperationsApi->get_asset_by_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->get_asset_by_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamGetAssetByCodeRequest**](DamGetAssetByCodeRequest.md)|  | 

### Return type

[**DamAsset**](DamAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_code_0**
> DamAsset get_asset_by_code_0(body)

Get Asset By Code

### Example


```python
import time
import os
import dam
from dam.models.dam_asset import DamAsset
from dam.models.dam_get_asset_by_code_request import DamGetAssetByCodeRequest
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
    body = dam.DamGetAssetByCodeRequest() # DamGetAssetByCodeRequest | 

    try:
        # Get Asset By Code
        api_response = api_instance.get_asset_by_code_0(body)
        print("The response of BasicOperationsApi->get_asset_by_code_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->get_asset_by_code_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamGetAssetByCodeRequest**](DamGetAssetByCodeRequest.md)|  | 

### Return type

[**DamAsset**](DamAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets**
> DamListAssetsResponse list_assets(body)

List Assets

### Example


```python
import time
import os
import dam
from dam.models.dam_list_assets_request import DamListAssetsRequest
from dam.models.dam_list_assets_response import DamListAssetsResponse
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
    body = dam.DamListAssetsRequest() # DamListAssetsRequest | 

    try:
        # List Assets
        api_response = api_instance.list_assets(body)
        print("The response of BasicOperationsApi->list_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->list_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamListAssetsRequest**](DamListAssetsRequest.md)|  | 

### Return type

[**DamListAssetsResponse**](DamListAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets_0**
> DamListAssetsResponse list_assets_0(body)

List Assets

### Example


```python
import time
import os
import dam
from dam.models.dam_list_assets_request import DamListAssetsRequest
from dam.models.dam_list_assets_response import DamListAssetsResponse
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
    body = dam.DamListAssetsRequest() # DamListAssetsRequest | 

    try:
        # List Assets
        api_response = api_instance.list_assets_0(body)
        print("The response of BasicOperationsApi->list_assets_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->list_assets_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamListAssetsRequest**](DamListAssetsRequest.md)|  | 

### Return type

[**DamListAssetsResponse**](DamListAssetsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets_by_codes**
> DamListAssetsByCodesResponse list_assets_by_codes(body)

List Assets By Codes

### Example


```python
import time
import os
import dam
from dam.models.dam_list_assets_by_codes_request import DamListAssetsByCodesRequest
from dam.models.dam_list_assets_by_codes_response import DamListAssetsByCodesResponse
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
    body = dam.DamListAssetsByCodesRequest() # DamListAssetsByCodesRequest | 

    try:
        # List Assets By Codes
        api_response = api_instance.list_assets_by_codes(body)
        print("The response of BasicOperationsApi->list_assets_by_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->list_assets_by_codes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamListAssetsByCodesRequest**](DamListAssetsByCodesRequest.md)|  | 

### Return type

[**DamListAssetsByCodesResponse**](DamListAssetsByCodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets_by_codes_0**
> DamListAssetsByCodesResponse list_assets_by_codes_0(body)

List Assets By Codes

### Example


```python
import time
import os
import dam
from dam.models.dam_list_assets_by_codes_request import DamListAssetsByCodesRequest
from dam.models.dam_list_assets_by_codes_response import DamListAssetsByCodesResponse
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
    body = dam.DamListAssetsByCodesRequest() # DamListAssetsByCodesRequest | 

    try:
        # List Assets By Codes
        api_response = api_instance.list_assets_by_codes_0(body)
        print("The response of BasicOperationsApi->list_assets_by_codes_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->list_assets_by_codes_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamListAssetsByCodesRequest**](DamListAssetsByCodesRequest.md)|  | 

### Return type

[**DamListAssetsByCodesResponse**](DamListAssetsByCodesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets_by_ids**
> DamListAssetsByIdsResponse list_assets_by_ids(body)

List Assets By Ids

### Example


```python
import time
import os
import dam
from dam.models.dam_list_assets_by_ids_request import DamListAssetsByIdsRequest
from dam.models.dam_list_assets_by_ids_response import DamListAssetsByIdsResponse
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
    body = dam.DamListAssetsByIdsRequest() # DamListAssetsByIdsRequest | 

    try:
        # List Assets By Ids
        api_response = api_instance.list_assets_by_ids(body)
        print("The response of BasicOperationsApi->list_assets_by_ids:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->list_assets_by_ids: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamListAssetsByIdsRequest**](DamListAssetsByIdsRequest.md)|  | 

### Return type

[**DamListAssetsByIdsResponse**](DamListAssetsByIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assets_by_ids_0**
> DamListAssetsByIdsResponse list_assets_by_ids_0(body)

List Assets By Ids

### Example


```python
import time
import os
import dam
from dam.models.dam_list_assets_by_ids_request import DamListAssetsByIdsRequest
from dam.models.dam_list_assets_by_ids_response import DamListAssetsByIdsResponse
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
    body = dam.DamListAssetsByIdsRequest() # DamListAssetsByIdsRequest | 

    try:
        # List Assets By Ids
        api_response = api_instance.list_assets_by_ids_0(body)
        print("The response of BasicOperationsApi->list_assets_by_ids_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->list_assets_by_ids_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamListAssetsByIdsRequest**](DamListAssetsByIdsRequest.md)|  | 

### Return type

[**DamListAssetsByIdsResponse**](DamListAssetsByIdsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset**
> DamAsset update_asset(body)

Update Asset

### Example


```python
import time
import os
import dam
from dam.models.dam_asset import DamAsset
from dam.models.dam_update_asset_request import DamUpdateAssetRequest
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
    body = dam.DamUpdateAssetRequest() # DamUpdateAssetRequest | 

    try:
        # Update Asset
        api_response = api_instance.update_asset(body)
        print("The response of BasicOperationsApi->update_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->update_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamUpdateAssetRequest**](DamUpdateAssetRequest.md)|  | 

### Return type

[**DamAsset**](DamAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_0**
> DamAsset update_asset_0(body)

Update Asset

### Example


```python
import time
import os
import dam
from dam.models.dam_asset import DamAsset
from dam.models.dam_update_asset_request import DamUpdateAssetRequest
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
    body = dam.DamUpdateAssetRequest() # DamUpdateAssetRequest | 

    try:
        # Update Asset
        api_response = api_instance.update_asset_0(body)
        print("The response of BasicOperationsApi->update_asset_0:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BasicOperationsApi->update_asset_0: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamUpdateAssetRequest**](DamUpdateAssetRequest.md)|  | 

### Return type

[**DamAsset**](DamAsset.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | When an endpoint receives a request with an invalid or unauthorized JWT token, a 401 error (Unauthorized) is thrown. This error indicates that the client is not authenticated or lacks the necessary permissions to access the requested resource. The server responds with the 401 error to enforce security measures and restrict unauthorized access. Clients should handle this error by taking appropriate actions, such as re-authenticating or obtaining a valid token, to gain authorized access. |  -  |
**500** | An internal error occurred is thrown when an incompatible payload is sent |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

