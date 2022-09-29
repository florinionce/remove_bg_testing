
# Remove BG Image Testing

### Using [Remove.bg](https://www.remove.bg/) thirdparty
```
$ cp .env.example .env
# edit the API key
$ bundle exec ruby remove_bg_api.rb
```
The output can be found in `output/remove_bg_api`


### Using image magick
#### prerequisites
- install image magick

usage:
```
$ bundle exec ruby image_magick.rb
```

The output can be found in `output/image_magick`


### Using image opencv
#### prerequisites
- install python, venv, pip

setup:
```
$ python3 -m venv venv
$ source venv/bin/activate
```

usage:
```
$ python opencv.py
```
