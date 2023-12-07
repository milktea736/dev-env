## GRAFANA
- GF_SECURITY_ADMIN_USER=admin
- GF_SECURITY_ADMIN_PASSWORD=prom-operator

## ElasticSearch
NOTES:
1. Watch all cluster members come up.
  `$ kubectl get pods --namespace=default -l app=elasticsearch-master -w`
2. Retrieve elastic user's password.
  `$ kubectl get secrets --namespace=default elasticsearch-master-credentials -ojsonpath='{.data.password}' | base64 -d`
3. Test cluster health using Helm test.
  `$ helm --namespace=default test elasticsearch`

## Kibana
1. Watch all containers come up.
  `$ kubectl get pods --namespace=default -l release=kibana -w`
2. Retrieve the elastic user's password.
  `$ kubectl get secrets --namespace=default elasticsearch-master-credentials -ojsonpath='{.data.password}' | base64 -d`
3. Retrieve the kibana service account token.
  `$ kubectl get secrets --namespace=default kibana-kibana-es-token -ojsonpath='{.data.token}' | base64 -d`