-- Creating the table to store collaboration data
CREATE TABLE Collaboration (
    id INT PRIMARY KEY,
    org1 VARCHAR(100),
    org2 VARCHAR(100),
    project VARCHAR(100),
    action VARCHAR(100),
    training_method VARCHAR(100),
    dataset_type TEXT
);

-- Inserting the sentence data into the table
INSERT INTO Collaboration (
    id, org1, org2, project, action, training_method, dataset_type
) VALUES (
    1, 'OpenAI', 'Microsoft', 'ChatGPT', 'Deploy', 'Reinforcement Learning from Human Feedback (RLHF)', 'Large-scale text datasets'
);

-- Viewing the inserted data
SELECT * FROM Collaboration;

