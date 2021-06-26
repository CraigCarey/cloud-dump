# TLDR
kubernetes is a container orchestrator


## Install kubectl
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin
```

## Using kubectl
```bash
# Get kubeconfig.yaml from master
export KUBECONFIG=kubeconfig.yaml

kubectl get nodes
kubectl cluster-info

# Create a q&d pod from the cmdline
kubectl run k8stutorial --image=sgccarey/website --port=80
kubectl get pods
kubectl describe pods
kubectl delete pods k8stutorial

# Create some pods from a config file
kubectl apply -f k8stutorial-deployment.yaml
kubectl get deployments

# modify the number of pods
kubectl edit deployment k8stutorial-deployment # doesn't work well with subl

# should see new pods
kubectl get pods -o wide
```

## Using a load-balancing service
```bash
kubectl apply -f k8stutorial-service.yaml
kubectl get services

# view the load balanced, public facing service
firefox <insert external IP>

kubectl describe services k8stutorial-service
```
