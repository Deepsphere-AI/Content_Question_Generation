-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 01, 2022 at 12:14 PM
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
-- Table structure for table `dsai_ilms_course_details`
--

CREATE TABLE `dsai_ilms_course_details` (
  `index` int(11) NOT NULL,
  `learning_path_id` varchar(100) NOT NULL,
  `course_id` varchar(100) NOT NULL,
  `course_original_id` varchar(50) NOT NULL,
  `course_code` varchar(50) NOT NULL,
  `course_name` varchar(200) NOT NULL,
  `course_sub_group` text NOT NULL,
  `course_description` varchar(25) NOT NULL,
  `course_status` varchar(25) NOT NULL,
  `is_demo` varchar(20) NOT NULL,
  `created_by` varchar(20) NOT NULL,
  `created_datetime` varchar(50) NOT NULL,
  `updated_by` varchar(25) NOT NULL,
  `updated_datetime` varchar(50) NOT NULL,
  `source` varchar(50) NOT NULL,
  `latest` varchar(20) NOT NULL DEFAULT 'Y'
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dsai_ilms_course_details`
--

INSERT INTO `dsai_ilms_course_details` (`index`, `learning_path_id`, `course_id`, `course_original_id`, `course_code`, `course_name`, `course_sub_group`, `course_description`, `course_status`, `is_demo`, `created_by`, `created_datetime`, `updated_by`, `updated_datetime`, `source`, `latest`) VALUES
(1, 'Z2qKOpV4srA1', 'h7_vznk0p041', '6209473', '', 'Course One - Introduction Artificial Intelligence', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Course', 'Y'),
(2, 'Z2qKOpV4srA1', '30Zjj-SyYKE1', '6209474', '', 'Course Two - Introduction to Advanced Computing', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Course', 'Y'),
(3, 'Z2qKOpV4srA1', 'futDGf0oQVI1', '6209475', '', 'Course Four - Role of Mathematics in AI', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Course', 'Y'),
(4, 'Z2qKOpV4srA1', 'f7Z9RYmA5Sk1', '6242176', '', 'Course Three : Introduction to Data Engineering', '{\n  \"6253090-6242177\": \"Part One:SQL for Data Science\",\n  \"6253306-6253233\": \"Part Two:Advanced Data Preparation and Exploratory Analysis for Data Science\"\n}', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Course', 'Y'),
(5, 'Dc4BaAYZgcA1', '3R-N7KdPWQU1', '6209476', '', 'Role of Statistics in AI', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Course', 'Y'),
(6, 'Dc4BaAYZgcA1', '_qts9UM7vVU1', '6209478', '', 'Introduction to Machine Learning', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Course', 'Y'),
(7, 'Dc4BaAYZgcA1', 'Sxp5tZO5Dns1', '6209479', '', 'Advanced Computing With Scala, GCP and Distributed Data Processing', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Course', 'Y'),
(8, 'Dc4BaAYZgcA1', 'nT9qRhETr8E1', '6209480', '', 'Introduction to Data Science', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Course', 'Y'),
(9, 'M9KaginLd1A1', '8qyTFVprT54UHX6HTTDXBQ2', '6209473', '6209473', 'Course One:  Introduction Artificial Intelligence', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Module', 'Y'),
(10, 'M9KaginLd1A1', 'goula4Xyt69Qjgcp3XbYxg2', '6209474', '6209474', 'Course Two :  Introduction to Advanced Computing', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Module', 'Y'),
(11, 'M9KaginLd1A1', '-FF8SrSG7kQk8HNp-ijiuA2', '6242176', '6242176', 'Course Three :  Introduction Data Engineering', '{\n  \"6253090-6242177\": \"Part One:SQL for Data Science\",\n  \"6253306-6253233\": \"Part Two:Advanced Data Preparation and Exploratory Analysis for Data Science\"\n}', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Module', 'Y'),
(12, 'M9KaginLd1A1', 'rs5KkHPgpJruORTu2My-QA2', '6209475', '6209475', 'Course Four :  Role of Mathematics in AI', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Module', 'Y'),
(13, 'dm3vL8-DWvY1', 'hEAn_EIrsVtEL-FrWs0TLA2', '6209476', '6209476', 'Course One: Role of Statistics in AI', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Module', 'Y'),
(14, 'dm3vL8-DWvY1', 'M-zBQBXLizEOBIJIx8KJEw2', '6209478', '6209478', 'Course Two :  Introduction to Machine Learning', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Module', 'Y'),
(15, 'dm3vL8-DWvY1', 'vVL3pksny2zd0qKbNAju6g2', '6209479', '6209479', 'Course Three :  Advanced Computing With Scala, GCP and Distributed Data Processing', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Module', 'Y'),
(16, 'dm3vL8-DWvY1', 'QlwUIwlzGnJrCxfGC2i_4A2', '6209480', '6209480', 'Course Four :  Introduction to Data Science', 'no response', '', '1', 'No', '15126700', '2022-01-12 10:54:57.397200', '15126700', '2022-01-12 10:54:57.397200', 'Module', 'Y'),
(17, 'NcCUMgR3uh01', 'kZ_lz2fBhSU1', '5324214', 'no response', 'Course Overview', 'no response', 'no response', 'True', 'no', 'Temp Admin', '2022-01-19 09:56:11.329706', 'Temp Admin', '2022-01-19 09:56:11.329711', 'Course', 'Y'),
(18, 'NcCUMgR3uh01', 'aGKt9RHg_m81', '6887444', 'no response', 'Course Overview - cc - data engineering - found', 'no response', 'no response', 'True', 'no', 'Temp Admin', '2022-01-19 10:27:17.221395', 'Temp Admin', '2022-01-19 10:27:17.221400', 'Course', 'Y'),
(19, 'ZBbx6dWkw9Q1', 'sEC1ud-kg5Y1', '6887448', 'no response', 'Course Overview - cc - data engineering - intermediate', 'no response', 'no response', 'True', 'no', 'Temp Admin', '2022-01-19 10:28:21.382102', 'Temp Admin', '2022-01-19 10:28:21.382108', 'Course', 'Y'),
(20, 'Oo6mR5YrEU01', 'obnzMs9NxzU1', '6887449', 'no response', 'Course Overview - cc - data engineering - advanced', 'no response', 'no response', 'True', 'no', 'Temp Admin', '2022-01-19 10:28:23.986625', 'Temp Admin', '2022-01-19 10:28:23.986629', 'Course', 'Y'),
(21, '2v8P2BaXQO41', 'fGqyCqZ41Gc1', '6887453', 'no response', 'Course overview - cc - advance computing - found', 'no response', 'no response', 'True', 'no', 'Temp Admin', '2022-01-19 10:35:10.619903', 'Temp Admin', '2022-01-19 10:35:10.619907', 'Course', 'Y'),
(22, 'z1jyi5hvZsg1', 'EmIso0Me-LU1', '6887455', 'no response', 'Course overview - cc - advance computing - Intermediate', 'no response', 'no response', 'True', 'no', 'Temp Admin', '2022-01-19 10:36:10.650761', 'Temp Admin', '2022-01-19 10:36:10.650765', 'Course', 'Y'),
(23, 'KO-qODp0jSI1', 'zeVzaGS3rBs1', '6887456', 'no response', 'Course overview - cc - advance computing - advanced', 'no response', 'no response', 'True', 'no', 'Temp Admin', '2022-01-19 10:36:12.297814', 'Temp Admin', '2022-01-19 10:36:12.297817', 'Course', 'Y');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dsai_ilms_course_details`
--
ALTER TABLE `dsai_ilms_course_details`
  ADD PRIMARY KEY (`index`),
  ADD KEY `learning_path_id` (`learning_path_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dsai_ilms_course_details`
--
ALTER TABLE `dsai_ilms_course_details`
  MODIFY `index` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
