googleappengine-python-flask-skeleton
=====================================

A skeleton for building Python applications on Google App Engine with the Flask micro framework.

Install
-------

```
# Install the Google App Engine Python SDK
cd
wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.10.zip
unzip google_appengine_1.9.10.zip
rm google_appengine_1.9.10.zip
export PATH=$PATH:~/google_appengine/

# Clone this repo
git clone git@github.com:davide-ceretti/googleappengine-python-flask-skeleton.git

# Install requirements (In your virtualenv)
cd googleappengine-python-flask-skeleton
pip install -r requirements.txt -t lib
pip install -r test-requirements.txt
```

Run server
----------

```
./run.sh
# App is served at http://localhost:8080/
# Admin interface is served at http://localhost:8000
```

Run tests
---------

```
./test.sh
```

Deploy
------

* Use the Admin Console to create a project/app id. (App id and project id are identical)
* Update app.yaml with the chosen app id
* ```./deploy.sh```
