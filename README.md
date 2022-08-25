# Overview

The idea behind this flask applications is to have easy to use, for a non-technical operations team, application that is designed for operation and monitoring of ETL job workflows.

## Endpoint description

* `/register (POST)` - app registration - public access
* `/login (POST)` - login to the app - public access
* `/home (POST)` - create new workflow from here - admin access
* `/home (GET)` - get list of workflow names
* `/home/<workflow_name>/delete (DELETE)` - delete workflow - admin access
* `/home/<workflow_name>/update (PUT)` - update input parameters of the workflow
* `/instances (POST)` - create new instance of given worflow
* `/instances/<instance_name> (PUT)` - update metadata (E.g. started_on, ended_on, status, log_url ) for given instance that was executed
* `/instances/<instance_name>/status (GET)` - get status of instance that has finished and send slack message if the job failed

## Database description

The backend database is hosted on RDS PostegreSQL instance.
Three tables are used for this application:
* `users` - used for users management
* `workflows` - used for creation of worklows
* `workflows_metadata` - used for storing the metadata for each instance of a workflow


## Get started
```
git clone https://gitlab.com/yani5/flask-etl-manager.git
cd flask-etl-manager   
```
Activate virtualenv.

Once the virtualenv is activated, you can install the required dependencies.
```
pip install -r requirements.txt
```
When the dependancies are installed you start the app.

```
python main.py
```

