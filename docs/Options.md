# Options

This object includes general Gnomock configuration, similar to all presets. Timeout configuration is especially useful for troubleshooting. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | Wait timeout in nanoseconds | [optional] 
**env** | **list[str]** | Array of environment variables to set in the container | [optional] 
**debug** | **bool** | Set to true to see logs inside the Gnomock container | [optional] [default to False]
**container_name** | **str** | Use a specific container name instead of a random one. In case a container with this name already exists, it is killed and replaced by a new container.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


