# Full_Stack_Nano

<h2>Project 5: Build an Item Catalog Application</h2>
</br>
<p><strong>Project Description</strong> (from Udacity):</p>
<blockquote>
<p>You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.</p>
</blockquote>
<h4>Environment Set up</h4>
<p>Make sure you have Git installed. If not, download <a href="https://git-scm.com/downloads" rel="nofollow">here</a> <br>
Download and install the correct version of <a href="https://www.vagrantup.com/downloads.html" rel="nofollow">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Downloads" rel="nofollow">VirtualBox</a> for your operating system <br>
Fork this directory and copy the newly forked repository path with clone <br>
From terminal:</p>
<pre><code>bash-3.2$ git clone PASTE_COPIED_REPO_LINK_HERE fullstack
</code></pre>
<p>Download application.py, database_populate.py, database_setup.py, static, and templates from this repository <br>
Copy these 3 files to the fullstack/catalog directory created from the git clone command</p>
<h4> To Run Program</h4>
<p>Open terminal and change directory to the cloned fullstack directory:</p>
<pre><code>bash-3.2$ cd FULL_PATH_TO_NEWLY_CLONED_DIRECTORY
</code></pre>
<p>Use the ls command to see 2 files and 1 directory: CODEOWNERS, README.md, vagrant. Change directory to the catalog directory in the vagrant folder:</p>
<pre><code>bash-3.2$ ls CODEOWNERS    README.md     vagrant
bash-3.2$ cd vagrant/catalog
</code></pre>
<p>Launch virtual machine:</p>
<pre><code>bash-3.2$ vagrant up
</code></pre>
<p>Log in the virtual machine:</p>
<pre><code>bash-3.2$ vagrant sh
vagrant@vagrant:~$
</code></pre>
<p>Change directory to correct folder</p>
<pre><code>vagrant@vagrant:~$ cd ../../vagrant/catalog
</code></pre>
<p>Install external python library required for script</p>
<pre><code>vagrant@vagrant:~$ sudo pip install flask_oauth
</code></pre>
<p>Setup &amp; populate database</p>
<pre><code>vagrant@vagrant:~$ python database_setup.py
vagrant@vagrant:~$ python gaming_consolez.py
</code></pre>
<p>Run program</p>
<pre><code>vagrant@vagrant:~$ python project.py
</code></pre>
