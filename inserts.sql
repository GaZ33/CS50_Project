-- Inserção de 10 registros para a tabela `instrutor`
INSERT INTO `autoescola`.`instrutor` (`email_instrutor`, `pnome_instrutor`, `snome_instrutor`, `senha`)
VALUES 
('instrutor1@exemplo.com', 'João', 'Silva', 'senha123'),
('instrutor2@exemplo.com', 'Maria', 'Oliveira', 'senha123'),
('instrutor3@exemplo.com', 'Pedro', 'Santos', 'senha123'),
('instrutor4@exemplo.com', 'Lucas', 'Costa', 'senha123'),
('instrutor5@exemplo.com', 'Ana', 'Lima', 'senha123'),
('instrutor6@exemplo.com', 'Roberto', 'Pereira', 'senha123'),
('instrutor7@exemplo.com', 'Fernanda', 'Souza', 'senha123'),
('instrutor8@exemplo.com', 'Carlos', 'Almeida', 'senha123'),
('instrutor9@exemplo.com', 'Júlia', 'Martins', 'senha123'),
('instrutor10@exemplo.com', 'Ricardo', 'Melo', 'senha123');

-- Inserção de 10 registros para a tabela `alunos`
INSERT INTO `autoescola`.`alunos` (`nascimento_aluno`, `email_aluno`, `cpf_aluno`, `senha_aluno`, `dataregistro_aluno`, `celular`, `bairro`, `rua`, `snome_aluno`, `pnome_aluno`)
VALUES 
('1995-03-12', 'aluno1@exemplo.com', '12345678901', 'senha123', '2024-01-01', '11987654321', 'Centro', 'Rua A', 'Souza', 'João'),
('1994-07-25', 'aluno2@exemplo.com', '12345678902', 'senha123', '2024-01-02', '11987654322', 'Jardim Paulista', 'Rua B', 'Silva', 'Ana'),
('1993-05-18', 'aluno3@exemplo.com', '12345678903', 'senha123', '2024-01-03', '11987654323', 'Vila Nova', 'Rua C', 'Oliveira', 'Pedro'),
('1992-11-05', 'aluno4@exemplo.com', '12345678904', 'senha123', '2024-01-04', '11987654324', 'Santa Tereza', 'Rua D', 'Costa', 'Lucas'),
('1996-09-30', 'aluno5@exemplo.com', '12345678905', 'senha123', '2024-01-05', '11987654325', 'Centro', 'Rua E', 'Pereira', 'Roberto'),
('1997-03-22', 'aluno6@exemplo.com', '12345678906', 'senha123', '2024-01-06', '11987654326', 'Vila Esperança', 'Rua F', 'Souza', 'Fernanda'),
('1998-02-14', 'aluno7@exemplo.com', '12345678907', 'senha123', '2024-01-07', '11987654327', 'Vila Maria', 'Rua G', 'Melo', 'Carlos'),
('1991-06-18', 'aluno8@exemplo.com', '12345678908', 'senha123', '2024-01-08', '11987654328', 'Jardim São Paulo', 'Rua H', 'Martins', 'Júlia'),
('1990-12-11', 'aluno9@exemplo.com', '12345678909', 'senha123', '2024-01-09', '11987654329', 'Parque Industrial', 'Rua I', 'Almeida', 'Ricardo'),
('1999-08-20', 'aluno10@exemplo.com', '12345678910', 'senha123', '2024-01-10', '11987654330', 'Vila das Flores', 'Rua J', 'Silva', 'José');

-- Inserção de 10 registros para a tabela `avaliacao`
INSERT INTO `autoescola`.`avaliacao` (`nota_avaliacao`, `tipo_avaliacao`, `desc_avaliacao`)
VALUES 
(8, 'teórica', 'Boa avaliação'),
(7, 'prática', 'Avaliação prática'),
(9, 'teórica', 'Ótima avaliação'),
(6, 'prática', 'Avaliação regular'),
(7, 'teórica', 'Avaliação regular'),
(10, 'prática', 'Avaliação excelente'),
(5, 'teórica', 'Avaliação fraca'),
(8, 'prática', 'Avaliação boa'),
(6, 'teórica', 'Avaliação média'),
(9, 'prática', 'Avaliação muito boa');

-- Inserção de 10 registros para a tabela `agendamento_aula`
INSERT INTO `autoescola`.`agendamento_aula` (`datetime`, `situacao_agendamento`, `instrutor_id_instrutor`, `alunos_id_aluno`, `avaliacao_id_avaliacao`)
VALUES 
('2024-02-01', 'agendado', 1, 1, 1),
('2024-02-02', 'cancelado', 2, 2, 2),
('2024-02-03', 'concluido', 3, 3, 3),
('2024-02-04', 'agendado', 4, 4, 4),
('2024-02-05', 'cancelado', 5, 5, 5),
('2024-02-06', 'concluido', 6, 6, 6),
('2024-02-07', 'agendado', 7, 7, 7),
('2024-02-08', 'cancelado', 8, 8, 8),
('2024-02-09', 'concluido', 9, 9, 9),
('2024-02-10', 'agendado', 10, 10, 10);

-- Inserção de 10 registros para a tabela `cnh`
INSERT INTO `autoescola`.`cnh` (`tipo_cnh`, `dataregistro_cnh`, `alunos_id_aluno`)
VALUES 
('A', '2024-01-01', 1),
('B', '2024-01-02', 2),
('C', '2024-01-03', 3),
('A', '2024-01-04', 4),
('B', '2024-01-05', 5),
('C', '2024-01-06', 6),
('A', '2024-01-07', 7),
('B', '2024-01-08', 8),
('C', '2024-01-09', 9),
('A', '2024-01-10', 10);

-- Inserção de 10 registros para a tabela `exame`
INSERT INTO `autoescola`.`exame` (`data_exame`, `resultado_exame`, `alunos_id_aluno`)
VALUES 
('2024-02-01', 1, 1),
('2024-02-02', 0, 2),
('2024-02-03', 1, 3),
('2024-02-04', 1, 4),
('2024-02-05', 0, 5),
('2024-02-06', 1, 6),
('2024-02-07', 0, 7),
('2024-02-08', 1, 8),
('2024-02-09', 1, 9),
('2024-02-10', 0, 10);

-- Inserção de 10 registros para a tabela `veiculo`
INSERT INTO `autoescola`.`veiculo` (`tipo_veiculo`, `marca_veiculo`, `placa_veiculo`, `vencimento_documento`)
VALUES 
('Carro', 'Toyota', 'ABC1234', '2024-12-31'),
('Moto', 'Honda', 'XYZ5678', '2024-11-30'),
('Carro', 'Ford', 'LMN9101', '2025-01-15'),
('Carro', 'Chevrolet', 'DEF2345', '2024-10-10'),
('Moto', 'Yamaha', 'GHI6789', '2025-02-20'),
('Carro', 'Fiat', 'JKL3456', '2024-12-01'),
('Carro', 'Volkswagen', 'QRS4567', '2025-06-30'),
('Moto', 'BMW', 'TUV8901', '2024-09-25'),
('Carro', 'Nissan', 'WXY1234', '2025-03-10'),
('Moto', 'Suzuki', 'ZAB5678', '2024-08-15');

-- Inserção de 10 registros para a tabela `verificacao_veiculo`
INSERT INTO `autoescola`.`verificacao_veiculo` (`solucionado_verificacao`, `desc_verificacao`, `tipo_verificacao`, `veiculo_id_veiculo`, `instrutor_id_instrutor`)
VALUES 
(1, 'Troca de óleo realizada', 'preventiva', 1, 1),
(0, 'Troca de pneus pendente', 'preditiva', 2, 2),
(1, 'Filtro de ar trocado', 'preventiva', 3, 3),
(0, 'Problema na suspensão', 'corretiva', 4, 4),
(1, 'Inspeção concluída', 'preventiva', 5, 5),
(1, 'Freios verificados', 'preventiva', 6, 6),
(0, 'Troca de pastilhas necessária', 'corretiva', 7, 7),
(1, 'Troca de óleo feita', 'preventiva', 8, 8),
(0, 'Bateria fraca', 'detectiva', 9, 9),
(1, 'Óleo e filtros substituídos', 'preventiva', 10, 10);
