# TLDR

Kafka is a distributed pub/sub messaging system.

It maintains a feed of messages in partitioned topics, replicated for durability.

Producers publish messages to a topic.
Topics are logs of events.
Consumers read messages from topics at their own pace. They can either read the next unread (from their perspective) message, or read the most recent.

## Setup
1. [Start a Kafka service using this guide](https://kafka.apache.org/quickstart)
2. [Start a MongoDB service using this guide](https://docs.mongodb.com/manual/tutorial/getting-started/)
3. Start the producer
4. Start the consumer
