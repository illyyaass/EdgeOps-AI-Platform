# جيب النسخة الخفيفة ديال Nginx
FROM nginx:alpine

# مسح الملفات الافتراضية ديال Nginx باش نخويو البلاصة
RUN rm -rf /usr/share/nginx/html/*

# نسخ الملف ديالنا من البيسي لداخل الـ Container
COPY index.html /usr/share/nginx/html/index.html

# حل الباب 80
EXPOSE 80

# خدم السيرفور
CMD ["nginx", "-g", "daemon off;"]