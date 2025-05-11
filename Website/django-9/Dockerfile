FROM python:3.12-alpine

# Atur direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt ke dalam container
COPY requirements.txt .

# Instal dependensi dari requirements.txt
RUN pip install -r requirements.txt

# Salin semua file proyek ke dalam container
COPY . .

# Jalankan server Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
