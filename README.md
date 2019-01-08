# Sport Catalog

Udacity Full Stack Fundamentals Course: Item Catalog Project

By Janet Vong

## Prequisites

### Set up

To run the server code, you need to have [Python 2](https://www.python.org/download/releases/2.7/) installed on your computer. You also need basic knowledge of linux. Some knowledge of python is good, but not necessary.

### Secret Key

To be able to run the sport catalog application, you'll need to create a secret_key.json file.

## How to open the sport catalog website

1. Clone or download all of the files in this project (folder: `fullstack-nanodegree-vm`).
2. Open your terminal and change to the `fullstack-nanodegree-vm` directory. The folder should be in your Downloads folder.
3. Once you're in the `fullstack-nanodegree-vm` directory, change to the `vagrant` directory:

```
cd vagrant
```

4. Start Vagrant:

 ```
 vagrant up
 ```

 then:

 ```
 vagrant ssh
 ```

5. You should see the message that "The shared directory is located at `/vagrant`". Change to that directory:

```
cd /vagrant
```

6. Change to the catalog directory

```
cd catalog
```

7. Create a project on Google Cloud Platform to get an OAuth 2.0 credential for your client_secrets.json file. Follow these steps.

a. Log in to your google account at: https://console.cloud.google.com/

b. In the left-side navigation go to:  **API & Services > Credentials**

c. Click the "Create credentials > OAuth client ID" drop down menu in the "Credentials" tab.

d. Select "Web Application", name your project, add "http://localhost:5000" to "Authorized JavaScript origins
", and add "	http://localhost:5000/login" and "	http://localhost:5000/gconnect" to "Authorized redirect URIs."  Click "save".

e. On the top bar, click "Download JSON" and save the file in the catalog folder, named as `client_secrets.json`.

7. Set up the database by running the following command once:

```
python database_setup.py
```

8. Populate your database by running the following command once:

```
python lotsofsportitems.py
```

9. Run the application:

```
python application.py
```

10. In your browser, visit: http://localhost:5000/
