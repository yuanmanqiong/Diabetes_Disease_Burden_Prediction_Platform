import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="糖尿病疾病负担预测平台", page_icon="🧊")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

def change_font(txt, font_size='12px', bold=False):
    font_weight = 'bold' if bold else 'normal'
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('*'), i;
            for (i = 0; i < elements.length; ++i) {{
                if (elements[i].innerText === '{txt}') {{
                    elements[i].style.fontSize = '{font_size}';
                    elements[i].style.fontWeight = '{font_weight}';
                }}
            }}
        </script>
    """
    components.html(htmlstr, height=0, width=0)

@st.cache_data
def get_csv(path):
    csv = pd.read_csv(path)
    return csv

def main():
    button_html = """
        <style>
            .stButton>button {
                background-color: #BEB8DC;
                border: none;
                color: white;
                padding: 20px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 60px !important; 
                margin: 0px;
                cursor: pointer;
                border-radius: 5px;
                width: 106%;
            }
            .stButton>button:hover {
                background-color: #E7EFFA;
                color: black;
            }

    """

    st.markdown(button_html, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        if st.button("📖首页", key="home"):
            navigateTo("home")
        change_font("📖首页", '23px', bold=True)
    with col2:
        if st.button("⌨️数据来源", key="introduction"):
            navigateTo("introduction")
        change_font("⌨️数据来源", '23px', bold=True)
    with col3:
        if st.button("📊现状", key="current"):
            navigateTo("current")
        change_font("📊现状", '23px', bold=True)
    with col4:
        if st.button("📈趋势", key="trends"):
            navigateTo("trends")
        change_font("📈趋势", '23px', bold=True)
    with col5:
        if st.button("⏩预测", key="forecast"):
            navigateTo("forecast")
        change_font("⏩预测", '23px', bold=True)

    selected_page = get_page_from_url()

    if selected_page == "home":
        homepage()
    elif selected_page == "introduction":
        display_introduction()
    elif selected_page == "current":
        display_current_status()
    elif selected_page == "trends":
        display_trends()
    elif selected_page == "forecast":
        display_forecast()
    else:
        homepage()

def navigateTo(page):
    st.query_params["page"] = page

def get_page_from_url():
    query_params = st.query_params
    return query_params.get('page', ['home'])

def homepage():
    st.title("""
            糖尿病疾病负担预测平台
            """)

    st.write("""
    <p style='text-indent: 2em; font-size: 20px; line-height: 2.0;'>
             <strong style='font-size: 24px;'>糖尿病</strong>作为一种营养代谢性疾病，已成为慢性非传染性疾病的重要组成部分，每年全球因此丧生的病例高达<strong>160万</strong><sup>[1]</sup>。
             近年来，随着生活方式的变迁和饮食结构的改变，糖尿病患病率逐年上升，严重危害居民健康，成为当前社会亟待解决的重大公共卫生挑战。预计到2045年，全球将有高达<strong>7.83亿人</strong>受到糖尿病的困扰<sup>[2]</sup>。
             过去30年，我国糖尿病患病率显著上升，2002年患病率首次超过全球平均水平，并在2002－2016年间始终<strong>高于</strong>平均全球水平<sup>[3]</sup>，但该病的知晓率及治愈率仍处于低水平<sup>[4,5]</sup>。
             本平台展示我国糖尿病疾病负担的现状与1900-2021年的发展趋势，并采用<strong>多种预测模型</strong>，预测<strong>不同场景下</strong>我国未来糖尿病疾病负担的发展趋势。
    <p>
    """, unsafe_allow_html=True)

    st.write("""
        <div style='position: fixed;
                    bottom: 0;
                    width: 93%;
                    background-color: #f1f1f1;
                    padding: 5px;
                    border-top: 2px solid #dcdcdc;
                    text-align: left;
                    box-shadow: 0px -0.2px 10px rgba(0, 0, 0, 0.1);'>
            <div style='font-size: 12px; line-height: 1.5;'>
                [1] BUDREVICIUTE A, DAMIATI S, SABIR D K, et al. Management and Prevention Strategies for Non-communicable Diseases (NCDs) and Their Risk Factors [J]. Front Public Health, 2020, 8: 574111.
            </div>
            <div style='font-size: 12px; line-height: 1.5;'>
                [2] SUN H, SAEEDI P, KARURANGA S, et al. IDF Diabetes Atlas: Global, regional and country-level diabetes prevalence estimates for 2021 and projections for 2045 [J]. Diabetes Res Clin Pract, 2022, 183: 109119.
            </div>
            <div style='font-size: 12px; line-height: 1.5;'>
                [3] 曹新西, 徐晨婕, 侯亚冰, et al. 1990—2025年我国高发慢性病的流行趋势及预测 [J]. 中国慢性病预防与控制, 2020, 28(01): 14-9.
            </div>
            <div style='font-size: 12px; line-height: 1.5;'>
                [4] SOCIETY C D. 中国2型糖尿病防治指南（2020年版）（上） [J]. 中国实用内科杂志, 2021, 41(08): 668-95.
            </div>
            <div style='font-size: 12px; line-height: 1.5;'>
                [5] ASSOCIATION D B O C M. 中国2型糖尿病防治指南（2020年版）（下） [J]. 中国实用内科杂志, 2021, 41(09): 757-84.
            </div>
        </div>
        """, unsafe_allow_html=True)

def display_introduction():
    st.title("数据来源基本介绍")
    st.write("""
        <p style='font-size: 20px; line-height: 2.0;'>
        本平台构建的糖尿病疾病负担预测模型，依托多个全球权威性的数据源，包括全球疾病负担（GBD）数据库、世界卫生组织数据库、世界银行数据库，以及非传染性疾病风险因素协作组等，覆盖了全球各地的疾病负担模式和发展趋势，使得预测模型具有较强的代表性和可靠性，能够为我国糖尿病疾病负担提供良好的预测与评估。
        <p>
        """, unsafe_allow_html=True)
    with st.expander("全球疾病负担数据库（Global of Burden Disease，GBD）"):
        st.write("""
        全球疾病负担数据库由美国华盛顿大学健康指标与评估研究所精心打造的，它基于全球众多数据源，运用统一且具备可比性的方法，依据年份、年龄、性别等维度对1990年以来全球204个国家和地区的369种疾病或伤害、87种危险因素的疾病负担数据进行估计和分析。本平台糖尿病疾病负担数据来源于GBD 2021数据库（<a href='https://ghdx.healthdata.org/gbd-2021' target='_blank'>https://ghdx.healthdata.org/gbd-2021</a>），提取1990-2021年全球与中国不同性别、不同年龄组的各项疾病负担指标包括患病率、发病率、伤残调整寿命年（DALY）、伤残减寿年数（YLD）、死亡减寿年数（YLL）。
        """, unsafe_allow_html=True)
    with st.expander("世界卫生组织数据库（the World Health Organization，WHO）"):
        st.write("""
        世界卫生组织数据库汇集了全球卫生领域关键信息和数据的综合资源，涵盖了全球范围内的卫生统计数据、环境与健康信息、疾病负担等多方面内容。
        """)
    with st.expander("世界银行数据库（World Bank Open Data，WBOD）"):
        st.write("""
        世界银行数据库是一个全面、权威的宏观经济数据库，它收录了来自全球各国的统计数据，涵盖了经济、财政、人口、健康、教育等多个方面。
        """)
    with st.expander("非传染性疾病风险因素协作组（NCD Risk Factor Collaboration，NCD-RisC）"):
        st.write("""
        非传染性疾病风险因素协作组致力于及时向全球200个国家和地区提供非传染性疾病（NCD）风险因素方面的数据。\n
        NCD-RisC运用先进的统计方法汇总高质量的基于人群的数据，这些统计方法专门用于分析NCD风险因素。\n
        自1957年以来，NCD-RisC目前已从197个国家收集到超过3300项基于人群的调查数据，有近2亿参与者的风险因素水平已被测量。""")

def display_current_status():
    st.title("基于GBD数据的2021年中国糖尿病疾病负担状况")
    with st.expander("发病情况"):
        st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Current%20Status/%E5%9F%BA%E4%BA%8EGBD%E6%95%B0%E6%8D%AE%E5%BA%93%E7%BB%98%E5%88%B62021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%8C%89%E5%B9%B4%E9%BE%84%E7%BB%84%E3%80%81%E6%80%A7%E5%88%AB%E5%88%92%E5%88%86%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E5%8F%91%E7%97%85%E6%83%85%E5%86%B5%EF%BC%88A-%E5%8F%91%E7%97%85%E6%95%B0%EF%BC%8CB-%E5%8F%91%E7%97%85%E7%8E%87%EF%BC%89.png?raw=true",
                 caption="基于GBD数据库绘制2021年中国按年龄组、性别划分的糖尿病发病情况（A-发病数，B-发病率）")
    with st.expander("死亡情况"):
        st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Current%20Status/%E5%9F%BA%E4%BA%8EGBD%E6%95%B0%E6%8D%AE%E5%BA%93%E7%BB%98%E5%88%B62021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%8C%89%E5%B9%B4%E9%BE%84%E7%BB%84%E3%80%81%E6%80%A7%E5%88%AB%E5%88%92%E5%88%86%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E6%AD%BB%E4%BA%A1%E6%83%85%E5%86%B5%EF%BC%88A-%E6%AD%BB%E4%BA%A1%E6%95%B0%EF%BC%8CB-%E6%AD%BB%E4%BA%A1%E7%8E%87.png?raw=true",
                 caption="基于GBD数据库绘制2021年中国按年龄组、性别划分的糖尿病死亡情况（A-死亡数，B-死亡率）")
    with st.expander("伤残调整寿命年（DALY）情况"):
        st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Current%20Status/%E5%9F%BA%E4%BA%8EGBD%E6%95%B0%E6%8D%AE%E5%BA%93%E7%BB%98%E5%88%B62021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E6%8C%89%E5%B9%B4%E9%BE%84%E7%BB%84%E3%80%81%E6%80%A7%E5%88%AB%E5%88%92%E5%88%86%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E4%BC%A4%E6%AE%8B%E8%B0%83%E6%95%B4%E5%AF%BF%E5%91%BD%E5%B9%B4%EF%BC%88Disability%20Adjusted%20Life%20Years,%20DALY%EF%BC%89%E6%83%85%E5%86%B5%EF%BC%88A-%20DALY%E6%95%B0%EF%BC%8CB-%20DALY%E7%8E%87%EF%BC%89.png?raw=true",
                 caption="基于GBD数据库绘制2021年中国按年龄组、性别划分的糖尿病伤残调整寿命年（Disability Adjusted Life Years, DALY）情况（A- DALY数，B- DALY率）")

def display_trends():
    st.title("基于GBD数据1990-2021年中国糖尿病疾病负担的趋势")
    with st.expander("发病趋势"):
        st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Trends/1990-2021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E7%B3%96%E5%B0%BF%E7%97%85%E7%9A%84%E5%8F%91%E7%97%85%E4%BE%8B%E6%95%B0%E4%B8%8E%E7%9B%B8%E5%BA%94%E7%9A%84%E6%A0%87%E5%8C%96%E7%8E%87%E5%8F%98%E5%8C%96%E8%B6%8B%E5%8A%BF.png?raw=true",
                 caption="1990-2021年中国糖尿病的发病例数与相应的标化率变化趋势（ASIR: age-standardized incident rate; ASMR: age-standardized mortality rate; ASDR: age-standardized DALY rate）")
    with st.expander("死亡趋势"):
        st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Trends/1990-2021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E7%B3%96%E5%B0%BF%E7%97%85%E7%9A%84%E6%AD%BB%E4%BA%A1%E4%BE%8B%E6%95%B0%E4%B8%8E%E7%9B%B8%E5%BA%94%E7%9A%84%E6%A0%87%E5%8C%96%E7%8E%87%E5%8F%98%E5%8C%96%E8%B6%8B%E5%8A%BF.png?raw=true",
                 caption="1990-2021年中国糖尿病的死亡例数与相应的标化率变化趋势\n（ASIR: age-standardized incident rate; ASMR: age-standardized mortality rate; ASDR: age-standardized DALY rate）")
    with st.expander("伤残调整寿命年（DALY）趋势"):
        st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Trends/1990-2021%E5%B9%B4%E4%B8%AD%E5%9B%BD%E7%B3%96%E5%B0%BF%E7%97%85%E7%9A%84DALY%E6%95%B0%E4%B8%8E%E7%9B%B8%E5%BA%94%E7%9A%84%E6%A0%87%E5%8C%96%E7%8E%87%E5%8F%98%E5%8C%96%E8%B6%8B%E5%8A%BF.png?raw=true",
                 caption="1990-2021年中国糖尿病的DALY数与相应的标化率变化趋势（ASIR: age-standardized incident rate; ASMR: age-standardized mortality rate; ASDR: age-standardized DALY rate）")

def display_forecast():
    try:
        st.title("未来糖尿病疾病负担的预测结果")

        selected_indicator = st.selectbox(
                                        "请选择指标",
                                          ["发病率",
                                         "死亡率",
                                         "伤残调整寿命年（Disability Adjusted Life Years, DALY）",
                                         "年龄标化发病率 (age-standardized incident rate, ASIR)",
                                         "年龄标化死亡率(age-standardized mortality rate, ASMR)",
                                         "年龄标化DALY率(age-standardized DALY rate, ASDR)"
                                        ])
        if selected_indicator == "发病率":
            st.write("发病率是指某一人群在一年内新发生糖尿病的频率")
        elif selected_indicator == "死亡率":
            st.write("死亡率是指某人群在一定期间内（通常以年为单位）死于糖尿病的人数在该人群中所占的比例")
        elif selected_indicator == "伤残调整寿命年（Disability Adjusted Life Years, DALY）":
            st.write("衡量从发病到死亡所损失的全部健康寿命年，综合考虑了因早死所致的寿命损失年 (Years of life lost, YLL)和疾病所致伤残引起的健康寿命损失年 (Years lived with disability, YLD)两部分")
        else: pass

        selected_model = st.selectbox("请选择模型", ["ARIMA模型（AutoRegressive Integrated Moving Average Model）",
                                                     "LSTM模型（Long Short Term Memory）",
                                                     "ARIMA-LSTM混合模型",
                                                     "GAMM模型（Generalized Additive Mixed Models, GAMM）"])

        if selected_model == "GAMM模型（Generalized Additive Mixed Models, GAMM）":
            st.write("GAMM是混合效应和相加模型的结合，其中混合模型引入了随机效应反映了不同对象之间的异质性，以及同一对象不同观测之间的相关性。GAMM综合了参数、非参数及随机效应的影响")
            selected_year = st.slider("请选择预测终止年份", 2022, 2040, 2022)

            selected_obese_trend = st.selectbox("请选择成人超重率（BMI ≥ 25kg/m², %）", ["维持2021年不变", "自然发展趋势", "自然发展趋势基础上上升", "自然发展趋势基础上下降"])
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Prediction/%E6%88%90%E4%BA%BA%E8%B6%85%E9%87%8D%E7%8E%87%E5%8F%91%E5%B1%95%E8%B6%8B%E5%8A%BF.png?raw=true",
                         caption="成人超重率（BMI ≥ 25kg/m², %）发展趋势")
            with col2:
                st.write("""
                <p style='font-size: 15px; line-height: 2.0;'>
                \n自然发展趋势：危险因素暴露水平维持过去三十年的平均变化速度，持续演进，未显露出明显的减缓或加剧迹象。（下同）
                <p>
                """, unsafe_allow_html=True)
            if selected_obese_trend == "自然发展趋势基础上上升":
                obese_up_percentage = st.slider("请选择上升百分比", 0, 100, 0, key="obese_up_percentage")
            elif selected_obese_trend == "自然发展趋势基础上下降":
                obese_down_percentage = st.slider("请选择下降百分比", 0, 100, 0, key="obese_down_percentage")

            selected_sdi_trend = st.selectbox("请选择SDI【社会人口指数（Socio-demographic Index, SDI）综合反应了一个国家/地区发展状况，由25岁以下女性的总体生育率、15岁及以上女性的平均教育水平、人均收入等数据综合评估得出】",
                                              ["维持2021年不变", "自然发展趋势", "自然发展趋势基础上上升", "自然发展趋势基础上下降"])
            if selected_sdi_trend == "自然发展趋势基础上上升":
                sdi_percentage = st.slider("请选择上升百分比", 0, 100, 0, key="sdi_up_perccentage")
            elif selected_sdi_trend == "自然发展趋势基础上下降":
                sdi_percentage = st.slider("请选择下降百分比", 0, 100, 0, key="sdi_down_percentage")

            selected_vegan_trend = st.selectbox("请选择人均蔬菜消费量", ["维持2021年不变", "自然发展趋势", "自然发展趋势基础上上升", "自然发展趋势基础上下降"])
            if selected_vegan_trend == "自然发展趋势基础上上升":
                vegan_percentage = st.slider("请选择上升百分比", 0, 100, 0, key="vegan_up_percentage")
            elif selected_vegan_trend == "自然发展趋势基础上下降":
                vegan_percentage = st.slider("请选择下降百分比", 0, 100, 0, key="vegan_down_percentage")

            selected_fruit_trend = st.selectbox("请选择人均水果消费量", ["维持2021年不变", "自然发展趋势", "自然发展趋势基础上上升", "自然发展趋势基础上下降"])
            if selected_fruit_trend == "自然发展趋势基础上上升":
                fruit_percentage = st.slider("请选择上升百分比", 0, 100, 0, key="fruit_up_percentage")
            elif selected_fruit_trend == "自然发展趋势基础上下降":
                fruit_percentage = st.slider("请选择下降百分比", 0, 100, 0, key="fruit_down_percentage")

            selected_meat_trend = st.selectbox("请选择人均红肉消费量", ["维持2021年不变", "自然发展趋势", "自然发展趋势基础上上升", "自然发展趋势基础上下降"])
            if selected_meat_trend == "自然发展趋势基础上上升":
                meat_percentage = st.slider("请选择上升百分比", 0, 100, 0, key="mean_up_percentage")
            elif selected_meat_trend == "自然发展趋势基础上下降":
                meat_percentage = st.slider("请选择下降百分比", 0, 100, 0, key="meat_down_percentage")

        elif selected_model == "ARIMA模型（AutoRegressive Integrated Moving Average Model）":
            st.write("ARIMA是一种基于随机理论的时间序列分析方法，通过整合自回归（AR）、差分（I）和移动平均（MA）三个成分，能够有效捕捉时间序列数据中的线性关系和趋势变化")
            selected_year = st.slider("请选择预测终止年份", 2022, 2040, 2022)
        elif selected_model == "LSTM模型（Long Short Term Memory）":
            st.write("LSTM是一种递归神经网络（RNN）的变体，它在处理长序列数据时，能够有效地解决标准 RNN 的梯度消失问题。相比于普通的神经网络，LSTM 模型引入了三个门控单元，即输入门、遗忘门和输出门，来控制信息的输入、输出和遗忘")
            selected_year = st.slider("请选择预测终止年份", 2022, 2040, 2022)
        elif selected_model == "ARIMA-LSTM混合模型":
            st.write("ARIMA-LSTM是一种结合了ARIMA和LSTM两种时间序列预测方法的技术。该模型利用ARIMA模型提取原始序列数据的线性特征，将ARIMA模型预测值与实际值之间的残差输入LSTM模型进行残差预测提取非线性特征。将线性部分和非线性部分结合起来，得到ARIMA-LSTM混合模型的预测结果")
            selected_year = st.slider("请选择预测终止年份", 2022, 2040, 2022)

        tab1, tab2 = st.tabs(["📈 预测结果可视化", "📅 显示预测数据"])

        with tab1:
            tab1.subheader("预测结果可视化")
            if selected_model == "GAMM模型（Generalized Additive Mixed Models, GAMM）":
                st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Prediction/%E5%9F%BA%E4%BA%8EGAMM%E6%A8%A1%E5%9E%8B%E6%8B%9F%E5%90%88%E7%9A%84SDI%E3%80%81%E6%88%90%E4%BA%BA%E8%B6%85%E9%87%8D%E7%8E%87%E4%B8%8E%E5%8F%91%E7%97%85%E7%8E%87%E9%97%B4%E7%9A%84%E6%9C%89%E6%95%88%E8%87%AA%E7%94%B1%E5%BA%A6.png?raw=true",
                         caption="基于GAMM模型拟合的SDI、成人超重率与发病率间的有效自由度")
                st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Prediction/%E5%9F%BA%E4%BA%8EGAMM%E6%A8%A1%E5%9E%8B%E9%A2%84%E6%B5%8B%E6%88%90%E4%BA%BA%E8%B6%85%E9%87%8D%E7%8E%87%E4%B8%8D%E5%90%8C%E5%8F%91%E5%B1%95%E5%9C%BA%E6%99%AF%E4%B8%8B%E4%B8%AD%E5%9B%BD%E7%B3%96%E5%B0%BF%E7%97%852022-2040%E5%B9%B4ASIR%E7%9A%84%E5%8F%91%E5%B1%95%E8%B6%8B%E5%8A%BF.png?raw=true",
                         caption="基于GAMM模型预测成人超重率不同发展场景下中国糖尿病2022-2040年ASIR的发展趋势（ASIR: age-standardized incident rate，年龄标化发病率）")
            elif selected_model == "ARIMA模型（AutoRegressive Integrated Moving Average Model）":
                st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Prediction/1990-2021%E5%B9%B4%E5%9F%BA%E4%BA%8EARIMA%E6%A8%A1%E5%9E%8B%E6%8B%9F%E5%90%88%E4%B8%AD%E5%9B%BD%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87.png?raw=true",
                         caption="1990-2021年基于ARIMA模型拟合中国糖尿病年龄标化发病率")
                st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Prediction/%E5%9F%BA%E4%BA%8EARIMA%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%9C%AA%E6%9D%A52022-2040%E5%B9%B4%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87%E9%A2%84%E6%B5%8B.png?raw=true",
                         caption="基于ARIMA模型对未来2022-2040年的糖尿病年龄标化发病率预测")
            elif selected_model == "LSTM模型（Long Short Term Memory）":
                st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Prediction/1990-2021%E5%B9%B4%E5%9F%BA%E4%BA%8ELSTM%E6%A8%A1%E5%9E%8B%E6%8B%9F%E5%90%88%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87.png?raw=true",
                         caption="1990-2021年基于LSTM模型拟合糖尿病年龄标化发病率")
                st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Prediction/%E5%9F%BA%E4%BA%8ELSTM%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%9C%AA%E6%9D%A52022-2040%E5%B9%B4%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87%E9%A2%84%E6%B5%8B.png?raw=true",
                         caption="基于LSTM模型对未来2022-2040年的糖尿病年龄标化发病率预测")
            else:
                st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Prediction/1990-2021%E5%B9%B4%E5%9F%BA%E4%BA%8EARIMA-LSTM%E6%B7%B7%E5%90%88%E6%A8%A1%E5%9E%8B%E5%90%88%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87.png?raw=true",
                         caption="1990-2021年基于ARIMA-LSTM混合模型合糖尿病年龄标化发病率")
                st.image(r"https://github.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/blob/main/images/Prediction/%E5%9F%BA%E4%BA%8EARIMA-LSTM%E6%B7%B7%E5%90%88%E6%A8%A1%E5%9E%8B%E5%AF%B9%E6%9C%AA%E6%9D%A52022-2040%E5%B9%B4%E7%9A%84%E7%B3%96%E5%B0%BF%E7%97%85%E5%B9%B4%E9%BE%84%E6%A0%87%E5%8C%96%E5%8F%91%E7%97%85%E7%8E%87%E9%A2%84%E6%B5%8B.png?raw=true",
                         caption="基于ARIMA-LSTM混合模型对未来2022-2040年的糖尿病年龄标化发病率预测")

        with tab2.container():
            tab2.subheader("预测数据")
            result_path = 'https://raw.githubusercontent.com/yuanmanqiong/China_Diabetes_Disease_Burden_Prediction_Platform/main/result.csv'
            result = get_csv(result_path)
            tab2.dataframe(result)
            result_csv = result.to_csv(index=False)
            tab2.download_button(label='下载数据（.csv）', data=result_csv, file_name='prediction_result.csv', mime="text/csv")
            
    except Exception as e:
        st.error("Oops! 发生了未知错误")


if __name__ == "__main__":
    main()
