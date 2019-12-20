#! /bin/bash

STACK=""
BUCKET=""

usage() {
  echo -n "$0 [OPTION]...

Options:
  --stack         Cloudformation stack name, default `imswe`
  -b, --bucket    Bucket for deployment.yaml, default `trek10-acaito-sandbox`

  -h, --help      Display this help and exit
"
}

while (( "$#" )); do
  case "$1" in
    -b|--bucket)    BUCKET=$2; shift 2;;
    --stack)        STACK=$2; shift 2;;
    -h|--help)      usage; exit ;;
    -*|--*=)        echo "Error: Unsupported argument $1" >&2; usage; exit 1 ;;
    *)              PARAMS+=("$1"); shift ;;
  esac
done
eval set -- "${PARAMS[@]}"

pipenv lock --requirements > app/requirements.txt
sam build --template template.yaml
sam package --template-file .aws-sam/build/template.yaml --s3-bucket $BUCKET --output-template-file deployment.yaml
sam deploy --s3-bucket $BUCKET --template-file deployment.yaml --stack-name $STACK