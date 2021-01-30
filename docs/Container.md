# Container

This object is a Gnomock wrapper of a regular docker container. It uses the same container ID as docker, and adds bound ports information. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Container ID | [optional] 
**host** | **str** | Host of bound ports | [optional] [default to 'localhost']
**ports** | **dict(str, object)** | A map of port bindings of a Gnomock container. Human readable names are used to make the values readable. &#x60;port&#x60; value is an actual port exposed on the host; use this port to connect to the container.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


