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
-- Table structure for table `dsai_ilms_learning_path`
--

CREATE TABLE `dsai_ilms_learning_path` (
  `index` int(11) NOT NULL,
  `learning_path_id` varchar(250) NOT NULL,
  `learning_path_name` varchar(500) NOT NULL,
  `learning_path_original_id` varchar(20) NOT NULL,
  `is_demo` varchar(25) NOT NULL,
  `created_by` varchar(50) NOT NULL,
  `created_datetime` varchar(50) NOT NULL,
  `updated_by` varchar(50) NOT NULL,
  `updated_datetime` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dsai_ilms_learning_path`
--

INSERT INTO `dsai_ilms_learning_path` (`index`, `learning_path_id`, `learning_path_name`, `learning_path_original_id`, `is_demo`, `created_by`, `created_datetime`, `updated_by`, `updated_datetime`) VALUES
(1, 'gSFkYKR2d_o1', 'Additional courses  - Certification Course - Advanced', '167868', 'No', '15126700', '2022-01-06 13:07:45:987000', '15126700', '2022-01-12 15:30:05:480000'),
(2, 'MtLf72-NMKc1', 'Additional courses  - Certification Course - Foundation', '167572', 'No', '15126700', '2022-01-04 16:33:00:587000', '15126700', '2022-01-06 11:33:55:713000'),
(3, 'y09RXG4wAUs1', 'Additional courses - Intermediate level - cc - part 1', '167680', 'No', '15126700', '2022-01-05 17:49:51:627000', '15126700', '2022-01-06 12:14:30:070000'),
(4, 'nvlXHF1_oVU1', 'Additional courses - Intermediate level - cc - part 2', '167867', 'No', '15126700', '2022-01-06 11:55:17:710000', '15126700', '2022-01-06 12:15:12:257000'),
(5, 'KO-qODp0jSI1', 'Advanced Computing -Certification course- Advanced', '168830', 'No', '15126700', '2022-01-12 14:29:27:730000', '15126700', '2022-01-12 10:53:37.651234'),
(6, 'z1jyi5hvZsg1', 'Advanced Computing -Certification course- Intermediate', '168829', 'No', '15126700', '2022-01-12 14:28:04:943000', '15126700', '2022-01-12 10:53:37.651234'),
(7, 'pPRmoawWgK81', 'Applied AI for Certification Course : Advanced Level', '167866', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(8, '0QjRftBaLYQ1', 'Applied AI for Certification Course : Foundation Level', '167570', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(9, '2_BbDHaod1U1', 'Applied AI for Certification Course : Intermediate Level', '167663', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(10, '2v8P2BaXQO41', 'Advanced Computing-Certification course- Foundation', '168827', 'No', '15126700', '2022-01-12 14:26:44:300000', '15126700', '2022-01-12 10:53:37.651234'),
(11, 'AtwlYnaHVIc1', 'certificate program -test', '166642', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(12, 'Oo6mR5YrEU01', 'Data Engineering-Certification course- Advanced', '168825', 'No', '15126700', '2022-01-12 14:25:53:733000', '15126700', '2022-01-12 10:53:37.651234'),
(13, 'NcCUMgR3uh01', 'Data Engineering-Certification course- Foundation', '168821', 'No', '15126700', '2022-01-12 14:15:58:600000', '15126700', '2022-01-12 10:53:37.651234'),
(14, 'ZBbx6dWkw9Q1', 'Data Engineering-Certification course- Intermediate', '168824', 'No', '15126700', '2022-01-12 14:25:22:883000', '15126700', '2022-01-12 10:53:37.651234'),
(15, 'JFsLJMWdTRo1', 'delta learning', '166645', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(16, 'FGeTT-uxhFw1', 'Course One - Unit 2 - Extra Learning', '164415', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(17, '7cdE6iyrn081', 'Applied Artificial Intelligence for 6th Grade', '143618', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(18, 'ta0vP-ytaOk1', 'Applied Artificial Intelligence for 7th Grade', '148273', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(19, '6dS3R8pcZ3Q1', 'Applied Artificial Intelligence for 8th Grade', '148174', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(20, 'QsBre2zhhpo1', 'Applied Artificial Intelligence for 9th Grade', '147412', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(21, 'vEYMVkEHKN81', 'Applied Artificial Intelligence for 10th Grade', '148177', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(22, 'Wj7tyo1kpfE1', 'Applied Artificial Intelligence for 11th Grade', '148175', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(23, '3E8miQ4H_9g1', 'Applied Artificial Intelligence for 12th Grade', '148176', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(24, 'f7E9QoiEL7g1', 'Applied artificial Intelligence for Executives', '144628', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(25, 'FNRQx6ZfL2c1', 'Applied Artificial Intelligence for Professionals', '152664', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(26, 'h0CRxDL3evw1', 'Applied Machine Learning on google cloud and colab', '148315', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(27, '2OK6uSI2Dy81', 'BCA With Specialization in Applied Artificial Intelligence', '149078', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(28, '5nP6-eBu2jk1', 'Advanced and Higher Educational Certificate Program for Hands-on Skill Development and Career Transformation & Advancement', '157701', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(29, 'jb0QtKfA96o1', 'Advanced and Higher Educational Certificate Program for Hands-on Skill Development and Career Transformation & Advancement', '157703', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(30, 'BrkSTxA7djA1', 'Advanced Computing for Enterprise Certificate Program', '156681', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(31, 'nI-JnqTQQZk1', 'Advanced Data Preparation and Exploratory Analysis for Data Science', '156054', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(32, 'sX_EXFpmdHs1', 'Applied AI for Enterprise Certificate Program', '156679', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(33, 'Z2qKOpV4srA1', 'Bachelor of Computer Applications in Artificial Intelligence and Data Science - Semester 1', '154844', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(34, 'McOi4t79q8w1', 'Applied AI for Schools : Foundation Level', '159882', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(35, '74WGtvXQqHI1', 'Applied AI for Schools : Intermediate Level', '159883', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(36, 'uWbP5Synv7o1', 'Applied AI for Schools : Advanced Level', '159884', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(37, 'Dc4BaAYZgcA1', 'Bachelor of Computer Applications in Artificial Intelligence and Data Science - Semester 2', '154845', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(38, 'LSB5LCBejnI1', 'Certificate Program', '157702', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(39, '22w-bAyfsQw1', 'Content and Assessment Generation', '154718', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(40, 'LaeMBjViheE1', 'Data Engineering for Enterprise Certificate Program', '156680', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(41, 'HmXdkjIuklo1', 'Reporting, Analytics and Insights', '154597', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(42, '14mWWtaJlIk1', 'SQL for Data Science', '156045', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(43, 'buOzqhYiQKU1', 'SRM-Introduction Artificial Intelligence- additional courses', '159532', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(44, 'ZDWLHmUXLBA1', 'SRM-Introduction Data Engineering - Advanced Data Preparation and Exploratory Analysis for Data Science - additional courses', '159537', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(45, 'em8fPGFBYHQ1', 'SRM-Introduction Data Engineering - SQL for Data Science - additional courses', '159536', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(46, 'z6K_wcnB4Ac1', 'SRM-Introduction to Advanced Computing- additional courses', '159534', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(47, 'mXeh0m_w9FI1', 'Advanced level additional courses', '160692', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(48, 'sjuYhi3mPaw1', 'SRM - Course1 - Unit', '159559', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(49, 'opPhS1BO0Rw1', 'SRM - Course4 - Unit', '159566', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(50, 'mtnye8Pcr6M1', 'dummy leanring', '149082', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(51, 'Kw_3qK66pxo1', 'SRM - Course2 - Unit', '159561', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(52, 'JpP200OygcU1', 'SRM - Course3 - Part1 - Unit', '159562', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(53, 'hHAd8RdYS041', 'SRM - Course3 - Part2 - Unit', '159563', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(54, '1PR781K8mUk1', '12th Grade additional courses', '159526', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(55, 'sHkHJGOiT2U1', '6th Grade additional courses', '159520', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(56, 'AqkleOitvbo1', '11th Grade additional courses', '159525', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(57, 'bY316uNCO2o1', '8th Grade additional courses', '159522', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(58, 'S-HxBL9S9pQ1', '9th Grade additional courses', '159523', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(59, 'QMffLtC5AOg1', '7th Grade additional courses', '159521', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(60, 'WRMP_lqLkHc1', 'Foundation level additional courses', '160694', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(61, '36aTvHRViWg1', '10th Grade additional courses', '159524', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(62, '3RvTUhsCp541', 'Intermediate level additional courses', '160693', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(63, '7iimxngO4rw1', 'Advanced Level - Additional Courses - Demo', '162536', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(64, 'Vpk6AnnJMm41', 'Applied AI for Schools : Foundation Level - Demo', '162525', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(65, 'G2xjEgNRl2U1', 'Applied AI for Schools : Intermediate Level Demo', '162530', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(66, 'GD5oCICbv8w1', 'Applied AI for Schools : Advanced Level - Demo', '162532', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(67, 'gE3MIFKQM5U1', 'Applied AI for Schools : Foundation Level - Beta', '162526', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(68, '_ARDCzSkebk1', 'Applied AI for Schools : Intermediate Level - Beta', '162527', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(69, 'RBiD6_y-xfU1', 'Applied AI for Schools : Advanced Level - Beta', '162529', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(70, 'Zof-aeAMg3Q1', 'foundation', '162518', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(71, 'ykP81B1k4BE1', 'Foundation Level - Additional Courses - Demo', '162534', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(72, 'xYnVYGyDHfg1', 'Intermediate Level - Additional Courses - Demo', '162535', 'No', '15126700', '2022-01-12 10:53:37.651234', '15126700', '2022-01-12 10:53:37.651234'),
(73, 'M9KaginLd1A1', 'Bachelor of Computer Applications in Artificial Intelligence and Data Science', '6222172', 'No', '15126700', '2022-01-12 10:53:37.674559', '15126700', '2022-01-12 10:53:37.674559'),
(74, 'dm3vL8-DWvY1', 'Bachelor of Computer Applications in Artificial Intelligence and Data Science', '6223529', 'No', '15126700', '2022-01-12 10:53:37.674559', '15126700', '2022-01-12 10:53:37.674559');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dsai_ilms_learning_path`
--
ALTER TABLE `dsai_ilms_learning_path`
  ADD PRIMARY KEY (`index`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dsai_ilms_learning_path`
--
ALTER TABLE `dsai_ilms_learning_path`
  MODIFY `index` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=75;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
