# Sport Catalog

Udacity Full Stack Fundamentals Course: Item Catalog Project

By Janet Vong

## Prequisites

To run the server code, you need to have [Python 2](https://www.python.org/download/releases/2.7/) installed on your computer. You also need basic knowledge of linux. Some knowledge of python is good, but not necessary.

## How to open the movie trailer website

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
catalog
```

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
