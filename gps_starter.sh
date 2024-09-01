#!/bin/bash

# Enable serial interface in raspi-config
echo "Enabling serial interface..."
sudo raspi-config nonint do_serial 2

# Stop gpsd service to reconfigure
echo "Stopping gpsd service..."
sudo systemctl stop gpsd.socket
sudo systemctl stop gpsd

# Configure gpsd to use /dev/serial0
echo "Configuring gpsd to use /dev/serial0..."
sudo bash -c 'cat << EOF > /etc/default/gpsd
# Default settings for gpsd
START_DAEMON="true"
GPSD_OPTIONS="-n"
DEVICES="/dev/serial0"
GPSD_SOCKET="/var/run/gpsd.sock"
EOF'

# Restart gpsd service with new configuration
echo "Restarting gpsd service..."
sudo systemctl start gpsd.socket
sudo systemctl enable gpsd.socket

# Test gpsd connection
echo "Testing GPS connection with cgps..."
cgps -s

echo "GPS setup complete. If cgps shows GPS data, you're good to go!"
