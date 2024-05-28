import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as s3 from 'aws-cdk-lib/aws-s3';

export class SimpleBucketStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const webbucket = new s3.Bucket(this, 'WebBucket', {
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });
  }
}