import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="بطاقة تفاعلية - IF / ELSE", page_icon="📝", layout="centered")

# تنسيق CSS لمطابقة التصميم الأصلي للصورة تماماً
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800&display=swap');

    /* خلفية الصفحة مع مربعات دفتر الرسم */
    .stApp {
        background-color: #f9f7f2;
        background-image: 
            linear-gradient(#e5e0d5 1.5px, transparent 1.5px),
            linear-gradient(90deg, #e5e0d5 1.5px, transparent 1.5px);
        background-size: 35px 35px;
        font-family: 'Cairo', sans-serif;
    }

    /* إخفاء شريط Streamlit العلوي الافتراضي */
    header {visibility: hidden;}
    
    /* صندوق السؤال الرئيسي */
    .question-wrapper {
        position: relative;
        max-width: 480px;
        margin: 10px auto 0 auto;
        text-align: center;
    }
    .pink-cap-top {
        background-color: #f4a4a4;
        border: 2.5px solid #2b3446;
        border-bottom: none;
        width: 110px;
        height: 14px;
        margin: 0 auto;
        border-radius: 8px 8px 0 0;
    }
    .question-box {
        background-color: #ffffff;
        border: 2.5px solid #2b3446;
        border-radius: 16px;
        padding: 18px 25px;
        font-size: 26px;
        font-weight: 800;
        color: #1f242d;
        box-shadow: 0 4px 10px rgba(0,0,0,0.04);
        line-height: 1.5;
    }
    .pink-cap-bottom {
        background-color: #f4a4a4;
        border: 2.5px solid #2b3446;
        border-top: none;
        width: 130px;
        height: 14px;
        margin: 0 auto;
        border-radius: 0 0 8px 8px;
    }

    /* الخط الرابط */
    .connector-line {
        width: 2.5px;
        height: 22px;
        background-color: #2b3446;
        margin: 0 auto;
    }

    /* شارات IF و ELSE */
    .badge-container {
        text-align: center;
        margin-bottom: -12px;
        position: relative;
        z-index: 5;
    }
    .if-top-bar {
        background-color: #a9d6f5;
        border: 2px solid #2b3446;
        border-bottom: none;
        width: 75px;
        height: 9px;
        margin: 0 auto;
        border-radius: 6px 6px 0 0;
    }
    .if-badge {
        background-color: #a9d6f5;
        border: 2.5px solid #2b3446;
        border-radius: 8px;
        display: inline-block;
        padding: 2px 35px;
        font-weight: 800;
        font-size: 18px;
        color: #1f242d;
        letter-spacing: 1px;
    }
    .else-top-bar {
        background-color: #f4a4a4;
        border: 2px solid #2b3446;
        border-bottom: none;
        width: 85px;
        height: 9px;
        margin: 0 auto;
        border-radius: 6px 6px 0 0;
    }
    .else-badge {
        background-color: #f4a4a4;
        border: 2.5px solid #2b3446;
        border-radius: 8px;
        display: inline-block;
        padding: 2px 28px;
        font-weight: 800;
        font-size: 18px;
        color: #1f242d;
        letter-spacing: 1px;
    }

    /* تنسيق حقول الإدخال لتطابق الصناديق البيضاء */
    div[data-testid="stTextArea"] {
        max-width: 580px;
        margin: 0 auto;
    }
    div[data-testid="stTextArea"] textarea {
        background-color: #ffffff !important;
        border: 2.5px solid #2b3446 !important;
        border-radius: 18px !important;
        padding: 22px 18px 15px 18px !important;
        font-family: 'Cairo', sans-serif !important;
        font-size: 18px !important;
        font-weight: 600 !important;
        color: #1f242d !important;
        text-align: center !important;
        direction: rtl !important;
        box-shadow: 0 4px 10px rgba(0,0,0,0.03) !important;
    }
    div[data-testid="stTextArea"] textarea:focus {
        border-color: #5b9bd5 !important;
        box-shadow: 0 0 0 3px rgba(169, 214, 245, 0.5) !important;
    }

    /* زر الاعتماد */
    div.stButton {
        text-align: center;
        margin-top: 15px;
    }
    div.stButton > button {
        background-color: #2b3446;
        color: #ffffff;
        font-family: 'Cairo', sans-serif;
        font-weight: 700;
        font-size: 17px;
        border-radius: 12px;
        padding: 10px 35px;
        border: none;
        transition: 0.2s;
    }
    div.stButton > button:hover {
        background-color: #42506b;
        color: #ffffff;
    }

    /* التذييل وأسماء الطالبات والدكتورة */
    .footer-credits {
        text-align: center;
        margin-top: 25px;
        font-size: 18px;
        font-weight: 800;
        color: #1f242d;
        line-height: 1.7;
        direction: rtl;
    }
</style>
""", unsafe_allow_html=True)

# 1. قسم السؤال العلوي
st.markdown("""
<div class="question-wrapper">
    <div class="pink-cap-top"></div>
    <div class="question-box">ماذا لو ضاعت أوراق<br>امتحانك ماذا ستفعلين؟</div>
    <div class="pink-cap-bottom"></div>
</div>
<div class="connector-line"></div>
""", unsafe_allow_html=True)

# 2. قسم شرط IF
st.markdown("""
<div class="badge-container">
    <div class="if-top-bar"></div>
    <div class="if-badge">IF</div>
</div>
""", unsafe_allow_html=True)

if_input = st.text_area(
    label="IF",
    label_visibility="collapsed",
    height=150,
    placeholder="اكتبي هنا: إذا وجدتِ الأوراق أو تذكرتِ مكانها..."
)

# الفاصل بين الصندوقين
st.markdown("""
<div style="background-color:#a9d6f5; border:2px solid #2b3446; border-top:none; width:100px; height:10px; margin:-16px auto 0 auto; border-radius:0 0 6px 6px;"></div>
<div class="connector-line"></div>
""", unsafe_allow_html=True)

# 3. قسم شرط ELSE
st.markdown("""
<div class="badge-container">
    <div class="else-top-bar"></div>
    <div class="else-badge">/ELSE</div>
</div>
""", unsafe_allow_html=True)

else_input = st.text_area(
    label="ELSE",
    label_visibility="collapsed",
    height=120,
    placeholder="اكتبي هنا: وإلا (في حال لم تجديها نهائياً) ماذا ستفعلين؟..."
)

st.markdown("""
<div style="background-color:#f4a4a4; border:2px solid #2b3446; border-top:none; width:100px; height:10px; margin:-16px auto 0 auto; border-radius:0 0 6px 6px;"></div>
""", unsafe_allow_html=True)

# 4. زر التفاعل وعرض النتيجة البرمجية
if st.button("✨ تنفيذ الشرط وعرض النتيجة"):
    if if_input.strip() and else_input.strip():
        st.success("✅ **تم بناء الجملة الشرطية بنجاح!**")
        st.code(f"""
if (أوراق_الامتحان_ضاعت):
    "{if_input}"
else:
    "{else_input}"
        """, language="python")
    else:
        st.warning("⚠️ فضلاً قومي بتعبئة مربعي IF و ELSE أولاً.")

# 5. الأسماء في الأسفل كما في الصورة
st.markdown("""
<div class="footer-credits">
    منى الخرجي - شهد الهويشان - شيخة العدنان -<br>
    مي الاحيمر - ندى البديري<br>
    د/ ولاء حلمي الدين
</div>
""", unsafe_allow_html=True)
