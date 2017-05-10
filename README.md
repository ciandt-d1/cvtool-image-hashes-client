# cvtool_image_hashes_client
Image Perceptual Hash services. Search for images that look similar to each other.

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: v1
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import cvtool_image_hashes_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import cvtool_image_hashes_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import cvtool_image_hashes_client
from cvtool_image_hashes_client.rest import ApiException
from pprint import pprint
# create an instance of the API class
api_instance = cvtool_image_hashes_client.DefaultApi()
tenant_id = 'tenant_id_example' # str | tenant id
project_id = 'project_id_example' # str | project id
image_hash_request = cvtool_image_hashes_client.ImageHashRequest() # ImageHashRequest | ImageHash to create

try:
    api_response = api_instance.add(tenant_id, project_id, image_hash_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->add: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://kingpick-image-hash-api.endpoints.ciandt-cognitive-sandbox.cloud.goog/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**add**](docs/DefaultApi.md#add) | **POST** /image-hashes | 
*DefaultApi* | [**search**](docs/DefaultApi.md#search) | **POST** /image-hashes/search | 


## Documentation For Models

 - [ImageHashRequest](docs/ImageHashRequest.md)
 - [ImageHashSearchRequest](docs/ImageHashSearchRequest.md)
 - [ImageMatchResponse](docs/ImageMatchResponse.md)
 - [ImageMatchSearchItem](docs/ImageMatchSearchItem.md)
 - [ImageMatchSearchResponse](docs/ImageMatchSearchResponse.md)
 - [Metadata](docs/Metadata.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author



