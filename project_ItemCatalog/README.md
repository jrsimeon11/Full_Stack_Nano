# Full_Stack_Nano

<h2>Project Part 4: Build an Item Catalog Application</h2>
</br>
<p><strong>Project Description</strong> (from Udacity):</p>
<blockquote>
<p>You will develop an application that provides a list of items within a variety of categories as well as provide a user registration and authentication system. Registered users will have the ability to post, edit and delete their own items.</p>
</blockquote>
<h4>Environment Set up</h4>
<p>Make sure you have Git installed. If not, download <a href="https://git-scm.com/downloads" rel="nofollow">here</a> <br>
Download and install the correct version of <a href="https://www.vagrantup.com/downloads.html" rel="nofollow">Vagrant</a> and <a href="https://www.virtualbox.org/wiki/Downloads" rel="nofollow">VirtualBox</a> for your operating system <br>
Fork this directory and copy the newly forked repository path with clone <br>
From the terminal:</p>
<pre><code>jrene@JRSimUI MINGw64 $ git clone "PASTE_THE_COPIED_REPOSITORY_LINK_HERE" fullstack
</code></pre>
<p>Download project.py, gaming_console.py, database_setup.py, client_secrets.json, fb_client_secrets.json, static, and templates from this repository <br>
Copy these 3 files to the fullstack/catalog directory created from the git clone command</p>
<h4> To Run Program</h4>
<p>Open terminal and change directory to the cloned fullstack directory:</p>
<pre><code>jrene@JRSimUI MINGw64 $ cd "FULL_PATH_TO_THE_CLONED_DIRECTORY"
</code></pre>
<p>Use the ls command to see 2 files and 1 directory: CODEOWNERS, README.md, vagrant. Change directory to the catalog directory in the vagrant folder:</p>
<pre><code>jrene@JRSimUI MINGw64 $ ls CODEOWNERS    README.md     vagrant
jrene@JRSimUI MINGw64 $ cd vagrant/ItemCatalogProject
</code></pre>
<p>Launch virtual machine:</p>
<pre><code>jrene@JRSimUI MINGw64 $ vagrant up
</code></pre>
<p>Log in the virtual machine:</p>
<pre><code>jrene@JRSimUI MINGw64 $ vagrant ssh
vagrant@vagrant:~$
</code></pre>
<p>Change directory to correct folder</p>
<pre><code>vagrant@vagrant:~$ cd /vagrant/ItemCatalogProject
</code></pre>
<p>Install external python library required for script</p>
<pre><code>vagrant@vagrant:~$ sudo pip install flask
vagrant@vagrant:~$ sudo pip install flask_oauth
</code></pre>
<p>Setup &amp; add data to the database</p>
<pre><code>vagrant@vagrant:~$ python database_setup.py
vagrant@vagrant:~$ python database_games.py
</code></pre>
<p>Run the program</p>
<pre><code>vagrant@vagrant:~$ python app.py
</code></pre>
