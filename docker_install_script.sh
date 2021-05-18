apt-get update
apt-get install -y python3-pip
pip install Cython --install-option="--no-cython-compile"
pip install scikit-learn==0.21.2
pip3 install pandas
pip install mdanalysis

apt-get install -y openbabel

mkdir /software_installation
cd /software_installation
apt-get install -y wget
wget http://vina.scripps.edu/download/autodock_vina_1_1_2_linux_x86.tgz
tar xzvf autodock_vina_1_1_2_linux_x86.tgz
echo 'export PATH=/software_installation/autodock_vina_1_1_2_linux_x86/bin/:$PATH' >> ~/.bashrc

mv /tactics_docker_dir/vmd-*.tar.gz .
tar -xzvf vmd-*.tar.gz
cd vmd-*
./configure
cd src/
apt-get install -y make
make install
cd ../..

wget https://compbio.cs.princeton.edu/concavity/concavity_distr.tar.gz
tar -xzvf concavity_distr.tar.gz
cd concavity_distr
apt-get install -y gcc
apt-get install -y g++
apt-get install -y freeglut3-dev
apt-get install -y libxxf86vm-dev
make clean; make
echo 'export PATH=/software_installation/concavity_distr/bin/x86_64/:$PATH' >> ~/.bashrc
cd ..

wget https://ccsb.scripps.edu/download/532/
tar -xzvf index.html
cd mgltools*/
./install.sh
cd ..

cd /tactics_docker_dir
mkdir tactics_protein_analysis
cd tactics_protein_analysis
