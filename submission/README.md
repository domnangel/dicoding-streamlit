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
streamlit run "C:\Users\Sheila\Documents\SMK\PKL\DB Dicoding\submission\dashboard\dashboard.py"