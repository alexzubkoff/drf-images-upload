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
![django_admin_1](https://user-images.githubusercontent.com/22620680/220641803-244eb4e0-4331-4e5d-a8ad-5dabc6eebb0d.png)
![django_admin_2](https://user-images.githubusercontent.com/22620680/220641815-cfd80c37-e731-4c8f-8570-75f908becda7.png)
![django_admin_add_image](https://user-images.githubusercontent.com/22620680/220641822-9e1a2dcd-3bc8-4dca-95c1-cf10fbeb8e0b.png)
![django_admin_user_change](https://user-images.githubusercontent.com/22620680/220641828-ed43fa3b-8228-4878-923a-fb8007a47c07.png)
![django_admin_user_profile_plan](https://user-images.githubusercontent.com/22620680/220641829-203ecf3f-e451-43f5-8e34-156ddf13661f.png)
![drf_browsable_api_image_link](https://user-images.githubusercontent.com/22620680/220641831-ade663cf-697f-4199-bc21-fb697888e8c6.png)
![drf_browsable_api_image_list](https://user-images.githubusercontent.com/22620680/220641834-3a1a8b07-9a3d-4bd8-b223-d80302de7fc6.png)
![drf_browsable_api_image_list_add_new_image](https://user-images.githubusercontent.com/22620680/220641838-ebaf5ee4-886e-4ce9-8406-74cac6d25f0b.png)
![drf_browsable_image_original](https://user-images.githubusercontent.com/22620680/220641844-4daea8d5-e2cc-4388-8377-0bcc05bcf7d5.png)
![thumbnails_images_resized_200_400](https://user-images.githubusercontent.com/22620680/220641849-abff7593-3604-432e-ab72-1b68c4301cc6.png)
![thumbnails_large_400](https://user-images.githubusercontent.com/22620680/220641857-6cbcf6fe-8f21-4096-bbb5-ff33dd5d54f8.png)
![thumbnails_small_200](https://user-images.githubusercontent.com/22620680/220641859-88e68174-322c-47dd-b74b-57bbfc92993b.png)
