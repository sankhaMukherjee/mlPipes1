#!/bin/bash


# Specify the image name here
image_name=omolluska/test-kubeflow-read-data 
image_tag=latest
full_image_name=${image_name}:${image_tag}
docker pull ${full_image_name}
kind load docker-image ${full_image_name}