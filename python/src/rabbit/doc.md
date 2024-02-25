# RabbitMQ:
- RabbitMQ is a message broker: it accepts and forwards messages. It is a software where queues can be defined, applications may connect to it, transfer data and consume data.

- And since we want our queue to remain durable even the pod crashes or restarts, we need to persist messages until they're delivered. which what we call **StatefulSet**.
- In s statefulset, each pod has a unique identity and a stable network identity. This is useful for stateful applications like RabbitMQ, this means theat if a pod fails, it will be replaced by a new one with the same identity and network address.
- And to do so we'll mount the physical storage on our local server to the pod, and we'll use the **PersistentVolume** and **PersistentVolumeClaim** to do so, so that when a new pos is deployed it will be able to mount the same storage.