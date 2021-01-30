# Rabbitmq

This object describes a RabbitMQ container. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **str** | Set a user name | [optional] [default to 'guest']
**password** | **str** | Set a password for a created user | [optional] [default to 'guest']
**version** | **str** | RabbitMQ version. | [optional] [default to '3.8.5-alpine']
**messages** | [**list[RabbitmqMessage]**](RabbitmqMessage.md) | A list of messages to send to RabbitMQ | [optional] 
**messages_files** | **list[str]** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


