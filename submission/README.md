# SETUP ENVIRONMENT 

## Membuat Virtual Environment
conda create --name dicoding-ds python=3.9

## Menambahkan Env ke Jupyter Notebook
conda install -c conda-forge nb_conda_kernels

## Mengaktifkan Virtual Environment
conda activate dicoding-ds

## Install Library yang Dibutuhkan
pip install numpy pandas matplotlib seaborn jupyter streamlit

## Menjalankan Streamlit
- Klik kanan pada file dashboard.py, pilih "Copy as path"
- Buka cmd, lalu ketikan: streamlit run "path\to\file\dashboard.py"
note: "path\to\file\dashboard.py" merupakan path yang sebelumnya sudah dicopy

## Menjalankan Streamlit di Streamlit Cloud
https://dashboardpy-bn5kksqsujxdxsptx4nejg.streamlit.app/
