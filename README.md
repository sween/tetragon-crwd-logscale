![Tetragon CRWD Logscale](assets/tetragon-crwd-logscale.png)

A DaemonSet to tail and push Tetragon Events to Crowdstrike Falcon LogScale SIEM ingestion endpoint.

## Quick Start
To be performed in the style of an Isovalent Lab.


### Kind Cluster
```

```

### Cilium
If for nothing else, Cilium[link] is a CNI of bad assery.
```

```

### Tetragon
Defaults should get it done with Tetragon[link], the star of our show.
```


```


### Crowdstrike LogScale Community


### Container

To Build the container...

```
docker build -t tetragon-crwd-logscale .
docker image tag tetragon-crwd-logscale sween/tetragon-crwd-logscale:latest
docker push sween/tetragon-crwd-logscale:latest # push wherever
```




