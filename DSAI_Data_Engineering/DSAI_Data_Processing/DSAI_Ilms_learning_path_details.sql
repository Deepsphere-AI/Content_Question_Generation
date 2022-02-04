-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 01, 2022 at 12:15 PM
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
-- Table structure for table `dsai_ilms_learning_path_details`
--

CREATE TABLE `dsai_ilms_learning_path_details` (
  `index` int(11) NOT NULL,
  `learning_path_id` varchar(100) NOT NULL,
  `learning_path_name` varchar(500) NOT NULL DEFAULT 'No response',
  `learning_path_major` varchar(100) NOT NULL,
  `learning_path_status` varchar(25) NOT NULL,
  `learning_path_grade` varchar(25) NOT NULL,
  `learning_path_active_status` varchar(15) NOT NULL DEFAULT 'No response',
  `learning_path_original_id` varchar(11) NOT NULL DEFAULT 'No response',
  `learning_path_description` varchar(100) NOT NULL DEFAULT 'No response',
  `is_demo` varchar(20) NOT NULL,
  `created_by` varchar(20) NOT NULL DEFAULT 'No response',
  `created_datetime` varchar(50) NOT NULL DEFAULT 'No response',
  `updated_by` varchar(20) NOT NULL DEFAULT 'No response',
  `updated_datetime` varchar(50) NOT NULL DEFAULT 'No response',
  `source` varchar(50) NOT NULL,
  `latest` varchar(20) NOT NULL DEFAULT 'Y'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Stores the details of all the available courses';

--
-- Dumping data for table `dsai_ilms_learning_path_details`
--

INSERT INTO `dsai_ilms_learning_path_details` (`index`, `learning_path_id`, `learning_path_name`, `learning_path_major`, `learning_path_status`, `learning_path_grade`, `learning_path_active_status`, `learning_path_original_id`, `learning_path_description`, `is_demo`, `created_by`, `created_datetime`, `updated_by`, `updated_datetime`, `source`, `latest`) VALUES
(1, 'gSFkYKR2d_o1', 'Additional courses  - Certification Course - Advanced', 'no response', 'no response', 'Professional', '1', '167868', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'N'),
(2, 'MtLf72-NMKc1', 'Additional courses  - Certification Course - Foundation', 'no response', 'no response', 'Professional', '1', '167572', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'N'),
(3, 'y09RXG4wAUs1', 'Additional courses - Intermediate level - cc - part 1', 'no response', 'no response', 'Professional', '1', '167680', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'N'),
(4, 'nvlXHF1_oVU1', 'Additional courses - Intermediate level - cc - part 2', 'no response', 'no response', 'Professional', '1', '167867', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'N'),
(5, 'KO-qODp0jSI1', 'Advanced Computing -Certification course- Advanced', 'no response', 'no response', 'Professional', '1', '168830', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'N'),
(6, 'z1jyi5hvZsg1', 'Advanced Computing -Certification course- Intermediate', 'no response', 'no response', 'Professional', '1', '168829', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'N'),
(7, 'pPRmoawWgK81', 'Applied AI for Certification Course : Advanced Level', ' Applied AI', 'no response', 'Professional', '1', '167866', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(8, '0QjRftBaLYQ1', 'Applied AI for Certification Course : Foundation Level', ' Applied AI', 'no response', 'Professional', '1', '167570', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(9, '2_BbDHaod1U1', 'Applied AI for Certification Course : Intermediate Level', ' Applied AI', 'no response', 'Professional', '1', '167663', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(10, '2v8P2BaXQO41', 'Advanced Computing-Certification course- Foundation', 'no response', 'no response', 'Professional', '1', '168827', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'N'),
(11, 'AtwlYnaHVIc1', 'certificate program -test', 'no response', 'no response', 'Professional', '1', '166642', 'certificate program', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(12, 'Oo6mR5YrEU01', 'Data Engineering-Certification course- Advanced', ' Data', 'no response', 'Professional', '1', '168825', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'N'),
(13, 'NcCUMgR3uh01', 'Data Engineering-Certification course- Foundation', ' Data', 'no response', 'Professional', '1', '168821', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'N'),
(14, 'ZBbx6dWkw9Q1', 'Data Engineering-Certification course- Intermediate', ' Data', 'no response', 'Professional', '1', '168824', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'N'),
(15, 'JFsLJMWdTRo1', 'delta learning', 'no response', 'no response', 'Professional', '1', '166645', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(16, 'FGeTT-uxhFw1', 'Course One - Unit 2 - Extra Learning', ' Learning', 'no response', 'Professional', '1', '164415', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(17, '7cdE6iyrn081', 'Applied Artificial Intelligence for 6th Grade', ' Applied Artificial Intelligence', 'Grade', '6th', '1', '143618', '<b>Interdisciplinary Foundational Learning Program</b><br>\r\n<b>Course Overview: </b>\r\nThe applied ar', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(18, 'ta0vP-ytaOk1', 'Applied Artificial Intelligence for 7th Grade', ' Applied Artificial Intelligence', 'Grade', '7th', '1', '148273', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(19, '6dS3R8pcZ3Q1', 'Applied Artificial Intelligence for 8th Grade', ' Applied Artificial Intelligence', 'Grade', '8th', '1', '148174', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(20, 'QsBre2zhhpo1', 'Applied Artificial Intelligence for 9th Grade', ' Applied Artificial Intelligence', 'Grade', '9th', '1', '147412', '<b>Interdisciplinary Intermediate Learning Program</b><br>\r\n<b>Course Overview</b>\r\nThe applied AI f', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(21, 'vEYMVkEHKN81', 'Applied Artificial Intelligence for 10th Grade', ' Applied Artificial Intelligence', 'Grade', '10th', '1', '148177', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(22, 'Wj7tyo1kpfE1', 'Applied Artificial Intelligence for 11th Grade', ' Applied Artificial Intelligence', 'Grade', '11th', '1', '148175', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(23, '3E8miQ4H_9g1', 'Applied Artificial Intelligence for 12th Grade', ' Applied Artificial Intelligence', 'Grade', '12th', '1', '148176', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(24, 'f7E9QoiEL7g1', 'Applied artificial Intelligence for Executives', ' Applied artificial Intelligence', 'no response', 'Professional', '1', '144628', '<b>Interdisciplinary Executive Learning Program</b><br>\r\n<b>Course Overview: </b>\r\nThe Applied Artif', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(25, 'FNRQx6ZfL2c1', 'Applied Artificial Intelligence for Professionals', ' Applied Artificial Intelligence', 'no response', 'Professional', '1', '152664', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(26, 'h0CRxDL3evw1', 'Applied Machine Learning on google cloud and colab', ' Applied Machine Learning', 'no response', 'Professional', '1', '148315', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(27, '2OK6uSI2Dy81', 'BCA With Specialization in Applied Artificial Intelligence', ' Applied Artificial Intelligence', 'no response', 'Professional', '1', '149078', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(28, '5nP6-eBu2jk1', 'Advanced and Higher Educational Certificate Program for Hands-on Skill Development and Career Transformation & Advancement', 'no response', 'no response', 'Professional', '1', '157701', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(29, 'jb0QtKfA96o1', 'Advanced and Higher Educational Certificate Program for Hands-on Skill Development and Career Transformation & Advancement', 'no response', 'no response', 'Professional', '1', '157703', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(30, 'BrkSTxA7djA1', 'Advanced Computing for Enterprise Certificate Program', 'no response', 'no response', 'Professional', '1', '156681', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(31, 'nI-JnqTQQZk1', 'Advanced Data Preparation and Exploratory Analysis for Data Science', ' Data Exploratory Analysis Data Science', 'no response', 'Professional', '0', '156054', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(32, 'sX_EXFpmdHs1', 'Applied AI for Enterprise Certificate Program', ' Applied AI', 'no response', 'Professional', '1', '156679', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(33, 'Z2qKOpV4srA1', 'Bachelor of Computer Applications in Artificial Intelligence and Data Science - Semester 1', ' Artificial Intelligence Data Science', 'Semester', '1', '0', '154844', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(34, 'McOi4t79q8w1', 'Applied AI for Schools : Foundation Level', ' Applied AI', 'Level', 'Professional', '1', '159882', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(35, '74WGtvXQqHI1', 'Applied AI for Schools : Intermediate Level', ' Applied AI', 'Level', 'Professional', '1', '159883', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(36, 'uWbP5Synv7o1', 'Applied AI for Schools : Advanced Level', ' Applied AI', 'Level', 'Professional', '1', '159884', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(37, 'Dc4BaAYZgcA1', 'Bachelor of Computer Applications in Artificial Intelligence and Data Science - Semester 2', ' Artificial Intelligence Data Science', 'Semester', '2', '1', '154845', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(38, 'LSB5LCBejnI1', 'Certificate Program', 'no response', 'no response', 'Professional', '1', '157702', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(39, '22w-bAyfsQw1', 'Content and Assessment Generation', 'no response', 'no response', 'Professional', '1', '154718', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(40, 'LaeMBjViheE1', 'Data Engineering for Enterprise Certificate Program', ' Data Engineering', 'no response', 'Professional', '1', '156680', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(41, 'HmXdkjIuklo1', 'Reporting, Analytics and Insights', 'no response', 'no response', 'Professional', '1', '154597', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(42, '14mWWtaJlIk1', 'SQL for Data Science', ' Data Science', 'no response', 'Professional', '0', '156045', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(43, 'buOzqhYiQKU1', 'SRM-Introduction Artificial Intelligence- additional courses', ' Artificial', 'no response', 'Professional', '1', '159532', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(44, 'ZDWLHmUXLBA1', 'SRM-Introduction Data Engineering - Advanced Data Preparation and Exploratory Analysis for Data Science - additional courses', ' Data Engineering Data Exploratory Analysis Data Science', 'no response', 'Professional', '1', '159537', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(45, 'em8fPGFBYHQ1', 'SRM-Introduction Data Engineering - SQL for Data Science - additional courses', ' Data Engineering Data Science', 'no response', 'Professional', '1', '159536', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(46, 'z6K_wcnB4Ac1', 'SRM-Introduction to Advanced Computing- additional courses', 'no response', 'no response', 'Professional', '1', '159534', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(47, 'mXeh0m_w9FI1', 'Advanced level additional courses', 'no response', 'no response', 'Professional', '1', '160692', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(48, 'sjuYhi3mPaw1', 'SRM - Course1 - Unit', 'no response', 'no response', 'Professional', '1', '159559', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(49, 'opPhS1BO0Rw1', 'SRM - Course4 - Unit', 'no response', 'no response', 'Professional', '1', '159566', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(50, 'mtnye8Pcr6M1', 'dummy leanring', 'no response', 'no response', 'Professional', '1', '149082', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(51, 'Kw_3qK66pxo1', 'SRM - Course2 - Unit', 'no response', 'no response', 'Professional', '1', '159561', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(52, 'JpP200OygcU1', 'SRM - Course3 - Part1 - Unit', 'no response', 'no response', 'Professional', '1', '159562', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(53, 'hHAd8RdYS041', 'SRM - Course3 - Part2 - Unit', 'no response', 'no response', 'Professional', '1', '159563', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(54, '1PR781K8mUk1', '12th Grade additional courses', 'no response', 'Grade', '12th', '1', '159526', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(55, 'sHkHJGOiT2U1', '6th Grade additional courses', 'no response', 'Grade', '6th', '1', '159520', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(56, 'AqkleOitvbo1', '11th Grade additional courses', 'no response', 'Grade', '11th', '1', '159525', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(57, 'bY316uNCO2o1', '8th Grade additional courses', 'no response', 'Grade', '8th', '1', '159522', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(58, 'S-HxBL9S9pQ1', '9th Grade additional courses', 'no response', 'Grade', '9th', '1', '159523', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(59, 'QMffLtC5AOg1', '7th Grade additional courses', 'no response', 'Grade', '7th', '1', '159521', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(60, 'WRMP_lqLkHc1', 'Foundation level additional courses', 'no response', 'no response', 'Professional', '1', '160694', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(61, '36aTvHRViWg1', '10th Grade additional courses', 'no response', 'Grade', '10th', '1', '159524', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(62, '3RvTUhsCp541', 'Intermediate level additional courses', 'no response', 'no response', 'Professional', '1', '160693', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(63, '7iimxngO4rw1', 'Advanced Level - Additional Courses - Demo', 'no response', 'no response', 'Professional', '1', '162536', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(64, 'Vpk6AnnJMm41', 'Applied AI for Schools : Foundation Level - Demo', ' Applied AI', 'Level', 'Professional', '1', '162525', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(65, 'G2xjEgNRl2U1', 'Applied AI for Schools : Intermediate Level Demo', ' Applied AI', 'Level', 'Professional', '1', '162530', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(66, 'GD5oCICbv8w1', 'Applied AI for Schools : Advanced Level - Demo', ' Applied AI', 'Level', 'Professional', '1', '162532', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(67, 'gE3MIFKQM5U1', 'Applied AI for Schools : Foundation Level - Beta', ' Applied AI', 'Level', 'Professional', '1', '162526', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(68, '_ARDCzSkebk1', 'Applied AI for Schools : Intermediate Level - Beta', ' Applied AI', 'Level', 'Professional', '1', '162527', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(69, 'RBiD6_y-xfU1', 'Applied AI for Schools : Advanced Level - Beta', ' Applied AI', 'Level', 'Professional', '1', '162529', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(70, 'Zof-aeAMg3Q1', 'foundation', 'no response', 'no response', 'Professional', '1', '162518', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(71, 'ykP81B1k4BE1', 'Foundation Level - Additional Courses - Demo', 'no response', 'no response', 'Professional', '1', '162534', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(72, 'xYnVYGyDHfg1', 'Intermediate Level - Additional Courses - Demo', 'no response', 'no response', 'Professional', '1', '162535', 'no response', 'no response', '15126700', '2022-01-12 10:53:37.661108', '15126700', '2022-01-12 10:53:37.661108', 'Learning path', 'Y'),
(73, 'M9KaginLd1A1', 'Bachelor of Computer Applications in Artificial Intelligence and Data Science', ' Artificial Intelligence Data Science', 'Semester', '1', '1', '6222172', 'no response', 'No', '15126700', '2022-01-12 10:53:37.674559', '15126700', '2022-01-12 10:53:37.674559', 'Course', ''),
(74, 'dm3vL8-DWvY1', 'Bachelor of Computer Applications in Artificial Intelligence and Data Science', ' Artificial Intelligence Data Science', 'Semester', '2', '1', '6223529', 'no response', 'No', '15126700', '2022-01-12 10:53:37.674559', '15126700', '2022-01-12 10:53:37.674559', 'Course', ''),
(75, '2v8P2BaXQO41', 'Advanced Computing-Certification course- Foundation', 'no response', 'no response', 'Professional', 'True', '168827', 'no response', 'no', '15126700', '2022-01-12 14:26:44:300000', '15126700', '2022-01-12 14:26:44:300000', 'Learning path', 'Y'),
(76, 'z1jyi5hvZsg1', 'Advanced Computing -Certification course- Intermediate', 'no response', 'no response', 'Professional', 'True', '168829', 'no response', 'no', '15126700', '2022-01-12 14:28:04:943000', '15126700', '2022-01-12 14:28:04:943000', 'Learning path', 'Y'),
(77, 'KO-qODp0jSI1', 'Advanced Computing -Certification course- Advanced', 'no response', 'no response', 'Professional', 'True', '168830', 'no response', 'no', '15126700', '2022-01-12 14:29:27:730000', '15126700', '2022-01-12 14:29:27:730000', 'Learning path', 'Y'),
(78, 'MtLf72-NMKc1', 'Additional courses  - Certification Course - Foundation', 'no response', 'no response', 'Professional', 'True', '167572', 'no response', 'no', '15126700', '2022-01-04 16:33:00:587000', '15126700', '2022-01-06 11:33:55:713000', 'Learning path', 'Y'),
(79, 'y09RXG4wAUs1', 'Additional courses - Intermediate level - cc - part 1', 'no response', 'no response', 'Professional', 'True', '167680', 'no response', 'no', '15126700', '2022-01-05 17:49:51:627000', '15126700', '2022-01-06 12:14:30:070000', 'Learning path', 'Y'),
(80, 'nvlXHF1_oVU1', 'Additional courses - Intermediate level - cc - part 2', 'no response', 'no response', 'Professional', 'True', '167867', 'no response', 'no', '15126700', '2022-01-06 11:55:17:710000', '15126700', '2022-01-06 12:15:12:257000', 'Learning path', 'Y');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dsai_ilms_learning_path_details`
--
ALTER TABLE `dsai_ilms_learning_path_details`
  ADD PRIMARY KEY (`index`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dsai_ilms_learning_path_details`
--
ALTER TABLE `dsai_ilms_learning_path_details`
  MODIFY `index` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
