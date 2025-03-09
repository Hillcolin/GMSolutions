Installation
Follow these steps to install the required packages on your Raspberry Pi:

Update and upgrade your Raspberry Pi OS:

sudo apt update
sudo apt upgrade -y
Install Python and Flask:

sudo apt install python3 python3-flask
Install additional required Python packages:

pip3 install flask-login flask-sqlalchemy waitress
Setting Up the Project
Create a Project Directory:
Navigate to the desired location and create a directory for your project:

mkdir ~/flask_project
cd ~/flask_project
Set Environment Variable:
Define the PYTHONPATH for your project:

export PYTHONPATH="/home/pi/flask_project"
Run the Flask Application:
Assuming your main script is named main.py, run it using:

python3 main.py
Connecting to the Server
Use ifconfig or hostname -I to find your Raspberry Pi's IP address.

Access the Flask server in a browser using the format:

http://<your-ip-address>:5000

can get your ip address by doing ipconfig in terminal and getting the first IPv4

Both Space and Time Complexity of the frontend it O(1)