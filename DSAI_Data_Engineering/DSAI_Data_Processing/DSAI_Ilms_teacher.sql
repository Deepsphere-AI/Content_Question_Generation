-- phpMyAdmin SQL Dump
-- version 4.9.7
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Feb 01, 2022 at 12:16 PM
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
-- Table structure for table `dsai_ilms_teacher`
--

CREATE TABLE `dsai_ilms_teacher` (
  `index` int(11) NOT NULL,
  `teacher_id` varchar(25) NOT NULL,
  `student_id` varchar(50) NOT NULL,
  `teacher_name` varchar(50) NOT NULL DEFAULT 'No response',
  `teacher_status` enum('A','I') NOT NULL DEFAULT 'A',
  `is_demo` varchar(20) NOT NULL,
  `created_by` varchar(25) NOT NULL DEFAULT 'No response',
  `created_datetime` varchar(50) NOT NULL DEFAULT 'No response',
  `updated_by` varchar(25) NOT NULL DEFAULT 'No response',
  `updated_datetime` varchar(50) NOT NULL DEFAULT 'No response'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='Stores the details of all teachers associated with this program';

--
-- Dumping data for table `dsai_ilms_teacher`
--

INSERT INTO `dsai_ilms_teacher` (`index`, `teacher_id`, `student_id`, `teacher_name`, `teacher_status`, `is_demo`, `created_by`, `created_datetime`, `updated_by`, `updated_datetime`) VALUES
(1, 'C_OfApHEy9sHULAsEqG5Yw2', 'C_OfApHEy9sHULAsEqG5Yw2', 'aneesh s', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(2, '9anatxj4nwtAxs9HeM6qjg2', '9anatxj4nwtAxs9HeM6qjg2', 'delta user', '', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(3, '-lYfm9hh93nviOhmatrEOw2', '-lYfm9hh93nviOhmatrEOw2', 'Lalitha P', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(4, '8Vet2nZB5ATvBMFs3tYRGA2', '8Vet2nZB5ATvBMFs3tYRGA2', 'Pandiyan Dr', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(5, 'SKUgQPBQ9l_i65oV2q09eQ2', 'SKUgQPBQ9l_i65oV2q09eQ2', 'Parthiban R', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(6, '_OBRiLbow-ddKaz4Kmt5_w2', '_OBRiLbow-ddKaz4Kmt5_w2', 'Ramla M', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(7, '0pUXHmpEyyMBmsVB6JrCaw2', '0pUXHmpEyyMBmsVB6JrCaw2', 'Rebecca Jayavadhanam', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(8, 'GleyV5tKlelsa-mcPXHDVg2', 'GleyV5tKlelsa-mcPXHDVg2', 'Sivakumar Dr', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(9, 'x5RFFprL4ZtRe2Ewjze7Yw2', 'x5RFFprL4ZtRe2Ewjze7Yw2', 'Sudha P', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(10, 'YO0Ozu891NAKsATLE0qnIA2', 'YO0Ozu891NAKsATLE0qnIA2', 'Sumathy1 Magesh1', 'A', 'yes', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(11, 'vOA3lKZUaW8q7EAV6Z-m6g2', 'vOA3lKZUaW8q7EAV6Z-m6g2', 'Vasavi J J', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(12, 'Gp37g_b7b7YAz6M-FGbeEw2', 'Gp37g_b7b7YAz6M-FGbeEw2', 'Venkata Subramanian', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(13, 'DiUmoR5UhLckVxDHTVvThw2', 'DiUmoR5UhLckVxDHTVvThw2', 'Vignesh T', 'A', 'no', '15126700', '2022-01-12 10:53:35.874250', '15126700', '2022-01-12 10:53:35.874250'),
(14, 'no response', '8Vet2nZB5ATvBMFs3tYRGA2', 'pandiyan', 'A', 'no', '15126700', '2021-09-23 17:07:28:887000', '24044601', '2022-01-29 10:54:34:137000');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dsai_ilms_teacher`
--
ALTER TABLE `dsai_ilms_teacher`
  ADD PRIMARY KEY (`index`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `dsai_ilms_teacher`
--
ALTER TABLE `dsai_ilms_teacher`
  MODIFY `index` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
