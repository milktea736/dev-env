# Create a Nginx proxy to access a Minikube cluster from a remote server

## Steps
- Copy the certificates from minikube.
    ```bash
    cp ~/.minikube/profiles/minikube/client.crt nginx/minikube/
    cp ~/.minikube/profiles/minikube/client.key nginx/minikube/
    ```

- Create a password using htpasswd for user minikube and store it.
    ```bash
    htpasswd -c nginx/minikube/.htpasswd minikube
    ```

- Create a nginx.conf
    - The first part is configured to proxy port 443 to the minikube.
    - The remaing ports are set up to proxy to exposed cluster ports.

- Create a image and run the container
    - The container must run in the same network as minikube
    ```bash
    docker build -t minikube-proxy

    docker run -d --rm --name proxy -p 443:443 -p 30000:30000 --network=minikube minikube-proxy
    ```

- Copy the `.kube` to client. 
    - Update the server: `minikube:<PASSWORD>@<REMOTE_SERVER>:443`
    - Update the path of certificates