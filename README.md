# 全球對台道安資訊地圖

Leaflet 製作的互動式世界地圖，蒐羅世界各國對於台灣交通安全的相關資訊，並與各國自身交通事故死亡率搭配。

## 螢幕截圖

![map screenshot](/data/screenshots/01.png)

## 作者

- [@FOBshippingpoint](https://www.github.com/FOBshippingpoint)

## 進度

- [x] reputation data creator (toJSON) in python
- [x] 決定地圖上的顏色代表什麼，reputation or death_rate
- [x] 決定資訊要放在在 popcontent or custom control
- [ ] 增加各國的對台交通資訊，目前只有加拿大、美國、澳洲、日本
- [ ] 增進翻譯品質，目前統一由 Google 翻譯
- [ ] 字太多怎麼辦？好像沒有 scrollbar
- [ ] 美化 leaflet custom control 區塊(div.info)
- [ ] 決定要不要繼續用 sveltekit，現階段根本沒用到

## 新增國家

1. 開啟[全球對台道安聲望試算表](https://docs.google.com/spreadsheets/d/10wiipUnJaQVOlCr5W_gl_t3MUNgUh6FKS79rZg6ROE0/edit#gid=0)，裡面有六個欄位：
```text
ADM0_A3: ISO_A3國碼
country: 中文國名，方便自己看的（未顯示）
reputation: 對台道安聲望，目前不知道怎麼定（未顯示）
original_text: 對台道安資訊原文
translated_text: 對台道安資訊譯文
reference: 資訊出處
```
2. 搜尋欲新增國家的ISO 3166-1 alpha-3的國碼並填入ADM0_A3欄
3. 尋找該國政府或可靠機構所提供的臺灣旅遊相關資訊填入網址至reference
4. 在originalText填入對「交通安全」相關的原文資訊
5. 在translatedText填入Google翻譯產生的文字（如果願意自行翻譯，請在後面該欄最末註記）

---

# countries geojson

https://github.com/AshKyd/geojson-regions

# Leaflet

[Interactive Choropleth Map - Leaflet - a JavaScript library for interactive maps](https://leafletjs.com/examples/choropleth/)

# collecting reputation data

- [[爆卦] 美英澳加日政府:台灣旅遊須知 交通安全篇 - 看板 Gossiping - 批踢踢實業坊](https://www.ptt.cc/bbs/Gossiping/M.1670471598.A.F23.html)
- [[問卦] 日本人：台灣交通超爛，想去觀光前應三思 - 看板 Gossiping - 批踢踢實業坊](https://www.ptt.cc/bbs/Gossiping/M.1637150397.A.2AF.html)
- [[爆卦] 歐洲國民：台灣旅遊須知 交通安全篇 - 看板 Gossiping - 批踢踢實業坊](https://www.ptt.cc/bbs/Gossiping/M.1637150397.A.2AF.html)

~~以 ISO_A3 為標準（3 碼）~~
以 ADM0_A3 為標準，see [ISO 3166-1 alpha-3](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3)

[WHO | Estimated road traffic death rate (per 100 000 population)](<https://www.who.int/data/gho/data/indicators/indicator-details/GHO/estimated-road-traffic-death-rate-(per-100-000-population)>)

# 各國對台道安資訊欄位

```text
ADM0_A3: ISO_A3國碼
reputation: 對台道安聲望，目前不知道怎麼定
original_text: 對台道安資訊原文
translated_text: 對台道安資訊譯文
reference: 資訊出處
death_rate: WHO交通事故死亡率
```

# Other

法國不知道為什麼 geojson 的 ISO_A3 是-99，挪威也是

或許要用 ADM0_A3？
