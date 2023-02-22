# drf-images-upload

## Installation

You have to install Docker on your PC.

Create a Directory for Work:
```sh
mkdir your_dir
cd your_dir 
```
Create and Activate the Virtual Environment:
```sh
python -m venv venv
venv\Scripts\activate (Windows)
```
Clone the project (after Git installation):
```sh
(venv) git clone git@github.com:alexzubkoff/drf-images-upload.git .

Create a Directory for images uploads into the root of the project:
```sh
mkdir media/images
```
```
Run to create Docker images and containers:
```sh
docker-compose  up -d --build 
```
Run the project:
```sh
load into your browser adress field:
http://127.0.0.1:8000/admin
```
Create superuser.
Loads new images from admin panel.
```sh
load into your browser adress field:
http://127.0.0.1:8000/imgs/api/v1/
```