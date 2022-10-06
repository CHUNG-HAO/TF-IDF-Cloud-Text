# tf-idf-python-視覺化
## 前言
我相信很多人喜歡聽歌，但是有沒有想過這些歌手的歌詞都喜歡用些甚麼?我有這個疑問，所以做了這個專案讓各位一看就知道這位歌手主要甚麼單字出現的頻率比較高。

# 架構
<img width="448" alt="image" src="https://user-images.githubusercontent.com/67829896/194298931-a4869fd3-1008-4716-ba0a-1fbbc5bc3fb9.png">

# 詞頻（term frequency，tf）
<img width="506" alt="image" src="https://user-images.githubusercontent.com/67829896/194294119-7558f55d-8554-4065-a790-1a59cc729f21.png">

# 逆向文件頻率（inverse document frequency，idf）

<img width="512" alt="image" src="https://user-images.githubusercontent.com/67829896/194294206-88a72b66-2680-418f-b80c-88730c11e569.png">

## 資料來源
利用網路爬蟲爬取魔鏡歌詞
<img width="344" alt="image" src="https://user-images.githubusercontent.com/67829896/194294299-94df3d38-6df3-49b3-a5f7-1e2d71c9700a.png">

## 存入csv
<img width="722" alt="image" src="https://user-images.githubusercontent.com/67829896/194294500-31f193d6-8560-4f5b-90b2-ff0b7cbdb70f.png">

## 讀取資料集
<img width="373" alt="image" src="https://user-images.githubusercontent.com/67829896/194294657-ba99e494-d384-4173-aa85-8185d9f48b02.png">

## 以jieba套件分詞
<img width="515" alt="image" src="https://user-images.githubusercontent.com/67829896/194294856-a47111c5-389b-4c21-b6ad-4b76d4958cdd.png">

## 統計詞頻
<img width="327" alt="image" src="https://user-images.githubusercontent.com/67829896/194294978-a9e71a1a-1797-45b3-b591-b1fe1338089b.png">

## 統計逆文件頻率
<img width="521" alt="image" src="https://user-images.githubusercontent.com/67829896/194295111-d23f2cf8-330e-4e7b-aca8-5bc7349d2176.png">

## 詞頻X逆文件頻率
<img width="458" alt="image" src="https://user-images.githubusercontent.com/67829896/194295232-82b4e204-c41f-4a63-afb9-4fb12ed6102e.png">

## WordCloud套件視覺化
<img width="648" alt="image" src="https://user-images.githubusercontent.com/67829896/194295502-17473957-f1fa-4839-a5e7-e67b94e81bd1.png">

## 結果
<img width="348" alt="image" src="https://user-images.githubusercontent.com/67829896/194295623-74ee4851-900b-4413-a9eb-566043acc075.png">
<img width="349" alt="image" src="https://user-images.githubusercontent.com/67829896/194295676-0d6db762-0a1f-4a3e-b90b-aab236ab8d30.png">
<img width="349" alt="image" src="https://user-images.githubusercontent.com/67829896/194295719-b7d2a6ba-e795-4dd4-982f-c6ce9c54c71d.png">

