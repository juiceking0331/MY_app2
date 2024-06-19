import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from tkinter.tix import COLUMN

st.title('무슨 일을 하고 싶은가? 🤔')

st.markdown('## 3D 모델러')
con1,con2 = st.columns([0.5,0.5])
con3,con4 = st.columns([0.5,0.5])
con5,con6 = st.columns([0.5,0.5])

with con1:
    st.markdown('### 담당업무')
    st.markdown('소속 크리에이터를 위한 캐릭터, 의상, 헤어 등 모델링 및 리깅')
    st.markdown('오리지널 캐릭터 기획 및 제작')
with con2:
    st.markdown('### 자격요건')
    st.markdown('학업 전공자 또는 관련 업무에 대한 경험')
    st.markdown('버츄얼 방송 및 생태계에 대한 관심과 이해')
with con3:
    st.markdown('### 우대사항')
    st.markdown('방송 플랫폼을 즐겨 보시는 분')
    st.markdown('불규칙한 근무 환경 수행에 지장이 없는 분')
with con4:
    st.markdown('### 근무조건')
    st.markdown('정규직 전환형 계약직')
    st.markdown('주5일 탄력근무')
    st.markdown('연봉 2880만원(포괄 임금제, 연차수당 포함)')
with con5:
    st.markdown('### 복지혜택')
    st.markdown('업무 중 식사 제공')
    st.markdown('특근비')
    st.markdown('야근 시 교통비 지급')
with con6:
    st.markdown('### 전형절차')
    st.markdown('1. 서류전형')
    st.markdown('2. 실무진 면접')
    st.markdown('3. 임원 면접')
    st.markdown('4. 최종합격')