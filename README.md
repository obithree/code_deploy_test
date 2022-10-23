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

