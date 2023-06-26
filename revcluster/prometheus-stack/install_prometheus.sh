#!/bin/bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
cat <<EOF | helm install prometheus-stack prometheus-community/kube-prometheus-stack \
--create-namespace -n monitoring -f -

grafana:
  enabled: true
  adminPassword: "passHere"
  persistence:
    enabled: false
  ingress:
    enabled: false
EOF
