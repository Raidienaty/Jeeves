
apt-installs:
	sudo apt install -y libasound-dev portaudio19-dev libportaudiocpp0

pip-installs:
	pip install -r requirements.txt

install-reqs: apt-installs pip-installs

start:
	python main.py