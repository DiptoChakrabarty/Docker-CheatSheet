# :star2: Docker-CheatSheet :star2:

A CheatSheet to get you started with docker 

<p align="center">
<img src="docker.png" height=520px width=400px>
</p>

## Installation 
```sh
 
  This is for Ubuntu
 
    - Install few packages which are required beforehand

    sudo apt install apt-transport-https ca-certificates curl software-properties-common

    - Add GPG key 

    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    - Add Docker repository to apt sources

    sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"

    - Update your existing list of packages
    
    sudo apt update

    - Install Docker-ce

    sudo apt install docker-ce

    - Start Docker Process

    sudo systemctl status docker 

```

## Difference between Docker and VMs

<p align="center">
<img src="https://uploads.toptal.io/blog/image/91505/toptal-blog-image-1438607369520-110213f5682347c7ea0c68d46bb17d6d.jpg" >
</p>


## Docker commands
```sh

 * Check all docker containers
   docker ps -a

 * Check all started docker containers
   docker ps

 * Start a stopped container
   docker start <container-name>

 * Stop a container
   docker stop <container-name>

 * Remove all containers
   docker stop $(docker ps -a -q)
   docker rm $(docker ps -a -q) 

 * Attach to a container
   docker start <container-name>
   docker attach <container-name>

 * Run bash shell in container
   docker container exec -it <container-name> bash
 
 * Delete container forcefully
   docker container rm -f <container-name>


```