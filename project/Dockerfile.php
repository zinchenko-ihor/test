FROM php:8.0-fpm

RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libxml2-dev \
    libzip-dev \
    libpq-dev \
    libcurl4-openssl-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-configure pgsql --with-pgsql=/usr/local/pgsql \
    && docker-php-ext-install -j$(nproc) \
        bcmath \
        curl \
        exif \
        gd \
        mysqli \
        pdo \
        pdo_mysql \
        pdo_pgsql \
        xml \
        zip

RUN pecl install redis && docker-php-ext-enable redis

WORKDIR /var/www/html

EXPOSE 9000

CMD ["php-fpm"]
