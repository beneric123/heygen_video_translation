# Simulated Video Translation Server for HeyGen

### HeyGen (Software Engineer, University Graduate) Take-Home Assignment
Benjamin Liang


#### Directory Structure:
```
├── heygen_video_translation
│   ├── heygen_video_translation
│       ├── __init__.py
│       ├── settings.py
│       ├── urls.py
│       ├── asgi.py
│       ├── wsgi.py
│   ├── vid_trans_api
│       ├── __init__.py
│       ├── migrations
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── tests.py
│       ├── urls.py
│       ├── views.py
│   ├── manage.py
│   ├── client.py
│   ├── test_integration.py
│   ├── db.sqlite3
│   ├── requirements.txt
├── README.md
```

#### Introduction:
- To install all necessary packages run ```pip install -r requirements.txt``` from the outer ```heygen_video_translation``` directory.
  
#### Server Attributes:
- possible statuses: pending, completed, or error
- configurable random delay

#### Key Files:
- 

#### Running the Server:
- blah
- test_integration.py

#### Core Features:
- features

#### Ease for Third-Party Use:
- package

#### Customer-Centric Design:
- Efficiency: Dynamic polling based on signals from server - reduces polling when job is far from being completed & increases frequency when completion is near
- Transparency: Provide real-time estimates of duration to completion to keep user constantly informed


