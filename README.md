# Election Transparency

<abstract>

<Link to article>


## Setup

Clone the repository and install the dependencies

```bash
git clone https://github.com/larc-logs-transparentes/tdsc.git
cd tdsc/logserver
./setup.sh
```


## Demo execution

A fast demo execution. It will instanciate the Election Transparency modules and populate it with X poll tapes from the 2022 Brazilian Election. The user interface can be access through browser in localhost:80. 

```bash
docker compose up -d
docker run --rm --network host --pull always ghcr.io/larc-logs-transparentes/bu-utils:gh-73
```


## Test operations performance

Evaluate the performance of the main verifications in Election Transparency (Table II).

##### Log Server
Create the trees with 1k, 10k, 100k, 500k, and 1M of leaves. It takes ~2 hours in DO-Premium-AMD with 8GB RAM.

```bash
cd logserver
./start.sh
```

##### Client
In another machine, install the dependencies and run the tests. It takes ~40 min in Intel Xeon 8168 with 4GB RAM with 50 samples.  Wait for the LogServer create all trees.

```bash
# Install the dependencies
cd client
./setup.sh

# activate the Python virtual environment. 
source ./venv/bin/activate

#  Run the tests. Substitute the <Logserver-IP> with the IP of the LogServer.
TL_MANAGER_URL=http://<LOGSERVER-IP>:8000 python3 test_verifications.py --sample_size=50
```


## Test with 2022 Brazilian presidential elections 

Recalculate the results of the 2022 Brazilian presidential elections using published poll tapes.

##### Log Server
Populate the LogServer with the ~500k poll tapes from the 2022 elections. It takes ~X hours in DO-Premium-AMD with 8GB RAM.

```bash
cd logserver
./setup.sh

# Reset old entries in tree
docker compose down
docker compose up -d

# start script
./populate-2022-elections.sh

# download poll tapes (adapted from https://bit.ly/3NXoUyT)
cd test-2022-elections
./download-and-extract.sh

# activate the Python virtual environment. 
source ./venv/bin/activate

# Insert poll tapes in the trees
python populate_db.py
./start.sh
```

##### Client
In another machine, install the dependencies and run the tests. It takes ~40 min in Intel Xeon 8168 with 4GB RAM with 50 samples.  Wait for the LogServer create all trees.

```bash
cd logserver
./start.sh
```

## 🖥️ Tested Environments

##### Log Server
Hardware: DO-Premium-AMD, 2vCPU, 8GB RAM
Software: Ubuntu 22.04 LTS, Docker version 27.3.1, Python 3.10.12

##### Client
Hardware: Intel Xeon Platinum 8168, 2vCPU, 4GB RAM
Software: Ubuntu 22.04 LTS, Docker version 27.3.1, Python 3.10.12


