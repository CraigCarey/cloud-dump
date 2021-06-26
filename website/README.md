## Building and tagging image

```bash
docker build . -t sgccarey/website
docker run -p 80:80 -d sgccarey/website
firefox localhost
```

## Deploying image to Docker hub
```bash
docker login --username sgccarey # enter access token from docker hub
docker push sgccarey/website
```
