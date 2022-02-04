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
-- Table structure for table `dsai_ilms_feedback_type`
--

CREATE TABLE `dsai_ilms_feedback_type` (
  `feedback_type_id` int(11) NOT NULL,
  `feedback_type_name` varchar(50) NOT NULL,
  `feedback_description` varchar(300) NOT NULL,
  `feedback_status` enum('A','I') NOT NULL DEFAULT 'A'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Stores the details of all types of feedbacks available.';

--
-- Dumping data for table `dsai_ilms_feedback_type`
--

INSERT INTO `dsai_ilms_feedback_type` (`feedback_type_id`, `feedback_type_name`, `feedback_description`, `feedback_status`) VALUES
(1, 'Work well with others ', 'fine', 'A'),
(2, 'Give Best Efforts', '', 'A'),
(3, 'Displays Positive Attitute', '', 'A'),
(4, 'Participation in all activities', '', 'A'),
(5, 'volunteer to answer questions', '', 'A'),
(6, 'Open to feedback', '                                          ', 'A'),
(7, 'Answering in poll', '', 'A'),
(8, 'Listening & Questioning', '', 'A'),
(9, 'Quiz participation', '', 'A'),
(10, 'ww', '                     ww                     ', 'I'),
(11, 'qqq', '                                                                      qqqqq              rrrrrrrrrrr                                          ', 'I'),
(12, 'Teacher Insights', 'Teacher\'s Holistic View on the Students Progress, Participation and other activities                               ', 'A'),
(13, 'Students Participation', 'Students Active Participation in the course module', 'A'),
(14, 'Students Recommendation', 'Students Behavioural and Attitudal Recommendation', 'A'),
(15, 'Parent\'s Recommendation', 'Recommendation provided to the parents on Student Participation and Progress', 'A');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dsai_ilms_feedback_type`
--
ALTER TABLE `dsai_ilms_feedback_type`
  ADD PRIMARY KEY (`feedback_type_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dsai_ilms_feedback_type`
--
ALTER TABLE `dsai_ilms_feedback_type`
  MODIFY `feedback_type_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
