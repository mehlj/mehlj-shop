# mehlj-shop
Simple eCommerce site for learning web development concepts

## Instructions

### Build
```
$ docker build -t mehlj-shop .
```

### Run
```
$ docker run -d -p 5000:5000 mehlj-shop
```
Or, alternatively, run with host-container volume sharing:
```
$ docker run -d -p 5000:5000 -v /home/mehlj/projects/mehlj-shop:/usr/src/app mehlj-shop
```


