import html
from datetime import datetime

import streamlit as st

# ─────────────────────────── إعدادات الصفحة ───────────────────────────
st.set_page_config(
    page_title="بطاقة تفاعلية | IF / ELIF / ELSE",
    page_icon="📝",
    layout="centered",
)

# ─────────────────────────── السيناريوهات ───────────────────────────
SCENARIOS = {
    "papers": {
        "title": "ضياع أوراق الامتحان",
        "question": "ماذا لو ضاعت أوراق<br>امتحانك ماذا ستفعلين؟",
        "var": "papers_status",
        "labels": {
            "if": "وجدتِ الأوراق أو تذكرتِ مكانها",
            "elif": "وجدتِ جزءاً منها فقط",
            "else": "لم تجديها نهائياً",
        },
        "placeholders": {
            "if": "اكتبي ماذا ستفعلين إذا وجدتِ الأوراق...",
            "elif": "اكتبي ماذا ستفعلين إذا وجدتِ جزءاً منها...",
            "else": "اكتبي ماذا ستفعلين إذا لم تجديها...",
        },
    },
    "laptop": {
        "title": "نسيان الحاسوب قبل العرض التقديمي",
        "question": "ماذا لو نسيتِ حاسوبك<br>قبل العرض التقديمي؟",
        "var": "laptop_status",
        "labels": {
            "if": "تمكنتِ من الحصول عليه بسرعة",
            "elif": "توفر لديكِ حاسوب بديل",
            "else": "لا يوجد أي جهاز متاح",
        },
        "placeholders": {
            "if": "اكتبي ماذا ستفعلين إذا حصلتِ عليه...",
            "elif": "اكتبي ماذا ستفعلين مع الحاسوب البديل...",
            "else": "اكتبي خطتك إذا لم يتوفر أي جهاز...",
        },
    },
    "internet": {
        "title": "انقطاع الإنترنت أثناء اختبار إلكتروني",
        "question": "ماذا لو انقطع الإنترنت<br>أثناء اختبار إلكتروني؟",
        "var": "internet_status",
        "labels": {
            "if": "عاد الاتصال خلال دقائق",
            "elif": "تذبذب الاتصال",
            "else": "انقطع الاتصال تماماً",
        },
        "placeholders": {
            "if": "اكتبي ماذا ستفعلين عند عودة الاتصال...",
            "elif": "اكتبي كيف ستتعاملين مع التذبذب...",
            "else": "اكتبي خطتك عند الانقطاع التام...",
        },
    },
}

MIN_CHARS = 5  # أقل عدد أحرف مقبول لكل إجابة

# ─────────────────────────── التنسيق (CSS) ───────────────────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800&display=swap');

html, body, .stApp, .stApp * { font-family: 'Cairo', sans-serif; }
code, pre, pre * { font-family: 'Consolas', 'Courier New', monospace !important; direction: ltr; text-align: left; }

.stApp {
    background-color: #f9f7f2;
    background-image:
        linear-gradient(#e5e0d5 1.5px, transparent 1.5px),
        linear-gradient(90deg, #e5e0d5 1.5px, transparent 1.5px);
    background-size: 35px 35px;
}
#MainMenu, footer, header { visibility: hidden; }
.block-container { max-width: 760px; padding-top: 1.5rem; direction: rtl; }

/* العنوان */
.hero { text-align: center; margin-bottom: 14px; direction: rtl; }
.hero h1 { font-size: 30px; font-weight: 800; color: #1f242d; margin: 0; }
.hero p  { font-size: 15px; font-weight: 600; color: #5a6275; margin: 4px 0 0 0; }

/* خطوات */
.step-title {
    direction: rtl; text-align: right; font-weight: 800; font-size: 17px;
    color: #1f242d; margin: 22px 0 8px 0;
}
.step-title span {
    background: #2b3446; color: #fff; border-radius: 50%;
    display: inline-block; width: 26px; height: 26px; line-height: 26px;
    text-align: center; font-size: 14px; margin-left: 8px;
}

/* صندوق السؤال */
.question-wrapper { max-width: 480px; margin: 6px auto 0 auto; text-align: center; }
.pink-cap-top, .pink-cap-bottom {
    background-color: #f4a4a4; border: 2.5px solid #2b3446; height: 14px; margin: 0 auto;
}
.pink-cap-top    { width: 110px; border-bottom: none; border-radius: 8px 8px 0 0; }
.pink-cap-bottom { width: 130px; border-top: none;    border-radius: 0 0 8px 8px; }
.question-box {
    background: #fff; border: 2.5px solid #2b3446; border-radius: 16px;
    padding: 18px 25px; font-size: 26px; font-weight: 800; color: #1f242d;
    box-shadow: 0 4px 10px rgba(0,0,0,.05); line-height: 1.5;
}
.connector-line { width: 2.5px; height: 20px; background: #2b3446; margin: 0 auto; }

/* الشارات */
.badge-container { text-align: center; margin-bottom: -12px; position: relative; z-index: 5; }
.top-bar { border: 2px solid #2b3446; border-bottom: none; height: 9px; margin: 0 auto; border-radius: 6px 6px 0 0; width: 80px; }
.badge {
    border: 2.5px solid #2b3446; border-radius: 8px; display: inline-block;
    padding: 2px 32px; font-weight: 800; font-size: 18px; color: #1f242d; letter-spacing: 1px;
    direction: ltr;
}
.c-if   { background: #a9d6f5; }
.c-elif { background: #ffe29a; }
.c-else { background: #f4a4a4; }
.badge-hint { text-align: center; font-size: 13px; font-weight: 700; color: #5a6275; margin: 16px 0 -2px 0; direction: rtl; }
.bottom-bar { border: 2px solid #2b3446; border-top: none; width: 100px; height: 10px; margin: -16px auto 0 auto; border-radius: 0 0 6px 6px; }

/* حقول الإدخال */
div[data-testid="stTextArea"] textarea {
    background: #fff !important; border: 2.5px solid #2b3446 !important; border-radius: 18px !important;
    padding: 22px 18px 15px 18px !important; font-size: 17px !important; font-weight: 600 !important;
    color: #1f242d !important; text-align: center !important; direction: rtl !important;
    box-shadow: 0 4px 10px rgba(0,0,0,.03) !important;
}
div[data-testid="stTextArea"] textarea:focus {
    border-color: #5b9bd5 !important; box-shadow: 0 0 0 3px rgba(169,214,245,.5) !important;
}

/* الأزرار */
div.stButton > button, div.stDownloadButton > button {
    background: #2b3446; color: #fff; font-weight: 700; font-size: 16px;
    border-radius: 12px; padding: 10px 28px; border: none; transition: .2s; width: 100%;
}
div.stButton > button:hover, div.stDownloadButton > button:hover { background: #42506b; color: #fff; }

/* مخطط التدفق */
.flow { display: flex; gap: 10px; justify-content: center; direction: ltr; margin: 10px 0; flex-wrap: wrap; }
.flow-card {
    flex: 1; min-width: 150px; max-width: 220px; border: 2.5px solid #2b3446; border-radius: 14px;
    padding: 10px 12px; text-align: center; background: #fff; opacity: .35; transition: .3s; direction: rtl;
}
.flow-card b { display: block; font-size: 16px; direction: ltr; }
.flow-card small { font-weight: 600; color: #3b4252; }
.flow-card.active { opacity: 1; transform: translateY(-4px); box-shadow: 0 8px 18px rgba(0,0,0,.15); }
.flow-card.active.c-if   { background: #a9d6f5; }
.flow-card.active.c-elif { background: #ffe29a; }
.flow-card.active.c-else { background: #f4a4a4; }

/* ناتج التنفيذ */
.output-box {
    background: #1f242d; color: #e8ecf3; border-radius: 14px; padding: 16px 20px;
    font-weight: 600; font-size: 17px; line-height: 1.8; direction: rtl; text-align: right;
    border-right: 6px solid #a9d6f5;
}
.output-box .tag { color: #9fb3d1; font-size: 13px; display: block; margin-bottom: 4px; }

/* التذييل */
.footer-credits {
    text-align: center; margin-top: 34px; padding-top: 14px; border-top: 2px dashed #cfc8b8;
    font-size: 17px; font-weight: 800; color: #1f242d; line-height: 1.8; direction: rtl;
}
"""
st.markdown(f"<style>{CSS}</style>", unsafe_allow_html=True)


# ─────────────────────────── دوال مساعدة ───────────────────────────
def esc(text: str) -> str:
    """تنظيف النص قبل عرضه داخل HTML مع الحفاظ على الأسطر."""
    return html.escape(text.strip()).replace("\n", "<br>")


def badge(kind: str, label: str) -> str:
    cls = {"if": "c-if", "elif": "c-elif", "else": "c-else"}[kind]
    return (
        f'<div class="badge-container"><div class="top-bar {cls}"></div>'
        f'<div class="badge {cls}">{label}</div></div>'
    )


def bottom_bar(kind: str) -> str:
    color = {"if": "#a9d6f5", "elif": "#ffe29a", "else": "#f4a4a4"}[kind]
    return f'<div class="bottom-bar" style="background:{color}"></div>'


def build_code(sc: dict, texts: dict, use_elif: bool, chosen: str) -> str:
    """يبني كود بايثون حقيقياً بأسماء إنجليزية ويُظهر الحالة المختارة."""
    var = sc["var"]
    lines = [f'{var} = "{chosen}"', ""]
    lines.append(f'if {var} == "if":')
    lines.append(f"    print({texts['if']!r})")
    if use_elif:
        lines.append(f'elif {var} == "elif":')
        lines.append(f"    print({texts['elif']!r})")
    lines.append("else:")
    lines.append(f"    print({texts['else']!r})")
    return "\n".join(lines)


# ─────────────────────────── الحالة (Session State) ───────────────────────────
if "history" not in st.session_state:
    st.session_state.history = []
if "result" not in st.session_state:
    st.session_state.result = None

# ─────────────────────────── العنوان ───────────────────────────
st.markdown(
    """
<div class="hero">
    <h1>📝 بطاقة تفاعلية: الجمل الشرطية</h1>
    <p>تعلّمي IF / ELIF / ELSE من مواقف الحياة الواقعية ثم شاهدي الكود وهو يُنفَّذ</p>
</div>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────── الخطوة 1: اختيار الموقف ───────────────────────────
st.markdown('<div class="step-title"><span>1</span>اختاري الموقف</div>', unsafe_allow_html=True)
key = st.selectbox(
    "الموقف",
    options=list(SCENARIOS.keys()),
    format_func=lambda k: SCENARIOS[k]["title"],
    label_visibility="collapsed",
)
sc = SCENARIOS[key]

use_elif = st.toggle(
    "إضافة حالة وسطى (ELIF) ليصبح الشرط من ثلاث حالات",
    value=False,
    key=f"elif_{key}",
)

st.markdown(
    f"""
<div class="question-wrapper">
    <div class="pink-cap-top"></div>
    <div class="question-box">{sc['question']}</div>
    <div class="pink-cap-bottom"></div>
</div>
<div class="connector-line"></div>
""",
    unsafe_allow_html=True,
)

# ─────────────────────────── الخطوة 2: كتابة الإجابات ───────────────────────────
st.markdown('<div class="step-title"><span>2</span>اكتبي إجاباتك</div>', unsafe_allow_html=True)

texts = {}

st.markdown(badge("if", "IF") + f'<div class="badge-hint">الشرط: {sc["labels"]["if"]}</div>', unsafe_allow_html=True)
texts["if"] = st.text_area("IF", label_visibility="collapsed", height=110,
                           placeholder=sc["placeholders"]["if"], key=f"if_{key}")
st.markdown(bottom_bar("if") + '<div class="connector-line"></div>', unsafe_allow_html=True)

if use_elif:
    st.markdown(badge("elif", "ELIF") + f'<div class="badge-hint">الشرط: {sc["labels"]["elif"]}</div>', unsafe_allow_html=True)
    texts["elif"] = st.text_area("ELIF", label_visibility="collapsed", height=110,
                                 placeholder=sc["placeholders"]["elif"], key=f"elif_txt_{key}")
    st.markdown(bottom_bar("elif") + '<div class="connector-line"></div>', unsafe_allow_html=True)

st.markdown(badge("else", "ELSE") + f'<div class="badge-hint">وإلا: {sc["labels"]["else"]}</div>', unsafe_allow_html=True)
texts["else"] = st.text_area("ELSE", label_visibility="collapsed", height=110,
                             placeholder=sc["placeholders"]["else"], key=f"else_{key}")
st.markdown(bottom_bar("else"), unsafe_allow_html=True)

# ─────────────────────────── الخطوة 3: محاكاة الواقع وتنفيذ الشرط ───────────────────────────
st.markdown('<div class="step-title"><span>3</span>ماذا حدث في الواقع؟ (جرّبي كل الحالات)</div>', unsafe_allow_html=True)

options = ["if", "elif", "else"] if use_elif else ["if", "else"]
chosen = st.radio(
    "الحالة",
    options=options,
    format_func=lambda k: f"{k.upper()}  ←  {sc['labels'][k]}",
    label_visibility="collapsed",
    key=f"choice_{key}_{use_elif}",
)

if st.button("▶️ تنفيذ الشرط وعرض النتيجة"):
    required = options  # الحقول المطلوبة حسب الوضع
    missing = [k.upper() for k in required if len(texts[k].strip()) < MIN_CHARS]
    if missing:
        st.session_state.result = None
        st.warning(f"⚠️ فضلاً أكملي الإجابات (على الأقل {MIN_CHARS} أحرف) في: {' ، '.join(missing)}")
    else:
        st.session_state.result = {
            "key": key,
            "use_elif": use_elif,
            "chosen": chosen,
            "texts": {k: texts[k].strip() for k in required},
        }
        st.session_state.history.append(
            {
                "time": datetime.now().strftime("%H:%M:%S"),
                "scenario": sc["title"],
                "chosen": chosen.upper(),
                "output": texts[chosen].strip(),
            }
        )

# ─────────────────────────── عرض النتيجة ───────────────────────────
res = st.session_state.result
if res and res["key"] == key:
    r_sc = SCENARIOS[res["key"]]
    r_opts = ["if", "elif", "else"] if res["use_elif"] else ["if", "else"]

    st.success("✅ تم تنفيذ الجملة الشرطية بنجاح")

    # مخطط التدفق: الفرع المنفَّذ فقط هو المضيء
    cards = ""
    for k in r_opts:
        active = "active" if k == res["chosen"] else ""
        cards += (
            f'<div class="flow-card c-{k} {active}"><b>{k.upper()}</b>'
            f'<small>{r_sc["labels"][k]}</small></div>'
        )
    st.markdown(f'<div class="flow">{cards}</div>', unsafe_allow_html=True)

    code = build_code(r_sc, res["texts"], res["use_elif"], res["chosen"])
    st.markdown("**🧩 الكود الناتج**")
    st.code(code, language="python")

    st.markdown(
        f'<div class="output-box"><span class="tag">🖥️ ناتج التنفيذ (Output)</span>'
        f'{esc(res["texts"][res["chosen"]])}</div>',
        unsafe_allow_html=True,
    )

    st.info(
        "💡 لاحظي: لا يُنفَّذ إلا فرع واحد فقط. بايثون يفحص الشروط بالترتيب "
        "ويتوقف عند أول شرط صحيح، وإذا لم يصح أي شرط ينفّذ ELSE."
    )

    st.download_button(
        "⬇️ تحميل الكود (.py)",
        data=code,
        file_name="conditional_card.py",
        mime="text/x-python",
    )

# ─────────────────────────── سجل التجارب ───────────────────────────
if st.session_state.history:
    with st.expander(f"🕘 سجل تجاربك ({len(st.session_state.history)})"):
        for item in reversed(st.session_state.history):
            st.markdown(
                f"**{item['time']}** — {item['scenario']} ← `{item['chosen']}`: {item['output']}"
            )
        if st.button("🗑️ مسح السجل"):
            st.session_state.history = []
            st.rerun()

# ─────────────────────────── التذييل ───────────────────────────
st.markdown(
    """
<div class="footer-credits">
    منى الخرجي - شهد الهويشان - شيخة العدنان -<br>
    مي الاحيمر - ندى البديري<br>
    د/ ولاء حلمي الدين
</div>
""",
    unsafe_allow_html=True,
)
