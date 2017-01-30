sudo apt-get install mongodb-server
pip install -r requirements.txt
mongoimport --db world_bank --collection project --drop --file world_bank.json
