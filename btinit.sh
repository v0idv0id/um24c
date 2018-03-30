hciconfig hci0 up
MAC=`hcitool scan | grep -i UM24 | awk '{print $1}'`
echo "Found: "${MAC}
rfcomm connect hci0 ${MAC} 

