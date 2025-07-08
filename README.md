# whisper_page
使用 OpenAI 的 whisper 建立一個本地端運行的產生逐字稿工具
程式本體完全由 ChatGPT 完成，因此請勿發 issues，請自行洽詢 ChatGPT

#安裝方式 搭配 WSL2 Ubuntu22.04<br>
#安裝 python3 & pip<br>
sudo apt upgrade<br>
sudo apt install python3 python3-pip<br>

#移除可能存在的同名套件<br>
sudo apt remove whisper<br>
sudo pip uninstall whisper<br>

#安裝依賴<br>
sudo pip install -U flask openai-whisper<br>

#檢查是否可運行<br>
whisper --help<br>

#如果需要提供他人存取, 要修改 conv.py 最後一行<br>
#app.run(debug=True, host='0.0.0.0', port=5000)<br>

#將檔案(conv.py)放到家目錄並執行<br>
python3 conv.py<br>

#測試看看<br>
#http://localhost:5000<br>

