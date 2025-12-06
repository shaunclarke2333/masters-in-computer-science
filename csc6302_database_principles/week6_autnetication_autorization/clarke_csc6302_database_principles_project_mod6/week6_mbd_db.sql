/*
Each time this script is ran it will drop the database if it already exists.
Mental Note: This workflow is not for production. Only required for weekly assignments.
*/
DROP DATABASE IF EXISTS `mbd`;
-- Creating the database that will be used
CREATE DATABASE IF NOT EXISTS `mbd`;
-- Making the databse we want to work with active and ready for crud operations
USE `mbd`;

-- Dropping table if it already exists
DROP TABLE IF EXISTS `users`;

-- creating users table
CREATE TABLE `users` (
  `user_id` INT AUTO_INCREMENT PRIMARY KEY,
  `name` VARCHAR(100),
  `email` VARCHAR(150) UNIQUE,
  `password_hash` VARCHAR(255),
  `created_at` DATETIME,
  `display_name` VARCHAR(100),
  `date_of_birth` DATE,
  `gender` ENUM('male','female','nonbinary','other'),
  `height` DECIMAL(5,2),
  `weight` DECIMAL(5,2)
);

-- Dropping table if it already exists
DROP TABLE IF EXISTS `exercises`;

-- creating exercises table
CREATE TABLE `exercises` (
  `exercise_id` INT AUTO_INCREMENT PRIMARY KEY,
  `exercise_name` VARCHAR(100),
  `exercise_category` VARCHAR(50),
  `muscle_group` VARCHAR(50)
);

-- Dropping table if it already exists
DROP TABLE IF EXISTS `goals`;

-- creating goals table
CREATE TABLE `goals` (
  `goal_id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT,
  `goal_type` VARCHAR(50),
  `target_value` DECIMAL(10,2),
  `unit` VARCHAR(20),
  `description` TEXT,
  `start_date` DATE,
  `end_date` DATE,
  `status` ENUM('active','completed','abandoned'),
   FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Dropping table if it already exists
DROP TABLE IF EXISTS `meals`;

-- creating meals table
CREATE TABLE `meals` (
  `meal_id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT,
  `meal_datetime` DATETIME,
  `meal_type` ENUM('breakfast','lunch','dinner','snack'),
  `notes` TEXT NULL,
  FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Dropping table if it already exists
DROP TABLE IF EXISTS `food`;

-- creating food table
CREATE TABLE `food` (
  `food_id` INT AUTO_INCREMENT PRIMARY KEY,
  `food_name` VARCHAR(100),
  `brand` VARCHAR(100) NULL,
  `serving_size_amount` DECIMAL(6,2),
  `serving_size_unit` VARCHAR(200),
  `calories_per_serving` INT,
  `protein` DECIMAL(6,2),
  `carbs` DECIMAL(6,2),
  `fat` DECIMAL(6,2)
);

-- Dropping table if it already exists
DROP TABLE IF EXISTS `meal_items`;

-- creating meal_items table
CREATE TABLE `meal_items` (
  `meal_item_id` INT AUTO_INCREMENT PRIMARY KEY,
  `meal_id` INT,
  `food_id` INT,
  `servings` DECIMAL(5,2),
  FOREIGN KEY (`meal_id`) REFERENCES `meals` (`meal_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`food_id`) REFERENCES `food` (`food_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Dropping table if it already exists
DROP TABLE IF EXISTS `mood_entries`;

-- creating mood_entries table
CREATE TABLE `mood_entries` (
  `mood_id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT,
  `entry_datetime` DATETIME,
  `mood_score` TINYINT,
  `energy_level` TINYINT NULL,
  `stress_level` TINYINT NULL,
  `note` TEXT,
  FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Dropping table if it already exists
DROP TABLE IF EXISTS `workout_sessions`;

-- creating workout_sessions table
CREATE TABLE `workout_sessions` (
  `sesion_id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT,
  `exercise_id` INT,
  `session_datetime` DATETIME,
  `duration_minutes` INT,
  `notes` TEXT NULL,
  `sets` INT NULL,
  `reps` INT NULL,
  `weight` DECIMAL(6,2) NULL,
  FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`exercise_id`) REFERENCES `exercises` (`exercise_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Dropping table if it already exists
DROP TABLE IF EXISTS `habits`;

-- creating habits table
CREATE TABLE `habits` (
  `habit_id` INT AUTO_INCREMENT PRIMARY KEY,
  `user_id` INT,
  `habit_name` VARCHAR(100),
  `habit_category` VARCHAR(50),
  `habit_target_frequency` VARCHAR(20),
  `active` TINYINT(1),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Dropping table if it already exists
DROP TABLE IF EXISTS `habit_logs`;

-- creating habit_logs table
CREATE TABLE `habit_logs` (
  `habit_log_id` INT AUTO_INCREMENT PRIMARY KEY,
  `habit_id` INT,
  `log_date` DATE,
  `completed` TINYINT(1),
  `value` DECIMAL(6,2),
  FOREIGN KEY (`habit_id`) REFERENCES `habits` (`habit_id`) ON DELETE CASCADE ON UPDATE CASCADE
);


