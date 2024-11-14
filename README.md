![Tetragon CRWD Logscale](assets/tetragon-crwd-logscale.png)

A DaemonSet to tail and push Tetragon Events to Crowdstrike LogScale Community SIEM ingestion endpoint. The solution is dead simple, powered by a standard Kubernetes Daemonset that schedules on the same nodes as Tetragon, and tails the `tetragon.log` that is available via hostPath, and sends each event with a simple python implemention to Crowdstrike, employing a parser bound to the api key. 

## Overview 
You have a Kubernetes Cluster protected with Tetragon, and you want to send those events to a CrowdStrike Logscale Community SIEM for observability of those events.

<image>

## Quick Install

Create a Secret housing the apikey for your Crowdstrike ingestion endpoint.

```
kubectl create secret generic cs-logscale-apikey -n kube-system     --from-literal=apikey="....-30c2-48a5-b986-....."
```

Install the Daemonset

```
kubectl apply -f https://raw.githubusercontent.com/sween/tetragon-crwd-logscale/refs/heads/main/chart/tetragon-crwd-logscale/templates/tetragon-crwd-logscale-daemonset.yaml
```


## Quick Start
To be performed in the style of an Isovalent Lab.


### Kind Cluster
Quick Kubernetes Cluster, 3 worker nodes wide.

```
cat <<EOF | kind create cluster -n tetralogscale --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
  - role: control-plane
  - role: worker
  - role: worker
  - role: worker
networking:
  disableDefaultCNI: true
EOF
```

### Cilium
If for nothing else, Cilium[link] is a CNI of bad assery.

```
cilium install version 1.16.2
```

### Tetragon
Defaults should get it done with Tetragon[link], the star of our show.

```
EXTRA_HELM_FLAGS=(--set tetragon.hostProcPath=/proc) # flags for helm install
helm repo add cilium https://helm.cilium.io
helm repo update
helm install tetragon ${EXTRA_HELM_FLAGS[@]} cilium/tetragon -n kube-system
kubectl rollout status -n kube-system ds/tetragon -w
```

### Tracing Policies
Load up the System with some tracingpolicies.

```

```

### Crowdstrike LogScale Community


###
Apply Workload

```
kubectl apply -f https://raw.githubusercontent.com/sween/basenube/refs/heads/main/scenarios/ciliumfhir/deploy/cilium-intersystems-fhir-starwars.yaml
```

### Container

To Build the container...

```
docker build -t tetragon-crwd-logscale .
docker image tag tetragon-crwd-logscale sween/tetragon-crwd-logscale:latest
docker push sween/tetragon-crwd-logscale:latest # push wherever
```




