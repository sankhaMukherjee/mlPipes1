#!/bin/bash -e
image_name=omolluska/test-kubeflow-write-data # Specify the image name here
image_tag=latest
full_image_name=${image_name}:${image_tag}

docker build -t "${full_image_name}" .

# Load this image directly into the kind registry ...
# This will have to be done within the Kubeflow workstation
# kind load docker-image ${full_image_name}

# Push it to the docker main center as well
docker push "$full_image_name"

# Output the strict image name (which contains the sha256 image digest)
docker inspect --format="{{index .RepoDigests 0}}" "${full_image_name}"
