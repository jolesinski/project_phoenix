#Core unit
    Main processing unit used in Phoenix. Communication between server (located in rover), 
    and client (stationary PC) is based on JSON-RPC protocol. 
##Server 
    Written in python.

##Client
    Written in C++.

##Usage
    After cloning repo to disk install dependencies and set commands by typing.
    `python setup.py develop`
    If you want to run server type:
    `python server/run.py`
    You can run tests by typing:
    `python setup.py test`