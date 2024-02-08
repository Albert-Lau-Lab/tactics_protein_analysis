apt-get update
apt-get install -y python3-pip
pip install Cython --install-option="--no-cython-compile"
pip install numpy==1.19.5
pip install scikit-learn==0.21.2
pip install mdanalysis==2.2.0
pip install pandas==1.4.4

apt-get install -y openbabel

mkdir /software_installation
cd /software_installation
apt-get install -y wget
wget https://vina.scripps.edu/wp-content/uploads/sites/55/2020/12/autodock_vina_1_1_2_linux_x86.tgz
tar xzvf autodock_vina_1_1_2_linux_x86.tgz
echo 'export PATH=/software_installation/autodock_vina_1_1_2_linux_x86/bin/:$PATH' >> ~/.bashrc

mv /tactics_docker_dir/vmd-*.tar* .
tar -xvf vmd-*.tar*
cd vmd-*
./configure
cd src/
apt-get install -y make
make install
cd ../..

apt-get install concavity

wget https://ccsb.scripps.edu/download/532/
tar -xzvf index.html
cd mgltools*/
./install.sh
cd ..

cd /tactics_docker_dir
mkdir tactics_protein_analysis
cd tactics_protein_analysis
