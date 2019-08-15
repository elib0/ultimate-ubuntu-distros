
rm /tmp/vscode-stable_current_amd64.deb

echo "downloading Visual Studio Code latest stable edition"
wget https://az764295.vo.msecnd.net/stable/2213894ea0415ee8c85c5eea0d0ff81ecc191529/code_1.36.1-1562627527_amd64.deb -O /tmp/vscode-stable_current_amd64.deb
sudo dpkg -i /tmp/vscode-stable_current_amd64.deb

rm /tmp/vscode-stable_current_amd64.deb

echo "################################################################"
echo "#################  Visual Studio Code installed ################"
echo "################################################################"
