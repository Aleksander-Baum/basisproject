# Basisproject Aleksander Baum
## 2CCS01 - r0930134

LINK HOSTED API: https://restaurant-service-aleksander-baum.cloud.okteto.net/

Voor dit project heb ik verkozen een restaurant API uit te werken. De werking achter restaurants interesseert me wel, en een API hierover kan ook makkelijk uitgebreid worden als dit nodig is. 

In mijn API zijn er 3 soorten data: Restaurants, Owners en Menu Items. Dit is zowat de basis dat een restaurant API moet hebben.

### Restaurants
Hierin wordt het id, naam, address en rating opgeslagen. Het id wordt automatisch gegeven. De rest van de data kan de gebruiker zelf invullen. Een restaurant kan je toevoegen en je kan ook alle restaurants tonen, of een specifiek restaurant door het id in te vullen.

### Owners
Hierin wordt het id, naam, telefoonnummer en het restaurant dat zij beheren opgeslagen. Het id wordt ook automatisch toegepast, maar de rest van de data kan de gebruiker zelf invullen. Een owner kan je toevoegen, en je kan alle owners tonen in een lijst.

### Menu Item
Hierin wordt het id, item name, description, price en restaurant id opgeslagen. Zoals tevoren wordt het id automatisch toegepast en kan de gebruiker de rest van de data zelf aanvullen. Hier kan je wat meer mee: je kan een item toevoegen, van een specifiek restaurant alle items tonen, en een item van een specifiek restaurant verwijderen.

### Rest API
In totaal zijn er 5 GET, 3 POST en 1 DELETE endpoints. Validaties heb ik gebruikt waar nodig/mogelijk, een een aangepast response wordt getoond. De path parameters heb ik ook zo logisch mogelijk proberen uit te werken.

SQLite had ik in het begin gebruikt voor data persistentie maar, omdat er extra punten zijn te verdienen, heb ik uiteindelijk MySQL gebruikt voor datapersistentie.

### Deploying
Mijn API wordt correct naar een docker opgebouwd dankzij automatische GitHub Actions. En de deployment naar Okteto verloopt ook volledig correct.

### Bijkomende componenten
Zoals hiervoor vermeld had ik verkozen SQLite te vervangen door MySQL om wat extra punten te verdienen, hierdoor moest ik wel een extra service aanmaken op docker, maar uiteindelijk werkt het perfect en is data persistent.

Hierbij heb ik ook nog een simpele front-end toegevoegd. Je kan hier alle simpele functies uitvoeren: restaurant, owner, en menu item toevoegen. Alle restaurants en owners worden automatisch getoond en menu items kan je krijgen door een restaurant id in te vullen.

## Werking API Postman
### Create restaurant
![1Add Restaurant](https://github.com/Aleksander-Baum/basisproject/assets/113974461/81421410-b82a-4ca9-b4a2-942a3208973c)

### Read restaurants
![2Show Restaurants](https://github.com/Aleksander-Baum/basisproject/assets/113974461/2ccb5ba7-55b8-4c86-8ff9-f2f604c05fea)

### Read specifi restaurant
![3Show Specifig Restaurant](https://github.com/Aleksander-Baum/basisproject/assets/113974461/666edcb6-5f48-42b1-9917-4853caefaecf)

### Create owner
![4Add Owner](https://github.com/Aleksander-Baum/basisproject/assets/113974461/97854ae9-5f78-4bba-8b51-1bdbb46c274f)

### Read owners
![5Show Owners](https://github.com/Aleksander-Baum/basisproject/assets/113974461/7f8dc11a-be3f-4e13-b3d6-e42d782667bb)

### Create Menu Item
![6Add Menu Item](https://github.com/Aleksander-Baum/basisproject/assets/113974461/db57bbfd-58e5-4681-be9b-89847fb5eb5f)

### Read Menu Items
![7Show Menu Items](https://github.com/Aleksander-Baum/basisproject/assets/113974461/6732ad10-a210-4d4c-8f13-e45ed4d5e66e)

### Delete Menu Item
![8Delete Item](https://github.com/Aleksander-Baum/basisproject/assets/113974461/6701a079-d1b6-45c0-84c7-fbf691532e49)

## OpenAPI Docs screenshots
![1OpenAPI](https://github.com/Aleksander-Baum/basisproject/assets/113974461/2414073c-6bff-4225-ba3e-ee6a7fe6ff6e)
![2OpenAPI](https://github.com/Aleksander-Baum/basisproject/assets/113974461/66e02043-187a-47ea-a8c4-f4dc5f75c19c)

### POST /restaurant/
![POSTrestaurant](https://github.com/Aleksander-Baum/basisproject/assets/113974461/7d5ac89f-8c3a-41a0-bcd9-92a219162c4c)

### GET /restaurants/
![GETrestaurants](https://github.com/Aleksander-Baum/basisproject/assets/113974461/7b968d46-8219-4262-9205-a2b4651def81)

### GET /restaurants/{restaurant_id}
![GETrestaurantsID](https://github.com/Aleksander-Baum/basisproject/assets/113974461/638fb5c0-0ba3-4740-8b4a-1bc3786bb24f)

### POST /owner/
![POSTowner](https://github.com/Aleksander-Baum/basisproject/assets/113974461/0b1a169f-bc84-4438-8917-793d4ea2e8d1)

### GET /owners/
![GETowners](https://github.com/Aleksander-Baum/basisproject/assets/113974461/eae29037-cc9e-47aa-a23e-1502418063af)

### POST /menuitem/
![POSTmenuitem](https://github.com/Aleksander-Baum/basisproject/assets/113974461/fe34cf61-9dd5-46ef-8d90-341923c2c37c)

### GET /menuitems/{restaurant_id}
![GETmenuitems](https://github.com/Aleksander-Baum/basisproject/assets/113974461/6d22cf00-51f5-4d4f-81ee-f0014425557e)

### DELETE /restaurants/{restaurant_id}/menuitems/{menu_item_id}
![DELETErestaurantsIDitemID](https://github.com/Aleksander-Baum/basisproject/assets/113974461/0d3ca863-3282-402c-a6b7-b27cda55eb6e)
