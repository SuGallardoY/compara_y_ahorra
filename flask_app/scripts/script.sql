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
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `apellido` VARCHAR(45) NULL,
  `fecha_nacimiento` DATE NULL,
  `correo` VARCHAR(45) NULL,
  `contrasena` VARCHAR(255) NULL,
  `cliente_empresa` TINYINT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `compara_y_ahorra`.`productos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `compara_y_ahorra`.`productos` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nombre` VARCHAR(45) NULL,
  `precio` VARCHAR(45) NULL,
  `stock` INT NULL,
  `descripcion` TEXT NULL,
  `empresas_id` INT NOT NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_productos_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_productos_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `compara_y_ahorra`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `compara_y_ahorra`.`boletas`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `compara_y_ahorra`.`boletas` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `monto` INT NULL,
  `fecha` DATE NULL,
  `productos_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_boletas_productos_idx` (`productos_id` ASC) VISIBLE,
  CONSTRAINT `fk_boletas_productos`
    FOREIGN KEY (`productos_id`)
    REFERENCES `compara_y_ahorra`.`productos` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `compara_y_ahorra`.`comentarios`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `compara_y_ahorra`.`comentarios` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `texto` TEXT NULL,
  `usuarios_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_comentarios_usuarios1_idx` (`usuarios_id` ASC) VISIBLE,
  CONSTRAINT `fk_comentarios_usuarios1`
    FOREIGN KEY (`usuarios_id`)
    REFERENCES `compara_y_ahorra`.`usuarios` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
