web: gunicorn biangelis.wsgi --log-file -

BUILD_DIR=${1:-}
CACHE_DIR=${2:-}
ENV_DIR=${3:-}

echo "------> Generating .profile.d file to generate google-credentials.json at startup"
mkdir -p $BUILD_DIR/.profile.d
echo "echo ${GOOGLE_CREDENTIALS@Q} > /biangelis/gcp.json" > $BUILD_DIR/.profile.d/gcp.sh
echo "echo ${ENV_VAR@Q} > /.env" > $BUILD_DIR/.env
chmod +x $BUILD_DIR/.profile.d/gcp.sh
chmod +x $BUILD_DIR/.profile.d/.env