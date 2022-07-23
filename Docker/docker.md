docker container run -it -p nginx 80:80
// pulls an image and builds a container.
// port mapping. First port is the port on your local machine that you want the docker image to be mapped to. The second port is the port the docker image uses.

docker container ls
// lists current containers.

docker container ls -a
//lists all running containers in interactive mode.

docker container rm id of the container or first 3 characters of the id.

docker images
// to check the images on your machine that have already been pulled.
