# アンケートフォームサーバー

アンケートフォームサーバーの実装例です．  
主に，以下のアンケートを実装しています．

- Affective Slider
  - 論文：Betella, A., & Verschure, P. F. (2016). The affective slider: A digital self-assessment scale for the measurement of human emotions. *PloS one, 11*(2), e0148037. https://doi.org/10.1371/journal.pone.0148037
  - リポジトリ：https://github.com/albertobeta/AffectiveSlider
- Godspeed Questionnaire
  - 論文：Bartneck, C., Kulic, D., Croft, E., & Zoghbi, S. (2009). Measurement instruments for the anthropomorphism, animacy, likeability, perceived intelligence, and perceived safety of robots. *International journal of social robotics, 1*(1), 71-81. https://doi.org/10.1007/s12369-008-0001-3
  - 日本語訳：Bartneck, C. (2023). Godspeed Questionnaire Series: Translations and Usage. In C. U. Krägeloh, O. N. Medvedev, & M. Alyami (Eds.), International Handbook of Behavioral Health Assessment (pp. 1-35). Springer. https://doi.org/10.1007/978-3-030-89738-3_24-1
    - https://www.bartneck.de/publications/2023/godspeed/bartneckGodspeedChapter2023.pdf
- The Personal Feelings Questionnaire-2 (PFQ-2)
  - 論文：Harder, D. H., & Zalma, A. (1990). Two promising shame and guilt scales: A construct validity comparison. *Journal of personality assessment, 55*(3-4), 729-745. https://doi.org/10.1080/00223891.1990.9674108
  - 「罪悪感 (Guilt)」のみ使用

## FastAPIのインストール

```zsh
pip install fastapi
```

## サーバー（FastAPI）の起動方法

```zsh
uvicorn app.main:app --reload --host=0.0.0.0 --port=8000
```

ブラウザで `http://localhost:8000` にアクセスしてください．  
タブレット等からアクセスする場合は，サーバーを起動したPCのIPアドレスを確認し， `http://<IP_ADDRESS>:8000` にアクセスしてください．

## データの保存場所

記録されたデータは，サーバーを起動したPCのカレントディレクトリに `questionnaires_result.csv` という名前で保存されます．

> [!CAUTION]
> 参加者IDが `0` の行はテストデータです．分析時には削除してください．

## License

This repository is distributed under the Creative Commons Attribution-ShareAlike 4.0 International License.
See `LICENSE` for details.

The Noto Sans font files included in this repository are not distributed under the Creative Commons Attribution-ShareAlike 4.0 International License.
They are distributed under the SIL Open Font License, Version 1.1.

## Third-party material

This repository includes material derived from Affective Slider.

Original repository: https://github.com/albertobeta/AffectiveSlider  
License: https://creativecommons.org/licenses/by-sa/4.0/

The Affective Slider-derived material has been adapted for use in a questionnaire form server.

## Fonts

This repository includes Noto Sans font files from Google Fonts.

The Noto Sans font files in `app/static/webfonts/Noto_Sans_JP` are distributed under the SIL Open Font License, Version 1.1.

Google Fonts: https://fonts.google.com/noto  
Noto Sans repository: https://github.com/notofonts/NotoSans  
License: https://openfontlicense.org/
