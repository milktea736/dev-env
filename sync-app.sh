#!/bin/bash

pod_name=$(kubectl get pods | grep python | awk '{print $1}')
kubectl cp es-client/es_client.py $pod_name:/tmp/