import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title('왜 하필 패러블인가? 🤔')

st.write('# 패러블 엔터테인먼트만의 특징')
st.write('# 메타버스 사업')

st.markdown('### 국내 최대 메타버스 공연, 이세계 페스티벌 개최')
img2 = Image.open('./images/ifes.webp')
img3 = Image.open('./images/dron.jpeg')
img4 = Image.open('./images/ifes2.jpg')


tab1, tab2= st.tabs(['이세계 페스티벌이란?' , '이세계 페스티벌 현장 사진'])

with tab1:
    st.write('현실과 가상세계가 음악을 통해 연결되는 한국 최초 메타버스 연계 오프라인 뮤직 페스티벌')
    st.write('현실 아티스트는 무대 위에서, 가상 아티스트는 대형 스크린을 통해 공연')
    st.write('인천경제자유구역청, LG전자, 한국콘텐츠진흥원의 지원을 받아 진행')
    st.write('20000여명의 관객을 동원하며 성공적으로 유치')

with tab2:
    button = st.button('사진 열람')
    if button:
     st.image(img2)
     st.image(img3)
     st.image(img4)


st.markdown('### VR 기기, 모션캡쳐 스튜디오 등 메타버스 장비 보유')

st.markdown('### 버츄얼 유튜버의 단독 오프라인 콘서트 개최 예정')

st.markdown('### 대한민국에서 가장 대중적이고 앞서가는 메타버스 기업')