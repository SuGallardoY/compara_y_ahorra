-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema compara_y_ahorra
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema compara_y_ahorra
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `compara_y_ahorra` DEFAULT CHARACTER SET utf8 ;
USE `compara_y_ahorra` ;

-- -----------------------------------------------------
-- Table `compara_y_ahorra`.`usuarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `compara_y_ahorra`.`usuarios` (
  `codigo_user` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `correo` VARCHAR(45) NULL,
  `contrasena` VARCHAR(255) NULL,
  `cliente_empresa` VARCHAR(50) NULL,
  PRIMARY KEY (`codigo_user`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `compara_y_ahorra`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `compara_y_ahorra`.`productos` (
  `codigo_prod` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `precio` VARCHAR(45) NULL,
  `stock` INT NULL,
  `descripcion` TEXT NULL,
  PRIMARY KEY (`codigo_prod`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
