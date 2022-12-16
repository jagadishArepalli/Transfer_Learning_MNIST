# Transfer_Learning_MNIST

# Cloud Computing
## Jagadish Arepalli 


### CURL requests

##### Request for handwritten digit 3

```sh
curl -i -X POST -H 'Content-Type: application/json' -d '{"url": "https://assign4handwritenimage.s3.amazonaws.com/handwritten3.jpeg"}' https://uiprenjrvk.execute-api.us-east-1.amazonaws.com/prod/
```

##### Request for handwritten digit 6

```sh
curl -i -X POST -H 'Content-Type: application/json' -d '{"url": "https://assign4handwritenimage.s3.amazonaws.com/handwritten6.jpeg"}' https://uiprenjrvk.execute-api.us-east-1.amazonaws.com/prod/
```

##### Request for handwritten digit 1

```sh
curl -i -X POST -H 'Content-Type: application/json' -d '{"url": "https://assign4handwritenimage.s3.amazonaws.com/handwritten1.jpeg"}' https://uiprenjrvk.execute-api.us-east-1.amazonaws.com/prod/
```



