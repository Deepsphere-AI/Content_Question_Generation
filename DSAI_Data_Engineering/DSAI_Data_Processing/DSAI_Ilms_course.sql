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
-- Table structure for table `dsai_ilms_course`
--

CREATE TABLE `dsai_ilms_course` (
  `index` int(11) NOT NULL,
  `course_id` varchar(250) NOT NULL,
  `course_name` varchar(500) NOT NULL,
  `course_original_id` varchar(20) NOT NULL,
  `is_demo` varchar(11) NOT NULL,
  `created_by` varchar(100) NOT NULL,
  `created_datetime` varchar(50) NOT NULL,
  `updated_by` varchar(50) NOT NULL,
  `updated_datetime` varchar(50) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Dumping data for table `dsai_ilms_course`
--

INSERT INTO `dsai_ilms_course` (`index`, `course_id`, `course_name`, `course_original_id`, `is_demo`, `created_by`, `created_datetime`, `updated_by`, `updated_datetime`) VALUES
(1, 'h7_vznk0p041', 'Course One - Introduction Artificial Intelligence', '6209473', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(2, '30Zjj-SyYKE1', 'Course Two - Introduction to Advanced Computing', '6209474', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(3, 'futDGf0oQVI1', 'Course Four - Role of Mathematics in AI', '6209475', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(4, 'f7Z9RYmA5Sk1', 'Course Three : Introduction to Data Engineering', '6242176', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(5, '3R-N7KdPWQU1', 'Role of Statistics in AI', '6209476', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(6, '_qts9UM7vVU1', 'Introduction to Machine Learning', '6209478', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(7, 'Sxp5tZO5Dns1', 'Advanced Computing With Scala, GCP and Distributed Data Processing', '6209479', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(8, 'nT9qRhETr8E1', 'Introduction to Data Science', '6209480', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(9, '8qyTFVprT54UHX6HTTDXBQ2', 'Course One:  Introduction Artificial Intelligence', 'no_response', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(10, 'goula4Xyt69Qjgcp3XbYxg2', 'Course Two :  Introduction to Advanced Computing', 'no_response', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(11, '-FF8SrSG7kQk8HNp-ijiuA2', 'Course Three :  Introduction Data Engineering', 'no_response', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(12, 'rs5KkHPgpJruORTu2My-QA2', 'Course Four :  Role of Mathematics in AI', 'no_response', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(13, 'hEAn_EIrsVtEL-FrWs0TLA2', 'Course One: Role of Statistics in AI', 'no_response', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(14, 'M-zBQBXLizEOBIJIx8KJEw2', 'Course Two :  Introduction to Machine Learning', 'no_response', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(15, 'vVL3pksny2zd0qKbNAju6g2', 'Course Three :  Advanced Computing With Scala, GCP and Distributed Data Processing', 'no_response', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(16, 'QlwUIwlzGnJrCxfGC2i_4A2', 'Course Four :  Introduction to Data Science', 'no_response', 'No', '15126700', '2022-01-12 10:54:53.639951', '15126700', '2022-01-12 10:54:53.639951'),
(17, 'kZ_lz2fBhSU1', 'Course Overview', '5324214', 'no', 'Temp Admin', '2022-01-19 09:56:11.329706', 'Temp Admin', '2022-01-19 09:56:11.329711'),
(18, 'aGKt9RHg_m81', 'Course Overview - cc - data engineering - found', '6887444', 'no', 'Temp Admin', '2022-01-19 10:27:17.221395', 'Temp Admin', '2022-01-19 10:27:17.221400'),
(19, 'sEC1ud-kg5Y1', 'Course Overview - cc - data engineering - intermediate', '6887448', 'no', 'Temp Admin', '2022-01-19 10:28:21.382102', 'Temp Admin', '2022-01-19 10:28:21.382108'),
(20, 'obnzMs9NxzU1', 'Course Overview - cc - data engineering - advanced', '6887449', 'no', 'Temp Admin', '2022-01-19 10:28:23.986625', 'Temp Admin', '2022-01-19 10:28:23.986629'),
(21, 'fGqyCqZ41Gc1', 'Course overview - cc - advance computing - found', '6887453', 'no', 'Temp Admin', '2022-01-19 10:35:10.619903', 'Temp Admin', '2022-01-19 10:35:10.619907'),
(22, 'EmIso0Me-LU1', 'Course overview - cc - advance computing - Intermediate', '6887455', 'no', 'Temp Admin', '2022-01-19 10:36:10.650761', 'Temp Admin', '2022-01-19 10:36:10.650765'),
(23, 'zeVzaGS3rBs1', 'Course overview - cc - advance computing - advanced', '6887456', 'no', 'Temp Admin', '2022-01-19 10:36:12.297814', 'Temp Admin', '2022-01-19 10:36:12.297817');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dsai_ilms_course`
--
ALTER TABLE `dsai_ilms_course`
  ADD PRIMARY KEY (`index`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dsai_ilms_course`
--
ALTER TABLE `dsai_ilms_course`
  MODIFY `index` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
