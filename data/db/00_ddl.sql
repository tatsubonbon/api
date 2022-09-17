CREATE DATABASE sample_db;

use sample_db;

DROP TABLE IF EXISTS `Follow`;

DROP TABLE IF EXISTS `Image`;

DROP TABLE IF EXISTS `Posts`;

DROP TABLE IF EXISTS `Role`;

DROP TABLE IF EXISTS `Users`;

-- Create Table --

CREATE TABLE
    `Follow` (
        `follower_id` BIGINT NOT NULL COMMENT 'フォローID',
        `followed_id` BIGINT NOT NULL COMMENT 'フォロワーID',
        `created_at` datetime DEFAULT NULL COMMENT '登録日時',
        `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時'
    );

CREATE TABLE
    `Image` (
        `id` VARCHAR(100) NOT NULL COMMENT 'イメージID',
        `post_id` VARCHAR(100) NOT NULL COMMENT '投稿ID',
        `image_path` VARCHAR(300) COMMENT '画像パス',
        `created_at` datetime DEFAULT NULL COMMENT '登録日時',
        `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
        PRIMARY KEY (`id`)
    );

CREATE TABLE
    `Posts` (
        `id` VARCHAR(100) NOT NULL COMMENT '投稿ID',
        `user_id` BIGINT NOT NULL COMMENT 'ユーザーID',
        `title` VARCHAR(100) COMMENT 'タイトル',
        `text` TEXT COMMENT 'テキスト',
        `created_at` datetime DEFAULT NULL COMMENT '登録日時',
        `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
        PRIMARY KEY (`id`)
    );

CREATE TABLE
    `Role` (
        `id` BIGINT NOT NULL COMMENT 'ロールID',
        `name` VARCHAR(64) NOT NULL COMMENT '名前',
        `default` BOOLEAN COMMENT 'デフォルト',
        `permissions` INT COMMENT 'パーミッション',
        `created_at` datetime DEFAULT NULL COMMENT '登録日時',
        `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
        PRIMARY KEY (`id`)
    );

CREATE TABLE
    `Users` (
        `id` BIGINT AUTO_INCREMENT NOT NULL COMMENT 'ユーザID',
        `user_name` VARCHAR(100) NOT NULL COMMENT 'ユーザー名',
        `email` VARCHAR(30) UNIQUE DEFAULT NULL COMMENT 'email',
        `password_hash` VARCHAR(100) NOT NULL COMMENT 'パスワード',
        -- `role_id` BIGINT NOT NULL COMMENT 'ロールID',
        `created_at` datetime DEFAULT NULL COMMENT '登録日時',
        `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新日時',
        PRIMARY KEY (`id`)
    );