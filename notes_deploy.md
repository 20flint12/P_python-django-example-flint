# https://www.cloudcontrol.com/console/account/flintcloudcontrol
# 20flint12@gmail.com 88888878


git config --local user.email "20flint12@gmail.com"
git config --local user.name "20flint12"
git config --local http.sslverify false

https://github.com/
20flint12 88888878f

[credential]
        username = 20flint12
        helper = cache --timeout=3600



git remote add origin https://github.com/20flint12/P_python-django-example-flint.git
git remote add ccOrigin ssh://testastroflint@cloudcontrolled.com/repository.git
git remote add ccOrigin2 ssh://testastroflint2@cloudcontrolled.com/repository.git
git remote add ccOrigin3 ssh://testastroflint3@cloudcontrolled.com/repository.git
git remote add ccOrigin4 ssh://testastroflint4@cloudcontrolled.com/repository.git
git remote -v



# https://www.cloudcontrol.com/dev-center/Guides/Python/Django

cctrlapp mypolltest create python
cctrlapp mypolltest push
cctrlapp mypolltest addon.add mysqls.free
cctrlapp mypolltest deploy
cctrlapp mypolltest run "python manage.py syncdb"



    cctrlapp mypolltest run "python manage.py sqlall records"
    cctrlapp mypolltest run "python manage.py makemigrations records"
    python manage.py sqlclear records

#########################################################

u8888
20flint12@gmail.com
987685

mypolltest.cloudcontrolled.com/polls


https://github.com/20flint12/P_python-django-example-flint.git
git remote add origin https://github.com/20flint12/P_python-django-example-flint.git
git remote -v



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
cctrlapp testastroflint create python
cctrlapp testastroflint push
cctrlapp testastroflint addon.add mysqls.free
cctrlapp testastroflint deploy
cctrlapp testastroflint run "python manage.py syncdb"
u166087
20flint12@gmail.com
768545367

testastroflint.cloudcontrolled.com/polls
testastroflint.cloudcontrolled.com/admin
kostia
098776789


cctrlapp testastroflint run "python manage.py syncdb"
cctrlapp testastroflint run "python manage.py makemigrations"
cctrlapp testastroflint run "python manage.py migrate"


cctrlapp testastroflint4/default create python
cctrlapp testastroflint4/default addon.add mysqls.free
cctrlapp testastroflint4/default deploy
cctrlapp testastroflint4/default run "python manage.py syncdb"



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

testastroflint2.cloudcontrolled.com/admin   admin2/admin2


cctrlapp testastroflint2/development push
git push ccOrigin2 development:master
cctrlapp testastroflint2 run "python manage.py syncdb"
cctrlapp testastroflint2 run "python manage.py makemigrations"
cctrlapp testastroflint2 run "python manage.py migrate"

//cctrlapp testastroflint2 deploy
cctrlapp testastroflint2/development deploy




%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
cctrlapp testastroflint2/default run bash
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

cctrlapp testastroflint2/default addon.add cloudamqp.lemur
cctrlapp testastroflint2/default addon.add config.free --SET_ENV_VARS --FLOWER_AUTH_EMAIL=20flint12@gmail.com

cctrlapp testastroflint2/default worker.add worker


# Worker configuration
# Add the following line to your app's Procfile:
# Usage:
WORKER_NAME: <command> [<args>]
# Example for a Procfile with one worker defined:
web: python server.py
reminder: python session_reminder.py



# Adding the Worker Add-on
# Before you can start a worker, add the add-on with the addon.add command.
cctrlapp testastroflint4/default addon.add worker.single


#Starting a Worker
#Workers can be started via the command line client's worker.add command.
cctrlapp APP_NAME/DEP_NAME worker.add WORKER_NAME [WORKER_PARAMS]
cctrlapp testastroflint2/default worker.add worker 
cctrlapp testastroflint4/default worker.add myworker

# you can always list running workers like this
cctrlapp testastroflint2/default worker

# To stop a running worker via the command line use the worker.remove command.
cctrlapp testastroflint4/default worker.remove WRK_ID

# and also check the worker's log output with
cctrlapp testastroflint2/default log worker

# To remove the Worker add-on use the addon.remove command.
cctrlapp testastroflint4/default addon.remove worker.single

# the available Add-on plans
cctrlapp testastroflint2/default addon.list

# To get the list of current Add-ons for a deployment
cctrlapp testastroflint2/default addon

# Adding an Add-on is just as easy.
cctrlapp APP_NAME/DEP_NAME addon.add ADDON_NAME.ADDON_OPTION

# To see the log output in a tail -f-like fashion use the cctrlapp log command
cctrlapp testastroflint2/default log [access,error,worker,deploy]
cctrlapp testastroflint2/default log deploy
cctrlapp testastroflint2/default log worker


$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Get the cron.free plan
# To add the cron.free plan to your deployment use
cctrlapp testastroflint2/default addon.add cron.free

# Adding the Cron Add-on
# Before you can add a Cron job, the Add-on itself has to be added:
cctrlapp APP_NAME/DEP_NAME addon.add cron.OPTION
cctrlapp testastroflint2/default addon.add cron.free

# Adding a URL for the Cron job
# To call an URL with the specific interval you write it as the parameter:
# for the default deployment
cctrlapp APP_NAME/DEP_NAME cron.add http[s]://[user:password@]APP_NAME.cloudcontrolled.com
cctrlapp testastroflint2/default cron.add http://testastroflint2.cloudcontrolled.com/weather

# List Cron overview
# Get an overview of all your Cron jobs:
cctrlapp testastroflint2/default cron

# Get the details of a specific Cron job:
cctrlapp testastroflint2/default cron CRON_ID

# Removing a Cron job:
# You can remove a Cron job by the job_id
cctrlapp testastroflint2/default cron.remove JOB_ID

# Upgrading / downgrading the Cron addon
cctrlapp testastroflint2/default addon.upgrade cron.free cron.hourly
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# To start a shell (e.g. bash) use the run command.
cctrlapp testastroflint2/default run bash
cctrlapp testastroflint4/default run bash


# command will list the environment variables. Note that the use of the quotes is required for a command that includes spaces.
cctrlapp testastroflint2/default run "env | sort"



%%%$%$%$%$%$%
web: gunicorn mysite.wsgi --config gunicorn_config.py --bind 0.0.0.0:${PORT:-5000}

web: celery flower --port=$PORT --broker=$CLOUDAMQP_URL --auth=$FLOWER_AUTH_EMAIL
worker: celery -A tasks worker --loglevel=info
$%$%$%$%$%$%$%

pip freeze
