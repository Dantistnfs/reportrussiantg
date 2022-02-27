

1. Install docker and docker-compose
2. Run `docker-compose build && docker-compose run app`

Note: container doesn't save your telegram session, so on restart you will need to relogin

## For beginners

1. Register or login on
https://digitalocean.com

2. Open https://cloud.digitalocean.com/droplets/new

3. Choose the same settings as on the images below
![docker image](https://user-images.githubusercontent.com/79193957/155883546-d192b561-848a-4b53-b83a-fc7e49cc29e1.png)

![base plan](https://user-images.githubusercontent.com/79193957/155883596-f297749a-7f0a-44ed-819c-4e1bfb5a1cea.png)

![region](https://user-images.githubusercontent.com/79193957/155883600-2ec154bf-8022-4eec-b135-59950bb5085a.png)

![password](https://user-images.githubusercontent.com/79193957/155883602-d7f2a58b-62e6-4977-a6f5-0398db7e6ef7.png)



4. Click 'Create droplet' in the bottom


5. After droplet was created, open details and click 'Access' on the left sidebar

6. Click 'Launch Droplet Console'
![access](https://user-images.githubusercontent.com/79193957/155883667-1a9d83ea-17a2-4c1d-bf5a-e2f2525f1c6f.png)

7. Paste these commands to the opened terminal window and press Enter
```shell
apt install -y unzip

wget https://github.com/Dantistnfs/reportrussiantg/archive/refs/heads/main.zip && unzip main && cd reportrussiantg-main
docker-compose build && docker-compose run app
```
8. After Install enter your phone number end press Enter
![tg](https://user-images.githubusercontent.com/79193957/155883822-bb95fb2b-c970-4584-85af-48e862128e4b.png)


9. Enter secret code and press Enter
