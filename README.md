Random stuff
# Kubernetes units 

## Deployment
Deployment is a description of desired state. It creates ReplicaSets and pods.

## ReplicaSet
It guarantees that specific number of identical pods will be available

## Pod
Smallest unit of computing that does some job

## Service
An abstract way to expose an application running on a set of Pods as a network service

## Project configuration
### proton-deployment
Creates ReplicaSet with two Pods based on backend image.

### frontend-deployment
In this case it creates just one instance as load balancing is done with AWS here.

### backend-service
It exposes backend Pods under specific hostname (backend_proton)

### fronted-service
It exposes frontend Pod and commision balancing to AWS load balancer

### psql-service
Creates alias name for AWS Aurora instance


# Usefull commands
List pods
`kubectl get pods`

Check pod logs
`kubectl logs <pod_name>`

Forward pod's XXXX port to YYYY in localhost
`kubectl port-forward <pod_name> YYYY:XXXX`
