#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from 'aws-cdk-lib';
import { SimpleBucketStack } from '../lib/simple-bucket-stack';

const app = new cdk.App();
new SimpleBucketStack(app, 'SimpleBucketStack', { });