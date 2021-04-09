# Write data

This is a simple file to check whether a pod is able to write
data to a PVC within kubernetes. The most important thing to 
rememebr is that this pod should be run within the `kubeflow`
namespace.

The persistent volume claim has already been generated and is shown
in the definition below. This is present in the file `ai-volume-claim-kf.yaml`

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