#!/bin/bash

function install_monitors() {
    helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
    helm repo update

    helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack --version 54.1.0
}


function install_es() {
    helm repo add elastic https://helm.elastic.co
    helm repo update

    helm install elasticsearch elastic/elasticsearch --version 8.5.1 --set antiAffinity=soft --set replicas=2
    helm install kibana elastic/kibana --version 8.5.1
}
