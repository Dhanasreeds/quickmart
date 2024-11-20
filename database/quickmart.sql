-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 02, 2024 at 03:02 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `quickmart`
--

-- --------------------------------------------------------

--
-- Table structure for table `cart`
--

CREATE TABLE `cart` (
  `cst_id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `shopname` varchar(255) NOT NULL,
  `productname` varchar(255) NOT NULL,
  `quantity` int(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `cart`
--

INSERT INTO `cart` (`cst_id`, `username`, `shopname`, `productname`, `quantity`) VALUES
(6, 'varsha@gmail.com', 'Aqua', 'salt', 1),
(6, 'varsha@gmail.com', 'Aqua', 'pasta', 2),
(6, 'varsha@gmail.com', 'eco', 'tomato sauce', 1);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `cst_mail` varchar(50) NOT NULL,
  `shopname` varchar(50) NOT NULL,
  `productname` varchar(50) NOT NULL,
  `price` varchar(20) NOT NULL,
  `quantity` int(50) NOT NULL,
  `net_price` int(11) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `cst_mail`, `shopname`, `productname`, `price`, `quantity`, `net_price`, `status`) VALUES
(45, 'brintha@gmail.com', 'Blue waves', 'tomato', '50', 2, 100, ''),
(46, 'brintha@gmail.com', 'Blue waves', 'cookies', '40', 1, 40, ''),
(47, 'varun@gmail.com', 'eco', 'rin powder', '100', 1, 100, ''),
(48, 'varun@gmail.com', 'DS stores', 'chips', '40', 2, 80, 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `product_upload`
--

CREATE TABLE `product_upload` (
  `pid` int(11) NOT NULL,
  `shop_name` varchar(255) NOT NULL,
  `product_name` varchar(50) NOT NULL,
  `product_quantity` varchar(50) NOT NULL,
  `product_price` int(50) NOT NULL,
  `units` varchar(20) NOT NULL,
  `product_image` varchar(255) NOT NULL,
  `product_description` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `product_upload`
--

INSERT INTO `product_upload` (`pid`, `shop_name`, `product_name`, `product_quantity`, `product_price`, `units`, `product_image`, `product_description`) VALUES
(12, 'vennila stores', 'bannana', '1', 50, 'kilograms', 'banana-2449019_640.jpg', 'fresh bannana'),
(13, 'vennila stores', 'veges', '1', 50, 'kilograms', 'veg2.avif', 'all veges are available'),
(14, 'Aqua', 'milk', '1', 60, 'liters', 'dairy2.jpg', 'vitamin '),
(15, 'Aqua', 'salt', '1', 60, 'kilograms', 'salt.webp', 'high quality'),
(16, 'Aqua', 'pasta', '1', 40, 'kilograms', 'pasta-1282067_1280.jpg', 'delisious'),
(17, 'Blue waves', 'cookies', '1', 40, 'kilograms', 'Bakery2.jpeg', 'choco cookies'),
(18, 'Blue waves', 'tomato', '1', 50, 'kilograms', 'tommato.webp', 'fresh tomato'),
(19, 'Blue waves', 'red chillli powder', '1', 60, 'kilograms', 'aachi-chilli-powder-1-kg.jpg', 'high quality red chilli powder'),
(20, 'eco', 'tomato sauce', '1', 120, 'liters', 'buhuOcpr.jpeg', 'freash sauce'),
(21, 'eco', 'fruits', '1', 200, 'kilograms', 'frurits.jpeg', 'all freash fruits'),
(22, 'eco', 'rin powder', '1', 100, 'kilograms', 'rin-soap-2220085516-vpaxshgy.avif', 'super wash'),
(23, 'DS stores', 'chips', '1', 40, 'kilograms', 'download.jpeg', 'high quality chips'),
(24, 'DS stores', 'cookies', '1', 70, 'kilograms', 'download (1).jpeg', 'teasty cookies');

-- --------------------------------------------------------

--
-- Table structure for table `shop_register`
--

CREATE TABLE `shop_register` (
  `id` int(11) NOT NULL,
  `shop_name` varchar(255) NOT NULL,
  `shop_photo` varchar(255) NOT NULL,
  `shop_address` varchar(255) NOT NULL,
  `City` varchar(20) NOT NULL,
  `pincode` int(10) NOT NULL,
  `State` varchar(255) NOT NULL,
  `Nationality` varchar(10) NOT NULL,
  `owner_name` varchar(50) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `owner_photo` varchar(255) NOT NULL,
  `Mail_id` varchar(100) NOT NULL,
  `password` varchar(20) NOT NULL,
  `Mobile` decimal(10,0) NOT NULL,
  `status` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `shop_register`
--

INSERT INTO `shop_register` (`id`, `shop_name`, `shop_photo`, `shop_address`, `City`, `pincode`, `State`, `Nationality`, `owner_name`, `Gender`, `owner_photo`, `Mail_id`, `password`, `Mobile`, `status`) VALUES
(11, 'DS stores', 'ds.png', '75,VINAYAKAR KOVIL STREET ,THALAVAIPETTAI,BHAVANI,ERODE', 'ERODE', 638312, 'Tamil Nadu', 'indian', 'Dhanasree', 'Female', 'man.jpg', 'dhanasree315@gmail.com', '12345', 9865327415, 'Approved'),
(12, 'Aqua', 'Untitled design (1).png', '75,VINAYAKAR KOVIL STREET ,THALAVAIPETTAI,BHAVANI,ERODE', 'ERODE', 638312, 'Tamil Nadu', 'indian', 'anu', 'Female', 'pexels-danxavier-1239291.jpg', 'anuaqua@gmail.com', '12345', 9638527417, 'Approved'),
(13, 'vennila stores', 'v.webp', '75,VINAYAKAR KOVIL STREET ,THALAVAIPETTAI,BHAVANI,ERODE', 'ERODE', 638312, 'Tamil Nadu', 'indian', 'vennila', 'Female', 'pexels-olly-762020.jpg', 'vennila@gmail.com', '12345', 7754321866, 'Approved'),
(14, 'Blue waves', 'Untitled design.png', '75,VINAYAKAR KOVIL STREET ,THALAVAIPETTAI,BHAVANI,ERODE', 'ERODE', 638312, 'Tamil Nadu', 'indian', 'arun', 'Male', 'pexels-italo-melo-881954-2379004.jpg', 'arun@gmail.com', '12345', 8542661497, 'Approved'),
(15, 'eco', 'Untitled design (2).png', '75,VINAYAKAR KOVIL STREET ,THALAVAIPETTAI,BHAVANI,ERODE', 'ERODE', 638312, 'Tamil Nadu', 'indian', 'priya', 'Female', 'pexels-hannah-nelson-390257-1065084.jpg', 'priya@gmail.com', '12345', 9995643742, 'Approved');

-- --------------------------------------------------------

--
-- Table structure for table `user_register`
--

CREATE TABLE `user_register` (
  `id` int(11) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `Mail_id` varchar(50) NOT NULL,
  `Mobile_num` decimal(10,0) NOT NULL,
  `Password` varchar(8) NOT NULL,
  `confrim_Password` varchar(8) NOT NULL,
  `Gender` varchar(8) NOT NULL,
  `Address` varchar(255) NOT NULL,
  `City` varchar(50) NOT NULL,
  `pincode` int(10) NOT NULL,
  `state` varchar(50) NOT NULL,
  `Nationality` varchar(50) NOT NULL,
  `status` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `user_register`
--

INSERT INTO `user_register` (`id`, `user_name`, `Mail_id`, `Mobile_num`, `Password`, `confrim_Password`, `Gender`, `Address`, `City`, `pincode`, `state`, `Nationality`, `status`) VALUES
(5, 'varun', 'varun@gmail.com', 8845632199, 'varun', 'varun', 'Male', '75,VINAYAKAR KOVIL STREET ,THALAVAIPETTAI,BHAVANI,ERODE', 'ERODE', 638312, 'Tamil Nadu', 'indian', ''),
(6, 'varsha', 'varsha@gmail.com', 8576429945, 'varsha', 'varsha', 'Female', '75,VINAYAKAR KOVIL STREET ,THALAVAIPETTAI,BHAVANI,ERODE', 'ERODE', 638312, 'Tamil Nadu', 'indian', ''),
(7, 'brintha', 'brintha@gmail.com', 7865498833, 'brintha', 'brintha', 'Female', '75,VINAYAKAR KOVIL STREET ,THALAVAIPETTAI,BHAVANI,ERODE', 'ERODE', 638312, 'Tamil Nadu', 'indian', '');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `product_upload`
--
ALTER TABLE `product_upload`
  ADD PRIMARY KEY (`pid`);

--
-- Indexes for table `shop_register`
--
ALTER TABLE `shop_register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `user_register`
--
ALTER TABLE `user_register`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT for table `product_upload`
--
ALTER TABLE `product_upload`
  MODIFY `pid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `shop_register`
--
ALTER TABLE `shop_register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `user_register`
--
ALTER TABLE `user_register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
