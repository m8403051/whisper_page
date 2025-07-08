# whisper_page
使用 OpenAI 的 whisper 建立一個本地端運行的產生逐字稿工具
程式本體完全由 ChatGPT 完成，因此請勿發 issues，請自行洽詢 ChatGPT

# 安裝方式 搭配 WSL2 Ubuntu22.04
# 安裝 python3 & pip
sudo apt upgrade
sudo apt install python3 python3-pip

# 移除可能存在的同名套件
sudo apt remove whisper
sudo pip uninstall whisper

# 安裝依賴
sudo pip install -U flask openai-whisper

# 檢查是否可運行
whisper --help

# 如果需要提供他人存取, 要修改最後一行
#app.run(debug=True, host='0.0.0.0', port=5000)

# 將檔案(conv.py)放到家目錄並執行
python3 conv.py

# http://localhost:5000
# 測試看看
