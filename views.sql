-- ----------------------------------------------------- 
-- Criação de Views
-- ----------------------------------------------------- 


-- Métrica usada pela empresa: Contagem de aprovação dos últimos 100 exames
CREATE VIEW aprovacao_ultimas_100_exames AS
SELECT COUNT(*)
FROM Exame
WHERE resultado_exame = 1
ORDER BY id_exame DESC
LIMIT 100;
SELECT * FROM aprovacao_ultimas_100_exames;


-- Últimas 10 verificações de veículos
CREATE VIEW ultimas_10_avaliacao AS
SELECT * 
FROM verificacao_veiculo
ORDER BY id_verificacao DESC
LIMIT 10;
SELECT * FROM ultimas_10_avaliacao;


-- Contagem de exames por aluno
CREATE VIEW exames_aluno AS
SELECT al.id_aluno AS aluno_id, COUNT(*) AS quantidade_exames
FROM alunos al
INNER JOIN exame e ON al.id_aluno = e.alunos_id_aluno
GROUP BY al.id_aluno;
SELECT * FROM exames_aluno;


-- Agendamentos de alunos
CREATE VIEW agendamentos_aluno AS
SELECT al.id_aluno, al.pnome_aluno, ag.datetime
FROM alunos al
INNER JOIN agendamento_aula ag ON al.id_aluno = ag.alunos_id_aluno
WHERE situacao_agendamento = 'agendado';
SELECT * FROM agendamentos_aluno;


-- Agendamentos de instrutores
CREATE VIEW agendamentos_instrutores AS
SELECT i.id_instrutor, i.pnome_instrutor, ag.datetime
FROM instrutor i
INNER JOIN agendamento_aula ag ON i.id_instrutor = ag.alunos_id_aluno
WHERE situacao_agendamento = 'agendado';
SELECT * FROM agendamentos_instrutores;


-- Média dos alunos
CREATE VIEW media_aluno AS
SELECT al.id_aluno, al.pnome_aluno, AVG(av.nota_avaliacao) AS "media"
FROM alunos al
INNER JOIN agendamento_aula ag ON al.id_aluno = ag.alunos_id_aluno
INNER JOIN avaliacao av ON ag.avaliacao_id_avaliacao = av.id_avaliacao
GROUP BY al.id_aluno;
SELECT * FROM media_aluno;