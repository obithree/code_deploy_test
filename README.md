# code_deploy_test

## AMI作成

```
mkdir /var/test
sudo yum update
sudo yum install ruby
sudo yum install wget
wget https://aws-codedeploy-ap-northeast-1.s3.ap-northeast-1.amazonaws.com/latest/install
chmod +x ./install
sudo ./install auto
sudo systemctl status codedeploy-agent.service 
```

https://docs.aws.amazon.com/ja_jp/codedeploy/latest/userguide/codedeploy-agent-operations-install-linux.html


# IAM

## CodeDeploy
```
DescribeInstanceStatus
RunInstances
pass_role 起動テンプレートで選んだIAMをec2につける権限が必要
```
https://docs.aws.amazon.com/ja_jp/codedeploy/latest/userguide/getting-started-create-service-role.html

## EC2
https://docs.aws.amazon.com/ja_jp/codedeploy/latest/userguide/getting-started-create-iam-instance-profile.html