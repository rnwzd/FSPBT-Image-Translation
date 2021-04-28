# download from
# https://drive.google.com/file/d/1WI71nYP-z0mfDpuUW36s3sswpwRwwfrN/view
# and unzip in the data folder

mkdir -p data
cd data

fileId=1WI71nYP-z0mfDpuUW36s3sswpwRwwfrN
fileName=webcam.zip
curl -sc /tmp/cookie "https://drive.google.com/uc?export=download&id=${fileId}" > /dev/null
code="$(awk '/_warning_/ {print $NF}' /tmp/cookie)"  
curl -Lb /tmp/cookie "https://drive.google.com/uc?export=download&confirm=${code}&id=${fileId}" -o ${fileName} 
unzip $fileName