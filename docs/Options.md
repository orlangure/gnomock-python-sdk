# Options

This object includes general Gnomock configuration, similar to all presets. Timeout configuration is especially useful for troubleshooting. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | Wait timeout in nanoseconds | [optional] 
**env** | **list[str]** | Array of environment variables to set in the container | [optional] 
**debug** | **bool** | Set to true to see logs inside the Gnomock container | [optional] [default to False]
**container_name** | **str** | Use a specific container name instead of a random one. In case a container with this name already exists, it is killed and replaced by a new container.  | [optional] 
**privileged** | **bool** | Runs a container in privileged mode. | [optional] 
**cmd** | **list[str]** | Command and its arguments to execute on container startup. | [optional] 
**disable_cleanup** | **bool** | Disables auto removal of this container after tests. | [optional] 
**use_local_images_first** | **bool** | If possible to avoid hitting the Docker Hub pull rate limit. | [optional] 
**auth** | **str** | base64 encoded JSON string with docker access credentials. JSON string should include two fields, username and password. For Docker Hub, if 2FA authentication is enabled, an access token should be used instead of a password.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


