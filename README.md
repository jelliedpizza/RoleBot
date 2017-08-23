# RoleBot: an open source bot whose sole purpose is role management (Proof of concept)


## **Requirements:**

### **A discord application**:
Create an application [here.](https://discordapp.com/developers/applications/me)
Give it a name and a picture (you can change these later).
And then create a bot account.
When you do you recive a token which you should never share with anyone else. That token authorizes code to interact with the bot account.
You will need the token later.


### **The newest python 3.6** is recommended but anything above python 3.5 will do:
[Download here](https://www.python.org/downloads/release) (Don't forget to check "python launcher" and "Add to PATH" when installing under Windows and macOS *and you can build it yourself  for if you want to for Linux.*  
[How to install it on Linux (The easy way)](https://packaging.python.org/guides/installing-using-linux-tools/) (Remember: Python 3)


### **dicord py, asyncio and urllib3**:
Open your preferred terminal interface (Could be Command Prompt, PowerShell or a Unix Terminal) and type:
```python
pip install discord.py asyncio urllib3
```

### **Git**:
For Windows http://git-scm.com/download/win  
For macOS http://git-scm.com/download/mac  
And if you are using linux you probably have it alredy


### **The bot itself**:
Go to the directory you want to donwload the bot to and type:
```bash
git clone https://github.com/jelliedpizza/RoleBot.git
```
*Alternatively you can click [here](https://github.com/jelliedpizza/RoleBot/archive/master.zip)*



## **Configuring and Running:**

### **The config file**:
Open up `config.json`   
Replace YOURID with your dicord ID for the bot to identify you
> Go to `User Settings` (bottom left gear icon) -> `Appearance` -> Enable `Developer Mode`  
> Right click on your name in any message and copy ID and paste it in inside the qutes  

Remember step one? Now enter your token inside the quotes from your discord applications.  
You can delete everythong from the squar brackets just remember the syntax if you want to load plugins on startup.  
Edit the prefix inside the quotes you to your liking (this what you write before commands to call them).

### **Understanding the plugin system**:
If you run `brain.py` it will give you a link that you can use to invite the bot to your server but it only responds to the built-in commands.  
This is because it doesn't have any plugins loaded in.  
Each plugin you generate contains a command that you can call after loading the plugin from the `plugins` folder with [p]plug (pluginname) *[p] is your prefix that you set in `config.json`*  
After loading a plugin you can do [p]help to see what plugins you have loaded and what are the commands that initiate those plugins. (The description of the plugin is always the message that the bot sends.)  

### **Creating plugins**:
Open up ``plugin_generator/plugin_generator.py``  
Follow the instructions  
Copy the generated plugin to the plugins folder
(Optional) Add `pluginname.py` to the startup plugins in the `config.json`

### **Running the bot**
If you are just testing open `brain.py` and enter the link in a browser to invite the bot to a server  
> but if you are running it on a windows/linux server click autorespawn .sh or .bat respectively and if it crashes, it will respawn the proces

### **Using a plugin with the bot**
There are some test plugins, feel free to delete them.  

I'm going to refer to your prefix as `[p]`  
Type `[p]plug pluginname-that's-in-the-plugins-folder` to load the plugin then  
Type `[p]commandname`: this will delete your message and execute the plugin in the current channel  




## **(Optional) How to set it up on a Linux server:**

1. Installl screen with your package managar (e.g.: Ubuntu: `sudo apt-get isntall screen`)
1. Type `screen` than press RETURN OR SPACE
1. Go to the directory that `autorespawn.sh` is in
1. Type ``chmod u+x script.sh`` to make the script runnable
1. Type `./autorespawn.sh` to run  

And your done. Now you can press `CTRL + a` then `d` to detach and then it's running in the backround. To reatach pres `CTRL + a` then `r` or if it did not detach properly press `CTRL + a` then `x`. 



## **Troubleshoothing:**

> T: The window immediatly desappears or it says that it doesn't have a module or autorespawn loops and does not work  
> A: Check your python version (Your python 3 should be 3.5.x or 3.6.x) and check if you have all the requirements  

Support server https://discord.gg/tQjbKu
