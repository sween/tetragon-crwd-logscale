![Tetragon CRWD Logscale](assets/tetragon-crwd-logscale.png)

A Daemonset to send Tetragon Events to Crowdstrike Falcon LogScale NG-SIEM



### Build
```
docker build -t tetragon-logscale .
docker image tag tetragon-logscale sween/tetragon-logscale:latest
docker push sween/tetragon-logscale:latest
```
