#!/bin/bash

function create_minikube(){
    # minikube delete 
    MEMORY="24G"
    CPUS="6"
    minikube start --kubernetes-version=v1.23.0 --memory="$MEMORY" --cpus="$CPUS" --bootstrapper=kubeadm --extra-config=kubelet.authentication-token-webhook=true --extra-config=kubelet.authorization-mode=Webhook --extra-config=scheduler.bind-address=0.0.0.0 --extra-config=controller-manager.bind-address=0.0.0.0
}

function enable_addons() {
    minikube addons enable metrics-server
}


create_minikube && enable_addons
