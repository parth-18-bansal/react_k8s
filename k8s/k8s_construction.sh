#!/bin/bash

# create a cluster
kind create cluster --name k8s-cluster --config ./k8s/cluster.yml

# create a service
kubectl apply -f ./k8s/frontend_service.yml

# create a deployment
kubectl apply -f ./k8s/frontend_deployment.yml