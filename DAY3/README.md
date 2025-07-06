## 📅 Day 3/ 100  - Convert Natural Language into Structured Formats

### 🧠 Skill of the Day:
Today, I learned how to convert a simple English sentence into **structured formats** like:
- 📦 JSON (commonly used in APIs and data storage)
- 📊 Table (used in SQL, Excel, and data visualization tools)
- 🌐 Graph (used in knowledge graphs and databases like Neo4j)

This skill helps break down unstructured natural language into machine-readable formats.

---

### ✨ Input Sentence:
> **"OpenAI collaborated with Microsoft to deploy ChatGPT, which was trained on large-scale text datasets using Reinforcement Learning from Human Feedback (RLHF)."**
---
### 📦 JSON Format
📁 JSON File: [ChatGPT.json](./ChatGPT.json)
#### ✅ How I Converted the Sentence to JSON:

The sentence talks about:
- A **collaboration** between two organizations: OpenAI and Microsoft.
- A **project** named ChatGPT.
- The **training method** used: RLHF.
- The **training data**: large-scale text datasets.

So I structured the sentence into JSON with two main sections:
1. `"collaboration"`: Contains the collaborators, project, and action.
2. `"training"`: Contains the model name, dataset type, and training method.
---
### 🗄️ SQL Format

To represent this information in a relational format, I created a table named `Collaboration`. This table is designed to store details about partnerships and model development projects.

#### 🔸 Table Structure:

| Column Name        | Data Type     | Description                                                        |
|--------------------|---------------|--------------------------------------------------------------------|
| `id`               | INT           | Primary key to uniquely identify each entry                        |
| `org1`             | VARCHAR(100)  | Name of the first organization (OpenAI)                            |
| `org2`             | VARCHAR(100)  | Name of the second organization (Microsoft)                        |
| `project`          | VARCHAR(100)  | Project name (ChatGPT)                                             |
| `action`           | VARCHAR(100)  | Action performed (Deploy)                                          |
| `training_method`  | VARCHAR(100)  | Method used to train the model (RLHF)                              |
| `dataset_type`     | TEXT          | Type of data used (Large-scale text datasets)                      |

#### 📌 Inserted Row Explanation:

| id | org1   | org2     | project | action | training_method                                    | dataset_type               |
|----|--------|----------|---------|--------|----------------------------------------------------|----------------------------|
| 1  | OpenAI | Microsoft| ChatGPT | Deploy | Reinforcement Learning from Human Feedback (RLHF) | Large-scale text datasets |

This row captures:
- The **collaboration** between OpenAI and Microsoft.
- The **project** they worked on (ChatGPT).
- The **deployment** of the model.
- The **training method** used: RLHF.
- The **dataset**: large-scale text-based data.

#### ⚙️ Environment Used:
- **SQL Engine**: MySQL
- **Version**: 8.0
- 🔗 SQL executed and tested using [DB Fiddle](https://www.db-fiddle.com/)

📁 SQL File: [ChatGPT.sql](./ChatGPT.sql)

🖼️ Output Screenshot:

![ChatGPT](https://github.com/user-attachments/assets/86a44ea4-e77a-4065-beab-77e9d6665140)
---

### 🔗 Neo4j Graph Format

#### 🧠 Sentence Breakdown

The original sentence:

> **"OpenAI collaborated with Microsoft to deploy ChatGPT, which was trained on large-scale text datasets using Reinforcement Learning from Human Feedback (RLHF)."**

can be represented as a **graph of connected entities**.

#### 🧩 Node Types:
- **Organization**: OpenAI, Microsoft
- **AI Model**: ChatGPT
- **Dataset**: Large-scale text datasets
- **Technique**: Reinforcement Learning from Human Feedback (RLHF)

#### 🔗 Relationships:
- `OpenAI` —[:COLLABORATED_WITH]→ `Microsoft`
- `OpenAI` —[:DEPLOYED]→ `ChatGPT`
- `Microsoft` —[:SUPPORTED_DEPLOYMENT_OF]→ `ChatGPT`
- `ChatGPT` —[:TRAINED_ON]→ `Large-scale text datasets`
- `ChatGPT` —[:USES_TECHNIQUE]→ `RLHF`

#### 🛠️ Cypher Query (Neo4j):

```cypher
// Creating organizations
CREATE (o1:Organization {name: 'OpenAI'});
CREATE (o2:Organization {name: 'Microsoft'});

// Creating AI model
CREATE (m:AIModel {name: 'ChatGPT'});

// Creating dataset
CREATE (d:Dataset {name: 'Large-scale text datasets', type: 'Text'});

// Creating technique
CREATE (t:Technique {name: 'Reinforcement Learning from Human Feedback', abbreviation: 'RLHF'});

// Creating relationships
MATCH (o1:Organization {name: 'OpenAI'}),
      (o2:Organization {name: 'Microsoft'}),
      (m:AIModel {name: 'ChatGPT'}),
      (d:Dataset {name: 'Large-scale text datasets'}),
      (t:Technique {name: 'Reinforcement Learning from Human Feedback'})
CREATE 
  (o1)-[:COLLABORATED_WITH]->(o2),
  (o1)-[:DEPLOYED]->(m),
  (o2)-[:SUPPORTED_DEPLOYMENT_OF]->(m),
  (m)-[:TRAINED_ON]->(d),
  (m)-[:USES_TECHNIQUE]->(t);
```
---
### 🌐 Viewing the Graph in Neo4j

To visualize the graph that was created from the sentence, you can use the following Cypher query in the **Neo4j Browser** or **Neo4j AuraDB** interface.

#### 🧠 I used **Neo4j AuraDB (Graph Database)** to create and explore this knowledge graph.

```cypher
// 🔍 This Cypher query is used to display the entire graph created from the sentence
MATCH (n)-[r]->(m)
RETURN n, r, m;
```

This will return:
- All nodes (`n` and `m`)
- All relationships (`r`)
- Displayed in the visual graph view inside Neo4j

🖼️ Graph View of the Sentence in Neo4j:
> Visual representation of relationships between OpenAI, Microsoft, ChatGPT, RLHF, and data.
![Neo4j](https://github.com/user-attachments/assets/6285e6b7-f7c5-4d09-a22b-5caeff76390b)

---
