'''
# AWS::SecurityLake Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_securitylake as securitylake
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for SecurityLake construct libraries](https://constructs.dev/search?q=securitylake)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::SecurityLake resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityLake.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::SecurityLake](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_SecurityLake.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDataLake(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake",
):
    '''Resource Type definition for AWS::SecurityLake::DataLake.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html
    :cloudformationResource: AWS::SecurityLake::DataLake
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_securitylake as securitylake
        
        cfn_data_lake = securitylake.CfnDataLake(self, "MyCfnDataLake",
            encryption_configuration=securitylake.CfnDataLake.EncryptionConfigurationProperty(
                kms_key_id="kmsKeyId"
            ),
            lifecycle_configuration=securitylake.CfnDataLake.LifecycleConfigurationProperty(
                expiration=securitylake.CfnDataLake.ExpirationProperty(
                    days=123
                ),
                transitions=[securitylake.CfnDataLake.TransitionsProperty(
                    days=123,
                    storage_class="storageClass"
                )]
            ),
            meta_store_manager_role_arn="metaStoreManagerRoleArn",
            replication_configuration=securitylake.CfnDataLake.ReplicationConfigurationProperty(
                regions=["regions"],
                role_arn="roleArn"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLake.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLake.LifecycleConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        meta_store_manager_role_arn: typing.Optional[builtins.str] = None,
        replication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLake.ReplicationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param encryption_configuration: Provides encryption details of Amazon Security Lake object.
        :param lifecycle_configuration: Provides lifecycle details of Amazon Security Lake object.
        :param meta_store_manager_role_arn: The Amazon Resource Name (ARN) used to index AWS Glue table partitions that are generated by the ingestion and normalization of AWS log sources and custom sources.
        :param replication_configuration: Provides replication details of Amazon Security Lake object.
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff487a50882ee11f396717fb970b445f3274af88108d1c1d390543dfb1fdf534)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataLakeProps(
            encryption_configuration=encryption_configuration,
            lifecycle_configuration=lifecycle_configuration,
            meta_store_manager_role_arn=meta_store_manager_role_arn,
            replication_configuration=replication_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d7a1c25528114b19a22f7fe9e5b4213f46c37e16f22245bc3dc38ad34fc7ef6)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb852df583c773c6f5d30c27afae6f598c8606ae40f25dd1885d8fbf5013661b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) created by you to provide to the subscriber.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrS3BucketArn")
    def attr_s3_bucket_arn(self) -> builtins.str:
        '''The ARN for the Amazon Security Lake Amazon S3 bucket.

        :cloudformationAttribute: S3BucketArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrS3BucketArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.EncryptionConfigurationProperty"]]:
        '''Provides encryption details of Amazon Security Lake object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12edf08ab82b633325fe7034b3424955ea7bff566dfa00928107723a5d0f6a72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="lifecycleConfiguration")
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.LifecycleConfigurationProperty"]]:
        '''Provides lifecycle details of Amazon Security Lake object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.LifecycleConfigurationProperty"]], jsii.get(self, "lifecycleConfiguration"))

    @lifecycle_configuration.setter
    def lifecycle_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.LifecycleConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__916659d1bcdf1d6d40de689f3b334b766e1a8fb681a493926742e61ce5ba40b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lifecycleConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="metaStoreManagerRoleArn")
    def meta_store_manager_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) used to index AWS Glue table partitions that are generated by the ingestion and normalization of AWS log sources and custom sources.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "metaStoreManagerRoleArn"))

    @meta_store_manager_role_arn.setter
    def meta_store_manager_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23cd82335763114e4ff9c52f4ff2b4db4b4be68cc8f5b468e1325fa0e0e79558)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metaStoreManagerRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="replicationConfiguration")
    def replication_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.ReplicationConfigurationProperty"]]:
        '''Provides replication details of Amazon Security Lake object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.ReplicationConfigurationProperty"]], jsii.get(self, "replicationConfiguration"))

    @replication_configuration.setter
    def replication_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.ReplicationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__647257bd68002b29a89b3128d4883d0c748e98d2c70a5b154446993271225230)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6654ce3b2fa02feedc8f03797f96ae7270d4bd79ef3c3791b522e8277fa3798c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key_id": "kmsKeyId"},
    )
    class EncryptionConfigurationProperty:
        def __init__(self, *, kms_key_id: typing.Optional[builtins.str] = None) -> None:
            '''Provides encryption details of Amazon Security Lake object.

            :param kms_key_id: The id of KMS encryption key used by Amazon Security Lake to encrypt the Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                encryption_configuration_property = securitylake.CfnDataLake.EncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c697088167e83d968076432c9f71877137655465afc625784270e3ba40d3f57b)
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The id of KMS encryption key used by Amazon Security Lake to encrypt the Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-encryptionconfiguration.html#cfn-securitylake-datalake-encryptionconfiguration-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake.ExpirationProperty",
        jsii_struct_bases=[],
        name_mapping={"days": "days"},
    )
    class ExpirationProperty:
        def __init__(self, *, days: typing.Optional[jsii.Number] = None) -> None:
            '''Provides data expiration details of Amazon Security Lake object.

            :param days: Number of days before data expires in the Amazon Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-expiration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                expiration_property = securitylake.CfnDataLake.ExpirationProperty(
                    days=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__676fee3c866c464d5b150fd2a1553faf30ba52129224b9869203f21574e77d9f)
                check_type(argname="argument days", value=days, expected_type=type_hints["days"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if days is not None:
                self._values["days"] = days

        @builtins.property
        def days(self) -> typing.Optional[jsii.Number]:
            '''Number of days before data expires in the Amazon Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-expiration.html#cfn-securitylake-datalake-expiration-days
            '''
            result = self._values.get("days")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExpirationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake.LifecycleConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"expiration": "expiration", "transitions": "transitions"},
    )
    class LifecycleConfigurationProperty:
        def __init__(
            self,
            *,
            expiration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLake.ExpirationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            transitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDataLake.TransitionsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Provides lifecycle details of Amazon Security Lake object.

            :param expiration: Provides data expiration details of Amazon Security Lake object.
            :param transitions: Provides data storage transition details of Amazon Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-lifecycleconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                lifecycle_configuration_property = securitylake.CfnDataLake.LifecycleConfigurationProperty(
                    expiration=securitylake.CfnDataLake.ExpirationProperty(
                        days=123
                    ),
                    transitions=[securitylake.CfnDataLake.TransitionsProperty(
                        days=123,
                        storage_class="storageClass"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__09cd166ed037b2c00b8a44dc0e94832b0851b09edc3ca5e9ac0de67068729149)
                check_type(argname="argument expiration", value=expiration, expected_type=type_hints["expiration"])
                check_type(argname="argument transitions", value=transitions, expected_type=type_hints["transitions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if expiration is not None:
                self._values["expiration"] = expiration
            if transitions is not None:
                self._values["transitions"] = transitions

        @builtins.property
        def expiration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.ExpirationProperty"]]:
            '''Provides data expiration details of Amazon Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-lifecycleconfiguration.html#cfn-securitylake-datalake-lifecycleconfiguration-expiration
            '''
            result = self._values.get("expiration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDataLake.ExpirationProperty"]], result)

        @builtins.property
        def transitions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLake.TransitionsProperty"]]]]:
            '''Provides data storage transition details of Amazon Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-lifecycleconfiguration.html#cfn-securitylake-datalake-lifecycleconfiguration-transitions
            '''
            result = self._values.get("transitions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDataLake.TransitionsProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LifecycleConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake.ReplicationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"regions": "regions", "role_arn": "roleArn"},
    )
    class ReplicationConfigurationProperty:
        def __init__(
            self,
            *,
            regions: typing.Optional[typing.Sequence[builtins.str]] = None,
            role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides replication details of Amazon Security Lake object.

            :param regions: Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets. Amazon S3 buckets that are configured for object replication can be owned by the same AWS account or by different accounts. You can replicate objects to a single destination bucket or to multiple destination buckets. The destination buckets can be in different AWS Regions or within the same Region as the source bucket.
            :param role_arn: Replication settings for the Amazon S3 buckets. This parameter uses the AWS Identity and Access Management (IAM) role you created that is managed by Security Lake, to ensure the replication setting is correct.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-replicationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                replication_configuration_property = securitylake.CfnDataLake.ReplicationConfigurationProperty(
                    regions=["regions"],
                    role_arn="roleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f5e309ce471c0b5b94d10c5cf8d75ece96a70a7112aa8396372449cae02d7005)
                check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if regions is not None:
                self._values["regions"] = regions
            if role_arn is not None:
                self._values["role_arn"] = role_arn

        @builtins.property
        def regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Replication enables automatic, asynchronous copying of objects across Amazon S3 buckets.

            Amazon S3 buckets that are configured for object replication can be owned by the same AWS account or by different accounts. You can replicate objects to a single destination bucket or to multiple destination buckets. The destination buckets can be in different AWS Regions or within the same Region as the source bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-replicationconfiguration.html#cfn-securitylake-datalake-replicationconfiguration-regions
            '''
            result = self._values.get("regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def role_arn(self) -> typing.Optional[builtins.str]:
            '''Replication settings for the Amazon S3 buckets.

            This parameter uses the AWS Identity and Access Management (IAM) role you created that is managed by Security Lake, to ensure the replication setting is correct.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-replicationconfiguration.html#cfn-securitylake-datalake-replicationconfiguration-rolearn
            '''
            result = self._values.get("role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReplicationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLake.TransitionsProperty",
        jsii_struct_bases=[],
        name_mapping={"days": "days", "storage_class": "storageClass"},
    )
    class TransitionsProperty:
        def __init__(
            self,
            *,
            days: typing.Optional[jsii.Number] = None,
            storage_class: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param days: Number of days before data transitions to a different S3 Storage Class in the Amazon Security Lake object.
            :param storage_class: The range of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-transitions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_securitylake as securitylake
                
                transitions_property = securitylake.CfnDataLake.TransitionsProperty(
                    days=123,
                    storage_class="storageClass"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aaac67133f980ed118f75aa7447b8e2c8f6a4e8d8fce97491e407d04b2924302)
                check_type(argname="argument days", value=days, expected_type=type_hints["days"])
                check_type(argname="argument storage_class", value=storage_class, expected_type=type_hints["storage_class"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if days is not None:
                self._values["days"] = days
            if storage_class is not None:
                self._values["storage_class"] = storage_class

        @builtins.property
        def days(self) -> typing.Optional[jsii.Number]:
            '''Number of days before data transitions to a different S3 Storage Class in the Amazon Security Lake object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-transitions.html#cfn-securitylake-datalake-transitions-days
            '''
            result = self._values.get("days")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def storage_class(self) -> typing.Optional[builtins.str]:
            '''The range of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-securitylake-datalake-transitions.html#cfn-securitylake-datalake-transitions-storageclass
            '''
            result = self._values.get("storage_class")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TransitionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_securitylake.CfnDataLakeProps",
    jsii_struct_bases=[],
    name_mapping={
        "encryption_configuration": "encryptionConfiguration",
        "lifecycle_configuration": "lifecycleConfiguration",
        "meta_store_manager_role_arn": "metaStoreManagerRoleArn",
        "replication_configuration": "replicationConfiguration",
        "tags": "tags",
    },
)
class CfnDataLakeProps:
    def __init__(
        self,
        *,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        meta_store_manager_role_arn: typing.Optional[builtins.str] = None,
        replication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.ReplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataLake``.

        :param encryption_configuration: Provides encryption details of Amazon Security Lake object.
        :param lifecycle_configuration: Provides lifecycle details of Amazon Security Lake object.
        :param meta_store_manager_role_arn: The Amazon Resource Name (ARN) used to index AWS Glue table partitions that are generated by the ingestion and normalization of AWS log sources and custom sources.
        :param replication_configuration: Provides replication details of Amazon Security Lake object.
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_securitylake as securitylake
            
            cfn_data_lake_props = securitylake.CfnDataLakeProps(
                encryption_configuration=securitylake.CfnDataLake.EncryptionConfigurationProperty(
                    kms_key_id="kmsKeyId"
                ),
                lifecycle_configuration=securitylake.CfnDataLake.LifecycleConfigurationProperty(
                    expiration=securitylake.CfnDataLake.ExpirationProperty(
                        days=123
                    ),
                    transitions=[securitylake.CfnDataLake.TransitionsProperty(
                        days=123,
                        storage_class="storageClass"
                    )]
                ),
                meta_store_manager_role_arn="metaStoreManagerRoleArn",
                replication_configuration=securitylake.CfnDataLake.ReplicationConfigurationProperty(
                    regions=["regions"],
                    role_arn="roleArn"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f98044af937b493e98dc654fc28cbeccbd1ee2f339cd00c1cc59056847b8fb37)
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument lifecycle_configuration", value=lifecycle_configuration, expected_type=type_hints["lifecycle_configuration"])
            check_type(argname="argument meta_store_manager_role_arn", value=meta_store_manager_role_arn, expected_type=type_hints["meta_store_manager_role_arn"])
            check_type(argname="argument replication_configuration", value=replication_configuration, expected_type=type_hints["replication_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if lifecycle_configuration is not None:
            self._values["lifecycle_configuration"] = lifecycle_configuration
        if meta_store_manager_role_arn is not None:
            self._values["meta_store_manager_role_arn"] = meta_store_manager_role_arn
        if replication_configuration is not None:
            self._values["replication_configuration"] = replication_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.EncryptionConfigurationProperty]]:
        '''Provides encryption details of Amazon Security Lake object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html#cfn-securitylake-datalake-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.EncryptionConfigurationProperty]], result)

    @builtins.property
    def lifecycle_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.LifecycleConfigurationProperty]]:
        '''Provides lifecycle details of Amazon Security Lake object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html#cfn-securitylake-datalake-lifecycleconfiguration
        '''
        result = self._values.get("lifecycle_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.LifecycleConfigurationProperty]], result)

    @builtins.property
    def meta_store_manager_role_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) used to index AWS Glue table partitions that are generated by the ingestion and normalization of AWS log sources and custom sources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html#cfn-securitylake-datalake-metastoremanagerrolearn
        '''
        result = self._values.get("meta_store_manager_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.ReplicationConfigurationProperty]]:
        '''Provides replication details of Amazon Security Lake object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html#cfn-securitylake-datalake-replicationconfiguration
        '''
        result = self._values.get("replication_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.ReplicationConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securitylake-datalake.html#cfn-securitylake-datalake-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataLakeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDataLake",
    "CfnDataLakeProps",
]

publication.publish()

def _typecheckingstub__ff487a50882ee11f396717fb970b445f3274af88108d1c1d390543dfb1fdf534(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    meta_store_manager_role_arn: typing.Optional[builtins.str] = None,
    replication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.ReplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d7a1c25528114b19a22f7fe9e5b4213f46c37e16f22245bc3dc38ad34fc7ef6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb852df583c773c6f5d30c27afae6f598c8606ae40f25dd1885d8fbf5013661b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12edf08ab82b633325fe7034b3424955ea7bff566dfa00928107723a5d0f6a72(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916659d1bcdf1d6d40de689f3b334b766e1a8fb681a493926742e61ce5ba40b7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.LifecycleConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23cd82335763114e4ff9c52f4ff2b4db4b4be68cc8f5b468e1325fa0e0e79558(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__647257bd68002b29a89b3128d4883d0c748e98d2c70a5b154446993271225230(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDataLake.ReplicationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6654ce3b2fa02feedc8f03797f96ae7270d4bd79ef3c3791b522e8277fa3798c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c697088167e83d968076432c9f71877137655465afc625784270e3ba40d3f57b(
    *,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__676fee3c866c464d5b150fd2a1553faf30ba52129224b9869203f21574e77d9f(
    *,
    days: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09cd166ed037b2c00b8a44dc0e94832b0851b09edc3ca5e9ac0de67068729149(
    *,
    expiration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.ExpirationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    transitions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.TransitionsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5e309ce471c0b5b94d10c5cf8d75ece96a70a7112aa8396372449cae02d7005(
    *,
    regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaac67133f980ed118f75aa7447b8e2c8f6a4e8d8fce97491e407d04b2924302(
    *,
    days: typing.Optional[jsii.Number] = None,
    storage_class: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f98044af937b493e98dc654fc28cbeccbd1ee2f339cd00c1cc59056847b8fb37(
    *,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lifecycle_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.LifecycleConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    meta_store_manager_role_arn: typing.Optional[builtins.str] = None,
    replication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDataLake.ReplicationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
