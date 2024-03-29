# Full_Stack_Nano

<h2>Project Part 5: Build a Linux Server</h2>
</br>
<p><strong>Project Description</strong> (from Udacity):</p>
<blockquote>
<p>You will take a baseline installation of a Linux server and prepare it to host your web applications. You will secure your server from a number of attack vectors, install and configure a database server, and deploy one of your existing web applications onto it.</p>
</blockquote>
<h3>IP Address, SSH Port, Grader Login, Application URL</h3>
<p><strong>Public IP Address:</strong> 3.89.185.192 <br>
<strong>SSH Port:</strong> 2200 <br>
<strong>SSH login as Grader</strong>:  ssh -v -i ~/.ssh/udacity_key.pem grader@3.89.185.192 -p 2200<br>
<strong>Item Catalog URL:</strong> <a href="http://ec2-3-89-185-192.compute-1.amazonaws.com" rel="nofollow"> http://ec2-3-89-185-192.compute-1.amazonaws.com</a>
<h3>Software Needed</h3>
<p><strong>Software Needed:</strong> <br>
Finger, Daemon NTPD, Apache2, Unattended Upgrades, Mod_wsgi (Apache HTTP server mod), Git, Pip, Flask, Virtualenv, Flask_oauth, httplib2, sqlalchemy, psycopg2, sqlalchemy_utils, Postgres, libpq-dev, Python
<br><br></p>
<p><strong>Changes Needed:</strong><br></p>
<ol>
<li>Add grader, give grader sudo permissions, and change root owner to Grader <br></li>
<li>Timezone set to UTC <br></li>
<li>Keys set for grader <br></li>
<li>Enforce a key-based authentication <br></li>
<li>Change the port from 22 to 2200 <br></li>
<li>Add a firewall permissions for SSH port 2200, HTTP port 80, NTP port 123 <br></li>
<li>Disable the ssh login for root/ubuntu user <br></li>
<li>Configure a virtual host and PostgreSQL for Item Catalog Project</li>
</ol>
<h3>Getting Started</h3>
<p>This project uses <a href="https://amazonlightsail.com/" rel="nofollow">Amazon Lightsail</a> to create a Linux server instance.</p>
<ol>
<li>
<p>Get your server.</p>
<ul>
<li>
<p>Start a new Ubuntu Linux server instance on Amazon Lightsail.</p>
<ul>
<li>Log in!</li>
<li>Create an instance</li>
<li>Choose an instance image: Ubuntu (OS only)</li>
<li>Choose your instance plan (lowest tier is fine)</li>
<li>Give your instance a hostname</li>
<li>Wait for startup</li>
<li>Once the instance has started up, follow the instructions provided to SSH into your server.</li>
</ul>
</li>
</ul>
</li>
<li>
<p>Secure your server.</p>
<ul>
<li>
<p>Update all currently installed packages.</p>
<pre><code>  sudo apt-get update
  sudo apt-get upgrade
</code></pre>
<p>auto upgrades run
sudo dpkg-reconfigure --priority=low unattended-upgrades</p>
</li>
<li>
<p>Change the SSH port from 22 to 2200. Make sure to configure the Lightsail firewall to allow it.</p>
<pre><code>  sudo nano /etc/ssh/sshd_config
</code></pre>
<p>change port form 22 to 2200</p>
</li>
<li>
<p>Configure the Uncomplicated Firewall (UFW) to only allow incoming connections for SSH (port 2200), HTTP (port 80), and NTP (port 123).</p>
<pre><code>  
  sudo ufw allow SSH
  sudo ufw allow 2200/tcp
  sudo ufw allow HTTP
  sudo ufw allow 80/tcp
  sudo ufw allow NTP
  sudo ufw allow 123/tcp
  sudo ufw enable
</code></pre>
<p>When changing the SSH port, make sure that the firewall is open for port 2200 first, so that you don't lock yourself out of the server. So add Port 2200 after Port 22. When you change the SSH port, the Lightsail instance will no longer be accessible through the web app 'Connect using SSH' button. The button assumes the default port is being used. There are instructions on the same page for connecting from your terminal to the instance.</p>
</li>
</ul>
</li>
<li>
<p>Give grader access.</p>
<p>In order for your project to be reviewed, the grader needs to be able to log in to your server.</p>
<ul>
<li>
<p>Create a new user account named grader.</p>
<pre><code>  sudo adduser grader
</code></pre>
</li>
<li>
<p>Give grader the permission to sudo.</p>
<pre><code>  sudo nano /etc/sudoers.d/grader
</code></pre>
<p>add text <code>grader ALL=(ALL) NOPASSWD:ALL</code></p>
</li>
<li>
<p>Create an SSH key pair for grader using the ssh-keygen tool.</p>
<pre><code>
ssh-keygen -t rsa
Login: ssh -v -i ~/.ssh/udacity_key.pem grader@3.89.185.192
</code></pre>
</li>
</ul>
</li>
<li>
<p>Prepare to deploy your project.</p>
<ul>
<li>
<p>Configure the local timezone to UTC.</p>
<pre><code>  sudo dpkg-reconfigure tzdata
</code></pre>
<ul>
<li>select none of the above, then UTC</li>
</ul>
</li>
<li>
<p>Install and configure Apache to serve a Python mod_wsgi application.</p>
<p>ngnix is used instead of Apache</p>
<ol>
<li>Install Apache and Wsgi</li>
</ol>
<pre><code>sudo apt-get install apache2
sudo apt-get install libapache2-mod-wsgi python-dev
sudo a2enmod wsgi
sudo service apache2 start
</code></pre>
<ol start="2">
<li>Install and set up Git stuff</li>
</ol>
<pre><code>sudo apt-get install git
git config --global user.name [YOUR GIT USERNAME]
git config --global user.email [YOUR GIT EMAIL]
sudo cd /var/www
sudo mkdir catalog
sudo cd catalog
sudo git clone [CLONE URL OF YOUR CATALOG PROJECT ON GITHUB] catalog
</code></pre>
<p></p>
</li>
<li>
<p>Install and configure PostgreSQL:</p>
<pre><code>  sudo apt-get install postgresql
</code></pre>
</li>
</ul>
</li>
<li>
<p>Remote connections must not be allowed</p>
<p>Create a new database user named catalog that has limited permissions to your catalog application database.</p>

</li>
<li>
<p>Deploy the Item Catalog project.</p>
<p><a href="http://3.89.185.192" rel="nofollow">Item Catalog</a></p>
</li>
</ol>
<h3>Resources</h3>
<p><strong>Thanks to these people for their README.md to help guide me through the project</strong> <br>
<a href="https://github.com/stueken/FSND-P5_Linux-Server-Configuration">stueken</a>,
<a href="https://github.com/rrjoson/udacity-linux-server-configuration">rrjoson</a>,
<a href="https://github.com/jessica-hsu/Full-stack-Nanodegree/tree/master/project7">jessica-hsu</a>
</article>