FROM node:20-slim AS frontend-builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build -- --configuration production

FROM nginx:1.28.0-alpine AS frontend

WORKDIR /app

COPY --from=frontend-builder /app/dist/accounts-v2 /usr/share/nginx/html

COPY nginx.conf /etc/nginx/conf.d/frontend.conf

EXPOSE 8080

CMD ["nginx", "-g", "daemon off;"]

# accounts-v2
