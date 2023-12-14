# RAPIDS LAB

## Preparation ubuntu 23.10
Install `nvidia-cuda-toolkit`
```sh
sudo add-apt-repository universe
sudo add-apt-repository multiverse
sudo apt install nvidia-cuda-toolkit
```

Install `nvidia-container-toolkit`
1. Configure the production repository:
```sh
curl -fsSL https://nvidia.github.io/libnvidia-container/gpgkey | sudo gpg --dearmor -o /usr/share/keyrings/nvidia-container-toolkit-keyring.gpg \
  && curl -s -L https://nvidia.github.io/libnvidia-container/stable/deb/nvidia-container-toolkit.list | \
    sed 's#deb https://#deb [signed-by=/usr/share/keyrings/nvidia-container-toolkit-keyring.gpg] https://#g' | \
    sudo tee /etc/apt/sources.list.d/nvidia-container-toolkit.list
```
2. Update the packages list from the repository:
```sh
sudo apt-get update
```
3. Install the NVIDIA Container Toolkit packages:
```sh
sudo apt-get install -y nvidia-container-toolkit
```

Configuring Docker
1. Configure the container runtime by using the `nvidia-ctk` command:
```sh
sudo nvidia-ctk runtime configure --runtime=docker
```
2. Restart the Docker daemon:
```sh
sudo systemctl restart docker
```

Configuring containerd
1. Configure the container runtime by using the `nvidia-ctk` command:
```sh
sudo nvidia-ctk runtime configure --runtime=containerd
```
2. Restart containerd:
```sh
sudo systemctl restart containerd
```
