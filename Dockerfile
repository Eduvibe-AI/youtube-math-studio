FROM python:3.12-slim
WORKDIR /app
COPY index.html ./
COPY shorts_*.js ./
COPY fonts_l2 ./fonts_l2
COPY csat2025_mock ./csat2025_mock
COPY csat_rpm771_series.html ./
COPY sejong_exam_twin_lab.html ./
COPY kice_sample.html ./
COPY view_lecture*.html ./
EXPOSE 8080
CMD ["python", "-m", "http.server", "8080"]
