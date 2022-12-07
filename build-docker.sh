#根據IP決定使用哪個環境變數檔
export VM_IP=$(ifconfig | grep 10.32.48 | awk '{print $2}')
export DOCKER_COMPOSE_FILE="docker-compose.yml"

# 傳入參數為 local則使用.env
if [ "$1" = "local" ]
then
    export DOCKER_ENV_FILE=.env
    export DOCKER_COMPOSE_FILE="docker-compose-no-db.yml"
elif [ "$VM_IP" = "10.32.48.117" ] 
then 
    export DOCKER_ENV_FILE=.env.dev
elif [ "$VM_IP" = "10.32.48.xxx" ] 
then 
    export DOCKER_ENV_FILE=.env.qas
elif [ "$VM_IP" = "10.32.48.ooo" ] 
then 
    export DOCKER_ENV_FILE=.env.prd
else 
    export DOCKER_ENV_FILE=.env
    export DOCKER_COMPOSE_FILE="docker-compose-no-db.yml"
fi

export $(grep '^DOCKER_' $DOCKER_ENV_FILE | xargs)

#根據有無設定proxy決定nginx conf
if [ "$DOCKER_NGINX_PROXY" = "" ] 
then 
    export DOCKER_NGINX_DOCKER_FILE=react.dockerfile
    export DOCKER_NGINX_BASE_ROUTE="try_files \$uri /index.html"
else 
    export DOCKER_NGINX_DOCKER_FILE=nginx.dockerfile
    export DOCKER_NGINX_BASE_ROUTE="proxy_pass ${DOCKER_NGINX_PROXY}"
fi

docker-compose -f $DOCKER_COMPOSE_FILE up --build -d 
docker exec $DOCKER_DJANGO_CONTAINER python manage.py makemigrations
docker exec $DOCKER_DJANGO_CONTAINER python manage.py migrate
