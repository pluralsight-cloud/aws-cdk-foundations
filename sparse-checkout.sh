mkdir s3-object-lambda
cd s3-object-lambda
git init
git remote add origin
https://github.com/aws-samples/aws-cdk-examples
git config core.sparseCheckout true
echo "typescript/s3-object-lambda" >> .git/info/sparse-checkout
git pull origin main
mv typescript/s3-object-lambda/* .
rm -rf typescript
git remote remove origin
