#!/bin/bash

# create a cluster
kind create cluster --name k8s-cluster --config cluster.yml

# create a service
kubectl apply -f frontend_service.yml

# create a deployment
kubectl apply -f frontend_deployment.yml

# create a backend flask deployment and service
kubectl apply -f backend_flask_deployment_service.yml