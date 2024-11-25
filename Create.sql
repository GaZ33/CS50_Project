DROP DATABASE autoescola;
-- SHOW databases;
-- ----------------------------------------------------- 
-- Criação do Banco de dados
-- ----------------------------------------------------- 
CREATE DATABASE autoescola;
use autoescola;


-- ----------------------------------------------------- 
-- Table `autoescola`.`instrutor` 
-- ----------------------------------------------------- 
CREATE TABLE IF NOT EXISTS `autoescola`.`instrutor` ( 
  `id_instrutor` INT NOT NULL AUTO_INCREMENT, 
  `email_instrutor` VARCHAR(50) NOT NULL, 
  `pnome_instrutor` VARCHAR(15) NOT NULL, 
  `snome_instrutor` VARCHAR(25) NOT NULL, 
  `senha` VARCHAR(100) NOT NULL, 
  
  PRIMARY KEY (`id_instrutor`), 
  UNIQUE INDEX `email_instrutor` (`email_instrutor` ASC) VISIBLE) 
ENGINE = InnoDB 
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_0900_ai_ci; 


-- ----------------------------------------------------- 
-- Table `autoescola`.`alunos` 
-- ----------------------------------------------------- 

CREATE TABLE IF NOT EXISTS `autoescola`.`alunos` ( 
  `id_aluno` INT NOT NULL AUTO_INCREMENT, 
  `nascimento_aluno` DATE NULL DEFAULT NULL, 
  `email_aluno` VARCHAR(50) NOT NULL, 
  `cpf_aluno` VARCHAR(11) NOT NULL, 
  `senha_aluno` VARCHAR(100) NOT NULL, 
  `dataregistro_aluno` DATE NOT NULL, 
  `celular` VARCHAR(15) NOT NULL, 
  `bairro` VARCHAR(25) NULL DEFAULT NULL, 
  `rua` VARCHAR(25) NULL DEFAULT NULL, 
  `snome_aluno` VARCHAR(25) NOT NULL, 
  `pnome_aluno` VARCHAR(15) NOT NULL, 

  PRIMARY KEY (`id_aluno`)) 
ENGINE = InnoDB 
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_0900_ai_ci; 

-- ----------------------------------------------------- 
-- Table `autoescola`.`avaliacao` 
-- ----------------------------------------------------- 
CREATE TABLE IF NOT EXISTS `autoescola`.`avaliacao` ( 
  `id_avaliacao` INT NOT NULL AUTO_INCREMENT, 
  `nota_avaliacao` INT NOT NULL, 
  `tipo_avaliacao` VARCHAR(15) NOT NULL, 
  `desc_avaliacao` VARCHAR(45) NULL DEFAULT NULL, 

  PRIMARY KEY (`id_avaliacao`)) 
ENGINE = InnoDB 
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_0900_ai_ci; 

-- ----------------------------------------------------- 
-- Table `autoescola`.`agendamento_aula` 
-- ----------------------------------------------------- 
CREATE TABLE IF NOT EXISTS `autoescola`.`agendamento_aula` ( 
  `id_agendamento` INT NOT NULL AUTO_INCREMENT, 
  `datetime` DATE NOT NULL, 
  `situacao_agendamento` ENUM("agendado", "cancelado", "concluido") NOT NULL, 
  `instrutor_id_instrutor` INT NOT NULL, 
  `alunos_id_aluno` INT NOT NULL, 
  `avaliacao_id_avaliacao` INT NOT NULL, 
  
  PRIMARY KEY (`id_agendamento`), 
  
  INDEX `fk_agendamento_aula_instrutor1_idx` (`instrutor_id_instrutor` ASC) VISIBLE, 
  INDEX `fk_agendamento_aula_alunos1_idx` (`alunos_id_aluno` ASC) VISIBLE, 
  INDEX `fk_agendamento_aula_avaliacao1_idx` (`avaliacao_id_avaliacao` ASC) VISIBLE, 
  
  CONSTRAINT `fk_agendamento_aula_instrutor1` 
    FOREIGN KEY (`instrutor_id_instrutor`) 
    REFERENCES `autoescola`.`instrutor` (`id_instrutor`) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION, 
  CONSTRAINT `fk_agendamento_aula_alunos1` 
    FOREIGN KEY (`alunos_id_aluno`) 
    REFERENCES `autoescola`.`alunos` (`id_aluno`) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION, 
  CONSTRAINT `fk_agendamento_aula_avaliacao1` 
    FOREIGN KEY (`avaliacao_id_avaliacao`) 
    REFERENCES `autoescola`.`avaliacao` (`id_avaliacao`) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION) 
ENGINE = InnoDB 
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_0900_ai_ci; 

-- ----------------------------------------------------- 
-- Table `autoescola`.`cnh` 
-- ----------------------------------------------------- 
CREATE TABLE IF NOT EXISTS `autoescola`.`cnh` ( 
  `id_cnh` INT NOT NULL AUTO_INCREMENT, 
  `tipo_cnh` VARCHAR(2) NOT NULL, 
  `dataregistro_cnh` DATE NOT NULL, 
  `alunos_id_aluno` INT NOT NULL, 
  PRIMARY KEY (`id_cnh`), 
  INDEX `fk_cnh_alunos1_idx` (`alunos_id_aluno` ASC) VISIBLE, 
  CONSTRAINT `fk_cnh_alunos1` 
    FOREIGN KEY (`alunos_id_aluno`) 
    REFERENCES `autoescola`.`alunos` (`id_aluno`) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION) 
ENGINE = InnoDB 
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_0900_ai_ci; 

-- ----------------------------------------------------- 
-- Table `autoescola`.`exame` 
-- ----------------------------------------------------- 
CREATE TABLE IF NOT EXISTS `autoescola`.`exame` ( 
  `id_exame` INT NOT NULL AUTO_INCREMENT, 
  `data_exame` DATE NOT NULL, 
  `resultado_exame` TINYINT NOT NULL, 
  `alunos_id_aluno` INT NOT NULL, 
  PRIMARY KEY (`id_exame`), 
  INDEX `fk_exame_alunos1_idx` (`alunos_id_aluno` ASC) VISIBLE, 
  CONSTRAINT `fk_exame_alunos1` 
    FOREIGN KEY (`alunos_id_aluno`) 
    REFERENCES `autoescola`.`alunos` (`id_aluno`) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION) 
ENGINE = InnoDB 
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_0900_ai_ci; 

-- ----------------------------------------------------- 
-- Table `autoescola`.`veiculo` 
-- ----------------------------------------------------- 
CREATE TABLE IF NOT EXISTS `autoescola`.`veiculo` ( 
  `id_veiculo` INT NOT NULL AUTO_INCREMENT, 
  `tipo_veiculo` VARCHAR(15) NOT NULL, 
  `marca_veiculo` VARCHAR(15) NOT NULL, 
  `placa_veiculo` VARCHAR(15) NOT NULL, 
  `vencimento_documento` DATE NOT NULL, 
  
  PRIMARY KEY (`id_veiculo`)) 
ENGINE = InnoDB 
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_0900_ai_ci; 

-- ----------------------------------------------------- 
-- Table `autoescola`.`verificacao_veiculo` 
-- ----------------------------------------------------- 
CREATE TABLE IF NOT EXISTS `autoescola`.`verificacao_veiculo` ( 
  `id_verificacao` INT NOT NULL AUTO_INCREMENT, 
  `solucionado_verificacao` TINYINT NOT NULL, 
  `desc_verificacao` VARCHAR(200) NOT NULL, 
  `tipo_verificacao` ENUM("preventiva", "preditiva", "corretiva", "detectiva", "emegerncia") NOT NULL, 
  `veiculo_id_veiculo` INT NOT NULL, 
  `instrutor_id_instrutor` INT NOT NULL,
  
  PRIMARY KEY (`id_verificacao`), 
  INDEX `fk_verificacao_veiculo_veiculo1_idx` (`veiculo_id_veiculo` ASC) VISIBLE, 
  INDEX `fk_verificacao_veiculo_instrutor1_idx` (`instrutor_id_instrutor` ASC) VISIBLE, 
  CONSTRAINT `fk_verificacao_veiculo_veiculo1` 
    FOREIGN KEY (`veiculo_id_veiculo`) 
    REFERENCES `autoescola`.`veiculo` (`id_veiculo`) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION, 
  CONSTRAINT `fk_verificacao_veiculo_instrutor1` 
    FOREIGN KEY (`instrutor_id_instrutor`) 
    REFERENCES `autoescola`.`instrutor` (`id_instrutor`) 
    ON DELETE NO ACTION 
    ON UPDATE NO ACTION) 
ENGINE = InnoDB 
DEFAULT CHARACTER SET = utf8mb4 
COLLATE = utf8mb4_0900_ai_ci; 


-- ----------------------------------------------------- 
-- Criação de Índices
-- ----------------------------------------------------- 
CREATE INDEX idx_login_alunos ON alunos(email_aluno, senha_aluno); 
CREATE INDEX idx_login_instrutor ON instrutor(email_instrutor, senha); 


