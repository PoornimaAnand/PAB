import boto.ec2

conn = boto.ec2.connect_to_region(
    "us-east-2",
    aws_access_key_id="AKIARFUWRU4FAWA2PDEN",
    aws_secret_access_key="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",
)
conn = boto.ec2.connect_to_region("us-east-2")
conn.run_instances(
    "ami-0ba62214afa52bec7",
    key_name="myKey",
    instance_type="t2.micro",
    security_groups=["your-security-group-here"],
)