
import numpy as np
import streamlit as st
# Nếu numpy chưa có attr 'dtypes', gán tạm để các thư viện legacy dùng được
if not hasattr(np, "dtypes"):
    np.dtypes = np.dtype

# --- CSS cho sidebar hẹp, đẹp ---
st.markdown("""
    <style>
        section[data-testid="stSidebar"] {
            width: 100px !important;
            padding: 1.5rem 1rem !important;
            background: #2c3e50 !important;
        }
        .block-container {
            margin-left: 100px !important;
            padding-top: 2rem !important;
            max-width: 90% !important;
            overflow-x: hidden !important;
        }
        html, body, [data-testid="stApp"] {
            overflow-x: hidden !important;
        }
        main .block-container {
            max-width: 100% !important;
            margin: 0 !important;
            padding-left: 2rem !important;
            padding-right: 2rem !important;
        }
        a[data-testid="stSidebarNavLink"] { display: none !important; }
        section[data-testid="stSidebar"] img {
            display: block; margin:0 auto 1rem; width:100px; height:100px;
            border-radius:50%; border:3px solid #f1c40f;
        }
        section[data-testid="stSidebar"] .sidebar-title {
            text-align:center; color:#f1c40f; font-size:20px; font-weight:600;
            margin-bottom:1rem;
        }
        .sidebar-menu .stButton > button {
            width:100% !important;
            min-height:3rem;
            text-align:left;
            background:#405167;
            color:white;
            border:none;
            border-radius:6px;
            box-shadow:0 3px 6px rgba(0,0,0,0.15);
            transition:0.2s;
            white-space: normal !important;
        }
        .sidebar-menu .stButton > button:hover {
            background:#3498db;
            transform:translateX(3px);
        }
    </style>
""", unsafe_allow_html=True)


# --- Sidebar với “tab” giả ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    # st.image("D:\MonHocKi2_2025\Final_XuLyAnh\image_main\DucDung.jpg", width=100)
    st.markdown('<div class="sidebar-title">📁 Danh mục dự án</div>', unsafe_allow_html=True)

    # 1) Radio để chọn nhóm như Tab
    group = st.radio("", ["📘 Bài học", "📝 Bài tập làm thêm"], index=0)

    # 2) Tạo 2 dict giống trước
    pages_lessons = {
        "👥 Giới thiệu bản thân": "pages/0_GioiThieuBanThan.py",
        "🙂 Nhận diện khuôn mặt": "pages/1_NhanDangKhuonMat_onnx.py",
        "🍎 Nhận diện trái cây": "pages/2_NhanDienTraiCay_yolov8.py",
        "🖼️ Xử lý bài ảnh số": "pages/3_xulyanhso.py",
        "🔢 Nhận diện chữ số": "pages/4_NhanDangChuSo.py",
    }
    pages_extras = {
        "🚗 Nhận diện đối tượng - 3D - dataset KITTI Lidar ": "pages/7_NhanDienDoiTuong.py",  # Thêm dòng này
        "🏃 Phát hiện biển số xe": "pages/6_NhanDienBienSoXe.py",
        "🚖 Phát hiện khói lửa": "pages/8_PhatHienLua.py",
        "🏃 Xác định hành động": "pages/5_HumanActivityRecognition.py",
    }

    # 3) Dựa vào giá trị group để render nút tương ứng
    st.markdown('<div class="sidebar-menu">', unsafe_allow_html=True)
    if group.startswith("📘"):
        for name, path in pages_lessons.items():
            if st.button(name, key=f"lesson_{name}"):
                st.session_state.current_page = path
    else:
        for name, path in pages_extras.items():
            if st.button(name, key=f"extra_{name}"):
                st.session_state.current_page = path
    st.markdown('</div>', unsafe_allow_html=True)

# --- Phần nội dung chính ---
st.markdown('<h1 style="text-align:center; color:#2c3e50;">📚 Student AI Portfolio</h1>', unsafe_allow_html=True)
st.markdown('<p style="text-align:center; color:#34495e;">Khám phá các dự án AI/CV của chúng tôi</p>', unsafe_allow_html=True)

# --- Load trang đã chọn ---
page_path = st.session_state.get("current_page", None)
if page_path:
    try:
        with open(page_path, encoding="utf-8") as f:
            exec(f.read())
    except Exception as e:
        st.error(f"❌ Không thể tải trang: {e}")
else:
    st.info("Vui lòng chọn mục trong sidebar.")
