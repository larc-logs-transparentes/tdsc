# Election Transparency

<abstract>

<Link to article>


## Setup

Clone the repository and install the dependencies

```bash
git clone https://github.com/larc-logs-transparentes/tdsc.git
cd tdsc
bash ./setup.sh
```


## Demo execution

A fast demo execution. It will instanciate the Election Transparency modules and populate it with 74 poll tapes from the 2022 Brazilian Election. The user interface can be access through browser in localhost:80. 

```bash
cd logserver
docker compose up -d
docker run --rm --network host --pull always ghcr.io/larc-logs-transparentes/bu-utils:gh-73
```


## Test operations performance

Evaluate the performance of the main verifications in Election Transparency (Table II).

##### Log Server
Create the trees with 1k, 10k, 100k, 500k, and 1M of leaves. It takes ~2 hours in DO-Premium-AMD with 8GB RAM.

```bash
cd logserver/test_operation_perfomance
./start.sh
```

##### Client
On another machine, install the dependencies and run the tests. It takes ~40 minutes on an Intel Xeon 8168 with 4GB RAM and 50 samples.  Wait for the LogServer to create all trees.

```bash
# activate the Python virtual environment. 
cd tdsc/
source .venv/bin/activate

#  Run the tests. Substitute the <Logserver-IP> with the IP of the LogServer.
cd client
LOGSERVER_IP=<LOGSERVER-IP> python3 test_verifications.py --sample_size=50
```


## Test with 2022 Brazilian presidential elections 

Recalculate the results of the 2022 Brazilian presidential elections using published poll tapes. Evaluate the performance of operations (Table III).

##### Log Server
Populate the LogServer with the ~500k poll tapes from the 2022 elections. It takes ~18 hours in DO-Premium-AMD with 8GB RAM.

```bash
# Reset docker compose state
cd logserver
docker compose down
docker compose up -d

# start script
cd populate-2022-election
bash ./start.sh
```

##### Client
On another machine, install the dependencies and run the tests. It takes ~X min on an Intel Xeon 8168 with 4GB RAM. Wait for the LogServer to insert all poll tapes.

```bash
# activate the Python virtual environment. 
cd tdsc/
source .venv/bin/activate

#  Run the tests. Substitute the <Logserver-IP> with the IP of the LogServer.
cd client
LOGSERVER_IP=<LOGSERVER-IP> python3 test_analysis.py --sample_size=50
```

## 🖥️ Tested Environments

##### Log Server
Hardware: DO-Premium-AMD, 2vCPU, 8GB RAM
Software: Ubuntu 22.04 LTS, Docker version 27.3.1, Python 3.10.12

##### Client
Hardware: Intel Xeon Platinum 8168, 2vCPU, 4GB RAM
Software: Ubuntu 22.04 LTS, Docker version 27.3.1, Python 3.10.12


