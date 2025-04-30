FROM node:18-slim

# Install system dependencies needed for 'sharp'
RUN apt-get update && apt-get install -y \
    libvips libvips-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY package.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]

