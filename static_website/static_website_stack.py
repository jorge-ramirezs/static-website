from aws_cdk import (
    CfnOutput,
    Stack,
    aws_s3 as s3,
    aws_cloudfront as cloudfront,
)
from constructs import Construct


class StaticWebsiteStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create S3 Bucket to store website files
        bucket = s3.Bucket(self, "StaticWebsiteBucket",
                           access_control=s3.BucketAccessControl.PRIVATE
                           )

        origin_access_identity = cloudfront.OriginAccessIdentity(
            self, 'OriginAccessIdentity')

        bucket.grant_read(origin_access_identity)

        distribution = cloudfront.CloudFrontWebDistribution(
            self,
            'StaticWebsiteDistribution',
            default_root_object='index.html',
            origin_configs=[
                cloudfront.SourceConfiguration(
                    s3_origin_source=cloudfront.S3OriginConfig(
                        s3_bucket_source=bucket,
                        origin_access_identity=origin_access_identity),
                    behaviors=[cloudfront.Behavior(
                        is_default_behavior=True)],
                )
            ]
        )

        # Output the CloudFront domain name
        CfnOutput(self, 'CloudFrontDomain',
                  value=distribution.distribution_domain_name
                  )
