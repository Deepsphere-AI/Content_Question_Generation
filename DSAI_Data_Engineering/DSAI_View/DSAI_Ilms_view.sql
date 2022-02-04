-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 01, 2022 at 12:12 PM
-- Server version: 5.6.51
-- PHP Version: 7.3.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dssaiai_lms_structure`
--

-- --------------------------------------------------------

--
-- Structure for view `dsai_ilms_view`
--

CREATE ALGORITHM=UNDEFINED DEFINER=`dssaiai`@`localhost` SQL SECURITY DEFINER VIEW `dsai_ilms_view`  AS SELECT `ud`.`user_id` AS `student_id`, `ud`.`user_original_id` AS `user_original_id`, `ud`.`student_external_id` AS `roll_no`, `ud`.`user_fullname` AS `student_name`, `ud`.`is_demo` AS `is_demo`, `t`.`teacher_id` AS `teacher_id`, `t`.`teacher_name` AS `teacher_name`, `lp`.`learning_path_name` AS `learning_path_name`, `lp`.`learning_path_major` AS `learning_path_major`, `lp`.`learning_path_id` AS `learning_path_id`, `lp`.`learning_path_original_id` AS `learning_path_original_id`, `lp`.`learning_path_grade` AS `learning_path_grade`, `lp`.`learning_path_status` AS `learning_path_status`, `c`.`course_id` AS `course_id`, `c`.`course_name` AS `course_name`, `u`.`unit_id` AS `unit_id`, `u`.`unit_original_id` AS `unit_original_id`, `u`.`unit_name` AS `unit_name`, `u`.`assesment_code` AS `assesment_code`, `lpu`.`user_id` AS `user_id`, `q`.`quiz_score` AS `quiz_score`, `uas`.`assignment_score` AS `assignment_score`, `q`.`assesment_grade` AS `assesment_grade` FROM (((((((`dsai_ilms_user_details` `ud` join `dsai_ilms_learning_path_users` `lpu` on((`lpu`.`user_id` = convert(`ud`.`user_id` using utf8mb4)))) join `dsai_ilms_learning_path_details` `lp` on(((`lp`.`learning_path_id` = `lpu`.`learning_path_id`) and (`lp`.`latest` = 'Y')))) left join `dsai_ilms_course_details` `c` on(((convert(`c`.`learning_path_id` using utf8mb4) = `lp`.`learning_path_id`) and (`c`.`latest` = 'Y')))) left join `dsai_ilms_unit` `u` on(((`u`.`course_id` = `c`.`course_id`) or (convert(`u`.`course_id` using utf8mb4) = `lp`.`learning_path_id`)))) left join `dsai_ilms_quiz` `q` on(((convert(`q`.`user_id` using utf8mb4) = `lpu`.`user_id`) and (`q`.`quiz_code` = `u`.`unit_original_id`) and (`q`.`latest` = 'Y')))) left join `dsai_ilms_assignment` `uas` on(((convert(`uas`.`user_id` using utf8mb4) = `lpu`.`user_id`) and (`uas`.`original_mod_id` = `u`.`unit_original_id`) and (`uas`.`latest` = 'Y')))) left join `dsai_ilms_teacher` `t` on((`t`.`teacher_id` = convert(`ud`.`teacher_id` using utf8mb4)))) WHERE ((`u`.`unit_name` not in ('Course Overview','Extra Learning')) AND (not((`u`.`unit_name` like '%Extra learning'))) AND (`ud`.`latest` = 'Y')) ORDER BY `ud`.`user_fullname` ASC, `c`.`course_name` ASC, `u`.`unit_name` ASC ;

--
-- VIEW  `dsai_ilms_view`
-- Data: None
--

COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
