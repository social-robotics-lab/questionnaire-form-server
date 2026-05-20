from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
import csv
import os
import pandas as pd
from pprint import pprint


app = FastAPI()
app.mount('/static', StaticFiles(directory='app/static'), name='static')
templates = Jinja2Templates(directory='app/templates')


# 情報記入画面
@app.get('/')
async def quest_index(request: Request):
    return templates.TemplateResponse('index.html', {'request': request})

# アンケート画面
@app.get('/survey')
async def quest_survey(request: Request):
    return templates.TemplateResponse('survey.html', {'request': request})


# CSVヘッダー
header = [
    'participant_id', 'condition_id',
    'AS-arousal', 'AS-pleasure',
    'godspeed_anthropo_natural', 'godspeed_anthropo_humanlike', 'godspeed_anthropo_conscious', 'godspeed_anthropo_lifelike', 'godspeed_anthropo_elegantly',
    'godspeed_animacy_alive', 'godspeed_animacy_lively', 'godspeed_animacy_organic', 'godspeed_animacy_lifelike', 'godspeed_animacy_interactive', 'godspeed_animacy_responsive',
    'godspeed_likability_like', 'godspeed_likability_friendly', 'godspeed_likability_kind', 'godspeed_likability_pleasant', 'godspeed_likability_nice',
    'godspeed_intelligence_competent', 'godspeed_intelligence_knowledgeable', 'godspeed_intelligence_responsible', 'godspeed_intelligence_intelligent', 'godspeed_intelligence_sensible',
    'godspeed_safety_relaxed', 'godspeed_safety_calm', 'godspeed_safety_surprised',
    'pfq2_mild_guilt', 'pfq2_worry', 'pfq2_intense_guilt', 'pfq2_regret', 'pfq2_criticism', 'pfq2_remorse',
    'timestamp',
]

# 提出完了画面
@app.post('/submit')
async def quest_submit(request: Request):
    form_data = await request.form()  # 全てのフォームデータを取得
    data_dict = dict(form_data)       # MutableMapping -> dict に変換

    # タイムスタンプを追加
    data_dict['timestamp'] = datetime.now().isoformat()

    pprint(data_dict, compact=True, sort_dicts=False)  # デバッグ用にコンソールに出力

    DATA_FILE = 'questionnaires_result.csv'
    file_exists = os.path.isfile(DATA_FILE)
    with open(DATA_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, header)

        # 最初のデータ書き込み時のみヘッダーを追加
        if not file_exists:
            writer.writeheader()  # ヘッダーを書き込む

        writer.writerow(data_dict)  # データを書き込む

    return templates.TemplateResponse('submit.html', {'request': request})
