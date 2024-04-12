## BDD test examples in Docker container


### Insturctions</h3>

1. Clone the repo into any convinient directory
   
   ```sh
   git clone https://github.com/trammik/bdd_docker.git
   ```

3. Build image with Dockerfile from cloned repo
 
   ```sh
   docker build -f Dockerfile -t pytest-bdd .
   ```

5. Run docker container from the builded image

   ```sh
   docker run -ti --name test -d pytest-bdd
   ```

7. Check the container output by passing container ID to ommand docker logs

   ```sh
   docker logs <container ID>
   ```
