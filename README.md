## Background Removal
> **Note**<br>
> Quantized U2-Net Pre-trained from [Kikedao](https://github.com/xuebinqin/U-2-Net/issues/295).<br>
> Original [U2-Net repo](https://github.com/xuebinqin/U-2-Net) and [paper](https://github.com/xuebinqin/U-2-Net).

Clone the repo : 
```bash
git clone https://github.com/drmwnrafi/background_removal.git
```
> **Warning**<br>
> This app cannot work properly with conda virtual environment.

Make a new python virtual environment (optional) :
```bash
python -m venv bg_erase
source bg_erase/bin/activate  # For Mac or Linux
bg_erase\Scripts\activate  # For Windows
```
Install all dependencies :
```bash
cd background_removal
pip install -r requirements.txt
```
Run the app : 
```bash
python app.py
```
Image with no background store in <code>/background_removal/outputs</code> directory.

![image](https://github.com/drmwnrafi/background_removal/assets/115781654/ce65e49e-6da7-41f4-9566-47587138acdf)
