# Kafka

This object describes a Kafka container. 
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**messages** | [**list[KafkaMessages]**](KafkaMessages.md) | A list of messages to send to Kafka. | [optional] 
**messages_files** | **list[str]** |  | [optional] 
**topics** | **list[str]** | Topic names to create in Kafka. | [optional] 
**version** | **str** | Kafka version. | [optional] [default to '2.5.1-L0']

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


