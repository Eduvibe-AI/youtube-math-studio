FROM nginx:alpine
RUN sed -i 's/listen  *80;/listen 8080;/' /etc/nginx/conf.d/default.conf
COPY index.html /usr/share/nginx/html/
COPY shorts_*.js /usr/share/nginx/html/
COPY fonts_l2 /usr/share/nginx/html/fonts_l2
COPY csat2025_mock /usr/share/nginx/html/csat2025_mock
COPY view_lecture*.html /usr/share/nginx/html/
EXPOSE 8080
