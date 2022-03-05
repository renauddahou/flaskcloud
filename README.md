# aws-elastic-beanstalk
A pipeline to auto-deploy a Flask web application on AWS Elastic Beanstalk.

<img src="img/Elastic-Beanstalk-PaaS.jpg" width="675">

NOTE: The Makefile deploy command sets up the app in AWS region us-east-2, which can be changed in this line:
```
eb init -r us-east-2 -p python-3.7 flask-auto-deploy
```

### Steps

1. Install EB CLI dependencies in an AWS Cloud9 envrionment: 

```
sudo yum groupinstall -y "Development Tools"
```
```
sudo yum install -y zlib-devel openssl-devel ncurses-devel libffi-devel sqlite-devel.x86_64 readline-devel.x86_64 bzip2-devel.x86_64
```

2. Install EB CLI:

```
git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup.git
```
```
./aws-elastic-beanstalk-cli-setup/scripts/bundled_installer
```

3. Ensure `eb` is in PATH:

```
echo 'export PATH="/home/ec2-user/.ebcli-virtual-env/executables:$PATH"' >> ~/.bash_profile && source ~/.bash_profile
```
```
eb --version
```

4. Clone this GitHub repo, and cd into the directory:

```
git clone https://github.com/ptdriscoll/aws-elastic-beanstalk.git
```
```
cd aws-elastic-beanstalk
```

5. Create and source the Python virtual environment:

```
python3 -m venv ~/.aws-elastic-beanstalk
```
```
source ~/.aws-elastic-beanstalk/bin/activate
```

6. Install packages:

```
make all
```

7. If you have never set up an Elastic Beanstalk app in your AWS account:
    - Some IAM roles need to be created with the correct permissions
    - The easiest way to do that is automatically, by creating a sample app through the console:
	    - [Creating an Elastic Beanstalk environment](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.environments.html)
		- [Unable to assume role [IAM Role ARM] Verify that the role exists](https://forums.aws.amazon.com/thread.jspa?threadID=213002)
	- Once the roles are created, they will be referenced by future Elastic Beanstalk apps		

8. Initialize eb app to default AWS region (first line), or to specified region (us-east-2 in second line):

```
eb init -p python-3.7 flask-auto-deploy
```

```
eb init -r us-east-2 -p python-3.7 flask-auto-deploy
```

9. As an option, to create SSH keys, run `eb init` again.

10. Create an environment and deploy:

```
eb create flask-auto-deploy-env
```

11. Go to [Elastic Beanstalk page](https://us-east-2.console.aws.amazon.com/elasticbeanstalk/) (region us-east-2 link) to view status and get URL.

12. Append "echo" and some value to url to see app output:

```
/echo/<something>
```

13. Set up continuous delivery with [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/concepts.html#concepts-how-it-works), using a buildspec file in a YAML format. A sample [buildspec.yml](/buildspec.yml) file, using these [specs](https://docs.aws.amazon.com/codebuild/latest/userguide/build-spec-ref.html), is included in this repository. To see an example of how CodeBuild can be set up, see step 14 in this [project](https://github.com/ptdriscoll/aws-s3).  

14. To terminate the environment, and all related AWS resources:

```
eb terminate flask-auto-deploy-env
```

### Video tutorial

- [Building a Website using PaaS with AWS Beanstalk](https://www.coursera.org/lecture/cloud-computing-foundations-duke/building-a-website-using-paas-with-aws-beanstalk-qKLVW)

### More references

- [Building Multiple Types of Websites](https://paiml.com/docs/home/books/cloud-computing-for-data/chapter02-cloud-foundations/#building-multiple-types-of-websites)
- [Deploying a Flask application to Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html)
- [GitHub: Flask-Elastic-Beanstalk](https://github.com/noahgift/Flask-Elastic-Beanstalk)
- [Install the EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html)
- [GitHub: EB CLI Installer](https://github.com/aws/aws-elastic-beanstalk-cli-setup)
- [AWS Elastic Beanstalk Documentation](https://docs.aws.amazon.com/elastic-beanstalk/index.html)
- [AWS CodeBuild Documentation](https://docs.aws.amazon.com/codebuild/index.html)
