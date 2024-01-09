## What is AI4MediaBench?

AI4MediaBench is an open-source web-based platform that enables researchers, developers, and data scientists to collaborate, 
with the goal of advancing research fields where machine learning and advanced computation is used. AI4MediaBench helps to 
solve many common problems in the arena of data-oriented research through its online community where people can participate in
competitions and benchmarks.



## Documentation

- [AI4MediaBench-Docs](https://github.com/AIMultimediaLab/AI4MediaBench-AIMultimediaLab)


## Quick installation (for Linux)

If you wish to configure your own instance of AI4MediaBench platform, here are the instructions:_


```
$ cp .env_sample .env
$ docker-compose up -d
$ docker-compose exec django ./manage.py migrate
$ docker-compose exec django ./manage.py generate_data
$ docker-compose exec django ./manage.py collectstatic --noinput
```

You can now login as username "admin" with password "admin" at http://localhost:8000

If you ever need to reset the database, use the script `./reset_db.sh`


## Create certs:

sudo certbot certonly --manual --preferred-challenges=dns -d '*.aimultimedialab.ro'
 
## License
This software is released under the Apache License 2.0 (the "License"); you may not use the software except in compliance with the License.

The text of the Apache License 2.0 can be found online at:
http://www.opensource.org/licenses/apache2.0.php

## Privacy Policy and Terms of Use
Please visit the following [link](https://github.com/AIMultimediaLab/AI4MediaBench-AIMultimediaLab/blob/main/Privacy-Policy-and-Terms-of-Use.MD) for information
regarding the privacy policy and terms of use.
