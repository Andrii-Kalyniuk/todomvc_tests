FROM jenkins/jenkins:lts-jdk11

# Switch to root user to install pyenv and poetry
USER root

# Print kernel and distro info (just for debugging reasons)
RUN echo "Distro info:" && uname -a && cat /etc/*release

# Makes the  default answers to be used for all questions for apt
ARG DEBIAN_FRONTEND=noninteractive
# Set of all dependencies needed for pyenv to work on Ubuntu
RUN apt-get update \
   && apt-get install -y --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev mecab-ipadic-utf8

# Set-up necessary Env vars for PyEnv
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
# -> in this image $HOME for root user
# -> for some reason is `/` :D
# -> ? can we find better place to install .pyenv and .poetry below

# Set-up necessary Env vars for Poetry
ENV POETRY_HOME $HOME/.poetry
ENV PATH="$PATH:$POETRY_HOME/bin"
# -> ? not sure if last line needed...
# ->   poetry might add itself to the PATH automatically

# The code below should work also without preinstalled python version via pyenv
# In such case the system python version should be used as default
# But if you want - you can preinstall the needed version of python, like below
ENV PYTHON_VERSION 3.9.0

# Install pyenv (with specified python) & poetry
# (set -e = Exit on first simple command with non-zero (false) result)
# (set -x = print actual interpolated command before calling it)
RUN set -ex \
   && curl https://pyenv.run | bash \
   && pyenv update \
   && pyenv install $PYTHON_VERSION \
   && pyenv global $PYTHON_VERSION \
   && pyenv rehash \
   && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 -

# Give permissions to jenkins user
RUN chown -R jenkins:jenkins $PYENV_ROOT
RUN chown -R jenkins:jenkins $POETRY_HOME

# Switch to jenkins user
USER jenkins
# Add plugins
RUN jenkins-plugin-cli --plugins allure-jenkins-plugin:latest \
   credentials-binding:latest \
   timestamper:latest \
   ws-cleanup:latest \
   workflow-aggregator:latest \
   github-branch-source:latest \
   build-timeout:latest \
   pipeline-github-lib:latest \
   pipeline-stage-view:latest \
   git:latest \
   email-ext:latest \
   mailer:latest \
   matrix-auth:latest \
   pam-auth:latest \
   ldap:latest

# Configure Allure plugin using groovy script
COPY init.groovy.d/ /var/jenkins_home/init.groovy.d/
# -> one final manual step still is needed: «activate: Allure Command line»
# -> in Manage Jenkins>Global Tool Configuration>Allure Commandline
# -> (or just open <JENKINS_URL>/configureTools/)
# -> press «Add Allure Commandline» and then «Save» buttons
