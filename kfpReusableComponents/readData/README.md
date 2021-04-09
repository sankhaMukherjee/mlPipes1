# Write data

This is a simple file to check whether a pod is able to write
data to a PVC within kubernetes. The most important thing to 
rememebr is that this pod should be run within the `kubeflow`
namespace.

Note that we have configured secrets for downloading images:

```
NAME                  TYPE                                  DATA   AGE
default-token-cp28l   kubernetes.io/service-account-token   3      7d19h
dockersecret          kubernetes.io/dockerconfigjson        1      36m
regcred               kubernetes.io/dockerconfigjson        1      89s
```

We shall use the last one `regcred` for downloading the 

The persistent volume claim has already been generated and is shown
in the definition below. This is present in the file `ai-volume-claim-kf.yaml`

omolluska/test-kubeflow-read-data:latest


```YAML
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc0001
  namespace: kubeflow
spec:
  storageClassName: standard
  volumeMode: Filesystem
  accessModes:
    - ReadWriteOnce # Only a single node can read/write
  resources:
    requests:
      storage: 4Gi
  volumeName: pv0001
```


All the examples will use the following path:

`/pipelines/component/src/data` to interact with the data within
Kubeflow, and all other containers. Hence, a configuration will
have to ge genertaed such that the data within the file system can
be written to and read from. 

This docker container will simply check the following things:
1. print the current working directory
2. pirnt all files present within the data folder
3. If there is a file named `data\test.txt`, it is going to pront that entire file

