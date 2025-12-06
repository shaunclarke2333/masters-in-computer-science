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

-- ****** Inserting sample data for my mbd wellness app database ******


/* ---------- USERS (10 rows) ---------- */
INSERT INTO users
  (name, email, password_hash, created_at, display_name, date_of_birth, gender, height, weight)
VALUES
  ('Shaun Clarke',      'shaun@example.com',    'hash_shaun_123', '2025-10-01 07:30:00', 'ShaunC',     '1983-04-12', 'male',      185.42, 107.50),
  ('Alicia Brown',      'alicia.b@example.com','hash_alicia_456','2025-10-02 08:15:00', 'AliciaB',    '1990-09-05', 'female',    168.20,  68.30),
  ('Marcus Lee',        'marcus.lee@example.com','hash_marcus_789','2025-10-02 19:45:00','MarcusL',   '1988-01-23', 'male',      178.90,  82.10),
  ('Priya Singh',       'priya.s@example.com', 'hash_priya_321', '2025-10-03 06:50:00', 'PriyaS',     '1993-07-18', 'female',    162.00,  59.80),
  ('Jordan Taylor',     'jordan.t@example.com','hash_jordan_654','2025-10-03 21:10:00', 'JordT',      '1995-11-30', 'nonbinary', 175.30,  75.40),
  ('Elena Martinez',    'elena.m@example.com', 'hash_elena_987', '2025-10-04 09:05:00', 'ElenaM',     '1986-02-10', 'female',    160.55,  62.20),
  ('David Chen',        'david.c@example.com', 'hash_david_147', '2025-10-04 18:35:00', 'DaveC',      '1991-06-02', 'male',      181.00,  88.70),
  ('Samantha Johnson',  'sam.j@example.com',   'hash_sam_258',   '2025-10-05 07:40:00', 'SamJ',       '1998-03-27', 'female',    170.10,  71.90),
  ('Omar Ali',          'omar.ali@example.com','hash_omar_369',  '2025-10-05 20:20:00', 'OmarA',      '1989-08-09', 'male',      179.60,  84.30),
  ('Taylor Brooks',     'taylor.b@example.com','hash_taylor_951','2025-10-06 10:25:00', 'TBrooks',    '1994-12-15', 'other',     172.75,  78.40);

/* ---------- EXERCISES (10 rows) ---------- */
INSERT INTO exercises
  (exercise_name, exercise_category, muscle_group)
VALUES
  ('Back Squat',              'strength',    'Quads & Glutes'),
  ('Bench Press',             'strength',    'Chest & Triceps'),
  ('Deadlift',                'strength',    'Posterior Chain'),
  ('Pull-up',                 'strength',    'Back & Biceps'),
  ('Push-up',                 'strength',    'Chest & Core'),
  ('Plank',                   'core',        'Abdominals'),
  ('Jogging (Treadmill)',     'cardio',      'Full Body'),
  ('Cycling (Stationary)',    'cardio',      'Legs & Cardio'),
  ('Yoga Flow',               'mobility',    'Full Body'),
  ('Box Breathing Meditation','mindfulness', 'Nervous System');

/* ---------- GOALS (10 rows) ---------- */
INSERT INTO goals
  (user_id, goal_type, target_value, unit, description, start_date, end_date, status)
VALUES
  (1, 'weight_loss',       5.00,  'lbs',     'Lose 5lbs before the end of the year',     '2025-10-01','2025-12-31','active'),
  (1, 'steps_per_day',    10000,  'steps',  'Average 10k steps per day',               '2025-10-01','2025-11-30','active'),
  (2, 'strength_squat',    90.00, 'lbs',     'Back squat bodyweight for 5 reps',        '2025-10-05','2026-01-15','active'),
  (3, 'sleep_hours',        8.00, 'hours',  'Maintain 8 hours of sleep per night',     '2025-09-20','2025-12-31','active'),
  (4, 'weekly_yoga',        3.00, 'sessions','Do yoga 3x per week',                    '2025-10-03','2025-12-31','active'),
  (5, 'meditation',        10.00, 'minutes','Meditate 10 minutes every morning',       '2025-10-01','2025-11-30','completed'),
  (6, '5k_time',           28.00, 'minutes','Run 5k under 28 minutes',                 '2025-08-01','2025-10-31','abandoned'),
  (7, 'body_weight',       82.00, 'lbs',     'Reach a stable weight of 82lbs',           '2025-09-01','2026-02-01','active'),
  (8, 'protein_intake',   100.00, 'grams',  'Hit 100g protein daily',                  '2025-10-10','2025-12-10','active'),
  (9, 'screen_time',        2.00, 'hours',  'Limit daily leisure screen time to 2h',   '2025-09-15','2025-11-15','completed');

/* ---------- MEALS (10 rows) ---------- */
INSERT INTO meals
  (user_id, meal_datetime, meal_type, notes)
VALUES
  (1, '2025-10-15 07:30:00', 'breakfast', 'Overnight oats with berries and hemp protein'),
  (1, '2025-10-15 13:00:00', 'lunch',     'Quinoa bowl with roasted veggies'),
  (1, '2025-10-15 19:15:00', 'dinner',    'Tofu stir-fry with brown rice'),
  (2, '2025-10-15 08:10:00', 'breakfast', 'Avocado toast and black coffee'),
  (2, '2025-10-15 12:40:00', 'lunch',     'Chickpea salad wrap'),
  (3, '2025-10-15 18:50:00', 'dinner',    'Lentil curry with basmati rice'),
  (3, '2025-10-16 10:30:00', 'snack',     'Apple with almond butter'),
  (4, '2025-10-16 07:45:00', 'breakfast', 'Tofu scramble and spinach'),
  (5, '2025-10-16 13:15:00', 'lunch',     'Grilled veggie sandwich'),
  (6, '2025-10-16 20:05:00', 'dinner',    'Black bean tacos with salsa');

/* ---------- FOOD (10 rows) ---------- */
INSERT INTO food
  (food_name, brand, serving_size_amount, serving_size_unit, calories_per_serving, protein, carbs, fat)
VALUES
  ('Overnight Oats Base',     'Homemade',  80.00,  'g',           300, 10.00, 45.00, 8.00),
  ('Mixed Berries',           'FrozenMix', 75.00,  'g',            40,  1.00, 10.00, 0.50),
  ('Hemp Protein Powder',     'Whole Foods',30.00, 'g',           120, 15.00,  7.00, 3.00),
  ('Quinoa (cooked)',         'Generic',  185.00,  'g (1 cup)',   220,  8.00, 39.00, 3.50),
  ('Roasted Veggies Mix',     'Homemade', 150.00,  'g',           110,  3.00, 18.00, 4.00),
  ('Firm Tofu',               'Nasoya',   100.00,  'g',           140, 14.00,  4.00, 8.00),
  ('Brown Rice (cooked)',     'Generic',  195.00,  'g (1 cup)',   215,  5.00, 45.00, 2.00),
  ('Chickpea Salad',          'Homemade', 150.00,  'g',           260, 12.00, 30.00, 9.00),
  ('Almond Butter',           'MaraNatha', 16.00,  'g (1 tbsp)',   98,  3.40,  3.40, 8.90),
  ('Black Bean Taco Filling', 'Homemade', 130.00,  'g',           190, 10.00, 26.00, 4.50);

/* ---------- MEAL_ITEMS (at least 10 rows) ---------- */
-- Menatl note: meals 1–3 are Shaun’s full day of eating, with realistic servings
-- meals separated by user id
INSERT INTO meal_items
  (meal_id, food_id, servings)
VALUES
  -- Meal 1: Overnight oats + berries + hemp protein
  (1, 1, 1.00),
  (1, 2, 1.00),
  (1, 3, 1.00),

  -- Meal 2: Quinoa bowl with roasted veggies
  (2, 4, 1.50),
  (2, 5, 1.00),

  -- Meal 3: Tofu stir fry with brown rice
  (3, 6, 1.00),
  (3, 7, 1.00),
  (3, 5, 0.75),

  -- Meal 4: Avocado toast not in food table, approximate with chickpea salad
  (4, 8, 0.80),

  -- Meal 5: Chickpea wrap + berries
  (5, 8, 1.00),
  (5, 2, 1.00),

  -- Meal 6: Lentil curry approximated with black bean filling + rice
  (6,10, 1.00),
  (6, 7, 0.75),

  -- Meal 7: Apple + almond butter
  (7, 9, 1.50),

  -- Meal 8: Tofu scramble + veggies
  (8, 6, 0.80),
  (8, 5, 0.60),

  -- Meal 9: Veggie sandwich approximated as roasted veggies and chickpea salad
  (9, 5, 0.80),
  (9, 8, 0.70),

  -- Meal 10: Black bean tacos
  (10,10, 1.50),
  (10, 7, 0.50);

/* ---------- MOOD_ENTRIES (30 rows for richer time series) ---------- */
-- Mental note: mix of users 1–5, different times and days
-- Again, i separate mood entries by users for my visual purposes.
INSERT INTO mood_entries
  (user_id, entry_datetime, mood_score, energy_level, stress_level, note)
VALUES
  (1, '2025-10-10 07:15:00', 8, 7, 3, 'Slept well, ready for the day'),
  (1, '2025-10-10 20:45:00', 6, 5, 5, 'Long work day, light workout helped'),
  (1, '2025-10-11 06:55:00', 7, 6, 4, 'CPAP fit felt better last night'),
  (1, '2025-10-11 21:10:00', 5, 4, 6, 'A bit drained, knees slightly sore'),
  (1, '2025-10-12 07:05:00', 8, 7, 3, 'Morning hoops, knee feels strong'),
  (1, '2025-10-12 21:00:00', 7, 6, 4, 'Good balance of work and recovery'),

  (2, '2025-10-10 08:30:00', 6, 5, 5, 'Rushed morning, skipped meditation'),
  (2, '2025-10-10 22:00:00', 7, 4, 3, 'Yoga class helped me unwind'),
  (2, '2025-10-11 08:10:00', 7, 6, 4, 'Solid breakfast, steady energy'),
  (2, '2025-10-11 21:40:00', 6, 5, 5, 'Screen time ran late, mind busy'),
  (2, '2025-10-12 09:00:00', 8, 7, 3, 'Walk outside felt grounding'),
  (2, '2025-10-12 21:30:00', 7, 5, 4, 'Feeling more consistent this week'),

  (3, '2025-10-09 07:00:00', 5, 4, 6, 'Did not sleep well, mind racing'),
  (3, '2025-10-09 19:45:00', 6, 5, 5, 'Evening run took edge off stress'),
  (3, '2025-10-10 07:20:00', 6, 5, 5, 'Still a bit groggy in the morning'),
  (3, '2025-10-10 20:10:00', 7, 6, 4, 'Dinner with friends boosted mood'),
  (3, '2025-10-11 07:10:00', 7, 6, 3, 'Started journaling again'),
  (3, '2025-10-11 22:00:00', 6, 4, 5, 'Late caffeine keeping me up'),

  (4, '2025-10-08 06:50:00', 8, 7, 3, 'Yoga and breathing felt amazing'),
  (4, '2025-10-08 21:20:00', 7, 5, 4, 'Mental load manageable today'),
  (4, '2025-10-09 06:45:00', 7, 6, 4, 'Slightly stiff but okay'),
  (4, '2025-10-09 20:55:00', 6, 4, 5, 'Too much context switching at work'),
  (4, '2025-10-10 06:40:00', 8, 7, 3, 'Meditation before email helped'),
  (4, '2025-10-10 21:05:00', 7, 5, 4, 'Ended day with light stretching'),

  (5, '2025-10-07 07:30:00', 6, 5, 5, 'Did not hit sleep goal'),
  (5, '2025-10-07 22:15:00', 5, 4, 6, 'Scrolling in bed too late'),
  (5, '2025-10-08 07:20:00', 7, 6, 4, 'Short meditation helped reset'),
  (5, '2025-10-08 21:45:00', 7, 5, 4, 'Screen time lower than usual'),
  (5, '2025-10-09 07:25:00', 8, 7, 3, 'Felt very focused this morning'),
  (5, '2025-10-09 21:35:00', 8, 6, 3, 'In bed by 10, proud of consistency');

/* ---------- WORKOUT_SESSIONS (>=10 rows) ---------- */
-- Note: primary key is 'sesion_id' per your table definition
INSERT INTO workout_sessions
  (user_id, exercise_id, session_datetime, duration_minutes, notes, sets, reps, weight)
VALUES
  (1, 7, '2025-10-10 05:45:00', 30, 'Light jog, testing knee',           NULL, NULL, NULL),
  (1, 1, '2025-10-11 06:15:00', 45, 'Back squat, focused on form',       4, 5,  80.00),
  (1, 10,'2025-10-11 06:55:00', 10, 'Box breathing cool-down',           NULL, NULL, NULL),
  (2, 9, '2025-10-10 18:00:00', 50, 'Vinyasa flow, moderate intensity',  NULL, NULL, NULL),
  (2, 6, '2025-10-11 07:30:00', 15, 'Core focus, timed planks',          3, 1,   NULL),
  (3, 8, '2025-10-09 18:30:00', 35, 'Stationary bike intervals',         NULL, NULL, NULL),
  (3, 2, '2025-10-10 17:45:00', 40, 'Bench press strength work',         5, 5,  75.00),
  (4, 9, '2025-10-08 06:00:00', 40, 'Morning yoga for mobility',         NULL, NULL, NULL),
  (4, 10,'2025-10-10 06:20:00', 8,  'Short guided breathing session',    NULL, NULL, NULL),
  (5, 7, '2025-10-07 18:10:00', 25, 'Easy treadmill jog after work',     NULL, NULL, NULL),
  (5, 3, '2025-10-09 17:30:00', 35, 'Light deadlifts, focus on hinge',   3, 5,  70.00),
  (6, 4, '2025-10-12 09:15:00', 20, 'Pull-ups EMOM, assisted',           6, 3,  NULL);

/* ---------- HABITS (10 rows) ---------- */
INSERT INTO habits
  (user_id, habit_name, habit_category, habit_target_frequency, active)
VALUES
  (1, 'Morning Walk',             'activity',  'daily',     1),
  (1, 'Lights Out by 10:30pm',    'sleep',     'daily',     1),
  (2, 'Yoga Session',             'activity',  '3x_week',   1),
  (2, 'No Screens After 9pm',     'sleep',     'daily',     1),
  (3, 'Evening Run',              'activity',  '3x_week',   1),
  (3, 'Gratitude Journal',        'mindset',   'daily',     1),
  (4, 'Morning Meditation',       'mindfulness','daily',    1),
  (4, 'Stretch Before Bed',       'mobility',  'daily',     1),
  (5, 'Track Screen Time',        'mindset',   'daily',     1),
  (5, 'No Caffeine After 2pm',    'nutrition', 'daily',     1);

/* ---------- HABIT_LOGS (>=10 rows; here 20 logs) ---------- */
INSERT INTO habit_logs
  (habit_id, log_date, completed, value)
VALUES
  -- User 1: Morning Walk & Lights Out
  (1, '2025-10-10', 1, 30.00),
  (1, '2025-10-11', 1, 28.00),
  (1, '2025-10-12', 0,  0.00),
  (2, '2025-10-10', 0, 23.30),
  (2, '2025-10-11', 1, 22.15),
  (2, '2025-10-12', 1, 22.05),

  -- User 2: Yoga Session & No Screens
  (3, '2025-10-08', 1, 45.00),
  (3, '2025-10-10', 1, 50.00),
  (3, '2025-10-12', 0,  0.00),
  (4, '2025-10-08', 1, 20.00),
  (4, '2025-10-09', 0,  0.00),
  (4, '2025-10-10', 1,  0.50),

  -- User 3: Evening Run & Gratitude Journal
  (5, '2025-10-09', 1, 25.00),
  (5, '2025-10-11', 0,  0.00),
  (6, '2025-10-09', 1,  3.00),
  (6, '2025-10-10', 1,  3.00),
  (6, '2025-10-11', 0,  0.00),

  -- User 4 & 5 habits
  (7, '2025-10-08', 1, 10.00),
  (7, '2025-10-09', 1, 12.00),
  (8, '2025-10-09', 0,  0.00),
  (9, '2025-10-07', 1,  2.50),
  (10,'2025-10-07',1,  0.00);


