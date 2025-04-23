FROM nginx:alpine

# copy the flask config file
COPY flask.conf /etc/nginx/conf.d/flask.conf

# copy the build folder
COPY ../frontend/build /usr/share/nginx/html

#Port expose
EXPOSE 80

# run the main command
CMD ["nginx", "-g", "daemon off;"]