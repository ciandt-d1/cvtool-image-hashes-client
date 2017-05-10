# swagger_client.DefaultApi

All URIs are relative to *https://kingpick-image-hash-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add**](DefaultApi.md#add) | **POST** /image-hashes | 
[**search**](DefaultApi.md#search) | **POST** /image-hashes/search | 


# **add**
> ImageMatchResponse add(tenant_id, project_id, image_hash_request)



Adds an image signature to the database.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
tenant_id = 'tenant_id_example' # str | tenant id
project_id = 'project_id_example' # str | project id
image_hash_request = swagger_client.ImageHashRequest() # ImageHashRequest | ImageHash to create

try: 
    api_response = api_instance.add(tenant_id, project_id, image_hash_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **project_id** | **str**| project id | 
 **image_hash_request** | [**ImageHashRequest**](ImageHashRequest.md)| ImageHash to create | 

### Return type

[**ImageMatchResponse**](ImageMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search**
> ImageMatchSearchResponse search(tenant_id, project_id, search_request)



Searches for a similar image in the database. Scores range from 0 to 100, with 100 being a perfect match.

### Example 
```python
from __future__ import print_statement
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
tenant_id = 'tenant_id_example' # str | tenant id
project_id = 'project_id_example' # str | project id
search_request = swagger_client.ImageHashSearchRequest() # ImageHashSearchRequest | Search parameters

try: 
    api_response = api_instance.search(tenant_id, project_id, search_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**| tenant id | 
 **project_id** | **str**| project id | 
 **search_request** | [**ImageHashSearchRequest**](ImageHashSearchRequest.md)| Search parameters | 

### Return type

[**ImageMatchSearchResponse**](ImageMatchSearchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

