# استخدام نسخة بايثون متوافقة
FROM python:3.10-slim

# إنشاء مستخدم حسب شروط أمان Hugging Face
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:$PATH"

# تحديد فولدر العمل
WORKDIR /app

# نسخ ملف المكتبات وتسطيبه
COPY --chown=user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# نسخ باقي ملفات المشروع
COPY --chown=user . /app

# تشغيل الموقع على البورت المخصص لـ Hugging Face (7860)
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:server"]